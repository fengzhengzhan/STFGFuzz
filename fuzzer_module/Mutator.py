import random

from fuzzer_module.Fuzzconfig import *

def getFillStr(length: int) -> str:
    fill_str = ""
    # 64 characters
    if length <= 64:
        default_str = "AAABAAACAAADAAAEAAAFAAAGAAAHAAAIAAAJAAAKAAALAAAMAAANAAAOAAAPAAAQ"
        fill_str = default_str[0:length]
    else:
        while len(fill_str) <= length:
            for cent in range(1, 4):
                for i in range(65, 91):
                    if len(fill_str) >= length:  # Each 100 characters judge it.
                        return fill_str[0:length]
                    for j in range(65, 91):
                        if i != j:
                            fill_str += chr(i) * (4 - cent) + chr(j) * cent
    return fill_str

def mutateSeeds(seed: str, filepath: str, label: str) -> 'list[StructSeed]':
    """
    Replace and add strings for variant input according to the sliding window.
    @param seed:
    @param filepath:
    @param label:
    @return:
    """
    seed_len = len(seed)
    mutate_listq = []
    # Substitution of bytes for seed mutation
    endnum = MUT_STEP + seed_len % MUT_STEP
    for i in range(0, seed_len-endnum, MUT_STEP):
        mutate_listq.append(StructSeed(filepath+getMutfilename(label),
                                       str(seed[0:i] + MUT_STR + seed[i + len(MUT_STR):seed_len]),
                                       MUT_TYPE_SUB,
                                       set([idx for idx in range(i, i + len(MUT_STR)+1)])))
    mutate_listq.append(StructSeed(filepath+getMutfilename(label),
                                   str(seed[0:seed_len-endnum] + MUT_STR[0:endnum]),
                                   MUT_TYPE_SUB,
                                   set([idx for idx in range(seed_len - endnum, seed_len+1)])))

    # Insert byte for seed variation
    for i in range(0, seed_len, MUT_STEP):
        mutate_listq.append(StructSeed(filepath+getMutfilename(label),
                                       str(seed[0:i] + MUT_STR + seed[i:seed_len]),
                                       MUT_TYPE_INSERT,
                                       set([idx for idx in range(i, i + len(MUT_STR)+1)])))
    mutate_listq.append(StructSeed(filepath+getMutfilename(label),
                                   str(seed + MUT_STR),
                                   MUT_TYPE_INSERT,
                                   set([idx for idx in range(seed_len, seed_len + len(MUT_STR)+1)])))
    # print(mutate_listq)
    return mutate_listq


def mutateSelectChar(seed: str, filepath: str, label: str, mutloc_list) -> StructSeed:
    """
    Mutate one character at a time.
    @return:
    """
    seedloc_list = list(seed)
    mut_str = getFillStr(len(mutloc_list))
    for i, loci in enumerate(mutloc_list):
        seedloc_list[loci] = mut_str[i]
    seed = ''.join(seedloc_list)
    temp_one: StructSeed = StructSeed(filepath + getMutfilename(label), str(seed), MUT_TYPE_SUB, set(mutloc_list))
    return temp_one

def mutateOneChar(seed: str, filepath: str, label: str, loc_list) -> StructSeed:
    """
    @param seed:
    @param filepath:
    @param label:
    @param loc_list:
    @return: only one seed
    """
    seedloc_list = list(seed)
    for i, loci in enumerate(loc_list):
        while True:
            tempc = chr(random.randint(48, 122))
            if seedloc_list[loci] != tempc:
                seedloc_list[loci] = tempc
                break
        # seedloc_list[loci] = chr(255 - ord(seedloc_list[loci]))
    seed = ''.join(seedloc_list)
    temp_one: StructSeed = StructSeed(filepath + getMutfilename(label), str(seed), MUT_TYPE_SUB, set(loc_list))
    return temp_one


if __name__ == "__main__":
    # mutate_seed_list = mutateSeeds("12345678123456789", "", "1")
    # print(mutate_seed_list)
    mutate_seed_list = mutateOneChar("1245678123456789", "", "", set([1]))
    print(mutate_seed_list.content)



