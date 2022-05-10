#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import random

from fuzzer_module.Fuzzconfig import *

'''
Multiple comparison type handling functions
'''


def handleStrMagic(seed_loc, bytes_flag, cont_list) -> dict:
    change_inputmap = {}
    fixed_cont = cont_list[0]
    if bytes_flag == PAR_CHGAFIX:
        fixed_cont = cont_list[1]

    for fix_i in range(len(fixed_cont)):
        change_inputmap[seed_loc[fix_i]] = bytes(fixed_cont[fix_i], encoding="utf-8")
    return change_inputmap


# Convert a string to a corresponding PAR_CONVER_BIT-bit integer
def strConverUnival(strvalue):
    # unique_val = USE_INITNUM
    if isinstance(strvalue, str):
        u = 0
        for str_i in range(0, len(strvalue)):
            u = u * PAR_CONVER_BIT
            u += ord(strvalue[str_i])
        unique_val = u
    else:
        raise Exception("Error ConverUnical Type")
    return unique_val


def univalConverStr(intvalue, strlen):
    cont = b""
    for l_i in range(0, strlen):
        rest = intvalue % 256
        intvalue = (intvalue - rest) // 256
        # print(rest, intvalue, chr(rest))
        cont = BYTES_ASCII[rest] + cont

    return cont


def handleDistanceNum(opt_seed, mut_seed, st_loc, cont_list, strategy) -> dict:
    ret_seed = opt_seed
    change_inputmap = {}

    # Type of int converse hex characters to compare distance.
    opt0 = strConverUnival(str(hex(int(cont_list[0]))[2:]))
    opt1 = strConverUnival(str(hex(int(cont_list[1]))[2:]))
    mut0 = strConverUnival(str(hex(int(cont_list[2]))[2:]))
    mut1 = strConverUnival(str(hex(int(cont_list[3]))[2:]))
    LOG(LOG_DEBUG, LOG_FUNCINFO(), opt_seed.content, mut_seed.content)
    # According distance to return which seed.
    if abs(opt0 - opt1) > abs(mut0 - mut1):  # Distance difference in a constraint.
        ret_seed = mut_seed
    elif abs(opt0 - opt1) < abs(mut0 - mut1):
        ret_seed = opt_seed
    elif abs(opt0 - opt1) == abs(mut0 - mut1):
        ret_seed = mut_seed if random.randint(0, 1) == 1 else opt_seed

    # According bytes location to mutation seed location.
    if strategy.curnum < strategy.endnum * 16:
        chari = strategy.curnum // 16
        charb = strategy.curnum % 16
        strategy.curnum += 1
        c = abs(ret_seed.content[st_loc[chari]] + MUT_BIT_LIST[charb]) % 256
        c = BYTES_ASCII[c]
        change_inputmap[st_loc[chari]] = c
        LOG(LOG_DEBUG, LOG_FUNCINFO(), chari, charb, st_loc, opt_seed.content, mut_seed.content, change_inputmap)
        LOG(LOG_DEBUG, LOG_FUNCINFO(), opt0, mut0, opt1, mut1, abs(opt0 - opt1), abs(mut0 - mut1), ret_seed.content)
    return ret_seed, change_inputmap


def handleDistanceStr(opt_seed, mut_seed, st_loc, cont_list, strategy) -> dict:
    ret_seed = opt_seed
    change_inputmap = {}

    opt0 = strConverUnival(cont_list[0])
    opt1 = strConverUnival(cont_list[1])
    mut0 = strConverUnival(cont_list[2])
    mut1 = strConverUnival(cont_list[3])
    LOG(LOG_DEBUG, LOG_FUNCINFO(), opt_seed.content, mut_seed.content)
    # According distance to return which seed.
    if abs(opt0 - opt1) > abs(mut0 - mut1):  # Distance difference in a constraint.
        ret_seed = mut_seed
    elif abs(opt0 - opt1) < abs(mut0 - mut1):
        ret_seed = opt_seed
    elif abs(opt0 - opt1) == abs(mut0 - mut1):
        ret_seed = mut_seed if random.randint(0, 1) == 1 else opt_seed

    # According bytes location to mutation seed location.
    if strategy.curnum < strategy.endnum * 16:
        chari = strategy.curnum // 16
        charb = strategy.curnum % 16
        strategy.curnum += 1
        c = abs(ret_seed.content[st_loc[chari]] + MUT_BIT_LIST[charb]) % 256
        c = BYTES_ASCII[c]
        change_inputmap[st_loc[chari]] = c
        LOG(LOG_DEBUG, LOG_FUNCINFO(), chari, charb, st_loc,
            opt_seed.content, mut_seed.content, change_inputmap, showlog=True)
        LOG(LOG_DEBUG, LOG_FUNCINFO(), opt0, mut0, opt1, mut1,
            abs(opt0 - opt1), abs(mut0 - mut1), ret_seed.content, showlog=True)
    return ret_seed, change_inputmap


