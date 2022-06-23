#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import faulthandler  # Use to find Segmentation Fault
import time

faulthandler.enable()

from fuzzer_module import *
from fuzzer_module.Fuzzconfig import *


# Close Address Space Layout Randomization.
# echo 0 > /proc/sys/kernel/randomize_va_space

# python3.7 STFGFuzzer.py -n demo -t sanitizer -- ./Programs/demo/code_Bin/demo -f @@
# python3.7 STFGFuzzer.py -n base64 -- ./Programs/base64/code_Bin/base64 -d @@
# python3.7 STFGFuzzer.py -n md5sum -- ./Programs/md5sum/code_Bin/md5sum -c @@
# python3.7 STFGFuzzer.py -n uniq -- ./Programs/uniq/code_Bin/uniq @@
# python3.7 STFGFuzzer.py -n who -- ./Programs/who/code_Bin/who @@
# python3.7 STFGFuzzer.py -n lava13796 -t sanitizer -- Programs/lava13796/code_Bin/lava13796 @@

def mainFuzzer():
    """
    The fuzzing Loop.
    @return:
    """
    print("{} Start Directed Fuzzing...".format(getTime()))
    stdout, stderr = Executor.run("cat /proc/sys/kernel/randomize_va_space")  # Default 2
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
    binline_dict = Builder.getBinaryInfo(path.data_graph)
    target_dict = Comparator.getTarget(path.data_patchloc, patchtype)
    map_numto_funcasm = Comparator.getDirectedNodeLoc(binline_dict, target_dict)
    sch = Scheduler.Scheduler()

    for tgt_ki, stu_vi in target_dict.items():
        sch.target_dict[tgt_ki] = set()
        for info_j in stu_vi.tgttrace:
            sch.target_dict[tgt_ki].add(str(info_j[1])+str(info_j[2]))
    LOG(LOG_DEBUG, LOG_FUNCINFO(), target_dict[0].tgtinfolen, map_numto_funcasm, sch.target_dict)
    del target_dict
    del binline_dict

    # Graph Information
    print("{} Build Graph Information...".format(getTime()))
    cglist, cfglist = Generator.createDotJsonFile(program_name, path.code_IR + program_name + GEN_TRACEBC_SUFFIX)
    cggraph, map_functo_cgnode = Builder.getCG(cglist)
    cfggraph_dict, map_guard_gvid, map_target = Builder.getCFG(cfglist, map_numto_funcasm)
    LOG(LOG_DEBUG, LOG_FUNCINFO(), map_guard_gvid, map_target)
    '''All node transfrom to the gvid to convenient calculation and expression.'''
    '''All the function name transfrom to the static symbol function name.'''
    '''Dynamic:guard  Static:gvid'''
    '''Dynamic:func  Static:symbol'''
    # map_target {0: {'_Z3bugv': [[0, [0], 0]], 'main': [[1, [31], 32]]}}
    Builder.buildBFSdistance(cggraph, cfggraph_dict)  # Build the distance between two nodes.
    map_tgtpredgvid_dis = Builder.getTargetPredecessorsGuard(cfggraph_dict, map_guard_gvid, map_target)
    tgtpred_offset = Builder.getFuncOffset(map_tgtpredgvid_dis, map_target)

    if len(map_target) != 0:
        sch.all_tgtnum = len(map_target)
    for k in map_functo_cgnode.keys():
        sch.trans_symbol_initguard[k] = USE_INITMAXNUM

    print("{} Directed Target Sequence...".format(getTime()))
    trace_orderdict = Builder.printTargetSeq(map_target)

    LOG(LOG_DEBUG, LOG_FUNCINFO(), map_guard_gvid, map_target, map_tgtpredgvid_dis)

    sch.file_crash_csv = file_crash_csv
    sch.path_crashseeds = path.seeds_crash
    # Init Loop Variables

    # Init seed lists
    print("{} Init Seed lists...".format(getTime()))
    init_seeds_list = Generator.prepareEnv(program_name)
    if len(init_seeds_list) > 0:
        temp_listq = []
        for each in init_seeds_list:
            temp_listq.append(
                Structures.StructSeed(path.seeds_mutate + each, readContent(path.seeds_mutate + each), SEED_INIT,
                                      set()))
        sch.addq(SCH_LOOP_SEED, temp_listq)
    else:
        sch.addq(SCH_LOOP_SEED,
                 [Structures.StructSeed(path.seeds_mutate + AUTO_SEED, USE_INITCONTENT, SEED_INIT, set()), ])

    # Create Memory Share.
    ana = Analyzer.Analyzer()
    create_seed = sch.selectOneSeed(
        SCH_THISMUT_SEED,
        Structures.StructSeed(path.seeds_mutate + AUTO_SEED, Mutator.getFillStr(64), SEED_INIT, set()))
    create_stdout, create_stderr = Executor.run(fuzz_command.replace('@@', create_seed.filename))
    ana.getShm(create_stdout[0:16])
    LOG(LOG_DEBUG, LOG_FUNCINFO(), create_seed.content)

    '''Fuzzing Cycle'''
    print("{} Fuzzing Loop...".format(getTime()))
    vis = Visualizer.Visualizer()
    vis.trace_orderdict = trace_orderdict
    # vis.showGraph(path.data_graph, cggraph, cfggraph_dict['main'])
    while sch.cur_tgtnum < sch.all_tgtnum and not sch.seedq.empty():
        eaexit = False
        vis.loop += 1

        # # Guard
        # ana.sendCmpid(TRACE_CMPGUARD)
        # init_stdout, init_stderr = Executor.run(fuzz_command.replace('@@', init_seed.filename))
        # sch.saveCrash(init_seed, init_stdout, init_stderr, vis.start_time, vis.last_time)
        # init_interlen, init_covernum = ana.getShm(init_stdout[0:16])
        # init_guardcov_list = ana.getRpt(init_interlen)
        # guard_set, guard_total = ana.traceGuardAnalysis(init_guardcov_list)
        # sch.coveragepath = guard_set
        # vis.num_pcguard = guard_total

        ana.sendCmpid(TRACE_CMP)
        # First run to collect information.
        vis.total += 1
        init_seed = sch.selectOneSeed(SCH_LOOP_SEED)
        init_stdout, init_stderr = Executor.run(fuzz_command.replace('@@', init_seed.filename))
        init_interlen, init_covernum = ana.getShm(init_stdout[0:16])
        # cmpcov_list = ana.getRpt(init_interlen)
        # initrpt_dict, initrpt_set = ana.traceAyalysis(cmpcovcont_list, sch.freezeid_rpt, sch) todo

        # Select the location to be mutated and add it to the location queue.
        sch.initEachloop(vis)

        '''Find correspondence: seed inputs -> cmp instruction -> cmp type (access method) -> braches'''

        '''ld -> Length Detection, Increase seed length'''
        # Increase the input length when the number of constraints does not change in the program.
        # If there is a change in the increase length then increase the length.
        b4ld_seed = init_seed
        b4ld_interlen = init_interlen
        LOG(LOG_DEBUG, LOG_FUNCINFO(), init_seed.content, ana.getRpt(init_interlen), showlog=True)
        while len(b4ld_seed.content) < sch.expand_size:
            vis.total += 1
            sch.expandnums += 1
            # if before_coverage == sch.coveragepath and len(init_seed.content) < SCH_EXPAND_MAXSIZE:
            # According fixed length to expand the content length of seed.
            ld_seed = Mutator.mutAddLength(b4ld_seed.content, path.seeds_mutate, LENGTH_STR, LD_EXPAND)
            ld_seed = sch.selectOneSeed(SCH_THISMUT_SEED, ld_seed)
            ld_stdout, ld_stderr = Executor.run(fuzz_command.replace('@@', ld_seed.filename))
            sch.saveCrash(ld_seed, ld_stdout, ld_stderr, vis)

            # 1 seed inputs
            ld_interlen, ld_covernum = ana.getShm(ld_stdout[0:16])
            LOG(LOG_DEBUG, LOG_FUNCINFO(), len(ld_seed.content), b4ld_interlen, ld_interlen)
            LOG(LOG_DEBUG, LOG_FUNCINFO(), ana.getRpt(ld_interlen))
            if b4ld_interlen != ld_interlen:
                b4ld_seed = ld_seed
                b4ld_interlen = ld_interlen
            elif b4ld_interlen == ld_interlen:
                # Current seed.
                ld_cmpcov_list = ana.getRpt(ld_interlen)  # report
                # Before seed.
                vis.total += 1
                b4ld_stdout, b4ld_stderr = Executor.run(fuzz_command.replace('@@', b4ld_seed.filename))
                b4ld_interlen, b4ld_covernum = ana.getShm(b4ld_stdout[0:16])
                b4ld_cmpcov_list = ana.getRpt(b4ld_interlen)
                LOG(LOG_DEBUG, LOG_FUNCINFO(), b4ld_cmpcov_list)
                if ld_cmpcov_list != b4ld_cmpcov_list:
                    b4ld_seed = ld_seed
                    b4ld_interlen = ld_interlen
                else:
                    break

            res = vis.display(ld_seed, set(), ld_stdout, ld_stderr, STG_LD, -1, sch)
            vis.showGraph(path.data_graph, cggraph, cfggraph_dict['main'])
            if res == VIS_Q:
                sch.quitFuzz()
        '''ld <-'''

        '''2 cmp filter -> Select compare instructions which close the target block. '''
        ana.sendCmpid(TRACE_CMPGUARDSYMBOL)
        # Reset the init_seed
        vis.total += 1
        init_seed = sch.selectOneSeed(SCH_THIS_SEED, b4ld_seed)
        init_stdout, init_stderr = Executor.run(fuzz_command.replace('@@', init_seed.filename))
        sch.saveCrash(init_seed, init_stdout, init_stderr, vis)

        # Get all the constraints.
        # Binary files each function blocks from 0.
        # Execution files each function blocks from n.
        # Get the offset of the address block.
        init_interlen, init_covernum = ana.getShm(init_stdout[0:16])
        init_guardcov_list = ana.getRpt(init_interlen)
        LOG(LOG_DEBUG, LOG_FUNCINFO(), init_guardcov_list, sch.trans_symbol_initguard, showlog=True)
        guard_set, guard_total = ana.getGuardNum(init_guardcov_list)
        sch.coverage_set = sch.coverage_set | guard_set
        vis.num_pcguard = guard_total

        # Update sch priority queue. Save cmpid for the next explore
        LOG(LOG_DEBUG, LOG_FUNCINFO(), map_tgtpredgvid_dis, tgtpred_offset, map_guard_gvid)
        sch.selectConstraint(init_guardcov_list, map_tgtpredgvid_dis, tgtpred_offset, map_guard_gvid, vis)
        # raise Exception()

        # init_cmp_dict = ana.traceAyalysis(init_cmpcov_list, sch.skip_cmpidset)
        # init_cmpset = set(init_cmp_dict)
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

        # Compare instruction type speculation based on input mapping,
        # then try to pass the corresponding constraint (1-2 rounds).
        LOG(LOG_DEBUG, LOG_FUNCINFO(), sch.targetcmp_pq)
        # while not sch.target_cmp.empty():
        #     LOG(LOG_DEBUG, LOG_FUNCINFO(), sch.target_cmp.get(), showlog=True)
        # raise Exception()

        '''Init status parameters.'''
        vis.cmptotal = sch.targetcmp_pq.qsize()
        sch.slid_window = max(len(sch.loc_coarse_list) // SCH_SLID_COUNT, SCH_SLID_MIN)
        # Update the min distance of target.
        if not sch.targetcmp_pq.empty():
            tempcmpid = sch.targetcmp_pq.get()
            sch.targetcmp_pq.put(tempcmpid)
            sch.cur_nearlydis = tempcmpid[0]

        '''3 cmp type'''
        '''st -> Constraints Analysis'''
        # Select one stcmpid_tuples.
        # for stcmpid_ki, stlocset_vi in cmpmaploc_dict.items():
        while not eaexit and not sch.targetcmp_pq.empty():

            stcmpid_tuples = sch.targetcmp_pq.get()
            stcmpid_weight, stcmpid_ki = stcmpid_tuples[0], stcmpid_tuples[1]
            LOG(LOG_DEBUG, LOG_FUNCINFO(), stcmpid_weight, stcmpid_ki, showlog=True)
            vis.cmpnum += 1
            # limiter
            if stcmpid_weight - sch.cur_nearlydis >= LIMITER:
                break

            ana.sendCmpid(stcmpid_ki)

            # Debug
            # filter = ["g0x4f99810x52a8b80x529492"]
            # print(".", end="")
            # if stcmpid_tuples not in filter:
            #     continue
            # print(stcmpid_tuples)

            # First run init seed after cmp filter.
            vis.total += 1
            init_stdout, init_stderr = Executor.run(fuzz_command.replace('@@', init_seed.filename))
            init_interlen, init_covernum = ana.getShm(init_stdout[0:16])
            init_cmpcov_list = ana.getRpt(init_interlen)
            # init_cmp_dict = ana.traceAyalysis(init_cmpcov_list, sch.skip_cmpidset)

            # Only the corresponding list data is retained, no parsing is required
            cmp_len = len(init_cmpcov_list)
            # Separate comparisons for each comparison instruction.
            for cmporder_j in range(0, cmp_len):
                if eaexit:
                    break

                if getCmpidOrder(stcmpid_ki, cmporder_j) in sch.pass_cmp_dict:
                    Mutator.mutLocFromMap(
                        init_seed, init_seed.content, path.seeds_mutate,
                        ST_STR + str(vis.loop), sch.pass_cmp_dict[getCmpidOrder(stcmpid_ki, cmporder_j)].inputmap
                    )
                    break
                '''sd -> Sliding Window Detection O(n/step)'''
                # Get a report on changes to comparison instructions. # todo multiprocessing
                before_sdloc_list = []
                coarse_head = 0
                cmpmaploc_dict = {}
                while coarse_head < len(sch.loc_coarse_list):
                    vis.total += 1
                    # 1 seed inputs
                    sdloc_list = sch.loc_coarse_list[coarse_head:coarse_head + sch.slid_window]
                    # print(sdloc_list)
                    coarse_head += sch.slid_window // 2
                    sd_seed = Mutator.mutSelectChar(
                        init_seed.content, path.seeds_mutate, COARSE_STR + str(vis.loop), sdloc_list)
                    sd_seed = sch.selectOneSeed(SCH_THISMUT_SEED, sd_seed)
                    sd_stdout, sd_stderr = Executor.run(fuzz_command.replace('@@', sd_seed.filename))
                    sch.saveCrash(sd_seed, sd_stdout, sd_stderr, vis)

                    # 1 seed inputs
                    sd_interlen, sd_covernum = ana.getShm(sd_stdout[0:16])
                    sd_cmpcov_list = ana.getRpt(sd_interlen)  # report

                    # Add number of bytes.
                    if len(sd_cmpcov_list) == 0 or ana.compareRptDiff(init_cmpcov_list, sd_cmpcov_list, cmporder_j):
                        # Determine if the dictionary is empty.
                        if stcmpid_ki not in cmpmaploc_dict:
                            cmpmaploc_dict[stcmpid_ki] = set(before_sdloc_list) | set(sdloc_list)
                        else:
                            cmpmaploc_dict[stcmpid_ki] |= set(sdloc_list)

                    before_sdloc_list = sdloc_list

                    # 5 visualize
                    res = vis.display(sd_seed, set(sdloc_list), sd_stdout, sd_stderr, STG_SD, stcmpid_weight, sch)
                    vis.showGraph(path.data_graph, cggraph, cfggraph_dict['main'])
                    if res == VIS_Q:
                        sch.quitFuzz()
                LOG(LOG_DEBUG, LOG_FUNCINFO(), cmpmaploc_dict, showlog=True)
                # raise Exception()
                '''sd <-'''
                # False positive comparison if all input bytes are covered
                # if len(stloclist_v) == len(init_seed.content):
                #     continue

                # Skip fix cmp
                if stcmpid_ki not in cmpmaploc_dict:
                    continue
                stlocset_vi = cmpmaploc_dict[stcmpid_ki]
                stloclist_v = list(stlocset_vi)
                stloclist_v.sort()

                vis.total += 1
                ststart_seed = Structures.StructSeed(
                    path.seeds_mutate + getMutfilename(ST_STR + str(vis.loop)), init_seed.content, SEED_INIT, set())
                ststart_seed = sch.selectOneSeed(SCH_THIS_SEED, ststart_seed)
                ststart_stdout, ststart_stderr = Executor.run(fuzz_command.replace('@@', ststart_seed.filename))

                ststart_interlen, ststart_covernum = ana.getShm(ststart_stdout[0:16])
                ststart_cmpcov_list = ana.getRpt(ststart_interlen)

                # # Removal of unmapped changes
                # vis.total += 1
                # repeat_seed = Structures.StructSeed(
                #     path.seeds_mutate + getMutfilename(REPEAT_STR + str(vis.loop)), init_seed.content, SEED_INIT, set())
                # repeat_seed = sch.selectOneSeed(SCH_THIS_SEED, repeat_seed)
                # repeat_stdout, repeat_stderr = Executor.run(fuzz_command.replace('@@', repeat_seed.filename))
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
                    vis.total += 1
                    bdloc_list = [one_loc, ]
                    bd_seed = Mutator.mutOneChar(ststart_seed.content, path.seeds_mutate, FINE_STR + str(vis.loop),
                                                 bdloc_list)
                    bd_seed = sch.selectOneSeed(SCH_THISMUT_SEED, bd_seed)
                    bd_stdout, bd_stderr = Executor.run(fuzz_command.replace('@@', bd_seed.filename))
                    sch.saveCrash(bd_seed, bd_stdout, bd_stderr, vis)

                    bd_interlen, bd_covernum = ana.getShm(bd_stdout[0:16])
                    bd_cmpcov_list = ana.getRpt(bd_interlen)

                    LOG(LOG_DEBUG, LOG_FUNCINFO(), ststart_cmpcov_list, bd_cmpcov_list, cmporder_j)
                    if len(bd_cmpcov_list) != 0 and ana.compareRptDiff(ststart_cmpcov_list, bd_cmpcov_list, cmporder_j):
                        st_cmploc.append(one_loc)
                    # 5 visualize
                    res = vis.display(bd_seed, set(st_cmploc), bd_stdout, bd_stderr, STG_BD, stcmpid_weight, sch)
                    vis.showGraph(path.data_graph, cggraph, cfggraph_dict['main'])
                    if res == VIS_Q:
                        sch.quitFuzz()
                LOG(LOG_DEBUG, LOG_FUNCINFO(), ststart_cmpcov_list[cmporder_j], st_cmploc, cmp_len, cmporder_j, showlog=True)
                '''bd <-'''

                ana.sendCmpid(stcmpid_ki)
                # Identification Type and Update opt seed (in Random change)
                # init_seed opt_seed
                vis.total += 1
                opt_seed = sch.selectOneSeed(SCH_THIS_SEED, init_seed)
                opt_stdout, opt_stderr = Executor.run(fuzz_command.replace('@@', opt_seed.filename))
                opt_interlen, opt_covernum = ana.getShm(opt_stdout[0:16])
                opt_cmpcov_list = ana.getRpt(opt_interlen)

                vis.total += 1
                st_seed = Mutator.mutSelectCharRand(
                    init_seed.content, path.seeds_mutate, ST_STR + str(vis.loop), st_cmploc)
                st_seed = sch.selectOneSeed(SCH_THIS_SEED, st_seed)
                st_stdout, st_stderr = Executor.run(fuzz_command.replace('@@', st_seed.filename))
                sch.saveCrash(st_seed, st_stdout, st_stderr, vis)
                st_interlen, st_covernum = ana.getShm(st_stdout[0:16])
                st_cmpcov_list = ana.getRpt(st_interlen)

                # 3 cmp type
                # Return cmp type and mutate strategy according to typeDetect
                '''Type detect and Generate Mutation strategy'''
                strategy_flag, cmp_flag, bytes_flag = Parser.typeDetect(
                    opt_cmpcov_list, st_cmpcov_list, cmporder_j)
                infer_strategy = Parser.devStrategy(
                    opt_cmpcov_list, cmporder_j, strategy_flag, cmp_flag, bytes_flag, st_cmploc)
                sch.strategyq.put(infer_strategy)

                if bytes_flag == PAR_FIXAFIX:
                    continue

                LOG(LOG_DEBUG, LOG_FUNCINFO(), strategy_flag, bytes_flag, opt_cmpcov_list, ststart_cmpcov_list, showlog=True)

                # fixme
                # opt_seed = Mutator.mutLocFromMap(opt_seed, opt_seed.content, path.seeds_mutate, ST_STR + str(vis.loop),
                #                                  {1:b'\x65',2:b'\x65', 3:b'\x65'})
                # opt_seed = sch.selectOneSeed(SCH_THIS_SEED, opt_seed)
                # opt_stdout, opt_stderr = Executor.run(fuzz_command.replace('@@', opt_seed.filename))
                # sch.saveCrash(opt_seed, opt_stdout, opt_stderr, vis)
                #
                # opt_interlen, opt_covernum = ana.getShm(opt_stdout[0:16])
                # opt_cmpcov_list = ana.getRpt(opt_interlen)

                '''Mutation strategy and Compare distance'''
                while not eaexit and not sch.strategyq.empty():
                    strategy = sch.strategyq.get()
                    LOG(LOG_DEBUG, LOG_FUNCINFO(), strategy, showlog=True)
                    # Type Detection and Breaking the Constraint Cycle (At lease 1 loops)
                    while not eaexit and strategy.curloop < strategy.endloop:
                        strategy.curloop += 1
                        strategy.curnum = 0
                        LOG(LOG_DEBUG, LOG_FUNCINFO(), eaexit, showlog=True)
                        if strategy.strategytype == STAT_FIN:
                            cmpidorder = getCmpidOrder(stcmpid_ki, cmporder_j)
                            if cmpidorder not in sch.pass_cmp_dict:
                                sch.pass_cmp_dict[cmpidorder] = \
                                    Structures.StructCmpInfo(stcmpid_ki, cmporder_j,
                                                             getLocInputValue(opt_seed.content, st_cmploc))
                            # sch.freeze_bytes = sch.freeze_bytes.union(set(st_cmploc))  # don't need it
                            vis.total += 1
                            opt_stdout, opt_stderr = Executor.run(fuzz_command.replace('@@', opt_seed.filename))
                            if len(opt_stderr) == 0:
                                sch.addq(SCH_LOOP_SEED, [opt_seed, ])
                            break

                        while not eaexit and strategy.curnum < strategy.endnum:
                            vis.total += 1

                            if strategy.curnum == 0:
                                locmapdet_dict = Parser.solveChangeMap(
                                    strategy, st_cmploc, st_seed, st_cmpcov_list, cmporder_j)
                            else:
                                locmapdet_dict = Parser.solveChangeMap(
                                    strategy, st_cmploc, opt_seed, opt_cmpcov_list, cmporder_j)
                            LOG(LOG_DEBUG, LOG_FUNCINFO(), strategy.curnum, strategy.endnum, locmapdet_dict,
                                opt_seed.content, st_seed.content, showlog=True)
                            # The next mutate seed
                            # Passing the constraint based on the number of cycles and the distance between comparisons.
                            if len(locmapdet_dict) == 0:
                                st_seed = st_seed
                            elif strategy.curnum == 0:
                                st_seed = Mutator.mutLocFromMap(
                                    st_seed, st_seed.content, path.seeds_mutate, ST_STR + str(vis.loop), locmapdet_dict
                                )
                                st_seed = sch.selectOneSeed(SCH_THISMUT_SEED, st_seed)
                            else:
                                st_seed = Mutator.mutLocFromMap(
                                    opt_seed, opt_seed.content, path.seeds_mutate, ST_STR + str(vis.loop),
                                    locmapdet_dict
                                )
                                st_seed = sch.selectOneSeed(SCH_THISMUT_SEED, st_seed)
                            vis.total += 1
                            st_stdout, st_stderr = Executor.run(fuzz_command.replace('@@', st_seed.filename))
                            sch.saveCrash(st_seed, st_stdout, st_stderr, vis)

                            # 2 cmp instruction
                            # Generate analysis reports.
                            st_interlen, st_covernum = ana.getShm(st_stdout[0:16])
                            st_cmpcov_list = ana.getRpt(st_interlen)

                            LOG(LOG_DEBUG, LOG_FUNCINFO(), strategy.curnum, strategy.endnum, strategy.curloop,
                                strategy.endloop, st_cmploc, locmapdet_dict, opt_seed.content, st_seed.content)
                            # Returns the status and the character to be mutated
                            # Comparison of global optimal values to achieve updated parameters
                            opt_seed, opt_cmpcov_list, exe_status = Parser.solveDistence(
                                strategy, opt_seed, st_seed, opt_cmpcov_list, st_cmpcov_list, cmporder_j)
                            LOG(LOG_DEBUG, LOG_FUNCINFO(), strategy.strategytype, strategy.bytestype, strategy.curloop,
                                strategy.endloop, opt_seed.content, opt_cmpcov_list, exe_status, locmapdet_dict)

                            # 5 visualize
                            res = vis.display(
                                opt_seed, set(st_cmploc), st_stdout, st_stderr, STG_ST, stcmpid_weight, sch)
                            vis.showGraph(path.data_graph, cggraph, cfggraph_dict['main'])
                            if res == VIS_Q:
                                sch.quitFuzz()
                            LOG(LOG_DEBUG, LOG_FUNCINFO(), st_seed.content)

                            strategy.curnum += 1
                            if exe_status == DIST_FINISH:
                                cmpidorder = getCmpidOrder(stcmpid_ki, cmporder_j)
                                if cmpidorder not in sch.pass_cmp_dict:
                                    sch.pass_cmp_dict[cmpidorder] = \
                                        Structures.StructCmpInfo(stcmpid_ki, cmporder_j,
                                                                 getLocInputValue(opt_seed.content, st_cmploc))
                                # sch.freeze_bytes = sch.freeze_bytes.union(set(st_cmploc))  # don't need it
                                vis.total += 1
                                ana.sendCmpid(TRACE_GUARDFAST)
                                trace_stdout, trace_stderr = Executor.run(fuzz_command.replace('@@', opt_seed.filename))
                                tgtsan = sch.saveCrash(opt_seed, trace_stdout, trace_stderr, vis)
                                if tgtsan:
                                    eaexit = True

                                LOG(LOG_DEBUG, LOG_FUNCINFO(), tgtsan, eaexit, sch.cur_tgtnum, showlog=True)
                                if len(opt_stderr) == 0:
                                    trace_interlen, trace_covernum = ana.getShm(trace_stdout[0:16])
                                    trace_guard_list = ana.getRpt(trace_interlen)
                                    near_dis = sch.findNearDistance(
                                        trace_guard_list, map_tgtpredgvid_dis, tgtpred_offset, map_guard_gvid)
                                    if near_dis < sch.cur_nearlydis:
                                        eaexit = True
                                    sch.addq(SCH_LOOP_SEED, [opt_seed, ])

                                ana.sendCmpid(stcmpid_ki)
                                break
                            elif len(locmapdet_dict) == 0 or exe_status == DIST_FAIL:
                                pass
                    sch.deleteSeeds(SCH_THISMUT_SEED)

        # raise Exception()
        # Endless fuzzing, add the length seed.
        LOG(LOG_DEBUG, LOG_FUNCINFO(), init_seed.content)
        sch.targetcmp_pq.queue.clear()
        sch.deleteSeeds(SCH_THIS_SEED)
        if sch.seedq.empty():
            sch.addq(SCH_LOOP_SEED, [init_seed, ])

        # Mutual mapping relationship
        # Key: cmpid  Value: branch_order cmp_type input_bytes branches
        # 4 branches

    sch.deleteSeeds(SCH_THIS_SEED)
    sch.deleteSeeds(SCH_THISMUT_SEED)
    for info in sch.target_crashinfo:
        print(info)
    print("(^_^)# Target vulnerability successfully reproduced.")


if __name__ == "__main__":
    mainFuzzer()
    # python3.7 STFGFuzzer.py -n demo -- ./Programs/demo/code_Bin/demo -f @@
    # python3.7 STFGFuzzer.py -n base64 -- ./Programs/base64/code_Bin/base64 -d @@

    # dot -Tpng CG.gv -o output.png

    # Handle Segmentation fault.  Generator the core files.
    # ulimit -c unlimited
    # python3 -X faulthandler my.py

    # std_out, std_err = Executor.run("./Programs/base64/code_Bin/base64 -d Programs/base64/seeds_crash/validate_inputs/utmp-fuzzed-222.b64")
    # print(std_out, std_err)
