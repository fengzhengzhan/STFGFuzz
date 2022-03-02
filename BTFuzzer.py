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
    Generator.prepareEnv()

    # Receive command line parameters.
    fuzz_command = ""
    program_name = ""
    filename_initseeds = ""
    filename_mutateseeds = ""
    filename_crashseeds = ""
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
        raise Exception("Error empty parameters for fuzzing test files.")

    filename_initseeds = "SeedPool" + os.sep + "init_seeds" + os.sep + program_name + os.sep
    filename_mutateseeds = "SeedPool" + os.sep + "mutate_seeds" + os.sep + program_name + os.sep
    filename_crashseeds = "SeedPool" + os.sep + "crash_seeds" + os.sep + program_name + os.sep
    FUZZLOGGING(DEBUG, LOG_STR(LOG_FUNCINFO(), filename_initseeds, filename_mutateseeds, filename_crashseeds))

    if os.path.isdir(filename_initseeds):
        init_seed = os.listdir(filename_initseeds)[0]

    fuzz_command = fuzz_command.replace('@@', filename_initseeds + init_seed)
    # print(fuzz_command)
    FUZZLOGGING(DEBUG, LOG_STR(LOG_FUNCINFO(), fuzz_command))

    # Fuzzing test procedure.




    # Fuzzing test cycle
    while True:
        ret_code, std_out, std_err = Executor.run(fuzz_command)
        Analyzer.traceAyalysis(std_out)


        # Visualizer.display()




if __name__ == "__main__":
    mainFuzzer()