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
    init_seed = ""
    start_time = time.time()
    loop = 0
    total = 0
    vis = Visualizer.Visualizer()
    sch = Scheduler.Scheduler()
    ana = Analyzer.Analyzer()

    try:
        opts, args = getopt.getopt(sys.argv[1:], "hn:")
        # print(opts, args)
        LOG(LOG_DEBUG, LOG_STR(LOG_FUNCINFO(), opts, args))
    except getopt.GetoptError:
        print("{}.py -- [files] [OPTIONS] @@".format(FUZZNAME))
        raise Exception("Error options.")

    for opt, arg in opts:
        if opt == "-h":
            print("{}.py -- [files] [OPTIONS] @@".format(FUZZNAME))
            print("e.g. python {}.py -n demo -- ./Programs/demo/code_Bin/demo -f @@".format(FUZZNAME))
            # python3.7 BTFuzzer.py -n demo -- ./Programs/demo/code_Bin/demo -f @@
            sys.exit()
        elif opt == "-n":
            program_name = arg

    fuzz_command = " ".join(args)

    if fuzz_command == "" or program_name == "":
        print("e.g. python {}.py -n demo -- ./Programs/Bin/demo -f @@".format(FUZZNAME))
        raise Exception("Error empty parameters for fuzzing test files.")

    filepath_initseeds = PROGRAMS + os.sep + program_name + os.sep + SEEDSINIT + os.sep
    filepath_mutateseeds = PROGRAMS + os.sep + program_name + os.sep + SEEDSMUTATE + os.sep
    filepath_crashseeds = PROGRAMS + os.sep + program_name + os.sep + SEEDSCRASH + os.sep
    LOG(LOG_DEBUG, LOG_STR(LOG_FUNCINFO(), filepath_initseeds, filepath_mutateseeds, filepath_crashseeds))

    # print(fuzz_command)
    LOG(LOG_DEBUG, LOG_STR(LOG_FUNCINFO(), fuzz_command))

    # Fuzzing test procedure.
    constraint_graph: 'list[dict, dict]' = StructConstraintGraph().constraintgraph
    cmp_map: dict = StructCmpMap().cmpmap
    input_map: dict[list] = {}
    mutate_loc = StructMutateLocation()
    eachloop_change_inputmap: dict = {}
    init_seeds_list = Generator.prepareEnv(program_name)
    temp_listq = []
    for each in init_seeds_list:
        temp_listq.append(StructSeed(filepath_mutateseeds+each, "", INIT, [0, 0]))
    sch.addSeeds(SCH_INIT_SEED, temp_listq)

    # Fuzzing test cycle
    while not sch.isEmpty(SCH_INIT_SEED):
        loop += 1
        # First run to collect information.
        init_seed = sch.selectOneSeed(SCH_INIT_SEED)
        saveAsFile(init_seed.content, init_seed.filename)
        init_ret_code, init_std_out, init_std_err = Executor.run(fuzz_command.replace('@@', init_seed.filename))
        init_trace_analysis = ana.traceAyalysis(init_std_out)
        init_num_of_pcguard = ana.getNumOfPcguard()

        # Mutate seeds to find where to change. Then perform to a directed mutate.
        temp_mutate_listq = Mutator.mutateSeeds(init_seed.content, filepath_mutateseeds, str(loop))
        sch.addSeeds(SCH_MUT_SEED, temp_mutate_listq)
        # print(mutate_seeds, record_list)

        while not sch.isEmpty(SCH_MUT_SEED):
            total += 1
            # Track execution information of mutate seeds.
            execute_seed = sch.selectOneSeed(SCH_MUT_SEED)
            saveAsFile(execute_seed.content, execute_seed.filename)
            mut_ret_code, mut_std_out, mut_std_err = Executor.run(fuzz_command.replace('@@', execute_seed.filename))
            mut_trace_analysis = ana.traceAyalysis(mut_std_out)

            # Analyze the differences in comparison.
            comparison_diffreport, comparison_onereport = Parser.compareBytes(execute_seed, init_trace_analysis, mut_trace_analysis)
            each_change_inputmap = Parser.typeSpeculation(comparison_diffreport, comparison_onereport, cmp_map, mutate_loc)

            mergeMapReport(each_change_inputmap, eachloop_change_inputmap)
            res = vis.display(start_time, execute_seed, eachloop_change_inputmap, loop, total)
            if res == 1:
                sch.deleteSeeds()
                return
        LOG(LOG_DEBUG, LOG_STR(LOG_FUNCINFO(), cmp_map, eachloop_change_inputmap))

        temp_content = list(init_seed.content)
        for k, v in eachloop_change_inputmap.items():
            temp_content[k] = v
        temp_content = ''.join(temp_content)
        sch.addSeeds(SCH_INIT_SEED, [StructSeed(filepath_mutateseeds+getMutfilename("loop"+str(loop)),
                                         temp_content, INIT, [0, 0])])
        # Mutator.mutateDeleteFile(filelist_mutateseeds, filepath_mutateseeds)
        # print(filelist_mutateseeds)
        # print(mutate_seeds)

        eachloop_change_inputmap = {}
        res = vis.display(start_time, init_seed, eachloop_change_inputmap, loop, total)
        if res == 1:
            sch.deleteSeeds()
            return
        # raise Exception("test")


if __name__ == "__main__":
    # mainFuzzer()
    try:
        mainFuzzer()
    except Exception as e:
        curses.endwin()
        print(e)


