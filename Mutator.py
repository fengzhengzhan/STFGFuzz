
from Fuzzconfig import *


def mutateSeeds(seed: str, filepath: str, label: str) -> list:
    '''
    Replace and add strings for variant input according to the sliding window.
    '''
    seed_len = len(seed)
    mutate_listq = []
    # Substitution of bytes for seed mutation
    endnum = MUT_STEP + seed_len % MUT_STEP
    for i in range(0, seed_len-endnum, MUT_STEP):
        mutate_listq.append(StructSeed(filepath+getMutfilename(label),
                                       str(seed[0:i] + MUT_STR + seed[i + len(MUT_STR):seed_len]),
                                       MUT_TYPE_SUB,
                                       [i, i + len(MUT_STR)]))
    mutate_listq.append(StructSeed(filepath+getMutfilename(label),
                                   str(seed[0:seed_len-endnum] + MUT_STR[0:endnum]),
                                   MUT_TYPE_SUB,
                                   [seed_len - endnum, seed_len]))

    # Insert byte for seed variation
    for i in range(0, seed_len, MUT_STEP):
        mutate_listq.append(StructSeed(filepath+getMutfilename(label),
                                       str(seed[0:i] + MUT_STR + seed[i:seed_len]),
                                       MUT_TYPE_INSERT,
                                       [i, i + len(MUT_STR)]))
    mutate_listq.append(StructSeed(filepath+getMutfilename(label),
                                   str(seed + MUT_STR),
                                   MUT_TYPE_INSERT,
                                   [seed_len, seed_len + len(MUT_STR)]))
    # print(mutate_listq)
    return mutate_listq


def mutateOneChar() -> list:
    '''
    Mutate one character at a time.
    '''
    mutate_listq = []

    return mutate_listq



if __name__ == "__main__":
    mutate_seed_list = mutateSeeds("12345678123456789")
    print(mutate_seed_list)
