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
        temp_listq.append(StructSeed(path_mutateseeds+each, "", INIT, {-1, }))
    sch.addSeeds(SCH_INIT_SEED, temp_listq)

    # Fuzzing test cycle
    while not sch.isEmpty(SCH_INIT_SEED):
        loop += 1
        # First run to collect information.
        init_seed = sch.selectOneSeed(SCH_INIT_SEED)
        init_retcode, init_stdout, init_stderr = Executor.run(fuzz_command.replace('@@', init_seed.filename))
        init_trace = ana.traceAyalysis(init_stdout)

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
        coarse_len = len(sch.locCoarseList)
        while coarse_head <= coarse_len:
            total += 1
            # 1 seed inputs
            mutloc_list = sch.locCoarseList[coarse_head:coarse_head+sch.slidWindow]
            coarse_head += sch.slidWindow
            mutseed = Mutator.mutateSelectChar(init_seed.content, path_mutateseeds, str(loop), mutloc_list)
            execute_seed = sch.selectOneSeed(SCH_THIS_SEED, mutseed)
            mut_retcode, mut_stdout, mut_stderr = Executor.run(fuzz_command.replace('@@', execute_seed.filename))
            mut_trace = ana.traceAyalysis(mut_stdout)

            # 2 cmp instruction
            # Track execution information of mutate seeds.

            raise Exception()

            # 3 cmp type

            # Analyze the differences in comparison.
            report_cmpdiff, report_cmpone = Parser.compareBytes(execute_seed, init_trace, mut_trace)
            each_change_inputmap = Parser.typeDetect(report_cmpdiff, report_cmpone, cmp_map, mutate_loc)
            # mergeMapReport(each_change_inputmap, eachloop_change_inputmap)

            # 4 branches

            # 5 visualize

            res = vis.display(start_time, execute_seed, eachloop_change_inputmap, loop, total)
            if res == 1:
                sch.deleteSeeds()
                return

        # Fine-Grained
        # Mutate seeds to find where to change. Then perform to a directed mutate.
        # Only the corresponding position is speculated. O(1)
        while True:
            break

        LOG(LOG_DEBUG, LOG_STR(LOG_FUNCINFO(), cmp_map, eachloop_change_inputmap))

        temp_content = list(init_seed.content)
        for k, v in eachloop_change_inputmap.items():
            temp_content[k] = v
        temp_content = ''.join(temp_content)
        sch.addSeeds(SCH_INIT_SEED, [StructSeed(path_mutateseeds+getMutfilename("loop"+str(loop)),
                                         temp_content, INIT, [0, 0])])
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


