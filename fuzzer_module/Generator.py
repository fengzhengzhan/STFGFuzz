import os
import getopt
from shutil import copy

from fuzzer_module.Fuzzconfig import *


def __createDir(path: str) -> None:
    if not os.path.exists(path):
        os.makedirs(path)

def genTerminal():
    try:
        opts, args = getopt.getopt(sys.argv[1:], "hn:t:")
        # print(opts, args)
        LOG(LOG_DEBUG, LOG_FUNCINFO(), opts, args)
    except getopt.GetoptError:
        print("python {}.py -h".format(FUZZNAME))
        raise Exception("Error options.")

    fuzz_command = " ".join(args)
    program_name = ""
    patchtype = USE_INITNUM

    LOG(LOG_DEBUG, LOG_FUNCINFO(), fuzz_command)

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

    return program_name, patchtype, fuzz_command


def prepareEnv(program_name: str) -> list:
    """
    Prepare the environment before running the fuzzing loop.
    @param program_name:
    @return:
    """
    # Programs
    # -- program_name
    # ---- code_sources
    # ---- code_Bin
    # ---- code_IR
    # ---- data_graph
    # ---- data_crashloc
    # ---- seeds_init
    # ---- seeds_mutate
    # ---- seeds_crash

    # Create Programs.
    __createDir(PROGRAMS)
    __createDir(PROGRAMS + os.sep + program_name)
    __createDir(PROGRAMS + os.sep + program_name + os.sep + CODESOURCES)
    __createDir(PROGRAMS + os.sep + program_name + os.sep + CODEIR)
    __createDir(PROGRAMS + os.sep + program_name + os.sep + CODEBIN)
    __createDir(PROGRAMS + os.sep + program_name + os.sep + DATAGRAPH)
    __createDir(PROGRAMS + os.sep + program_name + os.sep + DATAPATCHLOC)
    temp_seedsinit = PROGRAMS + os.sep + program_name + os.sep + SEEDSINIT
    __createDir(temp_seedsinit)
    temp_seedsmutate = PROGRAMS + os.sep + program_name + os.sep + SEEDSMUTATE
    __createDir(temp_seedsmutate)

    __createDir(PROGRAMS + os.sep + program_name + os.sep + SEEDSCRASH)


    # Copy all seed files from init_seeds to mutate_seeds
    # as the starting seeds from mutation.
    init_seeds_list = []
    for onefile in os.listdir(temp_seedsinit):
        copy(temp_seedsinit + os.sep + onefile, temp_seedsmutate)
        init_seeds_list.append(onefile)

    return init_seeds_list


def createDotJsonFile(program_name: str, bc_file: str) -> (list, list):
    """
    From .bc file get .dot files, then get Control Flow Graph and Call Graph.
    @param bc_file:
    @param program_name:
    @return:
    """

    temp_graphpath = PROGRAMS + os.sep + program_name + os.sep + DATAGRAPH
    copy(bc_file, temp_graphpath)  # Copy file to the graph location.

    # Change path to generator graph in the directed file.
    proj_path = os.getcwd()
    os.chdir(temp_graphpath)
    std_out, std_err = runothercmd(GEN_DOTCALLGRAPH + os.path.basename(bc_file))
    std_out, std_err = runothercmd(GEN_DOTCFG + os.path.basename(bc_file))

    temp_filelist = os.listdir()
    os.chdir(proj_path)

    # Get dot filename.
    cgdotlist = []  # Call Graph
    cfgdotlist = []  # Call Flow Graph
    for onefile in temp_filelist:
        if onefile.endswith(GEN_CG_SUFFIX):
            cgdotlist.append(PROGRAMS + os.sep + program_name + os.sep + DATAGRAPH + os.sep + onefile)
        elif onefile.endswith(GEN_CFG_SUFFIX):
            cfgdotlist.append(PROGRAMS + os.sep + program_name + os.sep + DATAGRAPH + os.sep + onefile)

    if len(cgdotlist) <= 0 or len(cfgdotlist) <= 0:
        raise Exception("Failed to generate dot file.")

    cglist = []  # json
    cfglist = []
    for each in cgdotlist:
        temp_path = each + ".json"
        std_out, std_err = runothercmd(GEN_DOTJSON + each + GEN_OVERLAY + temp_path)
        if not std_err:
            cglist.append(temp_path)

    for each in cfgdotlist:
        temp_path = each + ".json"
        std_out, std_err = runothercmd(GEN_DOTJSON + each + GEN_OVERLAY + temp_path)
        if not std_err:
            cfglist.append(temp_path)

    return cglist, cfglist


if __name__ == "__main__":
    # print(os.getcwd())
    # cglist, cfglist = createDotFile("Programs/IR/demo.ll", "demo")
    # print(cglist, cfglist)
    # print(os.getcwd())

    prepareEnv("demo")
