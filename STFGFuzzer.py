#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import faulthandler  # Use to find Segmentation Fault
import time

faulthandler.enable()

from fuzzer_module import *
from fuzzer_module.Fuzzconfig import *

# source env_python/bin/activate
# python3 STFGFuzzer.py -n demo  -- ./Programs/demo/code_Bin/demo -f @seed@
# python3 STFGFuzzer.py -n demo -t sanitize -- ./Programs/demo/code_Bin/demo -f @seed@
# python3 STFGFuzzer.py -n demo -t sanitize,manual,patch -- ./Programs/demo/code_Bin/demo -f @seed@
# python3 STFGFuzzer.py -n base64 -- ./Programs/base64/code_Bin/base64 -d @seed@
# python3 STFGFuzzer.py -n md5sum -- ./Programs/md5sum/code_Bin/md5sum -c @seed@
# python3 STFGFuzzer.py -n uniq -- ./Programs/uniq/code_Bin/uniq @seed@
# python3 STFGFuzzer.py -n who -- ./Programs/who/code_Bin/who @seed@
# python3 STFGFuzzer.py -n lava660 -t sanitize -- Programs/lava660/code_Bin/lava660 @seed@
# python3 STFGFuzzer.py -n lava2285 -t sanitize -- Programs/lava2285/code_Bin/lava2285 @seed@
# python3 STFGFuzzer.py -n lava13796 -t sanitize -- Programs/lava13796/code_Bin/lava13796 @seed@
# python3 STFGFuzzer.py -n CVE-2016-4487 -t manual -- Programs/CVE-2016-4487/code_Bin/CVE-2016-4487 @@seed@
# python3 STFGFuzzer.py -n binutils-c++filt -- Programs/binutils-c++filt/code_Bin/binutils-c++filt @@seed@
# python3 STFGFuzzer.py -n CVE-2016-4493 -t manual -- Programs/CVE-2016-4493/code_Bin/CVE-2016-4493 @@seed@

