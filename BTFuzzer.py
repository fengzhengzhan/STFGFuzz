import time
import sys
import getopt
import os
import re

import Analyzer
from Fuzzconfig import *
import Generator
import Monitor
import Mutator
import Executor
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
        seed_content = Analyzer.getSeedContent(execute_seedfile)
        ret_code, std_out, std_err = Executor.run(fuzz_command.replace('@@', execute_seedfile))
        num_of_pcguard, trace_analysis = Analyzer.traceAyalysis(std_out)

        # Mutate seeds to find where to change. Then perform to a directed mutate.
        mutate_seeds, record_list = Mutator.mutateSeeds(seed_content)
        # print(mutate_seeds, record_list)
        filelist_mutateseeds = Mutator.mutateSaveAsFile(mutate_seeds, filepath_mutateseeds, str(i))
        for each_mutate in filelist_mutateseeds:
            execute_seedfile = filepath_mutateseeds + each_mutate
            ret_code, std_out, std_err = Executor.run(fuzz_command.replace('@@', execute_seedfile))
            num_of_pcguard, trace_analysis = Analyzer.traceAyalysis(std_out)
            # Visualizer.display()
        Mutator.mutateDeleteFile(filelist_mutateseeds, filepath_mutateseeds)
        # print(mutate_seeds)

        # Visualizer.display()




if __name__ == "__main__":
    mainFuzzer()
