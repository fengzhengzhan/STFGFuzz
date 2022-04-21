#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import faulthandler

faulthandler.enable()

from fuzzer_module import *
from fuzzer_module.Fuzzconfig import *


def mainFuzzer():
    """
    The fuzzing Loop.
    @return:
    """
    # Receive command line parameters.
    program_name, patchtype, fuzz_command = Generator.genTerminal()
    if fuzz_command == "" or program_name == "" or patchtype not in COM_PATCHSET:
        print("python {}.py -h".format(FUZZNAME))
        raise Exception("Error parameters.")

    path_initseeds = PROGRAMS + os.sep + program_name + os.sep + SEEDSINIT + os.sep
    path_mutseeds = PROGRAMS + os.sep + program_name + os.sep + SEEDSMUTATE + os.sep
    path_crashseeds = PROGRAMS + os.sep + program_name + os.sep + SEEDSCRASH + os.sep
    path_graph = PROGRAMS + os.sep + program_name + os.sep + DATAGRAPH + os.sep
    path_codeIR = PROGRAMS + os.sep + program_name + os.sep + CODEIR + os.sep
    file_crash_csv = path_crashseeds + CRASH_CSVFILENAME
    LOG(LOG_DEBUG, LOG_FUNCINFO(), path_initseeds, path_mutseeds, path_crashseeds)

    '''Fuzzing test procedure.'''
    ana = Analyzer.Analyzer()
    sch = Scheduler.Scheduler()
    vis = Visualizer.Visualizer()
    # Directed Location
    binline_dict = Builder.getBinaryInfo(program_name)
    target_dict = Comparator.getTarget(program_name)
    map_numTofuncasm = Comparator.getDirectedNodeLoc(binline_dict, target_dict)
    # Graph Information
    cglist, cfglist = Generator.createDotJsonFile(program_name, path_codeIR + program_name + GEN_TRACEBC_SUFFIX)
    cggraph, map_funcTocgnode = Builder.getCG(cglist)
    cfggraph_dict, map_guardTocfgnode, map_numfuncTotgtnode = Builder.getCFG(cfglist, map_numTofuncasm)
    LOG(LOG_DEBUG, LOG_FUNCINFO(),
        cggraph, map_funcTocgnode, cfggraph_dict, map_guardTocfgnode, map_numfuncTotgtnode)

    # vis.showGraph(path_graph, cggraph, cfggraph_dict['main'])

    # Init Loop Variables
    before_coverage = sch.coveragepath

    # Init seed lists
    init_seeds_list = Generator.prepareEnv(program_name)
    if len(init_seeds_list) > 0:
        temp_listq = []
        for each in init_seeds_list:
            temp_listq.append(StructSeed(path_mutseeds + each, "", SEED_INIT, set()))
        sch.addq(SCH_LOOP_SEED, temp_listq)
    else:
        sch.addq(SCH_LOOP_SEED,
                 [StructSeed(path_mutseeds + AUTO_SEED, Mutator.getFillStr(64), SEED_INIT, set()), ])

    '''Fuzzing Cycle'''
    while not sch.isEmpty(SCH_LOOP_SEED):
        vis.loop += 1
        # First run to collect information.
        init_seed = sch.selectOneSeed(SCH_LOOP_SEED)
        init_stdout, init_stderr = Executor.run(fuzz_command.replace('@@', init_seed.filename))
        sch.saveCrash(
            file_crash_csv, path_crashseeds, init_seed, init_stdout, init_stderr,
            vis.start_time, vis.last_time
        )
        init_addr = ana.getAddr(init_stdout[0:16])
        init_interlen = ana.getInterlen(init_addr)
        # cmpcov_list = ana.getRpt(init_interlen, init_addr)
        # initrpt_dict, initrpt_set = ana.traceAyalysis(cmpcovcont_list, sch.freezeid_rpt, sch) todo

        # vis.num_pcguard = ana.getNumOfPcguard() # todo

        # Select the location to be mutated and add it to the location queue.
        sch.initEachloop(vis)

        '''Find correspondence: seed inputs -> cmp instruction -> cmp type (access method) -> braches'''

        '''ld -> Length Detection, Increase seed length'''
        # Increase the input length when the number of constraints does not change in the program.
        # If there is a change in the increase length then increase the length.
        b4ld_seed = init_seed
        b4ld_interlen = init_interlen
        while len(b4ld_seed.content) < sch.expand_size:
            vis.total += 1
            sch.expandnums += 1
            # if before_coverage == sch.coveragepath and len(init_seed.content) < SCH_EXPAND_MAXSIZE:
            # According fixed length to expand the content length of seed.
            ld_seed = Mutator.mutAddLength(b4ld_seed.content, path_mutseeds, LENGTH_STR, LD_EXPAND)
            ld_seed = sch.selectOneSeed(SCH_THIS_SEED, ld_seed)
            ld_stdout, ld_stderr = Executor.run(fuzz_command.replace('@@', ld_seed.filename))
            sch.saveCrash(
                file_crash_csv, path_crashseeds, ld_seed, ld_stdout, ld_stderr,
                vis.start_time, vis.last_time
            )

            # 1 seed inputs
            ld_addr = ana.getAddr(ld_stdout[0:16])
            ld_interlen = ana.getInterlen(ld_addr)
            LOG(LOG_DEBUG, LOG_FUNCINFO(), len(ld_seed.content), b4ld_interlen, ld_interlen)
            if b4ld_interlen != ld_interlen:
                b4ld_seed = ld_seed
                b4ld_interlen = ld_interlen
            elif b4ld_interlen == ld_interlen:
                # Current seed.
                ld_cmpcov_list = ana.getRpt(ld_interlen, ld_addr)  # report
                # Before seed.
                b4ld_stdout, b4ld_stderr = Executor.run(fuzz_command.replace('@@', b4ld_seed.filename))
                b4ld_addr = ana.getAddr(b4ld_stdout[0:16])
                b4ld_cmpcov_list = ana.getRpt(b4ld_interlen, b4ld_addr)
                if ld_cmpcov_list != b4ld_cmpcov_list:
                    b4ld_seed = ld_seed
                    b4ld_interlen = ld_interlen
                else:
                    break

            res = vis.display(ld_seed, set(), ld_stdout, ld_stderr, "LengthDetect", len(sch.coveragepath))
            vis.showGraph(path_graph, cggraph, cfggraph_dict['main'])
            if res == VIS_Q:
                sch.quitFuzz()
        '''ld <-'''


        # Reset the init_seed
        init_seed = b4ld_seed
        init_stdout, init_stderr = Executor.run(fuzz_command.replace('@@', init_seed.filename))
        sch.saveCrash(
            file_crash_csv, path_crashseeds, init_seed, init_stdout, init_stderr,
            vis.start_time, vis.last_time
        )
        init_addr = ana.getAddr(init_stdout[0:16])
        init_interlen = ana.getInterlen(init_addr)
        init_cmpcov_list = ana.getRpt(init_interlen, init_addr)
        init_cmp_dict = ana.traceAyalysis(init_cmpcov_list, sch.skip_cmpidset, FLAG_DICT)

        for loci in range(0, len(init_seed.content)):
            if loci not in sch.freeze_bytes:
                sch.loc_coarse_list.append(loci)

        '''sd -> Sliding Window Detection O(n/step)'''
        # Get a report on changes to comparison instructions. # todo multiprocessing
        before_sdloc_list = []
        coarse_head = 0
        need_fine_list = []
        while coarse_head < len(sch.loc_coarse_list):
            vis.total += 1
            # 1 seed inputs
            sdloc_list = sch.loc_coarse_list[coarse_head:coarse_head + sch.slid_window]
            coarse_head += sch.slid_window // 2
            sd_seed = Mutator.mutSelectChar(init_seed.content, path_mutseeds, COARSE_STR + str(vis.loop), sdloc_list)
            sd_seed = sch.selectOneSeed(SCH_THIS_SEED, sd_seed)
            sd_stdout, sd_stderr = Executor.run(fuzz_command.replace('@@', sd_seed.filename))
            sch.saveCrash(
                file_crash_csv, path_crashseeds, sd_seed, sd_stdout, sd_stderr,
                vis.start_time, vis.last_time
            )

            # 1 seed inputs
            sd_addr = ana.getAddr(sd_stdout[0:16])
            sd_interlen = ana.getInterlen(sd_addr)
            sd_diff = False
            if init_interlen != sd_interlen:
                sd_diff = True
            elif init_interlen == sd_interlen:
                # Current seed.
                sd_cmpcov_list = ana.getRpt(sd_interlen, sd_addr)  # report
                if init_cmpcov_list != sd_cmpcov_list:
                    sd_diff = True

            if sd_diff:
                if len(need_fine_list) == 0:
                    need_fine_list = before_sdloc_list + sdloc_list
                else:
                    need_fine_list += sdloc_list

            before_sdloc_list = sdloc_list

            # 5 visualize
            res = vis.display(sd_seed, set(sdloc_list), sd_stdout, sd_stderr, "SlidingDetect", len(sch.coveragepath))
            vis.showGraph(path_graph, cggraph, cfggraph_dict['main'])
            if res == VIS_Q:
                sch.quitFuzz()
        LOG(LOG_DEBUG, LOG_FUNCINFO(), need_fine_list, showlog=True)
        '''sd <-'''


        '''bd -> Byte Detection O(m)'''
        # Mutate seeds to find where to change. Then perform to a directed mutate.
        # Mutate only one position at a time. Only the corresponding position is speculated.
        cmpmaploc_dict = {}
        need_fine_list = list(set(need_fine_list))
        need_fine_list.sort()
        for one_loc in need_fine_list:
            vis.total += 1
            # 1 seed inputs
            bdloc_list = [one_loc, ]
            bd_seed = Mutator.mutOneChar(init_seed.content, path_mutseeds, FINE_STR + str(vis.loop), bdloc_list)
            bd_seed = sch.selectOneSeed(SCH_THIS_SEED, bd_seed)
            bd_stdout, bd_stderr = Executor.run(fuzz_command.replace('@@', bd_seed.filename))
            sch.saveCrash(
                file_crash_csv, path_crashseeds, bd_seed, bd_stdout, bd_stderr,
                vis.start_time, vis.last_time
            )

            # 2 cmp instruction
            # Track execution information of mutate seeds.
            bd_addr = ana.getAddr(bd_stdout[0:16])
            bd_interlen = ana.getInterlen(bd_addr)
            bd_cmpcov_list = ana.getRpt(bd_interlen, bd_addr)  # report

            bd_cmp_dict = ana.traceAyalysis(bd_cmpcov_list, sch.skip_cmpidset, FLAG_DICT)
            bd_diffcmp_set = ana.compareRptToLoc(init_cmp_dict, bd_cmp_dict)

            for cmpid_key in bd_diffcmp_set:  # Determine if the dictionary is empty.
                if cmpid_key not in sch.skip_cmpidset:
                    if cmpid_key not in cmpmaploc_dict:
                        cmpmaploc_dict[cmpid_key] = [one_loc, ]
                    else:
                        cmpmaploc_dict[cmpid_key].append(one_loc)

            # 5 visualize
            res = vis.display(bd_seed, set(bdloc_list), bd_stdout, bd_stderr, "ByteDetect", len(sch.coveragepath))
            vis.showGraph(path_graph, cggraph, cfggraph_dict['main'])
            if res == VIS_Q:
                sch.quitFuzz()
            LOG(LOG_DEBUG, LOG_FUNCINFO(), one_loc, bd_diffcmp_set, cmpmaploc_dict, showlog=True)
        '''bd <-'''

        '''3 cmp type'''
        '''st -> Constraints Analysis'''
        # Compare instruction type speculation based on input mapping,
        # then try to pass the corresponding constraint (1-2 rounds).
        vis.cmptotal = len(cmpmaploc_dict)
        for st_key, st_loclist in cmpmaploc_dict.items():
            ana.
            # False positive comparison if all input bytes are covered
            vis.cmpnum += 1
            if len(st_loclist) == len(init_seed.content):
                continue

            '''Type detect and Mutation strategy'''
            ststart_seed = Mutator.mutSelectChar(init_seed.content, path_mutseeds, ST_STR + str(vis.loop), st_loclist)
            # sch.addq(SCH_MUT_SEED, [st_seed, ])
            optrpt_dict = initrpt_dict
            opt_seed = init_seed
            before_locmapdet_dict = {}
            sch.strategyq.put(StructMutStrategy(TYPE_DEFAULT, 0, len(st_loclist), 0, 1))
            strategy = sch.strategyq.get()
            # Type Detection and Breaking the Constraint Cycle (At lease 1 loops)
            while strategy.curloop < strategy.endloop or not sch.strategyq.empty():
                # print(strategy.curloop)
                strategy.curloop += 1
                strategy.curnum = 0
                sch.addq(SCH_MUT_SEED, [ststart_seed, ])

                while not sch.isEmpty(SCH_MUT_SEED):
                    vis.total += 1
                    execute_seed = sch.selectOneSeed(SCH_MUT_SEED)
                    st_stdout, st_stderr = Executor.run(fuzz_command.replace('@@', execute_seed.filename))
                    sch.saveCrash(
                        file_crash_csv, path_crashseeds, execute_seed, st_stdout, st_stderr,
                        vis.start_time, vis.last_time
                    )

                    # 2 cmp instruction
                    # Generate analysis reports.
                    cmpcovcont_list, content = ana.getRpt(st_stdout)
                    strpt_dict, strpt_set = ana.traceAyalysis(cmpcovcont_list, content, sch.skip_cmpidset, sch)  # report
                    LOG(LOG_DEBUG, LOG_FUNCINFO(), opt_seed.content, execute_seed.content)

                    # 3 cmp type
                    # Return cmp type and mutate strategy according to typeDetect
                    ret_seed, type_infer_set, locmapdet_dict = Parser.typeDetect(
                        opt_seed, execute_seed, st_loclist, st_key,
                        optrpt_dict, strpt_dict, strategy, sch
                    )

                    # Comparison of global optimal values to achieve updated parameters
                    optrpt_dict = optrpt_dict if ret_seed == opt_seed else strpt_dict
                    opt_seed = ret_seed
                    # if before_locmapdet_dict == locmapdet_dict and not before_locmapdet_dict and not locmapdet_dict:
                    #     break
                    if before_locmapdet_dict == locmapdet_dict and not before_locmapdet_dict:
                        break
                    before_locmapdet_dict = locmapdet_dict

                    LOG(LOG_DEBUG, LOG_FUNCINFO(), vis.cmpnum, st_stderr,
                        locmapdet_dict, content, st_key, st_loclist, ret_seed.content)  # todo , showlog=True
                    LOG(LOG_DEBUG, LOG_FUNCINFO(), ret_seed.content, showlog=True)

                    # 5 visualize
                    res = vis.display(
                        ret_seed, set(st_loclist), st_stdout, st_stderr,
                        "Strategy", len(sch.coveragepath),
                        path_graph, cggraph, cfggraph_dict['main']
                    )
                    if res == VIS_Q:
                        sch.quitFuzz()

                    if TYPE_SOLVED in type_infer_set:
                        sch.skip_cmpidset.add(st_key)
                        sch.freeze_bytes = sch.freeze_bytes | set(st_loclist)
                        sch.recsol_cmpset.add(st_key)
                        sch.addq(SCH_LOOP_SEED, [ret_seed, ])
                        break

                    # Passing the constraint based on the number of cycles and the distance between comparisons.
                    st_seed = Mutator.mutLocFromMap(
                        ret_seed.content, path_mutseeds, ST_STR + str(vis.loop), locmapdet_dict
                    )
                    if st_seed is not None:
                        sch.addq(SCH_MUT_SEED, [st_seed, ])

        # Endless fuzzing, add the length seed.
        LOG(LOG_DEBUG, LOG_FUNCINFO(), b4ld_seed.content, showlog=True)
        # if sch.isEmpty(SCH_LOOP_SEED) or init_seed.content != b4ld_seed.content:
        if sch.isEmpty(SCH_LOOP_SEED):
            sch.addq(SCH_LOOP_SEED, [init_seed, ])

        # Mutual mapping relationship
        # Key: cmpid  Value: branch_order cmp_type input_bytes branches
        # 4 branches


if __name__ == "__main__":
    # python3.7 STFGFuzzer.py -n demo -- ./Programs/demo/code_Bin/demo -f @@
    # python3.7 STFGFuzzer.py -n base64 -- ./Programs/base64/code_Bin/base64 -d @@

    # Handle Segmentation fault.  Generator the core files.
    # ulimit -c unlimited
    # python3 -X faulthandler my.py
    mainFuzzer()
