import time
import sys
import getopt
import os
import re
import curses

from Fuzzconfig import *

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
    ana = Analyzer.Analyzer()



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
    constraint_graph: 'list[dict, dict]' = StructConstraintGraph().constraintgraph
    cmp_map: dict = StructCmpMap().cmpmap
    input_map: dict[list] = {}
    eachloop_input_map: dict = {}
    init_seeds_list = Generator.prepareEnv(program_name)
    temp_listq = []
    for each in init_seeds_list:
        temp_listq.append(StructSeed(filepath_mutateseeds+each, "", INIT, []))
    sch.addSeeds(SCH_INIT_SEED, temp_listq)

    # Fuzzing test cycle
    while True:
        loop += 1
        # First run to collect information.
        init_seed = sch.selectOneSeed(SCH_INIT_SEED)
        seed_content = init_seed.content
        saveAsFile(init_seed.content, init_seed.filename)
        init_ret_code, init_std_out, init_std_err = Executor.run(fuzz_command.replace('@@', init_seed.filename))
        init_trace_analysis = ana.traceAyalysis(init_std_out)
        init_num_of_pcguard = ana.getNumOfPcguard()

        # Mutate seeds to find where to change. Then perform to a directed mutate.
        temp_mutate_listq = Mutator.mutateSeeds(seed_content, filepath_mutateseeds, str(loop))
        sch.addSeeds(SCH_MUT_SEED, temp_mutate_listq)
        # print(mutate_seeds, record_list)

        while not sch.isEmpty(SCH_MUT_SEED):
            # Track execution information of mutate seeds.
            execute_seed = sch.selectOneSeed(SCH_MUT_SEED)
            saveAsFile(execute_seed.content, execute_seed.filename)
            mut_ret_code, mut_std_out, mut_std_err = Executor.run(fuzz_command.replace('@@', execute_seed.filename))
            mut_trace_analysis = ana.traceAyalysis(mut_std_out)

            # Analyze the differences in comparison.
            comparison_report = Parser.compareBytes(execute_seed, init_trace_analysis, mut_trace_analysis, cmp_map)
            
            eachloop_input_map = Parser.typeSpeculation(comparison_report, eachloop_input_map, cmp_map)
        # print(eachloop_input_map)
        LOG(LOG_DEBUG, LOG_STR(LOG_FUNCINFO(), cmp_map, eachloop_input_map))

        temp_content = list(seed_content)
        for k, v in eachloop_input_map.items():
            temp_content[k] = v
        temp_content = ''.join(temp_content)
        sch.addSeeds(SCH_INIT_SEED, [StructSeed(filepath_mutateseeds+getMutfilename("loop"+str(loop)),
                                         temp_content, INIT, [])])
        # Mutator.mutateDeleteFile(filelist_mutateseeds, filepath_mutateseeds)
        # print(filelist_mutateseeds)
        # print(mutate_seeds)

        res = vis.display(start_time, seed_content, eachloop_input_map)
        if res == 1:
            break
        eachloop_input_map = {}
        sch.deleteSeeds()
        # raise Exception("test")


if __name__ == "__main__":
    try:
        mainFuzzer()
    except Exception as e:
        curses.endwin()
        print(e)


