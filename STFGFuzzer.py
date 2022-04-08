import queue
import time

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
    vis = Visualizer.Visualizer()
    sch = Scheduler.Scheduler()
    ana = Analyzer.Analyzer()
    cglist, cfglist = Generator.createDotJsonFile(program_name, path_codeIR + program_name + GEN_TRACEBC_SUFFIX)
    cggraph, map_funcTocgname = Builder.getCG(cglist)
    cfggraph_dict, map_guardTocfgname = Builder.getCFG(cfglist)
    # vis.showGraph(path_graph, cggraph, cfggraph_dict['main'])

    # Init Loop Variables
    before_coverage = len(sch.coveragepath)

    # Init seed lists  # todo if == null
    init_seeds_list = Generator.prepareEnv(program_name)
    if len(init_seeds_list) > 0:
        temp_listq = []
        for each in init_seeds_list:
            temp_listq.append(StructSeed(path_mutseeds + each, "", SEED_INIT, set()))
        sch.addq(SCH_LOOP_SEED, temp_listq)
    else:
        sch.addq(SCH_LOOP_SEED,
                 [StructSeed(path_mutseeds + AUTO_SEED, Mutator.getFillStr(64), SEED_INIT, set()), ])

    '''Fuzzing test cycle'''
    while not sch.isEmpty(SCH_LOOP_SEED):
        vis.loop += 1
        # First run to collect information.
        init_seed = sch.selectOneSeed(SCH_LOOP_SEED)
        init_stdout, init_stderr = Executor.run(fuzz_command.replace('@@', init_seed.filename))
        sch.saveCrash(file_crash_csv, path_crashseeds, init_seed, init_stdout, init_stderr)
        cmpcovcont_list, content = ana.gainTraceRpt(init_stdout)
        initrpt_dict, initrpt_set = ana.traceAyalysis(cmpcovcont_list, content, sch.freezeid_rpt, sch)

        vis.num_pcguard = ana.getNumOfPcguard()

        # Select the location to be mutated and add it to the location queue.
        sch.initEachloop()
        for loci in range(0, len(init_seed.content)):
            if loci not in sch.freeze_bytes:
                sch.loc_coarse_list.append(loci)

        '''Find correspondence: seed inputs -> cmp instruction -> cmp type (access method) -> braches'''
        '''Coarse-Grained  O(n/step)'''  # todo multiprocessing
        # Get a report on changes to comparison instructions.
        before_stloc_list = []
        coarse_head = 0
        need_fine_list = []
        while coarse_head < len(sch.loc_coarse_list):
            vis.total += 1
            # 1 seed inputs
            stloc_list = sch.loc_coarse_list[coarse_head:coarse_head + sch.slid_window]
            coarse_head += sch.slid_window // 2
            mutseed = Mutator.mutSelectChar(init_seed.content, path_mutseeds, COARSE_STR + str(vis.loop), stloc_list)
            execute_seed = sch.selectOneSeed(SCH_THIS_SEED, mutseed)
            mut_stdout, mut_stderr = Executor.run(fuzz_command.replace('@@', execute_seed.filename))
            sch.saveCrash(file_crash_csv, path_crashseeds, execute_seed, mut_stdout, mut_stderr)

            # 2 cmp instruction
            # Track execution information of mutate seeds.
            cmpcovcont_list, content = ana.gainTraceRpt(mut_stdout)  # report
            mutrpt_dict, mutrpt_set = ana.traceAyalysis(cmpcovcont_list, content, sch.freezeid_rpt, sch)
            # Gain changed cmp instruction through compare.
            cmpmaploc_rptset = ana.compareRptToLoc(initrpt_dict, initrpt_set, mutrpt_dict, mutrpt_set)

            LOG(LOG_DEBUG, LOG_FUNCINFO(), cmpcovcont_list, content)
            LOG(LOG_DEBUG, LOG_FUNCINFO(), cmpmaploc_rptset)
            if cmpmaploc_rptset:
                if len(need_fine_list) == 0:
                    need_fine_list = before_stloc_list + stloc_list
                else:
                    need_fine_list += stloc_list
            before_stloc_list = stloc_list

            # 5 visualize
            res = vis.display(execute_seed, set(stloc_list), mut_stdout, mut_stderr,
                              "Coarse-Grained", len(sch.coveragepath))
            if res == VIS_Q:
                sch.quitFuzz()
            LOG(LOG_DEBUG, LOG_FUNCINFO(), mutrpt_dict, mutrpt_set, cmpmaploc_rptset)
            LOG(LOG_DEBUG, LOG_FUNCINFO(), need_fine_list)

        '''Fine-Grained O(m)'''
        # Mutate seeds to find where to change. Then perform to a directed mutate.
        # Mutate only one position at a time. Only the corresponding position is speculated.
        cmpmaploc_dict = {}
        need_fine_list = list(set(need_fine_list))
        need_fine_list.sort()
        for one_loc in need_fine_list:
            vis.total += 1
            # 1 seed inputs
            stloc_list = [one_loc, ]
            mutseed = Mutator.mutOneChar(init_seed.content, path_mutseeds, FINE_STR + str(vis.loop), stloc_list)
            execute_seed = sch.selectOneSeed(SCH_THIS_SEED, mutseed)
            mut_stdout, mut_stderr = Executor.run(fuzz_command.replace('@@', execute_seed.filename))
            sch.saveCrash(file_crash_csv, path_crashseeds, execute_seed, mut_stdout, mut_stderr)

            # 2 cmp instruction
            # Track execution information of mutate seeds.
            cmpcovcont_list, content = ana.gainTraceRpt(mut_stdout)  # report
            mutrpt_dict, mutrpt_set = ana.traceAyalysis(cmpcovcont_list, content, sch.freezeid_rpt, sch)
            cmpmaploc_rptset = ana.compareRptToLoc(initrpt_dict, initrpt_set, mutrpt_dict, mutrpt_set)

            for cmpid_key in cmpmaploc_rptset:  # Determine if the dictionary is empty.
                if cmpid_key not in sch.solved_cmpset:
                    if cmpid_key not in cmpmaploc_dict:
                        cmpmaploc_dict[cmpid_key] = [one_loc, ]
                    else:
                        cmpmaploc_dict[cmpid_key].append(one_loc)

            # 5 visualize
            res = vis.display(execute_seed, set(stloc_list), mut_stdout, mut_stderr,
                              "Fine-Grained", len(sch.coveragepath))
            if res == VIS_Q:
                sch.quitFuzz()

            LOG(LOG_DEBUG, LOG_FUNCINFO(), cmpmaploc_dict, showlog=True)

        '''3 cmp type'''
        # Compare instruction type speculation based on input mapping,
        # then try to pass the corresponding constraint (1-2 rounds).
        for st_key, st_loclist in cmpmaploc_dict.items():

            # False positive comparison if all input bytes are covered
            if len(st_loclist) == len(init_seed.content):
                continue

            '''Type detect and Mutation strategy'''
            ststart_seed = Mutator.mutSelectChar(init_seed.content, path_mutseeds, ST_STR + str(vis.loop), st_loclist)
            # sch.addq(SCH_MUT_SEED, [st_seed, ])
            optrpt_dict = initrpt_dict
            opt_seed = init_seed
            before_locmapdet_dict = {}
            sch.strategyq.put(StructMutStrategy(TYPE_DEFAULT, 0, len(st_loclist), 0, 2))
            strategy = sch.strategyq.get()
            # Type Detection and Breaking the Constraint Cycle (At lease 2 loops)
            while strategy.curloop < strategy.endloop or not sch.strategyq.empty():
                # print(strategy.curloop)
                strategy.curloop += 1
                strategy.curnum = 0
                sch.addq(SCH_MUT_SEED, [ststart_seed, ])

                while not sch.isEmpty(SCH_MUT_SEED):
                    vis.total += 1
                    execute_seed = sch.selectOneSeed(SCH_MUT_SEED)
                    st_stdout, st_stderr = Executor.run(fuzz_command.replace('@@', execute_seed.filename))
                    sch.saveCrash(file_crash_csv, path_crashseeds, execute_seed, st_stdout, st_stderr)

                    # 2 cmp instruction
                    # Generate analysis reports.
                    cmpcovcont_list, content = ana.gainTraceRpt(st_stdout)
                    strpt_dict, strpt_set = ana.traceAyalysis(cmpcovcont_list, content, sch.freezeid_rpt, sch)  # report
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

                    LOG(LOG_DEBUG, LOG_FUNCINFO(), locmapdet_dict, content, st_key, st_loclist)
                    LOG(LOG_DEBUG, LOG_FUNCINFO(), strategy.curloop, locmapdet_dict, ret_seed.content, type_infer_set)

                    # 5 visualize
                    res = vis.display(
                        ret_seed, set(st_loclist), st_stdout, st_stderr, "Strategy", len(sch.coveragepath)
                    )
                    if res == VIS_Q:
                        sch.quitFuzz()

                    if TYPE_SOLVED in type_infer_set:
                        sch.solved_cmpset.add(st_key)
                        sch.freeze_bytes = sch.freeze_bytes | set(st_loclist)
                        sch.freezeid_rpt.add(st_key)
                        sch.addq(SCH_LOOP_SEED, [ret_seed, ])
                        break

                    # Passing the constraint based on the number of cycles and the distance between comparisons.
                    st_seed = Mutator.mutLocFromMap(
                        ret_seed.content, path_mutseeds, ST_STR + str(vis.loop), locmapdet_dict
                    )
                    if st_seed is not None:
                        sch.addq(SCH_MUT_SEED, [st_seed, ])

        # Increase the input length when the number of constraints does not change in the program.
        # If there is a change in the increase length then increase the length.
        # if before_coverage == len(sch.coveragepath) and len(init_seed.content) < SCH_EXPAND_MAXSIZE:
        #     sch.expandnums += 1
        #     sch.addq(SCH_LOOP_SEED, [
        #         StructSeed(path_mutseeds + getTimeStr() + EXPAND_SEED, init_seed.content + init_seed.content,
        #                    MUT_SEED_INSERT, set())
        #     ])
        # before_coverage = len(sch.coveragepath)

        # Endless fuzzing
        if sch.isEmpty(SCH_LOOP_SEED):
            sch.addq(SCH_LOOP_SEED, [init_seed, ])

        # Mutual mapping relationship
        # Key: cmpid  Value: branch_order cmp_type input_bytes branches
        # 4 branches


if __name__ == "__main__":
    # python3.7 STFGFuzzer.py -n demo -- ./Programs/demo/code_Bin/demo -f @@
    # python3.7 STFGFuzzer.py -n base64 -- ./Programs/base64/code_Bin/base64 -d @@
    mainFuzzer()
