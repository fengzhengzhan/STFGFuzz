import datetime
import os

from Fuzzconfig import *


# Mutant seeds
def mutateSeeds(seed: str) -> list:
    '''
    Replace and add strings for variant input according to the sliding window.
    '''
    seed_len = len(seed)
    # Substitution of bytes for seed mutation
    sub_list = []
    endnum = STEP + seed_len%STEP
    for i in range(0, seed_len-endnum, STEP):
        sub_list.append(seed[0:i]+MUTATE_STR+seed[i+len(MUTATE_STR):seed_len])
    sub_list.append(seed[0:seed_len-endnum]+MUTATE_STR[0:endnum])

    # Insert byte for seed variation
    insert_list = []
    for i in range(0, seed_len, STEP):
        insert_list.append(seed[0:i]+MUTATE_STR+seed[i:seed_len])
    insert_list.append(seed+MUTATE_STR)
    # print(sub_list, insert_list)
    mutate_seed_list = sub_list + insert_list

    return mutate_seed_list


def mutateSaveAsFile(mutate_seeds: list, filepath_mutateseeds: str, label: str) -> list:
    '''
    Store mutated strings as files for easy reading by test programs.
    '''
    filelist_mutateseeds = []
    for one in mutate_seeds:
        temp_filename = str(datetime.datetime.now().strftime('%Y%m%d%H%M%S%f')) + "_" + str(label) + ".seed"
        filelist_mutateseeds.append(temp_filename)
        with open(filepath_mutateseeds + temp_filename, "w") as f:
            f.write(one)
    # print(filelist_mutateseeds)
    FUZZLOGGING(DEBUG, LOG_STR(LOG_FUNCINFO(), filelist_mutateseeds))
    return filelist_mutateseeds


def mutateDeleteFile(filelist_mutateseeds: list, filepath_mutateseeds: str):
    '''
    Delete mutated intermediate files.
    '''
    for each in filelist_mutateseeds:
        os.remove(filepath_mutateseeds + each)

if __name__ == "__main__":
    mutateSeeds("1234567812345678")
