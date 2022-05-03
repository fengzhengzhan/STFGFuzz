#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import random

from fuzzer_module.Fuzzconfig import *


def getFillStr(length: int) -> bytes:
    fill_bytes = b""
    # 64 characters
    if length <= 64:
        default_str = b"AAABAAACAAADAAAEAAAFAAAGAAAHAAAIAAAJAAAKAAALAAAMAAANAAAOAAAPAAAQ"
        fill_bytes = default_str[0:length]
    else:
        while len(fill_bytes) <= length:
            for cent in range(1, 4):
                for c_i in HEX_ASCII[65:91]:
                    if len(fill_bytes) >= length:  # Each 100 characters judge it.
                        return fill_bytes[0:length]
                    for c_j in HEX_ASCII[65:91]:
                        if c_i != c_j:
                            fill_bytes += bytes.fromhex(c_i) * (4 - cent) + bytes.fromhex(c_j) * cent
    return fill_bytes


def mutSeeds(seedcont: str, filepath: str, label: str) -> 'list[StructSeed]':
    """
    Replace and add strings for variant input according to the sliding window.
    @param seedcont:
    @param filepath:
    @param label:
    @return:
    """
    seed_len = len(seedcont)
    mutate_listq = []
    # Substitution of bytes for seed mutation
    endnum = MUT_STEP + seed_len % MUT_STEP
    for i in range(0, seed_len - endnum, MUT_STEP):
        mutate_listq.append(StructSeed(filepath + getMutfilename(label),
                                       str(seedcont[0:i] + MUT_STR + seedcont[i + len(MUT_STR):seed_len]),
                                       MUT_SEED_SUB,
                                       set([idx for idx in range(i, i + len(MUT_STR) + 1)])))
    mutate_listq.append(StructSeed(filepath + getMutfilename(label),
                                   str(seedcont[0:seed_len - endnum] + MUT_STR[0:endnum]),
                                   MUT_SEED_SUB,
                                   set([idx for idx in range(seed_len - endnum, seed_len + 1)])))

    # Insert byte for seed variation
    for i in range(0, seed_len, MUT_STEP):
        mutate_listq.append(StructSeed(filepath + getMutfilename(label),
                                       str(seedcont[0:i] + MUT_STR + seedcont[i:seed_len]),
                                       MUT_SEED_INSERT,
                                       set([idx for idx in range(i, i + len(MUT_STR) + 1)])))
    mutate_listq.append(StructSeed(filepath + getMutfilename(label),
                                   str(seedcont + MUT_STR),
                                   MUT_SEED_INSERT,
                                   set([idx for idx in range(seed_len, seed_len + len(MUT_STR) + 1)])))
    # print(mutate_listq)
    return mutate_listq


def mutSelectChar(seedcont: bytes, filepath: str, label: str, mutloc_list: list) -> StructSeed:
    """
    Mutate one character at a time.
    @return:
    """
    mut_bytes = getFillStr(len(mutloc_list))
    for i, loci in enumerate(mutloc_list):
        seedcont = seedcont[0:loci] + mut_bytes[i:i+1] + seedcont[loci + 1:]
    temp_one: StructSeed = StructSeed(filepath + getMutfilename(label), seedcont, MUT_SEED_SUB, set(mutloc_list))
    return temp_one


def mutOneChar(seedcont: str, filepath: str, label: str, loc_list) -> StructSeed:
    """
    @param seedcont:
    @param filepath:
    @param label:
    @param loc_list:
    @return: only one seed
    """
    seedloc_list = list(seedcont)
    for i, loci in enumerate(loc_list):
        while True:
            tempc = chr(random.randint(48, 122))
            if seedloc_list[loci] != tempc:
                seedloc_list[loci] = tempc
                break
        # seedloc_list[loci] = chr(255 - ord(seedloc_list[loci]))
    seedcont = ''.join(seedloc_list)
    temp_one = StructSeed(filepath + getMutfilename(label), str(seedcont), MUT_SEED_SUB, set(loc_list))
    return temp_one


def mutLocFromMap(seedcont: str, filepath: str, label: str, locmapdet_dict: 'dict[int:str]') -> StructSeed:
    if locmapdet_dict:
        seedloc_list = list(seedcont)
        for lockey, chgval in locmapdet_dict.items():
            seedloc_list[lockey] = chgval
        seedcont = ''.join(seedloc_list)
        temp_one = StructSeed(filepath + getMutfilename(label), str(seedcont), MUT_SEED_SUB, set(locmapdet_dict))
    else:
        temp_one = None
    return temp_one


def mutAddLength(seedcont: str, filepath: str, label: str, expand):
    multicont = seedcont + getFillStr(expand)
    loc_set = set([i for i in range(len(seedcont), len(multicont))])
    temp_one = StructSeed(filepath + getTimeStr() + EXPAND_SEED, multicont, MUT_SEED_INSERT, loc_set)
    return temp_one


if __name__ == "__main__":
    # mutate_seed_list = mutateSeeds("12345678123456789", "", "1")
    # print(mutate_seed_list)
    # mutate_seed_list = mutOneChar("1245678123456789", "", "", set([1]))
    # print(mutate_seed_list.content)
    # print(getFillStr(1024))
    print(mutSelectChar(b"ZZZZ","","",[0,1,2,3,4,5,6]).content)