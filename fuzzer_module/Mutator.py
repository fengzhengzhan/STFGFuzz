#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import random

from fuzzer_module.Fuzzconfig import *
from .Structures import *


def getFillStr(length: int) -> bytes:
    fill_bytes = b''
    # 64 characters
    if length <= 64:
        default_str = b'AAABAAACAAADAAAEAAAFAAAGAAAHAAAIAAAJAAAKAAALAAAMAAANAAAOAAAPAAAQ'
        fill_bytes = default_str[0:length]
    else:
        while len(fill_bytes) <= length:
            for cent in range(1, 4):
                for c_i in BYTES_ASCII[65:91]:
                    if len(fill_bytes) >= length:  # Each 100 characters judge it.
                        return fill_bytes[0:length]
                    for c_j in BYTES_ASCII[65:91]:
                        if c_i != c_j:
                            fill_bytes += c_i * (4 - cent) + c_j * cent
    return fill_bytes

def getExpandFillStr(length: int) -> bytes:
    fill_bytes = b''
    if length <= 64:
        default_str = b'0001000200030004000500060007000800091110111211131114111511161117'
        fill_bytes = default_str[0:length]
    else:
        while len(fill_bytes) <= length:
            for cent in range(1, 4):
                for c_i in BYTES_ASCII[48:58]:
                    if len(fill_bytes) >= length:  # Each 100 characters judge it.
                        return fill_bytes[0:length]
                    for c_j in BYTES_ASCII[48:58]:
                        if c_i != c_j:
                            fill_bytes += c_i * (4 - cent) + c_j * cent
    return fill_bytes


def mutSeeds(seedcont: bytes, filepath: str, label: str) -> 'list[StructSeed]':
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
                                       seedcont[0:i] + MUT_STR + seedcont[i + len(MUT_STR):seed_len],
                                       MUT_SEED_SUB,
                                       set([idx for idx in range(i, i + len(MUT_STR) + 1)])))
    mutate_listq.append(StructSeed(filepath + getMutfilename(label),
                                   seedcont[0:seed_len - endnum] + MUT_STR[0:endnum],
                                   MUT_SEED_SUB,
                                   set([idx for idx in range(seed_len - endnum, seed_len + 1)])))

    # Insert byte for seed variation
    for i in range(0, seed_len, MUT_STEP):
        mutate_listq.append(StructSeed(filepath + getMutfilename(label),
                                       seedcont[0:i] + MUT_STR + seedcont[i:seed_len],
                                       MUT_SEED_INSERT,
                                       set([idx for idx in range(i, i + len(MUT_STR) + 1)])))
    mutate_listq.append(StructSeed(filepath + getMutfilename(label),
                                   seedcont + MUT_STR,
                                   MUT_SEED_INSERT,
                                   set([idx for idx in range(seed_len, seed_len + len(MUT_STR) + 1)])))
    # print(mutate_listq)
    return mutate_listq


def mutOneChar(seedcont: bytes, filepath: str, label: str, loc_list) -> StructSeed:
    """
    @return: only one seed
    """
    for i, loci in enumerate(loc_list):
        while True:
            # rand_list = [48, 49, 50, 51, 52, 53, 54, 55, 56, 57,
            #              65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90,
            #              97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122]
            randi = random.randint(33, 126)
            tempc = BYTES_ASCII[randi]
            if seedcont[loci: loci + 1] != tempc:
                seedcont = seedcont[0:loci] + tempc + seedcont[loci + 1:]
                break
        # seedloc_list[loci] = chr(255 - ord(seedloc_list[loci]))
    temp_one = StructSeed(filepath + getMutfilename(label), seedcont, MUT_SEED_SUB, set(loc_list))
    return temp_one


def mutSelectChar(seedcont: bytes, filepath: str, label: str, mutloc_list: list) -> StructSeed:
    """
    Mutate one character at a time.
    @return:
    """
    mut_bytes = getFillStr(len(mutloc_list))
    for i, loci in enumerate(mutloc_list):
        seedcont = seedcont[0:loci] + mut_bytes[i:i + 1] + seedcont[loci + 1:]
    temp_one: StructSeed = StructSeed(filepath + getMutfilename(label), seedcont, MUT_SEED_SUB, set(mutloc_list))
    return temp_one


def mutSelectCharRand(seedcont: bytes, filepath: str, label: str, loc_list) -> StructSeed:
    """
    @return: only one seed
    """
    for i, loci in enumerate(loc_list):
        while True:
            randi = random.randint(0, 255)
            tempc = BYTES_ASCII[randi]
            if seedcont[loci: loci + 1] != tempc:
                seedcont = seedcont[0:loci] + tempc + seedcont[loci + 1:]
                break
        # seedloc_list[loci] = chr(255 - ord(seedloc_list[loci]))
    temp_one = StructSeed(filepath + getMutfilename(label), seedcont, MUT_SEED_SUB, set(loc_list))
    return temp_one


def mutLocFromMap(init_seed, seed, filepath: str, label: str, locmapdet_dict: 'dict[int:bytes]') -> StructSeed:
    if locmapdet_dict:
        # Remove the key which value equals b''
        for key in list(locmapdet_dict.keys()):
            if locmapdet_dict[key] == b'':
                locmapdet_dict[key] = init_seed.content[key:key+1]
        seedcont = seed.content
        for lockey, chgval in sorted(locmapdet_dict.items()):
            seedcont = seedcont[0:lockey] + chgval + seedcont[lockey + 1:]
        LOG(DEBUG, LOC(), seedcont, locmapdet_dict)
        temp_one = StructSeed(filepath + getMutfilename(label), seedcont, MUT_SEED_SUB, set(locmapdet_dict))
    else:
        temp_one = seed
    return temp_one


def mutAddLength(seedcont: bytes, filepath: str, expand_len):
    multicont = seedcont + getExpandFillStr(expand_len)
    loc_set = set([i for i in range(len(seedcont), len(multicont))])
    temp_one = StructSeed(filepath + getMutfilename(EXPAND_SEED), multicont, MUT_SEED_INSERT, loc_set)
    return temp_one

def mutSubLength(seedcont: bytes, filepath: str, sub_len):
    multicont = seedcont[0:len(seedcont) - sub_len]
    temp_one = StructSeed(filepath + getMutfilename(SUB_SEED), multicont, MUT_SEED_SUB, set())
    return temp_one

if __name__ == "__main__":
    # for each in mutSeeds(b"ZZZZZZZZZZZ", "", ""):
    #     print(each.content)
    # print(mutSelectChar(b"ZZZZ","","",[0,1,2,3,4,5,6]).content)
    # print(mutOneChar(b"ZZZZZZZ", "", "", [0]).content)
    # mutate_seed_list = mutateSeeds("12345678123456789", "", "1")
    # print(mutate_seed_list)
    # mutate_seed_list = mutOneChar("1245678123456789", "", "", set([1]))
    # print(mutate_seed_list.content)
    print(getFillStr(1024))
    # print(getExpandFillStr(128))
