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
    path_mutateseeds = PROGRAMS + os.sep + program_name + os.sep + SEEDSMUTATE + os.sep
    path_crashseeds = PROGRAMS + os.sep + program_name + os.sep + SEEDSCRASH + os.sep
    path_graph = PROGRAMS + os.sep + program_name + os.sep + DATAGRAPH + os.sep
    path_codeIR = PROGRAMS + os.sep + program_name + os.sep + CODEIR + os.sep
    LOG(LOG_DEBUG, LOG_FUNCINFO(), path_initseeds, path_mutateseeds, path_crashseeds)

    '''Fuzzing test procedure.'''
    vis = Visualizer.Visualizer()
    sch = Scheduler.Scheduler()
    ana = Analyzer.Analyzer()
    cglist, cfglist = Generator.createDotJsonFile(program_name, path_codeIR+program_name+GEN_TRACEBC_SUFFIX)
    cggraph, map_funcTocgname = Builder.getCG(cglist)
    cfggraph_dict, map_guardTocfgname = Builder.getCFG(cfglist)
    # vis.showGraph(path_graph, cggraph, cfggraph_dict['main'])

    start_time = time.time()
    loop = 0
    total = 0

    st_graph: 'list[dict, dict]' = StructSTGraph().constraintgraph
    cmp_map: dict = StructCmpMap().cmpmap
    input_map: dict[list] = {}
    mutate_loc = StructMutLoc()
    solved_cmpset = set()
    init_seeds_list = Generator.prepareEnv(program_name)

    # Init seed lists  # todo if == null
    temp_listq = []
    for each in init_seeds_list:
        temp_listq.append(StructSeed(path_mutateseeds+each, "", INIT, {USE_INITNUM}))
    sch.addSeeds(SCH_LOOP_SEED, temp_listq)

    # Fuzzing test cycle
    while not sch.isEmpty(SCH_LOOP_SEED):
        loop += 1
        # First run to collect information.
        init_seed = sch.selectOneSeed(SCH_LOOP_SEED)
        init_retcode, init_stdout, init_stderr = Executor.run(fuzz_command.replace('@@', init_seed.filename))
        cmpcovcont_list, content = ana.gainTraceRpt(init_stdout)
        initrpt_dict, initrpt_set = ana.traceAyalysis(cmpcovcont_list, content)

        num_pcguard = ana.getNumOfPcguard()

        # Select the location to be mutated and add it to the location queue.
        sch.initEachloop()
        for loci in range(0, len(init_seed.content)):
            if loci not in sch.freezebytes:
                sch.locCoarseList.append(loci)


        # Find correspondence
        '''XXX: seed inputs -> cmp instruction -> cmp type (access method) -> braches'''

        # Coarse-Grained  O(n)  # todo multiprocessing
        # Get a report on changes to comparison instructions.
        coarse_head = 0
        cmpmaploc_coarse_dict = {}
        while coarse_head < len(sch.locCoarseList):
            total += 1
            # 1 seed inputs
            stloc_list = sch.locCoarseList[coarse_head:coarse_head+sch.slidWindow]
            coarse_head += sch.slidWindow // 2
            mutseed = Mutator.mutateSelectChar(init_seed.content, path_mutateseeds, COARSE_STR+str(loop), stloc_list)
            execute_seed = sch.selectOneSeed(SCH_THIS_SEED, mutseed)
            mut_retcode, mut_stdout, mut_stderr = Executor.run(fuzz_command.replace('@@', execute_seed.filename))

            # 2 cmp instruction
            # Track execution information of mutate seeds.
            cmpcovcont_list, content = ana.gainTraceRpt(mut_stdout)  # report
            mutrpt_dict, mutrpt_set = ana.traceAyalysis(cmpcovcont_list, content)
            cmpmaploc_rptdict = Parser.compareRptToLoc(execute_seed, initrpt_dict, initrpt_set, mutrpt_dict, mutrpt_set)
            for cmp_key, cmp_val in cmpmaploc_rptdict.items():  # Determine if the dictionary is empty.
                if cmp_key not in solved_cmpset:
                    if cmp_key not in cmpmaploc_coarse_dict:
                        cmpmaploc_coarse_dict[cmp_key] = cmp_val
                    else:
                        cmpmaploc_coarse_dict[cmp_key] = cmpmaploc_coarse_dict[cmp_key] | cmp_val
            LOG(LOG_DEBUG, LOG_FUNCINFO(), mutrpt_dict, mutrpt_set, cmpmaploc_rptdict)

            # 5 visualize
            res = vis.display(execute_seed, set(stloc_list), mut_stdout, mut_stderr, start_time, loop, total)
            if res == QUIT_FUZZ:
                sch.quitFuzz()
        LOG(LOG_DEBUG, LOG_FUNCINFO(), cmpmaploc_coarse_dict)

        # 3 cmp type
        # Compare instruction type speculation based on input mapping,
        # then try to pass the corresponding constraint (1-2 rounds).
        for st_key, st_coarseval in cmpmaploc_coarse_dict.items():
            # Fine-Grained
            # Mutate seeds to find where to change. Then perform to a directed mutate.
            # Only the corresponding position is speculated. O(1)
            sch.locFineList = list(st_coarseval)
            sch.locFineList.sort()
            LOG(LOG_DEBUG, LOG_FUNCINFO(), sch.locFineList)
            find_head = 0
            fineloc_list = []
            while find_head < len(sch.locFineList):
                total += 1
                # 1 seed inputs
                stloc_list = [sch.locFineList[find_head], ]
                find_head += 1
                mutseed = Mutator.mutateOneChar(init_seed.content, path_mutateseeds, FINE_STR + str(loop), stloc_list)
                execute_seed = sch.selectOneSeed(SCH_THIS_SEED, mutseed)
                mut_retcode, mut_stdout, mut_stderr = Executor.run(fuzz_command.replace('@@', execute_seed.filename))

                # 2 cmp instruction
                # Track execution information of mutate seeds.
                cmpcovcont_list, content = ana.gainTraceRpt(mut_stdout)  # report
                mutrpt_dict, mutrpt_set = ana.traceAyalysis(cmpcovcont_list, content)
                cmpmaploc_rptdict = Parser.compareRptToLoc(execute_seed, initrpt_dict, initrpt_set, mutrpt_dict, mutrpt_set)
                if st_key in cmpmaploc_rptdict:
                    fineloc_list.extend(stloc_list)
                LOG(LOG_DEBUG, LOG_FUNCINFO(), mutrpt_dict, mutrpt_set, cmpmaploc_rptdict)

                # 5 visualize
                res = vis.display(execute_seed, set(stloc_list), mut_stdout, mut_stderr, start_time, loop, total)
                if res == QUIT_FUZZ:
                    sch.quitFuzz()
            LOG(LOG_DEBUG, LOG_FUNCINFO(), st_key, st_coarseval, fineloc_list)

            st_seed = Mutator.mutateSelectChar(init_seed.content, path_mutateseeds, ST_STR + str(loop), fineloc_list)
            sch.addSeeds(SCH_MUT_SEED, [st_seed])
            before_strpt_dict = initrpt_dict
            # Type Detection and Breaking the Constraint Cycle (At lease 2 loops)
            while not sch.isEmpty(SCH_MUT_SEED):
                total += 1
                execute_seed = sch.selectOneSeed(SCH_MUT_SEED)
                st_retcode, st_stdout, st_stderr = Executor.run(fuzz_command.replace('@@', execute_seed.filename))

                # 2 cmp instruction
                cmpcovcont_list, content = ana.gainTraceRpt(st_stdout)
                strpt_dict, strpt_set = ana.traceAyalysis(cmpcovcont_list, content)  # report
                # Return cmp type and mutate strategy according to typeDetect
                type_infer_set, locmapdet_dict = Parser.typeDetect(execute_seed, st_key, before_strpt_dict, strpt_dict)
                before_strpt_dict = strpt_dict
                if TYPE_MAGICNUMS in type_infer_set:
                    LOG(LOG_DEBUG, LOG_FUNCINFO(), cmpcovcont_list, content, print_mode=True)
                LOG(LOG_DEBUG, LOG_FUNCINFO(), type_infer_set, locmapdet_dict)
                if TYPE_SOLVED in type_infer_set:
                    solved_cmpset.add(st_key)
                    sch.freezebytes = sch.freezebytes | set(fineloc_list)
                    sch.addSeeds(SCH_LOOP_SEED, [execute_seed, ])
                # Passing the constraint based on the number of cycles and the distance between comparisons.
                st_seed = Mutator.mutateLocFromMap(execute_seed.content, path_mutateseeds, ST_STR + str(loop), locmapdet_dict)

                # 5 visualize
                res = vis.display(execute_seed, set(fineloc_list), st_stdout, st_stderr, start_time, loop, total)
                if res == QUIT_FUZZ:
                    sch.quitFuzz()

                if st_seed is not None:
                    sch.addSeeds(SCH_MUT_SEED, [st_seed, ])

        # Endless fuzzing
        if sch.isEmpty(SCH_LOOP_SEED):
            sch.addSeeds(SCH_LOOP_SEED, [init_seed, ])

        # 4 branches



if __name__ == "__main__":
    mainFuzzer()


