import os

from Fuzzconfig import *
from shutil import copy

import Executor


def __createDir(path: str) -> None:
    if not os.path.exists(path):
        os.makedirs(path)


def prepareEnv(program_name: str) -> None:
    '''
    Prepare the environment before running the fuzzing loop.
    '''
    # Seed files are managed using program_name.
    # Create SeedPool.
    __createDir(SEEDPOOL)
    __createDir(SEEDPOOL + os.sep + INITSEEDS)
    __createDir(SEEDPOOL + os.sep + CRASHSEEDS)
    __createDir(SEEDPOOL + os.sep + MUTATESEEDS)
    __createDir(SEEDPOOL + os.sep + INITSEEDS + os.sep + program_name)
    __createDir(SEEDPOOL + os.sep + CRASHSEEDS + os.sep + program_name)
    __createDir(SEEDPOOL + os.sep + MUTATESEEDS + os.sep + program_name)
    # Create InfoData.
    __createDir(INFODATA)
    __createDir(INFODATA + os.sep + GRAPHDATA)
    __createDir(INFODATA + os.sep + GRAPHDATA + os.sep + program_name)


    # Copy all seed files from init_seeds to mutate_seeds
    # as the starting seeds from mutation.

def createDotFile(bc_file: str, program_name: str) -> (list, list):
    '''
    From .bc file get .dot files, then get Control Flow Graph and Call Graph.
    '''

    temp_graphpath = INFODATA + os.sep + GRAPHDATA + os.sep + program_name
    copy(bc_file, temp_graphpath)  # Copy file to the graph location.

    # Change path to generator graph in the directed file.
    proj_path = os.getcwd()
    os.chdir(temp_graphpath)
    Executor.run(DOTCALLGRAPH + os.path.basename(bc_file))
    Executor.run(DOTCFG + os.path.basename(bc_file))

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

    return cglist, cfglist


if __name__ == "__main__":
    print(os.getcwd())
    cglist, cfglist = createDotFile("Programs/IR/demo.ll", "demo")
    print(cglist, cfglist)
    print(os.getcwd())
