#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import faulthandler  # Use to find Segmentation Fault

faulthandler.enable()

from fuzzer_module import *
from fuzzer_module.Fuzzconfig import *


# Close Address Space Layout Randomization.
# echo 0 > /proc/sys/kernel/randomize_va_space

# python3.7 STFGFuzzer.py -n demo -- ./Programs/demo/code_Bin/demo -f @@
# python3.7 STFGFuzzer.py -n base64 -- ./Programs/base64/code_Bin/base64 -d @@

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
    sch.file_crash_csv = file_crash_csv
    sch.path_crashseeds = path_crashseeds
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
            temp_listq.append(StructSeed(path_mutseeds + each, readContent(path_mutseeds + each), SEED_INIT, set()))
        sch.addq(SCH_LOOP_SEED, temp_listq)
    else:
        sch.addq(SCH_LOOP_SEED,
                 [StructSeed(path_mutseeds + AUTO_SEED, Mutator.getFillStr(64), SEED_INIT, set()), ])

    '''Fuzzing Cycle'''
    while not sch.seedq.empty():
        vis.loop += 1
        # First run to collect information.
        init_seed = sch.selectOneSeed(SCH_LOOP_SEED)
        init_stdout, init_stderr = Executor.run(fuzz_command.replace('@@', init_seed.filename))
        ana.getShm(init_stdout[0:16])
        ana.sendCmpid("Guard")

        init_stdout, init_stderr = Executor.run(fuzz_command.replace('@@', init_seed.filename))
        sch.saveCrash(init_seed, init_stdout, init_stderr, vis.start_time, vis.last_time)
        init_interlen, init_covernum = ana.getShm(init_stdout[0:16])
        init_guardcov_list = ana.getRpt(init_interlen)
        guard_set, guard_total = ana.traceGuardAnalysis(init_guardcov_list)
        sch.coveragepath = guard_set
        vis.num_pcguard = guard_total

        ana.sendCmpid("None")
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
        LOG(LOG_DEBUG, LOG_FUNCINFO(), init_seed.content, ana.getRpt(init_interlen))
        while len(b4ld_seed.content) < sch.expand_size:
            vis.total += 1
            sch.expandnums += 1
            # if before_coverage == sch.coveragepath and len(init_seed.content) < SCH_EXPAND_MAXSIZE:
            # According fixed length to expand the content length of seed.
            ld_seed = Mutator.mutAddLength(b4ld_seed.content, path_mutseeds, LENGTH_STR, LD_EXPAND)
            ld_seed = sch.selectOneSeed(SCH_THIS_SEED, ld_seed)
            ld_stdout, ld_stderr = Executor.run(fuzz_command.replace('@@', ld_seed.filename))
            sch.saveCrash(ld_seed, ld_stdout, ld_stderr, vis.start_time, vis.last_time)

            # 1 seed inputs
            ld_interlen, ld_covernum = ana.getShm(ld_stdout[0:16])
            LOG(LOG_DEBUG, LOG_FUNCINFO(), len(ld_seed.content), b4ld_interlen, ld_interlen, showlog=True)
            LOG(LOG_DEBUG, LOG_FUNCINFO(), ana.getRpt(ld_interlen), showlog=True)
            if b4ld_interlen != ld_interlen:
                b4ld_seed = ld_seed
                b4ld_interlen = ld_interlen
            elif b4ld_interlen == ld_interlen:
                # Current seed.
                ld_cmpcov_list = ana.getRpt(ld_interlen)  # report
                # Before seed.
                b4ld_stdout, b4ld_stderr = Executor.run(fuzz_command.replace('@@', b4ld_seed.filename))
                b4ld_interlen, b4ld_covernum = ana.getShm(b4ld_stdout[0:16])
                b4ld_cmpcov_list = ana.getRpt(b4ld_interlen)
                LOG(LOG_DEBUG, LOG_FUNCINFO(), b4ld_cmpcov_list, showlog=True)
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

        init_interlen, init_covernum = ana.getShm(init_stdout[0:16])
        init_cmpcov_list = ana.getRpt(init_interlen)
        init_cmp_dict = ana.traceAyalysis(init_cmpcov_list, sch.skip_cmpidset, FLAG_DICT)
        init_cmpset = set(init_cmp_dict)

        for loci in range(0, len(init_seed.content)):
            if loci not in sch.freeze_bytes:
                sch.loc_coarse_list.append(loci)

        '''sd -> Sliding Window Detection O(n/step)'''
        # Get a report on changes to comparison instructions. # todo multiprocessing
        before_sdloc_list = []
        coarse_head = 0
        cmpmaploc_dict = {}
        while coarse_head < len(sch.loc_coarse_list):
            vis.total += 1
            # 1 seed inputs
            sdloc_list = sch.loc_coarse_list[coarse_head:coarse_head + sch.slid_window]
            coarse_head += sch.slid_window // 2
            sd_seed = Mutator.mutSelectChar(init_seed.content, path_mutseeds, COARSE_STR + str(vis.loop), sdloc_list)
            sd_seed = sch.selectOneSeed(SCH_THIS_SEED, sd_seed)
            sd_stdout, sd_stderr = Executor.run(fuzz_command.replace('@@', sd_seed.filename))
            sch.saveCrash(sd_seed, sd_stdout, sd_stderr, vis.start_time, vis.last_time)

            # 1 seed inputs
            sd_interlen, sd_covernum = ana.getShm(sd_stdout[0:16])
            sd_cmpcov_list = ana.getRpt(sd_interlen)  # report

            sd_cmp_dict = ana.traceAyalysis(sd_cmpcov_list, sch.skip_cmpidset, FLAG_DICT)
            sd_diffcmp_set = ana.compareRptToLoc(init_cmp_dict, init_cmpset, sd_cmp_dict)
            # LOG(LOG_DEBUG, LOG_FUNCINFO(), sd_seed.content, init_cmp_dict['g0x4f98aa0x4faa2b'], bd_cmp_dict['g0x4f98aa0x4faa2b'], showlog=True)

            for cmpid_key in sd_diffcmp_set:  # Determine if the dictionary is empty.
                if cmpid_key not in sch.skip_cmpidset:
                    if cmpid_key not in cmpmaploc_dict:
                        cmpmaploc_dict[cmpid_key] = set(before_sdloc_list) | set(sdloc_list)
                    else:
                        cmpmaploc_dict[cmpid_key] |= set(sdloc_list)

            before_sdloc_list = sdloc_list

            # 5 visualize
            res = vis.display(sd_seed, set(sdloc_list), sd_stdout, sd_stderr, "SlidingDetect", len(sch.coveragepath))
            vis.showGraph(path_graph, cggraph, cfggraph_dict['main'])
            if res == VIS_Q:
                sch.quitFuzz()
        LOG(LOG_DEBUG, LOG_FUNCINFO(), cmpmaploc_dict, showlog=True)
        '''sd <-'''

        '''3 cmp type'''
        '''st -> Constraints Analysis'''
        # Compare instruction type speculation based on input mapping,
        # then try to pass the corresponding constraint (1-2 rounds).
        vis.cmptotal = len(cmpmaploc_dict)
        for stcmpid_ki, stlocset_vi in cmpmaploc_dict.items():
            vis.total += 3
            ana.sendCmpid(stcmpid_ki)
            # False positive comparison if all input bytes are covered
            # if len(stloclist_v) == len(init_seed.content):
            #     continue
            vis.cmpnum += 1

            '''Type detect and Generate Mutation strategy'''
            stloclist_v = list(stlocset_vi)
            stloclist_v.sort()
            ststart_seed = Mutator.mutSelectChar(init_seed.content, path_mutseeds, ST_STR + str(vis.loop), stloclist_v)
            ststart_seed = sch.selectOneSeed(SCH_THIS_SEED, ststart_seed)
            ststart_stdout, ststart_stderr = Executor.run(fuzz_command.replace('@@', ststart_seed.filename))

            ststart_interlen, ststart_covernum = ana.getShm(ststart_stdout[0:16])
            ststart_cmpcov_list = ana.getRpt(ststart_interlen)

            # Removal of unmapped changes
            repeat_seed = Mutator.mutSelectChar(
                init_seed.content, path_mutseeds, REPEAT_STR + str(vis.loop), stloclist_v)
            repeat_seed = sch.selectOneSeed(SCH_THIS_SEED, repeat_seed)
            repeat_stdout, repeat_stderr = Executor.run(fuzz_command.replace('@@', repeat_seed.filename))

            repeat_interlen, repeat_covernum = ana.getShm(repeat_stdout[0:16])
            repeat_cmpcov_list = ana.getRpt(repeat_interlen)

            if not ana.compareRptOne(ststart_cmpcov_list, repeat_cmpcov_list, -1):
                continue

            # Only the corresponding list data is retained, no parsing is required
            cmp_len = len(ststart_cmpcov_list)
            # Separate comparisons for each comparison instruction.
            for cmporder_j in range(0, cmp_len):
                vis.total += 1
                '''bd -> Byte Detection O(m)'''
                # Single-byte comparison in order
                st_cmploc = []
                for one_loc in stloclist_v:
                    vis.total += 1
                    bdloc_list = [one_loc, ]
                    bd_seed = Mutator.mutOneChar(ststart_seed.content, path_mutseeds, FINE_STR + str(vis.loop),
                                                 bdloc_list)
                    bd_seed = sch.selectOneSeed(SCH_THIS_SEED, bd_seed)
                    bd_stdout, bd_stderr = Executor.run(fuzz_command.replace('@@', bd_seed.filename))
                    sch.saveCrash(bd_seed, bd_stdout, bd_stderr, vis.start_time, vis.last_time)

                    bd_interlen, bd_covernum = ana.getShm(bd_stdout[0:16])
                    bd_cmpcov_list = ana.getRpt(bd_interlen)

                    LOG(LOG_DEBUG, LOG_FUNCINFO(), ststart_cmpcov_list, bd_cmpcov_list)
                    if not ana.compareRptOne(ststart_cmpcov_list, bd_cmpcov_list, cmporder_j):
                        st_cmploc.append(one_loc)
                    # 5 visualize
                    res = vis.display(
                        bd_seed, set(st_cmploc), bd_stdout, bd_stderr,
                        "Byte", len(sch.coveragepath),
                    )
                    vis.showGraph(path_graph, cggraph, cfggraph_dict['main'])
                    if res == VIS_Q:
                        sch.quitFuzz()
                LOG(LOG_DEBUG, LOG_FUNCINFO(), ststart_cmpcov_list[cmporder_j], st_cmploc, showlog=True)
                '''bd <-'''

                ana.sendCmpid(stcmpid_ki)
                # Identification Type and Update opt seed (in Random change)
                # init_seed opt_seed
                opt_seed = sch.selectOneSeed(SCH_THIS_SEED, init_seed)
                opt_stdout, opt_stderr = Executor.run(fuzz_command.replace('@@', opt_seed.filename))
                sch.saveCrash(opt_seed, opt_stdout, opt_stderr, vis.start_time, vis.last_time)

                opt_interlen, opt_covernum = ana.getShm(opt_stdout[0:16])
                opt_cmpcov_list = ana.getRpt(opt_interlen)

                # 3 cmp type
                # Return cmp type and mutate strategy according to typeDetect
                bytes_flag, strategy_flag = Parser.typeDetect(opt_cmpcov_list, ststart_cmpcov_list, cmporder_j)
                infer_strategy = Parser.devStrategy(opt_cmpcov_list, cmporder_j, bytes_flag, strategy_flag, st_cmploc)
                sch.strategyq.put(infer_strategy)

                LOG(LOG_DEBUG, LOG_FUNCINFO(), bytes_flag, strategy_flag, opt_cmpcov_list, ststart_cmpcov_list,
                    showlog=True)

                '''Mutation strategy and Compare distance'''
                while not sch.strategyq.empty():
                    strategy = sch.strategyq.get()
                    # Type Detection and Breaking the Constraint Cycle (At lease 1 loops)
                    while strategy.curloop < strategy.endloop:
                        strategy.curloop += 1
                        strategy.curnum = 0
                        vis.total += 1
                        st_seed = Mutator.mutSelectCharRand(
                            ststart_seed.content, path_mutseeds, ST_STR + str(vis.loop), st_cmploc)
                        st_seed = sch.selectOneSeed(SCH_THIS_SEED, st_seed)
                        st_stdout, st_stderr = Executor.run(fuzz_command.replace('@@', st_seed.filename))
                        sch.saveCrash(st_seed, st_stdout, st_stderr, vis.start_time, vis.last_time)
                        st_interlen, st_covernum = ana.getShm(opt_stdout[0:16])
                        st_cmpcov_list = ana.getRpt(st_interlen)

                        while strategy.curnum < strategy.endnum:
                            vis.total += 1
                            LOG(LOG_DEBUG, LOG_FUNCINFO(), opt_seed.content, st_seed.content, showlog=True)
                            # Returns the status and the character to be mutated
                            # Comparison of global optimal values to achieve updated parameters
                            opt_seed, opt_cmpcov_list, exe_status, locmapdet_dict = \
                                Parser.solveDistence(strategy, st_cmploc, opt_seed, st_seed,
                                                     opt_cmpcov_list, st_cmpcov_list, cmporder_j)
                            LOG(LOG_DEBUG, LOG_FUNCINFO(), strategy.strategytype, strategy.conttype, strategy.curloop,
                                strategy.endloop, opt_cmpcov_list, exe_status, locmapdet_dict, showlog=True)

                            strategy.curnum += 1

                            if exe_status == DIST_FINISH:
                                sch.skip_cmpidset.add(stcmpid_ki)
                                sch.freeze_bytes = sch.freeze_bytes.union(set(st_cmploc))
                                sch.recsol_cmpset.add(stcmpid_ki)
                                sch.addq(SCH_LOOP_SEED, [opt_seed, ])
                                break
                            elif len(locmapdet_dict) == 0 or exe_status == DIST_FAIL:
                                pass

                            # The next mutate seed
                            # Passing the constraint based on the number of cycles and the distance between comparisons.
                            if len(locmapdet_dict) == 0:
                                st_seed = opt_seed
                            else:
                                st_seed = Mutator.mutLocFromMap(
                                    opt_seed.content, path_mutseeds, ST_STR + str(vis.loop), locmapdet_dict
                                )
                                st_seed = sch.selectOneSeed(SCH_THIS_SEED, st_seed)
                            st_stdout, st_stderr = Executor.run(fuzz_command.replace('@@', st_seed.filename))
                            sch.saveCrash(st_seed, st_stdout, st_stderr, vis.start_time, vis.last_time)

                            # 2 cmp instruction
                            # Generate analysis reports.
                            st_interlen, st_covernum = ana.getShm(st_stdout[0:16])
                            st_cmpcov_list = ana.getRpt(st_interlen)

                            # 5 visualize
                            res = vis.display(
                                opt_seed, set(st_cmploc), st_stdout, st_stderr,
                                "Strategy", len(sch.coveragepath),
                            )
                            vis.showGraph(path_graph, cggraph, cfggraph_dict['main'])
                            if res == VIS_Q:
                                sch.quitFuzz()
                            LOG(LOG_DEBUG, LOG_FUNCINFO(), st_seed.content, showlog=True)

        # Endless fuzzing, add the length seed.
        LOG(LOG_DEBUG, LOG_FUNCINFO(), init_seed.content, showlog=True)
        if sch.seedq.empty():
            sch.addq(SCH_LOOP_SEED, [init_seed, ])

        # Mutual mapping relationship
        # Key: cmpid  Value: branch_order cmp_type input_bytes branches
        # 4 branches


if __name__ == "__main__":
    mainFuzzer()
    # python3.7 STFGFuzzer.py -n demo -- ./Programs/demo/code_Bin/demo -f @@
    # python3.7 STFGFuzzer.py -n base64 -- ./Programs/base64/code_Bin/base64 -d @@

    # dot -Tpng CG.gv -o output.png

    # Handle Segmentation fault.  Generator the core files.
    # ulimit -c unlimited
    # python3 -X faulthandler my.py

    # std_out, std_err = runothercmd("./Programs/base64/code_Bin/base64 -d Programs/base64/seeds_crash/validate_inputs/utmp-fuzzed-222.b64")
    # print(std_out, std_err)
