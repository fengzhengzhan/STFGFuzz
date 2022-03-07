import datetime
import os

from Fuzzconfig import *


def mutateSeeds(seed: str) -> (list, list):
    '''
    Replace and add strings for variant input according to the sliding window.
    '''
    seed_len = len(seed)
    record_list = []
    # Substitution of bytes for seed mutation
    sub_list = []
    endnum = MUT_STEP + seed_len % MUT_STEP
    for i in range(0, seed_len-endnum, MUT_STEP):
        sub_list.append(seed[0:i] + MUT_STR + seed[i + len(MUT_STR):seed_len])
        record_list.append([MUT_TYPE_SUB, i, i + len(MUT_STR)])
    sub_list.append(seed[0:seed_len-endnum] + MUT_STR[0:endnum])
    record_list.append([MUT_TYPE_SUB, seed_len - endnum, seed_len])

    # Insert byte for seed variation
    insert_list = []
    for i in range(0, seed_len, MUT_STEP):
        insert_list.append(seed[0:i] + MUT_STR + seed[i:seed_len])
        record_list.append([MUT_TYPE_INSERT, i, i + len(MUT_STR)])
    insert_list.append(seed + MUT_STR)
    record_list.append([MUT_TYPE_INSERT, seed_len, seed_len + len(MUT_STR)])
    # print(sub_list, insert_list)
    mutate_seed_list = sub_list + insert_list

    return mutate_seed_list, record_list


def mutateOneChar() -> (list, list):
    '''
    Mutate one character at a time.
    '''
    mutate_seed_list = []
    record_list = []

    return mutate_seed_list, record_list


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
    LOG(LOG_DEBUG, LOG_STR(LOG_FUNCINFO(), filelist_mutateseeds))
    return filelist_mutateseeds


def mutateDeleteFile(filelist_mutateseeds: list, filepath_mutateseeds: str):
    '''
    Delete mutated intermediate files.
    '''
    for each in filelist_mutateseeds:
        os.remove(filepath_mutateseeds + each)

if __name__ == "__main__":
    mutate_seed_list = mutateSeeds("12345678123456789")
    print(mutate_seed_list)