def mainFuzzer():
    """
    The fuzzing Loop.
    @return:
    """
    print("{} Start Directed Fuzzing...".format(getTime()))
    # Close Address Space Layout Randomization.
    stdout, stderr = Executor.runNoLimit("cat /proc/sys/kernel/randomize_va_space")  # Default 2
    if stdout != b'0\n':
        raise Exception("Please turn off address randomization -> echo 0 > /proc/sys/kernel/randomize_va_space")

    # Receive command line parameters.
    program_name, patchtype, fuzz_command = Generator.genTerminal()
    if fuzz_command == "" or program_name == "":
        print("python {}.py -h".format(FUZZNAME))
        raise Exception("Error parameters.")

    path = Structures.StructPath(program_name)
    file_crash_csv = path.seeds_crash + CRASH_CSVFILENAME

    '''Fuzzing test procedure'''

    # Directed Location
    print("{} Build Directional Position...".format(getTime()))
    target_dict = Comparator.getTarget(path.data_patchloc, patchtype)
    LOG(DEBUG, LOC(), target_dict, show=True)

    sch = Scheduler.Scheduler()
    for tgt_ki, stu_vi in target_dict.items():
        sch.target_dict[tgt_ki] = set()
        for info_j in stu_vi:
            sch.target_dict[tgt_ki].add(str(info_j[1]) + str(info_j[2]))

    LOG(DEBUG, LOC(), sch.target_dict)
    # If it is repeated, it is not loaded.
    cmptgt = Comparator.compareTargetDiff(path.data_patchloc, target_dict)
    if cmptgt:
        print("{} Build binary target information...".format(getTime()))
        binline_dict = Builder.getBinaryInfo(path.data_graph)
        map_numto_funcasm = Comparator.getDirectedNodeLoc(binline_dict, target_dict)
        LOG(DEBUG, LOC(), binline_dict, target_dict, map_numto_funcasm, sch.target_dict)

        # Graph Information
        print("{} Build Graph Information...".format(getTime()))
        # Load the .dot file into networkx.
        cglist, cfglist = Generator.createDotJsonFile(program_name, path.code_IR + program_name + GEN_TRACEBC_SUFFIX)
        LOG(DEBUG, LOC(), cglist, cfglist)
        cggraph, map_functo_cgnode = Builder.getCG(cglist)
        cfggraph_dict, map_guard_gvid, map_target = Builder.getCFG(cfglist, map_numto_funcasm, target_dict)
        # map_target {0: {'_Z3bugv': [[0, [0], 0]], 'main': [[1, [31], 32]]}}
        LOG(DEBUG, LOC(), map_guard_gvid, map_target, map_numto_funcasm, target_dict, map_functo_cgnode)
        '''All node transfrom to the gvid to convenient calculation and expression.'''
        '''All the function name transfrom to the static symbol function name.'''
        '''Dynamic:guard  Static:gvid'''
        '''Dynamic:func  Static:symbol'''
        print("{} Construct target distance information...".format(getTime()))
        # map_target {0: {'_Z3bugv': [[0, [0], 0]], 'main': [[1, [31], 32]]}}
        Builder.buildBFSdistance(cggraph, cfggraph_dict)  # Build the distance between two nodes.
        map_tgtpredgvid_dis, map_callfuncs = Builder.getTargetPredecessorsGuard(
            cggraph, cfggraph_dict, map_guard_gvid, map_target, target_dict)
        tgtpred_offset = Builder.getFuncOffset(map_tgtpredgvid_dis, map_target, map_callfuncs)
        LOG(DEBUG, LOC(), map_guard_gvid, map_target, target_dict, map_tgtpredgvid_dis, tgtpred_offset, map_callfuncs)

        print("{} Save as pkl files...".format(getTime()))
        saveAsPkl(path.data_patchloc+".map_functo_cgnode.pkl", map_functo_cgnode)
        saveAsPkl(path.data_patchloc+".map_guard_gvid.pkl", map_guard_gvid)
        saveAsPkl(path.data_patchloc+".map_target.pkl", map_target)
        saveAsPkl(path.data_patchloc+".map_tgtpredgvid_dis.pkl", map_tgtpredgvid_dis)
        saveAsPkl(path.data_patchloc+".tgtpred_offset.pkl", tgtpred_offset)
        saveAsPkl(path.data_patchloc + B4TGT_FILE, target_dict)  # Compare target.
    else:
        # Load variables from PKL files Load variables.
        print("{} Target unchanged, load From pkl files...".format(getTime()))
        map_functo_cgnode = loadFromPkl(path.data_patchloc+".map_functo_cgnode.pkl")
        map_guard_gvid = loadFromPkl(path.data_patchloc+".map_guard_gvid.pkl")
        map_target = loadFromPkl(path.data_patchloc+".map_target.pkl")
        map_tgtpredgvid_dis = loadFromPkl(path.data_patchloc+".map_tgtpredgvid_dis.pkl")
        tgtpred_offset = loadFromPkl(path.data_patchloc+".tgtpred_offset.pkl")
    LOG(DEBUG, LOC(), map_functo_cgnode, map_guard_gvid, map_target, map_tgtpredgvid_dis, tgtpred_offset)

    if len(map_target) != 0:
        sch.all_tgtnum = len(map_target)
    for k in map_functo_cgnode.keys():
        sch.trans_symbol_initguard[k] = USE_INITMAXNUM

    print("{} Directed Target Sequence...".format(getTime()))
    trace_orderdict = Builder.printTargetSeq(map_target)

    LOG(DEBUG, LOC(), map_guard_gvid, map_target, map_tgtpredgvid_dis)

    sch.file_crash_csv = file_crash_csv
    sch.path_crashseeds = path.seeds_crash

    # Init Loop Variables
    loop_weight, loop_covernum, loop_mutloc = USE_INITMAXNUM, 1, set()

    # Init seed lists
    print("{} Init Seed lists...".format(getTime()))
    init_seeds_list = Generator.prepareEnv(program_name)
    LOG(DEBUG, LOC(), init_seeds_list, len(init_seeds_list))
    if len(init_seeds_list) > 0:
        temp_listq = []
        for each in init_seeds_list:
            temp_listq.append(
                Structures.StructSeed(path.seeds_mutate + each, readContent(path.seeds_mutate + each), SEED_INIT,
                                      set()))
        sch.addq(SCH_LOOP_SEED, temp_listq, calPriotiryValue(loop_weight, 0, 0))
    else:
        sch.addq(SCH_LOOP_SEED,
                 [Structures.StructSeed(path.seeds_mutate + AUTO_SEED, Mutator.getExpandFillStr(SCH_EXPAND_SIZE), SEED_INIT, set()), ],
                 calPriotiryValue(loop_weight, 0, 0))

    # Visualizer
    vis = Visualizer.Visualizer()
    vis.trace_orderdict = trace_orderdict
    vis.show_pname = program_name
    # vis.showGraph(path.data_graph, cggraph, cfggraph_dict['main'])

    # Create Memory Share.
    ana = Analyzer.Analyzer()
    create_seed = sch.selectOneSeed(
        SCH_THISMUT_SEED,
        Structures.StructSeed(path.seeds_mutate + AUTO_SEED, Mutator.getExpandFillStr(SCH_EXPAND_SIZE), SEED_INIT, set()))
    create_stdout, create_stderr = Executor.runTimeLimit(fuzz_command.replace(REPLACE_COMMAND, create_seed.filename), vis)
    sch.saveCrash(create_seed, create_stdout, create_stderr, vis)
    ana.getShm(create_stdout[0:16])
    LOG(DEBUG, LOC(), create_seed.content)

    '''Fuzzing Cycle'''
    print("{} Fuzzing Loop...".format(getTime()))
    while sch.cur_tgtnum < sch.all_tgtnum and not sch.seedq.empty():
        loop_mutloc = set()
        eaexit = False
        vis.loop += 1
        # print("{} loop...".format(getTime()))
        # # Guard
        # ana.sendCmpid(TRACE_CMPGUARD)
        # init_stdout, init_stderr = Executor.run(fuzz_command.replace(REPLACE_COMMAND, init_seed.filename))
        # eaexit = sch.saveCrash(init_seed, init_stdout, init_stderr, vis.start_time, vis.last_time)
        # init_interlen, init_covernum = ana.getShm(init_stdout[0:16])
        # init_guardcov_list = ana.getRpt(init_interlen)
        # guard_set, guard_total = ana.traceGuardAnalysis(init_guardcov_list)
        # sch.coveragepath = guard_set
        # vis.num_pcguard = guard_total

        ana.sendCmpid(TRACE_CMP)
        # First run to collect information.
        init_seed = sch.selectOneSeed(SCH_LOOP_SEED)
        opt_seed = init_seed
        init_stdout, init_stderr = Executor.runTimeLimit(fuzz_command.replace(REPLACE_COMMAND, init_seed.filename), vis)
        sch.saveCrash(init_seed, init_stdout, init_stderr, vis)
        init_interlen, init_covernum = ana.getShm(init_stdout[0:16])
        # cmpcov_list = ana.getRpt(init_interlen)
        # initrpt_dict, initrpt_set = ana.traceAyalysis(cmpcovcont_list, sch.freezeid_rpt, sch)
        loop_covernum = init_covernum
        LOG(DEBUG, LOC(), init_seed.content, init_stdout, init_interlen, init_covernum)


        # Select the location to be mutated and add it to the location queue.
        sch.initEachloop(vis)

        '''Find correspondence: seed inputs -> cmp instruction -> cmp type (access method) -> braches'''

        # print("{} ld...".format(getTime()))
        '''ld -> Length Detection, Increase seed length, Subtract seed length. '''
        # Increase the input length when the number of constraints does not change in the program.
        # If there is a change in the increase length then increase the length.
        b4len = len(init_seed.content)

        b4ld_seed = init_seed
        b4ld_interlen = init_interlen
        # LOG(DEBUG, LOC(), init_seed.content, ana.getRpt(init_interlen))
        while len(b4ld_seed.content) < sch.expand_size:

            sch.expandnums += 1
            # if before_coverage == sch.coveragepath and len(init_seed.content) < SCH_EXPAND_MAXSIZE:
            # According fixed length to expand the content length of seed.
            ld_seed = Mutator.mutAddLength(b4ld_seed.content, path.seeds_mutate, LD_EXPAND)
            ld_seed = sch.selectOneSeed(SCH_THISMUT_SEED, ld_seed)
            ld_stdout, ld_stderr = Executor.runTimeLimit(fuzz_command.replace(REPLACE_COMMAND, ld_seed.filename), vis)
            eaexit = sch.saveCrash(ld_seed, ld_stdout, ld_stderr, vis)

            # 1 seed inputs
            ld_interlen, ld_covernum = ana.getShm(ld_stdout[0:16])
            LOG(DEBUG, LOC(), len(ld_seed.content), b4ld_interlen, ld_interlen, ana.getRpt(ld_interlen))
            if b4ld_interlen != ld_interlen:
                b4ld_seed = ld_seed
                b4ld_interlen = ld_interlen
            elif b4ld_interlen == ld_interlen:
                # Current seed.
                ld_cmpcov_list = ana.getRpt(ld_interlen)  # report
                # Before seed.
                b4ld_stdout, b4ld_stderr = Executor.runTimeLimit(fuzz_command.replace(REPLACE_COMMAND, b4ld_seed.filename), vis)
                sch.saveCrash(b4ld_seed, b4ld_stdout, b4ld_stderr, vis)
                b4ld_interlen, b4ld_covernum = ana.getShm(b4ld_stdout[0:16])
                b4ld_cmpcov_list = ana.getRpt(b4ld_interlen)
                LOG(DEBUG, LOC(), b4ld_cmpcov_list)
                if ld_cmpcov_list != b4ld_cmpcov_list:
                    b4ld_seed = ld_seed
                    b4ld_interlen = ld_interlen
                else:
                    break

            res = vis.display(ld_seed, set(), ld_stdout, ld_stderr, STG_LD, -1, sch)
            # vis.showGraph(path.data_graph, cggraph, cfggraph_dict['main'])
            if res == VIS_Q:
                sch.quitFuzz()

        # Subtract seed length.
        # if len(b4ld_seed.content) == b4len:
        #     while len(b4ld_seed.content) > b4len // 2:
        #     # while True:
        #         # According fixed length to expand the content length of seed.
        #         ld_seed = Mutator.mutSubLength(b4ld_seed.content, path.seeds_mutate, len(b4ld_seed.content)//LD_SUB)
        #         ld_seed = sch.selectOneSeed(SCH_THISMUT_SEED, ld_seed)
        #         ld_stdout, ld_stderr = Executor.run(fuzz_command.replace(REPLACE_COMMAND, ld_seed.filename), vis)
        #         eaexit = sch.saveCrash(ld_seed, ld_stdout, ld_stderr, vis)
        #
        #         # 1 seed inputs
        #         ld_interlen, ld_covernum = ana.getShm(ld_stdout[0:16])
        #         LOG(DEBUG, LOC(), len(ld_seed.content), b4ld_interlen, ld_interlen, ana.getRpt(ld_interlen))
        #         if b4ld_interlen != ld_interlen:
        #             break
        #         elif b4ld_interlen == ld_interlen:
        #             # Current seed.
        #             ld_cmpcov_list = ana.getRpt(ld_interlen)  # report
        #             # Before seed.
        #             b4ld_stdout, b4ld_stderr = Executor.run(fuzz_command.replace(REPLACE_COMMAND, b4ld_seed.filename), vis)
        #             b4ld_interlen, b4ld_covernum = ana.getShm(b4ld_stdout[0:16])
        #             b4ld_cmpcov_list = ana.getRpt(b4ld_interlen)
        #             LOG(DEBUG, LOC(), ld_seed.filename, b4ld_seed.filename, ld_cmpcov_list, b4ld_cmpcov_list)
        #             if ld_cmpcov_list != b4ld_cmpcov_list:
        #                 break
        #             else:
        #                 b4ld_seed = ld_seed
        #                 b4ld_interlen = ld_interlen
        #
        #         res = vis.display(ld_seed, set(), ld_stdout, ld_stderr, STG_LD, -1, sch)
        #         # vis.showGraph(path.data_graph, cggraph, cfggraph_dict['main'])
        #         if res == VIS_Q:
        #             sch.quitFuzz()
        # LOG(DEBUG, LOC(), b4ld_seed.content, show=True)
        '''ld <-'''

        # print("{} cf...".format(getTime()))
        '''2 cmp filter -> Select compare instructions which close the target block. '''
        LOG(DEBUG, LOC(), sch.cur_tgtnum)
        if len(map_tgtpredgvid_dis[sch.cur_tgtnum]) == 0:
            ana.sendCmpid(TRACE_CMP)
        else:
            ana.sendCmpid(TRACE_CMPGUARDSYMBOL)
        # Reset the init_seed

        init_seed = sch.selectOneSeed(SCH_THIS_SEED, b4ld_seed)
        init_stdout, init_stderr = Executor.runTimeLimit(fuzz_command.replace(REPLACE_COMMAND, init_seed.filename), vis)
        eaexit = sch.saveCrash(init_seed, init_stdout, init_stderr, vis)
        # print("{} eaexit...".format(getTime()))

        # Get all the constraints.
        # Binary files each function blocks from 0.
        # Execution files each function blocks from n.
        # Get the offset of the address block.
        init_interlen, init_covernum = ana.getShm(init_stdout[0:16])
        init_guardcov_list = ana.getRpt(init_interlen)
        LOG(DEBUG, LOC(), init_guardcov_list, sch.trans_symbol_initguard)
        guard_set, guard_total = ana.getGuardNum(init_guardcov_list)
        sch.coverage_set = sch.coverage_set | guard_set
        vis.num_pcguard = guard_total

        # Update sch priority queue. Save cmpid for the next explore
        # LOG(DEBUG, LOC(), init_guardcov_list, map_tgtpredgvid_dis, tgtpred_offset, map_guard_gvid)
        # print("{} b4select...".format(getTime()))
        sch.selectConstraint(init_guardcov_list, map_tgtpredgvid_dis, tgtpred_offset, map_guard_gvid, vis)
        # print("{} select...".format(getTime()))
        # raise Exception()

        # init_cmp_dict = ana.traceAyalysis(init_cmpcov_list, sch.skip_cmpidset)
        # init_cmpset = set(init_cmp_dict)
        # Compare instruction type speculation based on input mapping,
        # then try to pass the corresponding constraint (1-2 rounds).
        # LOG(DEBUG, LOC(), sch.targetcmp_pq, show=True)
        # while not sch.targetcmp_pq.empty():
        #     LOG(DEBUG, LOC(), sch.targetcmp_pq.get(), show=True)
        # raise Exception()
        '''cf'''

        # print(init_seed.content)
        # Get the length of seed, transform it to num array.
        if len(init_seed.content) != len(sch.loc_coarse_list):
            sch.loc_coarse_list = []
            for loci in range(0, len(init_seed.content)):
                if loci not in sch.freeze_bytes:
                    sch.loc_coarse_list.append(loci)

        # You can always add elements to the priority queue.
        # If the number covered changes, it is considered to have passed this constraint,
        # so it enters the next round of comparison instruction recognition

        '''Init status parameters.'''
        vis.cmptotal = sch.targetcmp_pq.qsize()
        # Update the min distance of target.
        if not sch.targetcmp_pq.empty():
            tempcmpid = sch.targetcmp_pq.get()
            sch.targetcmp_pq.put(tempcmpid)
            sch.cur_nearlydis = tempcmpid[0]

        # Debug:
        # while not sch.targetcmp_pq.empty():
        #     LOG(DEBUG,LOC(), sch.targetcmp_pq.get(), show=True)
        # raise Exception

        # print("{} st...".format(getTime()))
        '''3 cmp type'''
        '''st -> Constraints Analysis'''
        # Select one stcmpid_tuples.
        # for stcmpid_ki, stlocset_vi in cmpmaploc_dict.items():
        nearest_set = set()
        while not eaexit and not sch.targetcmp_pq.empty():

            stcmpid_tuples = sch.targetcmp_pq.get()
            stcmpid_weight, stcmpid_ki, stcmpid_loci, stcmpid_symboldebug = \
                stcmpid_tuples[0], stcmpid_tuples[1], stcmpid_tuples[2]*2, stcmpid_tuples[3]



            # debug
            # ana.sendCmpid(TRACE_GUARDFAST)
            # cur_stdout, cur_stderr = Executor.runTimeLimit(fuzz_command.replace(REPLACE_COMMAND, init_seed.filename), vis)
            # sch.saveCrash(init_seed, cur_stdout, cur_stderr, vis)
            # cur_interlen, cur_covernum = ana.getShm(cur_stdout[0:16])
            # cur_guard_list = ana.getRpt(cur_interlen)
            # cur_dis = sch.findNearDistance(
            #     cur_guard_list, map_tgtpredgvid_dis, tgtpred_offset, map_guard_gvid)
            # LOG(DEBUG, LOC(), cur_dis, stcmpid_weight, show=True)
            # # fixme
            # raise Exception()


            # LOG(DEBUG, LOC(), stcmpid_weight, stcmpid_ki, stcmpid_loci, stcmpid_symboldebug, show=True)
            vis.cmpnum += 1
            vis.cmporder = 0

            # Only mutate nearest constraint.
            LOG(DEBUG, LOC(), nearest_set, show=True)
            if len(nearest_set) == NEAREST_NUMBER and stcmpid_weight not in nearest_set:
                break
            nearest_set.add(stcmpid_weight)
            # limiter Use it from select constraint.
            if stcmpid_weight - sch.cur_nearlydis >= LIMITER:
                break
            LOG(DEBUG, LOC(), sch.skipInvalidState(stcmpid_ki, {stcmpid_ki: {0}}))
            if sch.skipInvalidState(stcmpid_ki, {stcmpid_ki: {0}}):
                continue

            ana.sendCmpid(stcmpid_ki)
            # Debug
            # fixme switch instructions have trip in loop.
            # if stcmpid_ki[0] == 'i':
            #     continue
            # if stcmpid_ki == "g0x4f9aaf0x51c4a50x518557":
            #     LOG(LOG_DEBUG, LOG_FUNCINFO(), "g0x4f9aaf0x51c4a50x518557", showlog=True)
            # filter = ["g0x4f99810x52a8b80x529492"]
            # print(".", end="")
            # if stcmpid_tuples not in filter:
            #     continue
            # print(stcmpid_tuples)

            # First run init seed after cmp filter.
            init_stdout, init_stderr = Executor.runTimeLimit(fuzz_command.replace(REPLACE_COMMAND, init_seed.filename), vis)
            sch.saveCrash(init_seed, init_stdout, init_stderr, vis)
            init_interlen, init_covernum = ana.getShm(init_stdout[0:16])
            init_cmpcov_list = ana.getRpt(init_interlen)
            LOG(DEBUG, LOC(), init_cmpcov_list, show=True)
            # init_cmp_dict = ana.traceAyalysis(init_cmpcov_list, sch.skip_cmpidset)

            # Only the corresponding list data is retained, no parsing is required
            cmp_len = len(init_cmpcov_list)
            exloc_list = sch.extensionLocation(stcmpid_loci, cmp_len)
            # LOG(DEBUG, LOC(), exloc_list, show=True)
            # Separate comparisons for each comparison instruction.
            # for cmporder_j in range(0, cmp_len):
            for cmporder_j in exloc_list:
                # LOG(DEBUG, LOC(), cmporder_j, show=True)

                vis.cmporder += 1
                if eaexit:
                    break

                # reuse
                if getCmpidOrder(stcmpid_ki, cmporder_j) in sch.pass_cmp_dict:
                    Mutator.mutLocFromMap(
                        init_seed, init_seed, path.seeds_mutate,
                        ST_STR + str(vis.loop), sch.pass_cmp_dict[getCmpidOrder(stcmpid_ki, cmporder_j)].inputmap
                    )
                    break

                '''sd -> Sliding Window Detection O(n/step)'''
                # Get a report on changes to comparison instructions.
                slid_list = sch.loc_coarse_list
                slid_window = max(len(slid_list) // SCH_SLID_SLICE, SCH_SLID_MIN)
                b4_slid_window = max(len(slid_list) // SCH_SLID_SLICE, SCH_SLID_MIN) + SLID_GAP + 1
                # before_sdloc_list = []
                cmpmaploc_dict = {}
                # multiprocessing multi slidling windows.
                while b4_slid_window - slid_window > SLID_GAP:
                    coarse_head = 0
                    cmpmaploc_dict = {}
                    b4_slid_window = slid_window
                    LOG(DEBUG, LOC(), b4_slid_window, slid_window, cmpmaploc_dict, slid_list)
                    while coarse_head < len(slid_list):

                        # 1 seed inputs
                        sdloc_list = slid_list[coarse_head:coarse_head + slid_window]
                        # print(sdloc_list)
                        # coarse_head += slid_window // 2
                        coarse_head += slid_window
                        sd_seed = Mutator.mutSelectChar(
                            init_seed.content, path.seeds_mutate, COARSE_STR + str(vis.loop), sdloc_list)
                        sd_seed = sch.selectOneSeed(SCH_THISMUT_SEED, sd_seed)
                        sd_stdout, sd_stderr = Executor.runTimeLimit(fuzz_command.replace(REPLACE_COMMAND, sd_seed.filename), vis)
                        # sch.saveCrash(sd_seed, sd_stdout, sd_stderr, vis)
                        # 5 visualize
                        res = vis.display(sd_seed, set(sdloc_list), sd_stdout, sd_stderr, STG_SD, stcmpid_weight, sch)
                        # vis.showGraph(path.data_graph, cggraph, cfggraph_dict['main'])
                        if res == VIS_Q:
                            sch.quitFuzz()
                        eaexit = sch.saveCrash(sd_seed, sd_stdout, sd_stderr, vis)

                        # 1 seed inputs
                        sd_interlen, sd_covernum = ana.getShm(sd_stdout[0:16])
                        sd_cmpcov_list = ana.getRpt(sd_interlen)  # report

                        LOG(DEBUG, LOC(), sd_seed.content, init_cmpcov_list, sd_cmpcov_list, cmporder_j)
                        # Add number of bytes.
                        if ana.compareRptDiff(init_cmpcov_list, sd_cmpcov_list, cmporder_j):
                            # Determine if the dictionary is empty.
                            if stcmpid_ki not in cmpmaploc_dict:
                                # cmpmaploc_dict[stcmpid_ki] = set(before_sdloc_list) | set(sdloc_list)
                                cmpmaploc_dict[stcmpid_ki] = set(sdloc_list)
                            else:
                                cmpmaploc_dict[stcmpid_ki] |= set(sdloc_list)

                        # LOG(DEBUG, LOC(), init_cmpcov_list, sd_cmpcov_list, cmporder_j, slid_window, len(cmpmaploc_dict), len(sdloc_list))
                    if stcmpid_ki in cmpmaploc_dict:
                        slid_list = list(cmpmaploc_dict[stcmpid_ki])
                        slid_list.sort()

                    if len(slid_list) == sch.loc_coarse_list or stcmpid_ki not in cmpmaploc_dict:
                        break

                    slid_window = max(len(slid_list) // SCH_SLID_SLICE, SCH_SLID_MIN)

                    # before_sdloc_list = sdloc_list
                # LOG(DEBUG, LOC(), init_seed.content, cmpmaploc_dict, show=True)

                # raise Exception()
                '''sd <-'''
                # False positive comparison if all input bytes are covered
                # if len(stloclist_v) == len(init_seed.content):
                #     continue

                # Skip fix cmp
                LOG(DEBUG, LOC(), stcmpid_weight, stcmpid_ki, stcmpid_loci, cmpmaploc_dict)
                sch.updateInvalidCmp(stcmpid_ki)
                if sch.skipInvalidState(stcmpid_ki, cmpmaploc_dict):
                    continue

                sch.clearInvalidCmp(stcmpid_ki)


                stlocset_vi = cmpmaploc_dict[stcmpid_ki]
                stloclist_v = list(stlocset_vi)
                stloclist_v.sort()


                ststart_seed = Structures.StructSeed(
                    path.seeds_mutate + getMutfilename(ST_STR + str(vis.loop)), init_seed.content, SEED_INIT, set())
                ststart_seed = sch.selectOneSeed(SCH_THIS_SEED, ststart_seed)
                ststart_stdout, ststart_stderr = Executor.runTimeLimit(fuzz_command.replace(REPLACE_COMMAND, ststart_seed.filename), vis)
                sch.saveCrash(ststart_seed, ststart_stdout, ststart_stderr, vis)

                ststart_interlen, ststart_covernum = ana.getShm(ststart_stdout[0:16])
                ststart_cmpcov_list = ana.getRpt(ststart_interlen)

                # # Removal of unmapped changes
                # repeat_seed = Structures.StructSeed(
                #     path.seeds_mutate + getMutfilename(REPEAT_STR + str(vis.loop)), init_seed.content, SEED_INIT, set())
                # repeat_seed = sch.selectOneSeed(SCH_THIS_SEED, repeat_seed)
                # repeat_stdout, repeat_stderr = Executor.run(fuzz_command.replace(REPLACE_COMMAND, repeat_seed.filename), vis)
                #
                # repeat_interlen, repeat_covernum = ana.getShm(repeat_stdout[0:16])
                # repeat_cmpcov_list = ana.getRpt(repeat_interlen)
                #
                # if ana.compareRptDiff(ststart_cmpcov_list, repeat_cmpcov_list, -1):
                #     continue

                '''bd -> Byte Detection O(m)'''
                # Single-byte comparison in order
                st_cmploc = []
                for one_loc in stloclist_v:

                    bdloc_list = [one_loc, ]
                    bd_seed = Mutator.mutOneChar(ststart_seed.content, path.seeds_mutate, FINE_STR + str(vis.loop),
                                                 bdloc_list)
                    bd_seed = sch.selectOneSeed(SCH_THISMUT_SEED, bd_seed)
                    bd_stdout, bd_stderr = Executor.runTimeLimit(fuzz_command.replace(REPLACE_COMMAND, bd_seed.filename), vis)
                    # sch.saveCrash(bd_seed, bd_stdout, bd_stderr, vis)
                    # 5 visualize
                    res = vis.display(bd_seed, set(st_cmploc), bd_stdout, bd_stderr, STG_BD, stcmpid_weight, sch)
                    # vis.showGraph(path.data_graph, cggraph, cfggraph_dict['main'])
                    if res == VIS_Q:
                        sch.quitFuzz()
                    eaexit = sch.saveCrash(bd_seed, bd_stdout, bd_stderr, vis)

                    bd_interlen, bd_covernum = ana.getShm(bd_stdout[0:16])
                    bd_cmpcov_list = ana.getRpt(bd_interlen)

                    LOG(DEBUG, LOC(), ststart_cmpcov_list, bd_cmpcov_list, cmporder_j)
                    if len(bd_cmpcov_list) != 0 and ana.compareRptDiff(ststart_cmpcov_list, bd_cmpcov_list, cmporder_j):
                        st_cmploc.append(one_loc)

                # LOG(DEBUG, LOC(), st_cmploc, loop_mutloc, len(set(st_cmploc) - loop_mutloc), show=True)
                # Early exit if all location is mutated.
                if len(set(st_cmploc) - loop_mutloc) <= 0:
                    break
                if len(loop_mutloc) == len(ststart_seed.content):
                    eaexit = True
                loop_mutloc = set(st_cmploc) | loop_mutloc

                '''bd <-'''

                ana.sendCmpid(stcmpid_ki)
                # Identification Type and Update opt seed (in Random change)
                # init_seed opt_seed

                opt_seed = sch.selectOneSeed(SCH_THIS_SEED, init_seed)
                opt_stdout, opt_stderr = Executor.runTimeLimit(fuzz_command.replace(REPLACE_COMMAND, opt_seed.filename), vis)
                sch.saveCrash(opt_seed, opt_stdout, opt_stderr, vis)
                opt_interlen, opt_covernum = ana.getShm(opt_stdout[0:16])
                opt_cmpcov_list = ana.getRpt(opt_interlen)


                st_seed = Mutator.mutSelectCharRand(
                    init_seed.content, path.seeds_mutate, ST_STR + str(vis.loop), st_cmploc)
                st_seed = sch.selectOneSeed(SCH_THIS_SEED, st_seed)
                st_stdout, st_stderr = Executor.runTimeLimit(fuzz_command.replace(REPLACE_COMMAND, st_seed.filename), vis)
                eaexit = sch.saveCrash(st_seed, st_stdout, st_stderr, vis)
                st_interlen, st_covernum = ana.getShm(st_stdout[0:16])
                st_cmpcov_list = ana.getRpt(st_interlen)

                if len(loop_mutloc) == len(st_seed.content):
                    eaexit = True

                # 3 cmp type
                # Return cmp type and mutate strategy according to typeDetect
                '''Type detect and Generate Mutation strategy'''
                strategy_flag, cmp_flag, bytes_flag = Parser.typeDetect(
                    opt_cmpcov_list, st_cmpcov_list, cmporder_j)
                infer_strategy = Parser.devStrategy(
                    opt_cmpcov_list, cmporder_j, strategy_flag, cmp_flag, bytes_flag, st_cmploc)
                sch.strategyq.put(infer_strategy)

                LOG(DEBUG, LOC(), infer_strategy.curloop, infer_strategy.endloop, infer_strategy.strategytype)
                if bytes_flag == PAR_FIXAFIX:
                    continue
                # LOG(DEBUG, LOC(), opt_cmpcov_list, ststart_cmpcov_list, cmporder_j, show=True)
                LOG(DEBUG, LOC(), strategy_flag, bytes_flag, opt_cmpcov_list[cmporder_j], ststart_cmpcov_list[cmporder_j], show=True)

                # fixme
                # opt_seed = Mutator.mutLocFromMap(opt_seed, opt_seed, path.seeds_mutate, ST_STR + str(vis.loop),
                #                                  {1:b'\x65',2:b'\x65', 3:b'\x65'})
                # opt_seed = sch.selectOneSeed(SCH_THIS_SEED, opt_seed)
                # opt_stdout, opt_stderr = Executor.run(fuzz_command.replace(REPLACE_COMMAND, opt_seed.filename))
                # eaexit = sch.saveCrash(opt_seed, opt_stdout, opt_stderr, vis)
                #
                # opt_interlen, opt_covernum = ana.getShm(opt_stdout[0:16])
                # opt_cmpcov_list = ana.getRpt(opt_interlen)

                '''Mutation strategy and Compare distance'''
                strategy = None
                while not eaexit and (not sch.strategyq.empty() or strategy != None):
                    if strategy == None:
                        strategy = sch.strategyq.get()

                    LOG(DEBUG, LOC(), strategy.curloop, strategy.endloop)
                    # Type Detection and Breaking the Constraint Cycle (At lease 1 loops)
                    if strategy.curloop >= strategy.endloop:
                        strategy = None
                        continue

                    strategy.curloop += 1
                    strategy.curnum = 0
                    LOG(DEBUG, LOC(), eaexit)
                    if strategy.strategytype == STAT_FIN:
                        cmpid_order = getCmpidOrder(stcmpid_ki, cmporder_j)
                        if cmpid_order not in sch.pass_cmp_dict:
                            sch.pass_cmp_dict[cmpid_order] = \
                                Structures.StructCmpInfo(stcmpid_ki, cmporder_j,
                                                         getLocInputValue(opt_seed.content, st_cmploc))
                        # sch.freeze_bytes = sch.freeze_bytes.union(set(st_cmploc))  # don't need it
                        ana.sendCmpid(stcmpid_ki)
                        opt_stdout, opt_stderr = Executor.runTimeLimit(fuzz_command.replace(REPLACE_COMMAND, opt_seed.filename), vis)
                        sch.saveCrash(opt_seed, opt_stdout, opt_stderr, vis)
                        if len(opt_stderr) == 0:
                            sch.addq(SCH_LOOP_SEED, [opt_seed, ],
                                     calPriotiryValue(stcmpid_weight, st_covernum, len(opt_seed.content)))
                        break

                    while not eaexit and strategy.curnum < strategy.endnum:

                        # Change the first mutate seed. Other status will use opt_seed.
                        if strategy.curnum == 0:
                            locmapdet_dict = Parser.solveChangeMap(
                                strategy, st_cmploc, st_seed, st_cmpcov_list, cmporder_j)
                        else:
                            locmapdet_dict = Parser.solveChangeMap(
                                strategy, st_cmploc, opt_seed, opt_cmpcov_list, cmporder_j)

                        vis.change_map = locmapdet_dict
                        # The next mutate seed
                        # Passing the constraint based on the number of cycles and the distance between comparisons.
                        if len(locmapdet_dict) == 0:
                            st_seed = st_seed
                        elif strategy.curnum == 0:
                            st_seed = Mutator.mutLocFromMap(
                                init_seed, st_seed,
                                path.seeds_mutate, ST_STR + str(vis.loop), locmapdet_dict
                            )
                            st_seed = sch.selectOneSeed(SCH_THISMUT_SEED, st_seed)
                        else:
                            st_seed = Mutator.mutLocFromMap(
                                init_seed, opt_seed,
                                path.seeds_mutate, ST_STR + str(vis.loop), locmapdet_dict
                            )
                            st_seed = sch.selectOneSeed(SCH_THISMUT_SEED, st_seed)
                        LOG(DEBUG, LOC(), st_seed.content, opt_seed.content, locmapdet_dict)
                        LOG(DEBUG, LOC(), fuzz_command.replace(REPLACE_COMMAND, st_seed.filename))
                        ana.sendCmpid(stcmpid_ki)
                        st_stdout, st_stderr = Executor.runTimeLimit(fuzz_command.replace(REPLACE_COMMAND, st_seed.filename), vis)
                        # sch.saveCrash(st_seed, st_stdout, st_stderr, vis)
                        LOG(DEBUG, LOC(), "after run")
                        # 5 visualize
                        res = vis.display(
                            st_seed, set(st_cmploc), st_stdout, st_stderr, STG_ST, stcmpid_weight, sch)
                        # vis.showGraph(path.data_graph, cggraph, cfggraph_dict['main'])
                        if res == VIS_Q:
                            sch.quitFuzz()
                        eaexit = sch.saveCrash(st_seed, st_stdout, st_stderr, vis)

                        # 2 cmp instruction
                        # Generate analysis reports.
                        st_interlen, st_covernum = ana.getShm(st_stdout[0:16])
                        vis.coverage_num = st_covernum

                        st_cmpcov_list = ana.getRpt(st_interlen)
                        # Returns the status and the character to be mutated
                        # Comparison of global optimal values to achieve updated parameters
                        opt_seed, opt_cmpcov_list, exe_status = Parser.solveDistance(
                            strategy, opt_seed, st_seed, opt_cmpcov_list, st_cmpcov_list, cmporder_j)
                        # LOG(DEBUG, LOC(), opt_cmpcov_list, st_cmpcov_list, cmporder_j, show=True)
                        LOG(DEBUG, LOC(), locmapdet_dict, exe_status, locmapdet_dict, opt_cmpcov_list[cmporder_j], show=True)

                        strategy.curnum += 1
                        if exe_status == DIST_FINISH:
                            cmpid_order = getCmpidOrder(stcmpid_ki, cmporder_j)
                            if cmpid_order not in sch.pass_cmp_dict:
                                sch.pass_cmp_dict[cmpid_order] = \
                                    Structures.StructCmpInfo(stcmpid_ki, cmporder_j,
                                                             getLocInputValue(opt_seed.content, st_cmploc))
                            # sch.freeze_bytes = sch.freeze_bytes.union(set(st_cmploc))  # don't need it
                            ana.sendCmpid(TRACE_GUARDFAST)
                            trace_stdout, trace_stderr = Executor.runTimeLimit(fuzz_command.replace(REPLACE_COMMAND, opt_seed.filename), vis)
                            LOG(DEBUG, LOC(), trace_stdout, trace_stderr)
                            eaexit = sch.saveCrash(opt_seed, trace_stdout, trace_stderr, vis)


                            # if len(opt_stderr) == 0:
                            trace_interlen, trace_covernum = ana.getShm(trace_stdout[0:16])
                            trace_guard_list = ana.getRpt(trace_interlen)
                            near_dis = sch.findNearDistance(
                                trace_guard_list, map_tgtpredgvid_dis, tgtpred_offset, map_guard_gvid)
                            LOG(DEBUG, LOC(), near_dis, sch.cur_nearlydis)
                            if near_dis < sch.cur_nearlydis:
                                eaexit = True
                            sch.addq(SCH_LOOP_SEED, [opt_seed, ],
                                     calPriotiryValue(near_dis, st_covernum, len(opt_seed.content)))
                            LOG(DEBUG, LOC(), eaexit, strategy.curloop, strategy.endloop, near_dis, sch.cur_nearlydis)
                            ana.sendCmpid(stcmpid_ki)
                            break
                        elif len(locmapdet_dict) == 0 or exe_status == DIST_FAIL:
                            break

                        # According covernum and distance directly change the seed which is execution.
                        LOG(DEBUG, LOC(), st_covernum, loop_covernum, st_seed.content, opt_seed.content,
                            loop_mutloc, show=True)
                        if st_covernum > loop_covernum:
                            ana.sendCmpid(TRACE_GUARDFAST)
                            cur_stdout, cur_stderr = Executor.runTimeLimit(fuzz_command.replace(REPLACE_COMMAND, st_seed.filename), vis)
                            sch.saveCrash(st_seed, cur_stdout, cur_stderr, vis)
                            cur_interlen, cur_covernum = ana.getShm(cur_stdout[0:16])
                            cur_guard_list = ana.getRpt(cur_interlen)
                            cur_dis = sch.findNearDistance(
                                cur_guard_list, map_tgtpredgvid_dis, tgtpred_offset, map_guard_gvid)
                            LOG(DEBUG, LOC(), cur_dis, sch.cur_nearlydis, loop_covernum, st_covernum, show=True)
                            if cur_dis <= sch.cur_nearlydis:
                                sch.cur_nearlydis = cur_dis
                                LOG(DEBUG, LOC(), opt_seed.content, st_seed.content, cur_dis, stcmpid_weight, cur_covernum, vis.loop, loop_mutloc, show=True)
                                opt_seed = st_seed

                                sch.addq(SCH_LOOP_SEED, [st_seed, ],
                                         calPriotiryValue(cur_dis, cur_covernum, len(st_seed.content)))
                                loop_covernum = cur_covernum

                    sch.deleteSeeds(SCH_THISMUT_SEED)

        '''Mutation all location.'''
        # Again sufficient mutation according to the index
        # Missed byte
        if eaexit == False:
            miss_set = set([i for i in range(0, len(init_seed.content))]) - loop_mutloc
            # LOG(DEBUG, LOC(), len(init_seed.content), loop_mutloc, miss_set, show=True)
            # raise Exception()

            # mutated byte*bitlen counts, only monitor coverage and distance.
            # for bytes_loc in miss_set:
            for bytes_loc in range(0, len(opt_seed.content)):
                for change_loc in range(0, MUT_BIT_LEN):
                    if change_loc in MUT_SKIP:
                        continue
                    locmapdet_dict = {}
                    locmapdet_dict[bytes_loc] = BYTES_ASCII[change_loc]

                    miss_seed = Mutator.mutLocFromMap(
                        init_seed, opt_seed,
                        path.seeds_mutate, MISS_STR + str(vis.loop), locmapdet_dict
                    )

                    miss_seed = sch.selectOneSeed(SCH_THISMUT_SEED, miss_seed)
                    miss_stdout, miss_stderr = Executor.runTimeLimit(
                        fuzz_command.replace(REPLACE_COMMAND, miss_seed.filename), vis)
                    sch.saveCrash(miss_seed, miss_stdout, miss_stderr, vis)
                    res = vis.display(miss_seed, set([change_loc]), miss_stdout, miss_stderr, STG_MS, sch.cur_nearlydis, sch)
                    # vis.showGraph(path.data_graph, cggraph, cfggraph_dict['main'])
                    if res == VIS_Q:
                        sch.quitFuzz()
                    miss_interlen, miss_covernum = ana.getShm(miss_stdout[0:16])
                    LOG(DEBUG, LOC(), sch.cur_nearlydis, loop_covernum, miss_covernum, miss_seed.content, show=True)
                    # if miss_covernum > loop_covernum or abs(miss_covernum - loop_covernum) >= GAP_VALUE:
                    if miss_covernum > loop_covernum:
                        ana.sendCmpid(TRACE_GUARDFAST)
                        cur_stdout, cur_stderr = Executor.runTimeLimit(
                            fuzz_command.replace(REPLACE_COMMAND, miss_seed.filename), vis)
                        sch.saveCrash(miss_seed, cur_stdout, cur_stderr, vis)

                        cur_interlen, cur_covernum = ana.getShm(cur_stdout[0:16])
                        cur_guard_list = ana.getRpt(cur_interlen)
                        cur_dis = sch.findNearDistance(
                            cur_guard_list, map_tgtpredgvid_dis, tgtpred_offset, map_guard_gvid)
                        res = vis.display(miss_seed, set([change_loc]), cur_stdout, cur_stderr, STG_MS, cur_dis, sch)
                        # vis.showGraph(path.data_graph, cggraph, cfggraph_dict['main'])
                        if res == VIS_Q:
                            sch.quitFuzz()
                        LOG(DEBUG, LOC(), cur_dis, sch.cur_nearlydis, loop_covernum, miss_covernum, miss_seed.content, show=True)
                        if cur_dis <= sch.cur_nearlydis:
                            sch.cur_nearlydis = cur_dis
                            opt_seed = miss_seed

                            sch.addq(SCH_LOOP_SEED, [miss_seed, ],
                                     calPriotiryValue(cur_dis, cur_covernum, len(miss_seed.content)))
                            loop_covernum = cur_covernum

        # raise Exception()
        # Endless fuzzing, add the length seed.
        LOG(DEBUG, LOC(), init_seed.content)
        sch.targetcmp_pq.queue.clear()
        sch.deleteSeeds(SCH_THIS_SEED)
        if sch.seedq.empty():
            sch.addq(SCH_LOOP_SEED, [init_seed, ], calPriotiryValue(loop_weight, init_covernum, len(init_seed.content)))

        # xxx = 0
        # if xxx < 1:
        #     xxx += 1
        # else:
        #     while not sch.seedq.empty():
        #         tmp_seed = sch.seedq.get()
        #         LOG(DEBUG, LOC(), tmp_seed[0], tmp_seed[1].content,show=True)
        #     raise Exception
        # while not sch.seedq.empty():
        #     tmp_seed = sch.seedq.get()
        #     LOG(DEBUG, LOC(), tmp_seed[0], tmp_seed[1].content,show=True)
        # raise Exception

        # Mutual mapping relationship
        # Key: cmpid  Value: branch_order cmp_type input_bytes branches
        # 4 branches
        # raise Exception()

    sch.deleteSeeds(SCH_THIS_SEED)
    sch.deleteSeeds(SCH_THISMUT_SEED)
    vis.visquit()
    time.sleep(1)
    print()
    if len(sch.target_crashinfo) == 0:
        print("{} No Target.".format(getTime()))
    else:
        for idx, info in enumerate(sch.target_crashinfo):
            print("-{}-> {}".format(idx, info))
        print("{} (^_^)# Target vulnerability successfully reproduced.".format(getTime()))
    print()


if __name__ == "__main__":
    mainFuzzer()
    # python3 STFGFuzzer.py -n demo -- ./Programs/demo/code_Bin/demo -f @@
    # python3 STFGFuzzer.py -n base64 -- ./Programs/base64/code_Bin/base64 -d @@

    # dot -Tpng CG.gv -o output.png

    # Handle Segmentation fault.  Generator the core files.
    # ulimit -c unlimited
    # python3 -X faulthandler my.py

    # std_out, std_err = Executor.run("./Programs/base64/code_Bin/base64 -d Programs/base64/seeds_crash/validate_inputs/utmp-fuzzed-222.b64")
    # print(std_out, std_err)