# Turn single-byte variants into +1 -1 operations on the total length
def handleDistanceCheckSums(opt_seed, mut_seed, st_loc, cont_list, strategy):
    ret_seed = opt_seed
    change_inputmap = {}

    opt0 = strConverUnival(cont_list[0])
    opt1 = strConverUnival(cont_list[1])
    mut0 = strConverUnival(cont_list[2])
    mut1 = strConverUnival(cont_list[3])
    LOG(LOG_DEBUG, LOG_FUNCINFO(), opt_seed.content, mut_seed.content)
    # According distance to return which seed.
    if abs(opt0 - opt1) > abs(mut0 - mut1):  # Distance difference in a constraint.
        ret_seed = mut_seed
    elif abs(opt0 - opt1) < abs(mut0 - mut1):
        ret_seed = opt_seed
    elif abs(opt0 - opt1) == abs(mut0 - mut1):
        ret_seed = mut_seed if random.randint(0, 1) == 1 else opt_seed

    # According bytes location to mutation seed location.
    if strategy.curnum < strategy.endnum * 16:
        st_len = len(st_loc)
        bit_len = st_len * 8 - 1
        # Return full string.
        cont = ""
        for loc_i in st_loc:
            cont += ret_seed.content[loc_i]
        cont_num = strConverUnival(cont)
        addnum = ((-1) ** (strategy.curnum % 2)) * (2 ** (bit_len - (strategy.curnum) // 2))
        cont_num = cont_num + addnum
        # print(addnum, cont_num)
        cont = univalConverStr(cont_num, st_len)
        for loc_idx, loc_i in enumerate(st_loc):
            change_inputmap[loc_i] = cont[loc_idx:loc_idx + 1]
        strategy.curnum += 1

    return ret_seed, change_inputmap


# def handleChecksums():
#     pass
#
#
# def handleUndefined():
#     pass

def handleRamdom():
    pass


'''
Try to solve the constraint according to the distance
'''
def solveDistence(strategy: StructMutStrategy, st_cmploc, opt_seed, st_seed, opt_cmpcov_list, st_cmpcov_list, cmpk_i):
    ret_seed = opt_seed
    ret_cmpcov_list = opt_cmpcov_list
    exe_status = DIST_CONTINUE
    locmapdet_dict = {}
    cont_list = [opt_cmpcov_list[cmpk_i][IDX_ARG1], opt_cmpcov_list[cmpk_i][IDX_ARG2],
                 st_cmpcov_list[cmpk_i][IDX_ARG1], st_cmpcov_list[cmpk_i][IDX_ARG2]]
    if strategy.strategytype == TYPE_DEFAULT:
        pass
    elif strategy.strategytype == TYPE_UNDEFINED:
        pass
    elif strategy.strategytype == TYPE_SOLVED:
        pass
    elif strategy.strategytype == TYPE_MAGICSTR:
        if strategy.conttype == PAR_CHGACHG:
            handleDistanceStr(opt_seed, st_seed, st_cmploc, cont_list, strategy)
        else:
            handleStrMagic(st_cmploc, strategy.conttype, cont_list)
    elif strategy.strategytype == TYPE_MAGICNUMS:
        handleDistanceNum(opt_seed, st_seed, st_cmploc, cont_list, strategy)
    elif strategy.strategytype == TYPE_CHECKCUMS:
        handleDistanceCheckSums(opt_seed, st_seed, st_cmploc, cont_list, strategy)
    elif strategy.strategytype == TYPE_RANDOM:
        pass

    return ret_seed, ret_cmpcov_list, exe_status, locmapdet_dict


'''
Type Inference Module.
'''
# Infer bytes status according bytes change.
def inferFixedOrChanged(ori_one, st_one) -> int:
    ori0, ori1, st0, st1 = ori_one[IDX_ARG1], ori_one[IDX_ARG2], st_one[IDX_ARG1], st_one[IDX_ARG2]
    # Original group <-> Control group
    bytesflag = PAR_CHGACHG
    if st0 == st1:
        bytesflag = PAR_SOLVED
    elif ori0 == st0 and ori1 == st1:
        bytesflag = PAR_FIXAFIX
    elif ori0 == st0 and ori1 != st1:
        bytesflag = PAR_FIXACHG
    elif ori0 != st0 and ori1 == st1:
        bytesflag = PAR_CHGAFIX
    elif ori0 != st0 and ori1 != st1:
        bytesflag = PAR_CHGACHG
    return bytesflag

def listIsdigit(cont_list):
    for cont_i in cont_list:
        if isinstance(cont_i, str) and not cont_i.isdigit():
            return False
    return True

def typeDetect(opt_cmpcov_list, ststart_cmpcov_list, cmpk_i):
    """
    Type identification and speculation.
    @return:
    """
    LOG(LOG_DEBUG, LOG_FUNCINFO(), opt_cmpcov_list, ststart_cmpcov_list, cmpk_i)
    bytes_flag = PAR_UNDEFINED
    strategy_flag = STAT_SUC
    if cmpk_i >= len(opt_cmpcov_list) or cmpk_i >= len(ststart_cmpcov_list):
        # Additional processing required
        strategy_flag = STAT_FAIL
    else:
        # Determining the type of comparison instruction
        # Determining byte types
        # Determine the strategy to be executed
        type_flag = opt_cmpcov_list[cmpk_i][IDX_CMPTYPE]
        opt_one = opt_cmpcov_list[cmpk_i]
        ststart_one = ststart_cmpcov_list[cmpk_i]
        if type_flag in TRACENUMCMPSET:
            # Determining the type of variables
            bytes_flag = inferFixedOrChanged(opt_one, ststart_one)
            # Speculative change type
            if bytes_flag == TYPE_SOLVED:
                strategy_flag = STAT_FIN
            elif bytes_flag == PAR_FIXAFIX or bytes_flag == PAR_FIXACHG or bytes_flag == PAR_CHGAFIX:
                strategy_flag = TYPE_MAGICNUMS
            elif bytes_flag == PAR_CHGACHG:
                strategy_flag = TYPE_CHECKCUMS

        elif type_flag in HOOKSTRCMPSET:
            # Determining the type of variables
            bytes_flag = inferFixedOrChanged(opt_one, ststart_one)
            # Speculative change type
            if bytes_flag == TYPE_SOLVED:
                strategy_flag = STAT_FIN
            elif bytes_flag == PAR_FIXAFIX or bytes_flag == PAR_FIXACHG or bytes_flag == PAR_CHGAFIX:
                strategy_flag = TYPE_MAGICSTR
            elif bytes_flag == PAR_CHGACHG:
                strategy_flag = TYPE_CHECKCUMS

        elif type_flag == COV_SWITCH:
            if listIsdigit(opt_one[4: 5 + int(opt_one[2])]):
                strategy_flag = TYPE_MAGICNUMS
            else:
                strategy_flag = TYPE_MAGICSTR

    return bytes_flag, strategy_flag


def devStrategy(opt_one, bytes_flag, strategy_flag, st_cmploc):
    """
    Develop a strategy based on type
    """
    # According type flag to determine which one strategy will be executed.
    temp_strategy = StructMutStrategy(strategy_flag, bytes_flag, 0, 0, 0, 0)
    # Determining the executor numbers
    temp_strategy.curnum = 0
    temp_strategy.endnum = len(st_cmploc) * len(MUT_BIT_LIST)
    # Determining the loop type
    if opt_one[IDX_CMPTYPE] == COV_SWITCH:
        temp_strategy.curloop = 0
        temp_strategy.endloop = opt_one[2]
    else:
        temp_strategy.curloop = 0
        temp_strategy.endloop = 1

    return temp_strategy


if __name__ == "__main__":
    opt_seed = StructSeed("path", "AAAC", MUT_SEED_SUB, set([0, 1]))
    mut_seed = StructSeed("path", "AAAD", MUT_SEED_SUB, set([0, 1]))
    st_loc = [1, 2, 3]
    cont_list = ["AAAC", "BEBF", "AAAD", "BEBF"]
    for i in range(0, 100):
        strategy = StructMutStrategy(TYPE_DEFAULT, PAR_FIXACHG, i, 3, 0, 2)
        ret_seed, change_inputmap = handleDistanceCheckSums(opt_seed, mut_seed, st_loc, cont_list, strategy)
        print(ret_seed.content, change_inputmap)
