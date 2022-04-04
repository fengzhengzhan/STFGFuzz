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
    cglist, cfglist = Generator.createDotJsonFile(program_name, path_codeIR+program_name+GEN_TRACEBC_SUFFIX)
    cggraph, map_funcTocgname = Builder.getCG(cglist)
    cfggraph_dict, map_guardTocfgname = Builder.getCFG(cfglist)
    # vis.showGraph(path_graph, cggraph, cfggraph_dict['main'])

    input_map: dict[list] = {}
    init_seeds_list = Generator.prepareEnv(program_name)

    # Init seed lists  # todo if == null
    temp_listq = []
    for each in init_seeds_list:
        temp_listq.append(StructSeed(path_mutseeds + each, "", SEED_INIT, {USE_INITNUM}))
    sch.addSeeds(SCH_LOOP_SEED, temp_listq)

    '''Fuzzing test cycle'''
    while not sch.isEmpty(SCH_LOOP_SEED):
        vis.loop += 1
        # First run to collect information.
        init_seed = sch.selectOneSeed(SCH_LOOP_SEED)
        init_stdout, init_stderr = Executor.run(fuzz_command.replace('@@', init_seed.filename))
        sch.saveCrash(file_crash_csv, path_crashseeds, init_seed, init_stdout, init_stderr)
        cmpcovcont_list, content = ana.gainTraceRpt(init_stdout)
        initrpt_dict, initrpt_set = ana.traceAyalysis(cmpcovcont_list, content, sch.freezeid_rpt)

        num_pcguard = ana.getNumOfPcguard()

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
        cmpmaploc_coarse_dict = {}
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
            mutrpt_dict, mutrpt_set = ana.traceAyalysis(cmpcovcont_list, content, sch.freezeid_rpt)
            # Gain changed cmp instruction through compare.
            cmpmaploc_rptdict = ana.compareRptToLoc(execute_seed, initrpt_dict, initrpt_set, mutrpt_dict, mutrpt_set)

            LOG(LOG_DEBUG, LOG_FUNCINFO(), cmpcovcont_list, content)
            LOG(LOG_DEBUG, LOG_FUNCINFO(), cmpmaploc_rptdict)

            for cmpid_key, cmploc_val in cmpmaploc_rptdict.items():  # Determine if the dictionary is empty.
                if cmpid_key not in sch.solved_cmpset:
                    if cmpid_key not in cmpmaploc_coarse_dict:
                        cmpmaploc_coarse_dict[cmpid_key] = cmploc_val | set(before_stloc_list)
                    else:
                        cmpmaploc_coarse_dict[cmpid_key] = cmpmaploc_coarse_dict[cmpid_key] | cmploc_val
            before_stloc_list = stloc_list
            LOG(LOG_DEBUG, LOG_FUNCINFO(), mutrpt_dict, mutrpt_set, cmpmaploc_rptdict)

            # 5 visualize
            res = vis.display(execute_seed, set(stloc_list), mut_stdout, mut_stderr)
            if res == QUIT_FUZZ:
                sch.quitFuzz()
        LOG(LOG_DEBUG, LOG_FUNCINFO(), cmpmaploc_coarse_dict)

        '''3 cmp type'''
        # Compare instruction type speculation based on input mapping,
        # then try to pass the corresponding constraint (1-2 rounds).
        for st_key, st_coarseval in cmpmaploc_coarse_dict.items():
            '''Fine-Grained O(m)'''
            # Mutate seeds to find where to change. Then perform to a directed mutate.
            # Mutate only one position at a time. Only the corresponding position is speculated.
            sch.loc_fine_list = list(st_coarseval)
            sch.loc_fine_list.sort()
            LOG(LOG_DEBUG, LOG_FUNCINFO(), sch.loc_fine_list)
            find_head = 0
            fineloc_list = []
            while find_head < len(sch.loc_fine_list):
                vis.total += 1
                # 1 seed inputs
                stloc_list = [sch.loc_fine_list[find_head], ]
                find_head += 1
                mutseed = Mutator.mutOneChar(init_seed.content, path_mutseeds, FINE_STR + str(vis.loop), stloc_list)
                execute_seed = sch.selectOneSeed(SCH_THIS_SEED, mutseed)
                mut_stdout, mut_stderr = Executor.run(fuzz_command.replace('@@', execute_seed.filename))
                sch.saveCrash(file_crash_csv, path_crashseeds, execute_seed, mut_stdout, mut_stderr)

                # 2 cmp instruction
                # Track execution information of mutate seeds.
                cmpcovcont_list, content = ana.gainTraceRpt(mut_stdout)  # report
                mutrpt_dict, mutrpt_set = ana.traceAyalysis(cmpcovcont_list, content, sch.freezeid_rpt)
                cmpmaploc_rptdict = ana.compareRptToLoc(
                    execute_seed,
                    initrpt_dict, initrpt_set,
                    mutrpt_dict, mutrpt_set
                )
                if st_key in cmpmaploc_rptdict:
                    fineloc_list.extend(stloc_list)

                LOG(LOG_DEBUG, LOG_FUNCINFO(), mutrpt_dict, mutrpt_set, cmpmaploc_rptdict)
                # 5 visualize
                res = vis.display(execute_seed, set(stloc_list), mut_stdout, mut_stderr)
                if res == QUIT_FUZZ:
                    sch.quitFuzz()
            LOG(LOG_DEBUG, LOG_FUNCINFO(), st_key, st_coarseval, fineloc_list)

            '''Type detect and Mutation strategy'''
            fineloc_list.sort()
            st_seed = Mutator.mutSelectChar(init_seed.content, path_mutseeds, ST_STR + str(vis.loop), fineloc_list)
            sch.addSeeds(SCH_MUT_SEED, [st_seed, ])
            optrpt_dict = initrpt_dict
            opt_seed = init_seed
            # Type Detection and Breaking the Constraint Cycle (At lease 2 loops)
            while not sch.isEmpty(SCH_MUT_SEED):
                vis.total += 1
                execute_seed = sch.selectOneSeed(SCH_MUT_SEED)
                st_stdout, st_stderr = Executor.run(fuzz_command.replace('@@', execute_seed.filename))
                sch.saveCrash(file_crash_csv, path_crashseeds, execute_seed, st_stdout, st_stderr)

                # 2 cmp instruction
                # Generate analysis reports.
                cmpcovcont_list, content = ana.gainTraceRpt(st_stdout)
                strpt_dict, strpt_set = ana.traceAyalysis(cmpcovcont_list, content, sch.freezeid_rpt)  # report
                LOG(LOG_DEBUG, LOG_FUNCINFO(), opt_seed.content, execute_seed.content)

                # 3 cmp type
                # Return cmp type and mutate strategy according to typeDetect
                ret_seed, type_infer_set, locmapdet_dict = Parser.typeDetect(
                    opt_seed, execute_seed, fineloc_list, st_key,
                    optrpt_dict, strpt_dict, sch
                )

                # Comparison of global optimal values to achieve updated parameters
                optrpt_dict = optrpt_dict if ret_seed == opt_seed else strpt_dict
                opt_seed = ret_seed

                LOG(LOG_DEBUG, LOG_FUNCINFO(), locmapdet_dict, content, st_key, fineloc_list)
                LOG(LOG_DEBUG, LOG_FUNCINFO(), execute_seed.location, ret_seed.content, type_infer_set)

                if TYPE_SOLVED in type_infer_set:
                    sch.solved_cmpset.add(st_key)
                    sch.freeze_bytes = sch.freeze_bytes | set(fineloc_list)
                    sch.freezeid_rpt.add(st_key)
                    sch.addSeeds(SCH_LOOP_SEED, [ret_seed, ])
                # Passing the constraint based on the number of cycles and the distance between comparisons.
                st_seed = Mutator.mutLocFromMap(ret_seed.content, path_mutseeds, ST_STR + str(vis.loop), locmapdet_dict)

                if st_seed is not None:
                    sch.addSeeds(SCH_MUT_SEED, [st_seed, ])

                # 5 visualize
                res = vis.display(ret_seed, set(fineloc_list), st_stdout, st_stderr)
                if res == QUIT_FUZZ:
                    sch.quitFuzz()

        # Endless fuzzing
        if sch.isEmpty(SCH_LOOP_SEED):
            sch.addSeeds(SCH_LOOP_SEED, [init_seed, ])

        # 4 branches



if __name__ == "__main__":
    mainFuzzer()


