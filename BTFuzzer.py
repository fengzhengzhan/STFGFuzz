import time
import sys
import getopt
import os
import re
import curses

from Fuzzconfig import *
from Tools import *

import Analyzer
import Builder
import Executor
import Generator
import History
import Monitor
import Mutator
import Parser
import Scheduler
import Visualizer


def mainFuzzer():
    '''
    The fuzzing Loop.
    '''

    # Receive command line parameters.
    program_name = ""
    init_seed = ""
    start_time = time.time()
    loop = 0
    vis = Visualizer.Visualizer()
    sch = Scheduler.Scheduler()

    try:
        opts, args = getopt.getopt(sys.argv[1:], "hn:")
        # print(opts, args)
        LOG(LOG_DEBUG, LOG_STR(LOG_FUNCINFO(), opts, args))
    except getopt.GetoptError:
        print("{}.py -- [files] [OPTIONS] @@".format(BTFUZZ))
        raise Exception("Error options.")

    for opt, arg in opts:
        if opt == "-h":
            print("{}.py -- [files] [OPTIONS] @@".format(BTFUZZ))
            print("e.g. python {}.py -n demo -- ./Programs/Bin/demo -f @@".format(BTFUZZ))
            # python3.7 BTFuzzer.py -n demo -- ./Programs/Bin/demo -f @@
            sys.exit()
        elif opt == "-n":
            program_name = arg

    fuzz_command = " ".join(args)

    if fuzz_command == "" or program_name == "":
        print("e.g. python {}.py -n demo -- ./Programs/Bin/demo -f @@".format(BTFUZZ))
        raise Exception("Error empty parameters for fuzzing test files.")

    filepath_initseeds = SEEDPOOL + os.sep + INITSEEDS + os.sep + program_name + os.sep
    filepath_mutateseeds = SEEDPOOL + os.sep + MUTATESEEDS + os.sep + program_name + os.sep
    filepath_crashseeds = SEEDPOOL + os.sep + CRASHSEEDS + os.sep + program_name + os.sep
    LOG(LOG_DEBUG, LOG_STR(LOG_FUNCINFO(), filepath_initseeds, filepath_mutateseeds, filepath_crashseeds))

    # print(fuzz_command)
    LOG(LOG_DEBUG, LOG_STR(LOG_FUNCINFO(), fuzz_command))

    # Fuzzing test procedure.
    constraint_graph: list[dict, dict] = []
    cmp_map: dict = {}
    input_map: dict[list] = {}
    eachloop_input_map: dict = {}
    init_seeds_list = Generator.prepareEnv(program_name)
    sch.addSeeds(filepath_mutateseeds, init_seeds_list)

    # Fuzzing test cycle
    while True:
        loop += 1
        # First run to collect information.
        init_seed = sch.selectOneSeed()
        seed_content = init_seed.content
        init_ret_code, init_std_out, init_std_err = Executor.run(fuzz_command.replace('@@', init_seed.filename))
        init_num_of_pcguard, init_trace_analysis = Analyzer.traceAyalysis(init_std_out)

        # Mutate seeds to find where to change. Then perform to a directed mutate.
        mutate_contents, record_list = Mutator.mutateSeeds(seed_content)
        # print(mutate_seeds, record_list)
        structseed_list = Mutator.mutateSaveAsFile(mutate_contents, record_list, filepath_mutateseeds, str(loop))
        sch.addMutSeeds(structseed_list)

        while not sch.mutateTestqEmpty():
            # Track execution information of mutate seeds.
            execute_seed = sch.selectMutOneSeed()
            mut_ret_code, mut_std_out, mut_std_err = Executor.run(fuzz_command.replace('@@', execute_seed.filename))
            mut_num_of_pcguard, mut_trace_analysis = Analyzer.traceAyalysis(mut_std_out)

            # Analyze the differences in comparison.
            comparison_report, cmp_map = Parser.compareBytes(init_trace_analysis, mut_trace_analysis, [execute_seed.seedtype, execute_seed.location[0], execute_seed.location[1]], cmp_map)
            cmp_map, eachloop_input_map = Parser.typeSpeculation(comparison_report, cmp_map, eachloop_input_map)
        # print(eachloop_input_map)
        LOG(LOG_DEBUG, LOG_STR(LOG_FUNCINFO(), cmp_map, eachloop_input_map))
        sch.deleteSeeds()

        temp_content = list(seed_content)
        for k, v in eachloop_input_map.items():
            temp_content[k] = v
        temp_content = ''.join(temp_content)
        filelist_mutateseeds = Mutator.mutateSaveAsFile([temp_content], filepath_mutateseeds, "loop"+str(loop))
        execute_seed = filepath_mutateseeds + filelist_mutateseeds[0]
        sch.addSeeds()
        # Mutator.mutateDeleteFile(filelist_mutateseeds, filepath_mutateseeds)
        # print(filelist_mutateseeds)
        # print(mutate_seeds)

        res = vis.display(start_time, seed_content, eachloop_input_map)
        if res == 1:
            break
        eachloop_input_map = {}
        # raise Exception("test")


if __name__ == "__main__":
    try:
        mainFuzzer()
    except Exception as e:
        curses.endwin()
        print(e)


