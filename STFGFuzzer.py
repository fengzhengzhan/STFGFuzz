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
    LOG(LOG_DEBUG, LOG_STR(LOG_FUNCINFO(), path_initseeds, path_mutateseeds, path_crashseeds))

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
    eachloop_change_inputmap: dict = {}
    init_seeds_list = Generator.prepareEnv(program_name)

    # Init seed lists  # todo if == null
    temp_listq = []
    for each in init_seeds_list:
        temp_listq.append(StructSeed(path_mutateseeds+each, "", INIT, {USE_INITNUM}))
    sch.addSeeds(SCH_INIT_SEED, temp_listq)

    # Fuzzing test cycle
    while not sch.isEmpty(SCH_INIT_SEED):
        loop += 1
        # First run to collect information.
        init_seed = sch.selectOneSeed(SCH_INIT_SEED)
        init_retcode, init_stdout, init_stderr = Executor.run(fuzz_command.replace('@@', init_seed.filename))
        initrpt_dict, initrpt_set = ana.traceAyalysis(init_stdout)
        num_pcguard = ana.getNumOfPcguard()

        # Select the location to be mutated and add it to the location queue.
        sch.initEachloop()
        for loci in range(0, len(init_seed.content)):
            sch.locCoarseList.append(loci)

        # Find correspondence
        '''XXX: seed inputs -> cmp instruction -> cmp type (access method) -> braches'''

        # Coarse-Grained  O(n)  # todo multiprocessing
        # Get a report on changes to comparison instructions.
        coarse_head = 0
        fine_set = set()
        while coarse_head < len(sch.locCoarseList):
            total += 1
            # 1 seed inputs
            stloc_list = sch.locCoarseList[coarse_head:coarse_head+sch.slidWindow]
            coarse_head += sch.slidWindow
            mutseed = Mutator.mutateSelectChar(init_seed.content, path_mutateseeds, COARSE_STR+str(loop), stloc_list)
            execute_seed = sch.selectOneSeed(SCH_THIS_SEED, mutseed)
            mut_retcode, mut_stdout, mut_stderr = Executor.run(fuzz_command.replace('@@', execute_seed.filename))

            # 2 cmp instruction
            # Track execution information of mutate seeds.
            mutrpt_dict, mutrpt_set = ana.traceAyalysis(mut_stdout)  # report
            cmpmaploc_rptdict = Parser.compareRptToLoc(execute_seed, initrpt_dict, initrpt_set, mutrpt_dict, mutrpt_set)
            if cmpmaploc_rptdict:  # Determine if the dictionary is empty.
                fine_set = fine_set | set(stloc_list)

            LOG(LOG_DEBUG, LOG_STR(LOG_FUNCINFO(), mutrpt_dict, mutrpt_set, cmpmaploc_rptdict))
            res = vis.display(start_time, execute_seed, eachloop_change_inputmap, loop, total)
            if res == 1:
                sch.deleteSeeds()
                return

        # Fine-Grained
        # Mutate seeds to find where to change. Then perform to a directed mutate.
        # Only the corresponding position is speculated. O(1)
        sch.locFineList = list(fine_set)
        LOG(LOG_DEBUG, LOG_STR(LOG_FUNCINFO(), sch.locFineList))
        find_head = 0
        cmpmaploc_dict = {}
        while find_head < len(sch.locFineList):
            total += 1
            # 1 seed inputs
            stloc_list = [sch.locFineList[find_head], ]
            find_head += 1
            mutseed = Mutator.mutateOneChar(init_seed.content, path_mutateseeds, FINE_STR+str(loop), stloc_list)
            execute_seed = sch.selectOneSeed(SCH_THIS_SEED, mutseed)
            mut_retcode, mut_stdout, mut_stderr = Executor.run(fuzz_command.replace('@@', execute_seed.filename))

            # 2 cmp instruction
            # Track execution information of mutate seeds.
            mutrpt_dict, mutrpt_set = ana.traceAyalysis(mut_stdout)  # report
            cmpmaploc_rptdict = Parser.compareRptToLoc(execute_seed, initrpt_dict, initrpt_set, mutrpt_dict, mutrpt_set)
            if cmpmaploc_rptdict:  # Determine if the dictionary is empty.
                for ck, cv in cmpmaploc_rptdict.items():
                    if ck not in cmpmaploc_dict:
                        cmpmaploc_dict[ck] = cv
                    else:
                        cmpmaploc_dict[ck] = cmpmaploc_dict[ck] | cv
            LOG(LOG_DEBUG, LOG_STR(LOG_FUNCINFO(), mutrpt_dict, mutrpt_set, cmpmaploc_rptdict))
            res = vis.display(start_time, execute_seed, eachloop_change_inputmap, loop, total)
            if res == 1:
                sch.deleteSeeds()
                return
        LOG(LOG_DEBUG, LOG_STR(LOG_FUNCINFO(), cmpmaploc_dict, print_mode=True))

        # 3 cmp type
        # Compare instruction type speculation based on input mapping,
        # then try to pass the corresponding constraint (1-2 rounds).
        for st_key, st_val in cmpmaploc_dict.items():
            total += 1
            # 1 seed inputs
            stloc_list = list(st_val)
            st_seed = Mutator.mutateSelectChar(init_seed.content, path_mutateseeds, ST_STR+str(loop), stloc_list)
            execute_seed = sch.selectOneSeed(SCH_THIS_SEED, st_seed)
            st_retcode, st_stdout, st_stderr = Executor.run(fuzz_command.replace('@@', execute_seed.filename))

            # 2 cmp instruction
            strpt_dict, strpt_set = ana.traceAyalysis(st_stdout)  # report
            # Return cmp type and mutate strategy according to typeDetect
            cmpmaploc_rptdict = Parser.typeDetect(execute_seed, st_key, initrpt_dict, strpt_dict)
            # Passing the constraint based on the number of cycles and the distance between comparisons.
            while True:
                Parser.exeTypeStrategy()
                if sch.isEmpty(SCH_MUT_SEED):
                    break

        # Analyze the differences in comparison.
        # mergeMapReport(each_change_inputmap, eachloop_change_inputmap)

        # 4 branches

        # 5 visualize

        # res = vis.display(start_time, execute_seed, eachloop_change_inputmap, loop, total)
        # if res == 1:
        #     sch.deleteSeeds()
        #     return


        temp_content = list(init_seed.content)
        for k, v in eachloop_change_inputmap.items():
            temp_content[k] = v
        temp_content = ''.join(temp_content)
        sch.addSeeds(SCH_INIT_SEED, [
            StructSeed(path_mutateseeds+getMutfilename("loop"+str(loop)), temp_content, INIT, {USE_INITNUM})])
        # Mutator.mutateDeleteFile(filelist_mutateseeds, path_mutateseeds)
        # print(filelist_mutateseeds)
        # print(mutate_seeds)

        eachloop_change_inputmap = {}
        res = vis.display(start_time, init_seed, eachloop_change_inputmap, loop, total)
        if res == 1:
            sch.deleteSeeds()
            return
        # raise Exception("test")


if __name__ == "__main__":
    mainFuzzer()


