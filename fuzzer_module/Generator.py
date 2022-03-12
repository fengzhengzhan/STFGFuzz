import os
from shutil import copy

from fuzzer_module.Fuzzconfig import *


def __createDir(path: str) -> None:
    if not os.path.exists(path):
        os.makedirs(path)


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
    __createDir(PROGRAMS + os.sep + program_name + os.sep + DATACRASHLOC)
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


def createDotFile(bc_file: str, program_name: str) -> (list, list):
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
    ret_code, std_out, std_err = runothercmd(DOTCALLGRAPH + os.path.basename(bc_file))
    ret_code, std_out, std_err = runothercmd(DOTCFG + os.path.basename(bc_file))

    temp_filelist = os.listdir()
    os.chdir(proj_path)

    # Get dot filename.
    cglist = []  # Call Graph
    cfglist = []  # Call Flow Graph
    for onefile in temp_filelist:
        if onefile.find(CG_SUFFIX) >= 0:
            cglist.append(onefile)
        elif onefile.find(CFG_SUFFIX) >= 0:
            cfglist.append(onefile)

    if len(cglist) <= 0 or len(cfglist) <= 0:
        raise Exception("Failed to generate dot file.")

    return cglist, cfglist



if __name__ == "__main__":
    # print(os.getcwd())
    # cglist, cfglist = createDotFile("Programs/IR/demo.ll", "demo")
    # print(cglist, cfglist)
    # print(os.getcwd())

    prepareEnv("demo")
