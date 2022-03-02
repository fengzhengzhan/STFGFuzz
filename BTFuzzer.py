import time
import sys
import getopt

from Fuzzconfig import *
import Monitor
import Mutator
import Executor
import Scheduler
import Visualizer


def mainFuzzer():
    # Receive command line parameters.
    try:
        opts, args = getopt.getopt(sys.argv[1:], "h")
        # print(opts, args)
        FUZZLOGGING(DEBUG, LOG_STR(LOG_FUNCINFO(), opts, args))
    except getopt.GetoptError:
        print("{}.py -- [files] [OPTIONS] @@".format(BTFUZZ))
        raise Exception("Error options.")
    for opt, arg in opts:
        if opt == "-h":
            print("{}.py -- [files] [OPTIONS] @@".format(BTFUZZ))
            print("e.g. {}.py -- ./demo -f @@".format(BTFUZZ))
            sys.exit()

    fuzz_command = ""
    for fuzzarg in args:
        fuzz_command += str(fuzzarg) + " "
    print(fuzz_command)
    FUZZLOGGING(DEBUG, LOG_STR(LOG_FUNCINFO(), fuzz_command))
    if fuzz_command == "":
        raise Exception("Error empty parameters for fuzzing test files.")



    # Fuzzing test procedure.



    # Fuzzing test cycle
    while True:
        ret_code, std_out, std_err = Executor.run(fuzz_command)
        print(ret_code, std_out, std_err)

        # Visualizer.display()




if __name__ == "__main__":
    mainFuzzer()