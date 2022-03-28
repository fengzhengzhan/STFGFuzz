import time
import sys
import getopt
import os
import re
import curses

from fuzzer_module import *
from fuzzer_module.Fuzzconfig import *


def mainFuzzer():
    """
    The fuzzing Loop.
    @return:
    """

    # Receive command line parameters.
    program_name = ""
    patchtype = USE_INITNUM

    try:
        opts, args = getopt.getopt(sys.argv[1:], "hn:t:")
        # print(opts, args)
        LOG(LOG_DEBUG, LOG_STR(LOG_FUNCINFO(), opts, args))
    except getopt.GetoptError:
        print("python {}.py -h".format(FUZZNAME))
        raise Exception("Error options.")

    for opt, arg in opts:
        if opt == "-h":
            print()
            print("Usage:")
            print(" python {}.py [OPTIONS] -- [files] [OPTIONS] @@".format(FUZZNAME))
            print(" python {}.py -n demo -- ./Programs/demo/code_Bin/demo -f @@".format(FUZZNAME))
            print(" python {}.py -n demo -t manual -- ./Programs/demo/code_Bin/demo -f @@".format(FUZZNAME))
            print()
            print("STFGFuzzer")
            print()
            print("Options:")
            print(" -n <program_name>   Specify the name of the program item to be mutated.")
            print(" -t ['patch','sanitizer','manual']   Specify the target location file type.")
            print()
            sys.exit()
        elif opt == "-n":
            program_name = arg
        elif opt == "-t":
            patchtype = arg

    fuzz_command = " ".join(args)

    if fuzz_command == "" or program_name == "" or patchtype not in COM_PATCHSET:
        print("python {}.py -h".format(FUZZNAME))
        raise Exception("Error parameters.")

    path_initseeds = PROGRAMS + os.sep + program_name + os.sep + SEEDSINIT + os.sep
    path_mutateseeds = PROGRAMS + os.sep + program_name + os.sep + SEEDSMUTATE + os.sep
    path_crashseeds = PROGRAMS + os.sep + program_name + os.sep + SEEDSCRASH + os.sep
    path_graph = PROGRAMS + os.sep + program_name + os.sep + DATAGRAPH + os.sep
    path_codeIR = PROGRAMS + os.sep + program_name + os.sep + CODEIR + os.sep
    LOG(LOG_DEBUG, LOG_STR(LOG_FUNCINFO(), path_initseeds, path_mutateseeds, path_crashseeds))

    # print(fuzz_command)
    LOG(LOG_DEBUG, LOG_STR(LOG_FUNCINFO(), fuzz_command))

    '''Fuzzing test procedure.'''
    start_time = time.time()
    loop = 0
    total = 0
    loc_interval = 8
    vis = Visualizer.Visualizer()
    sch = Scheduler.Scheduler()
    ana = Analyzer.Analyzer()
    cglist, cfglist = Generator.createDotJsonFile(program_name, path_codeIR+program_name+GEN_TRACEBC_SUFFIX)
    cggraph, map_funcTocgname = Builder.getCG(cglist)
    cfggraph_dict, map_guardTocfgname = Builder.getCFG(cfglist)
    # vis.showGraph(path_graph, cggraph, cfggraph_dict['main'])

    constraint_graph: 'list[dict, dict]' = StructSTGraph().constraintgraph
    cmp_map: dict = StructCmpMap().cmpmap
    input_map: dict[list] = {}
    mutate_loc = StructMutLoc()
    eachloop_change_inputmap: dict = {}
    init_seeds_list = Generator.prepareEnv(program_name)

    # Init seed lists
    temp_listq = []
    for each in init_seeds_list:
        temp_listq.append(StructSeed(path_mutateseeds+each, "", INIT, {-1, }))
    sch.addSeeds(SCH_INIT_SEED, temp_listq)

    # Fuzzing test cycle
    while not sch.isEmpty(SCH_INIT_SEED):
        loop += 1
        # First run to collect information.
        init_seed = sch.selectOneSeed(SCH_INIT_SEED)
        saveAsFile(init_seed.content, init_seed.filename)
        init_retcode, init_stdout, init_stderr = Executor.run(fuzz_command.replace('@@', init_seed.filename))
        init_trace = ana.traceAyalysis(init_stdout)
        num_pcguard = ana.getNumOfPcguard()

        # Mutate seeds to find where to change. Then perform to a directed mutate.
        # temp_mutate_listq = Mutator.mutateSeeds(init_seed.content, path_mutateseeds, str(loop))
        # sch.addSeeds(SCH_MUT_SEED, temp_mutate_listq)
        # print(mutate_seeds, record_list)
        for loci in range(0, len(init_seed.content)):
            sch.locCoarseq.put(loci)

        # Find correspondence
        '''XXX: seed inputs -> cmp instruction -> cmp type (access method) -> braches'''
        # Coarse-Grained  O(n)  # todo multiprocessing
        # Get a report on changes to comparison instructions.
        while not sch.isEmpty(SCH_COARSE_SEED):
            total += 1
            # 1 seed inputs
            loc_set = set()
            for locl in range(0, sch.slidWindow):
                if not sch.isEmpty(SCH_COARSE_SEED):
                    loc_set.add(sch.getValue(SCH_COARSE_SEED))
            # print(loc_set)

            # 2 cmp instruction

            # Track execution information of mutate seeds.
            # execute_seed = sch.selectOneSeed(SCH_MUT_SEED)
            execute_seed = Mutator.mutateSelectChar(init_seed.content, path_mutateseeds, str(loop), loc_set)
            sch.addDeleteq(execute_seed)
            saveAsFile(execute_seed.content, execute_seed.filename)
            mut_retcode, mut_stdout, mut_stderr = Executor.run(fuzz_command.replace('@@', execute_seed.filename))
            mut_trace = ana.traceAyalysis(mut_stdout)
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
        # Only the corresponding position is speculated. O(1)

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


