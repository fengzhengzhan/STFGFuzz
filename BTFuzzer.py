import time
import sys
import getopt
import os
import re

import Parser
from Fuzzconfig import *
import Analyzer
import Builder
import Executor
import Generator
import History
import Monitor
import Mutator
import Scheduler
import Visualizer


def mainFuzzer():
    '''
    The fuzzing Loop.
    '''

    # Receive command line parameters.
    fuzz_command = ""
    program_name = ""
    init_seed = ""

    try:
        opts, args = getopt.getopt(sys.argv[1:], "hn:")
        # print(opts, args)
        FUZZLOGGING(DEBUG, LOG_STR(LOG_FUNCINFO(), opts, args))
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
    FUZZLOGGING(DEBUG, LOG_STR(LOG_FUNCINFO(), filepath_initseeds, filepath_mutateseeds, filepath_crashseeds))

    if os.path.isdir(filepath_initseeds):
        init_seed = os.listdir(filepath_initseeds)[0]

    # print(fuzz_command)
    FUZZLOGGING(DEBUG, LOG_STR(LOG_FUNCINFO(), fuzz_command))

    # Fuzzing test procedure.
    Generator.prepareEnv(program_name)
    execute_seedfile = filepath_initseeds + init_seed

    # Fuzzing test cycle
    # while True:
    for i in range(1):
        # First run to collect information.
        init_seedfile = execute_seedfile
        seed_content = Analyzer.getSeedContent(init_seedfile)
        init_ret_code, init_std_out, init_std_err = Executor.run(fuzz_command.replace('@@', init_seedfile))
        init_num_of_pcguard, init_trace_analysis = Analyzer.traceAyalysis(init_std_out)

        # Mutate seeds to find where to change. Then perform to a directed mutate.
        mutate_seeds, record_list = Mutator.mutateSeeds(seed_content)
        # print(mutate_seeds, record_list)
        filelist_mutateseeds = Mutator.mutateSaveAsFile(mutate_seeds, filepath_mutateseeds, str(i))

        for index, each_mutate in enumerate(filelist_mutateseeds):
            # Track execution information of mutate seeds.
            execute_seedfile = filepath_mutateseeds + each_mutate
            mut_ret_code, mut_std_out, mut_std_err = Executor.run(fuzz_command.replace('@@', execute_seedfile))
            mut_num_of_pcguard, mut_trace_analysis = Analyzer.traceAyalysis(mut_std_out)

            # Analyze the differences in comparison.
            comparison_report = Builder.compareBytes(init_trace_analysis, mut_trace_analysis, record_list[index])
            Parser.typeSpeculation(comparison_report)



        Mutator.mutateDeleteFile(filelist_mutateseeds, filepath_mutateseeds)
        # print(mutate_seeds)

        # Visualizer.display()




if __name__ == "__main__":
    mainFuzzer()
