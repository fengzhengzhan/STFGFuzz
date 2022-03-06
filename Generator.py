import os

from Fuzzconfig import *


def __createDir(path: str) -> None:
    if not os.path.exists(path):
        os.makedirs(path)


def prepareEnv(program_name: str) -> None:
    '''
    Prepare the environment before running the fuzzing loop.
    '''
    # Seed files are managed using program_name.
    __createDir(SEEDPOOL)
    __createDir(SEEDPOOL + os.sep + INITSEEDS)
    __createDir(SEEDPOOL + os.sep + CRASHSEEDS)
    __createDir(SEEDPOOL + os.sep + MUTATESEEDS)
    __createDir(SEEDPOOL + os.sep + INITSEEDS + os.sep + program_name)
    __createDir(SEEDPOOL + os.sep + CRASHSEEDS + os.sep + program_name)
    __createDir(SEEDPOOL + os.sep + MUTATESEEDS + os.sep + program_name)

    # Copy all seed files from init_seeds to mutate_seeds
    # as the starting seeds from mutation.

