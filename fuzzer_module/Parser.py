#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import random

from fuzzer_module.Fuzzconfig import *


# Convert bytes to a corresponding PAR_CONVER_BIT-bit integer
def bytesConverUnival(value):
    # unique_val = USE_INITNUM
    if isinstance(value, bytes):
        u = 0
        for b_i in range(0, len(value)):
            u = u * PAR_CONVER_BIT
            u += value[b_i]
        unique_val = u
    else:
        raise Exception("Error ConverUnical Type")
    return unique_val


def univalConverBytes(intvalue, blen):
    cont = b''
    for l_i in range(0, blen):
        rest = intvalue % 256
        intvalue = (intvalue - rest) // 256
        # print(rest, intvalue, chr(rest))
        cont = BYTES_ASCII[rest] + cont

    return cont


def getNumDistance(cont_list):
    distance = 0
    # Type of int converse hex characters to compare distance.
    opt0 = bytesConverUnival(bytes(hex(int(cont_list[0]))[2:], encoding="utf-8"))
    opt1 = bytesConverUnival(bytes(hex(int(cont_list[1]))[2:], encoding="utf-8"))
    mut0 = bytesConverUnival(bytes(hex(int(cont_list[2]))[2:], encoding="utf-8"))
    mut1 = bytesConverUnival(bytes(hex(int(cont_list[3]))[2:], encoding="utf-8"))
    # opt0 = cont_list[0]
    # opt1 = cont_list[1]
    # mut0 = cont_list[2]
    # mut1 = cont_list[3]
    # LOG(LOG_DEBUG, LOG_FUNCINFO(), opt0, opt1, mut0, mut1)

    # According distance to return which seed.
    if abs(opt0 - opt1) > abs(mut0 - mut1):  # Distance difference in a constraint.
        distance = 1
    elif abs(opt0 - opt1) < abs(mut0 - mut1):
        distance = -1
    elif abs(opt0 - opt1) == abs(mut0 - mut1):
        distance = 0
    LOG(LOG_DEBUG, LOG_FUNCINFO(), opt0, opt1, mut0, mut1, abs(opt0 - opt1), abs(mut0 - mut1))
    return distance


def getBytesDistance(cont_list):
    distance = 0
    opt0 = bytesConverUnival(cont_list[0])
    opt1 = bytesConverUnival(cont_list[1])
    mut0 = bytesConverUnival(cont_list[2])
    mut1 = bytesConverUnival(cont_list[3])
    # According distance to return which seed.
    if abs(opt0 - opt1) > abs(mut0 - mut1):  # Distance difference in a constraint.
        distance = 1
    elif abs(opt0 - opt1) < abs(mut0 - mut1):
        distance = -1
    elif abs(opt0 - opt1) == abs(mut0 - mut1):
        distance = 0
    LOG(LOG_DEBUG, LOG_FUNCINFO(), opt0, opt1, mut0, mut1, abs(opt0 - opt1), abs(mut0 - mut1))
    return distance


def gainRetSeed(distance, opt_seed, mut_seed):
    """
    d < 0 ret left, d > 0 ret right, d == 0 ret random.
    """
    # According distance to return which seed.
    ret_seed = opt_seed
    if distance > 0:  # Distance difference in a constraint.
        ret_seed = mut_seed
    elif distance < 0:
        ret_seed = opt_seed
    elif distance == 0:
        ret_seed = mut_seed if random.randint(0, 1) == 1 else opt_seed
    return ret_seed


def gainMagicChangeMap(ret_seed, st_loc, strategy):
    change_inputmap = {}
    if strategy.curnum < strategy.endnum:
        chari = strategy.curnum // 16
        charb = strategy.curnum % 16
        c = abs(ret_seed.content[st_loc[chari]] + MUT_BIT_LIST[charb]) % 256
        bc = BYTES_ASCII[c]
        change_inputmap[st_loc[chari]] = bc
    LOG(LOG_DEBUG, LOG_FUNCINFO(), st_loc, ret_seed.content, change_inputmap)
    return change_inputmap


def gainCheckSumsChangeMap(ret_seed, st_loc, strategy):
    change_inputmap = {}
    if strategy.curnum < strategy.endnum:
        st_len = len(st_loc)
        bit_len = st_len * 8 - 1
        # Return full string.
        cont = b''
        for loc_i in st_loc:
            cont += ret_seed.content[loc_i:loc_i + 1]
        cont_num = bytesConverUnival(cont)
        addnum = ((-1) ** (strategy.curnum % 2)) * (2 ** (bit_len - (strategy.curnum) // 2))
        cont_num = cont_num + addnum
        # print(addnum, cont_num)
        cont = univalConverBytes(cont_num, st_len)
        for idx, loc_i in enumerate(st_loc):
            change_inputmap[loc_i] = cont[idx:idx + 1]
    return change_inputmap


'''
Multiple comparison type handling functions
'''


def handleBytesMagic(st_seed, seed_loc, bytes_flag, cont_list):
    change_inputmap = {}
    fixed_cont = cont_list[0]
    if bytes_flag == PAR_CHGAFIX:
        fixed_cont = cont_list[1]

    for fix_i in range(min(len(seed_loc), len(fixed_cont))):
        change_inputmap[seed_loc[fix_i]] = fixed_cont[fix_i:fix_i + 1]
    return st_seed, change_inputmap


def handleDistanceNum(opt_seed, mut_seed, st_loc, cont_list, strategy):
    # According distance to return which seed.
    distance = getNumDistance(cont_list)
    ret_seed = gainRetSeed(distance, opt_seed, mut_seed)
    # According bytes location to mutation seed location.
    change_inputmap = gainMagicChangeMap(ret_seed, st_loc, strategy)

    return ret_seed, change_inputmap


def handleDistanceBytes(opt_seed, mut_seed, st_loc, cont_list, strategy):
    # According distance to return which seed.
    distance = getBytesDistance(cont_list)
    ret_seed = gainRetSeed(distance, opt_seed, mut_seed)
    # According bytes location to mutation seed location.
    change_inputmap = gainMagicChangeMap(ret_seed, st_loc, strategy)

    return ret_seed, change_inputmap


# Turn single-byte variants into +1 -1 operations on the total length
def handleDistanceCheckSums(opt_seed, mut_seed, st_loc, cont_list, strategy):
    # According distance to return which seed.
    distance = getBytesDistance(cont_list)
    ret_seed = gainRetSeed(distance, opt_seed, mut_seed)
    # According bytes location to mutation seed location.
    change_inputmap = gainMagicChangeMap(ret_seed, st_loc, strategy)

    return ret_seed, change_inputmap


# def handleChecksums():
#     pass
#
#
# def handleUndefined():
#     pass

def handleRandom():
    raise Exception("Mutate Random!")


'''
Try to solve the constraint according to the distance
'''


def solveDistence(strategy, st_cmploc, opt_seed, st_seed, opt_cmpcov_list, st_cmpcov_list, cmporder_num):
    """
    Resolving the distance between constraints
    strategy: StructMutStrategy
    @return:
    """
    LOG(LOG_DEBUG, LOG_FUNCINFO(), st_cmploc, opt_seed.content, st_seed.content, opt_cmpcov_list, st_cmpcov_list,
        cmporder_num, showlog=True)
    ret_seed = opt_seed
    ret_cmpcov_list = opt_cmpcov_list
    exe_status = DIST_FAIL
    locmapdet_dict = {}
    if cmporder_num < len(opt_cmpcov_list) and cmporder_num < len(st_cmpcov_list):
        opt_one = opt_cmpcov_list[cmporder_num][1:]
        st_one = st_cmpcov_list[cmporder_num][1:]
        if opt_one[IDX_CMPTYPE] == COV_SWITCH:
            cont_list = [opt_one[4], opt_one[4 + strategy.curloop],
                         st_one[4], st_one[4 + strategy.curloop]]
        else:
            cont_list = [opt_one[IDX_ARG], opt_one[IDX_ARG + strategy.curloop],
                         st_one[IDX_ARG], st_one[IDX_ARG + strategy.curloop]]
        LOG(LOG_DEBUG, LOG_FUNCINFO(),
            strategy.strategytype, opt_cmpcov_list[cmporder_num], st_cmpcov_list[cmporder_num], cont_list, showlog=True)

        if strategy.strategytype == TYPE_DEFAULT:
            handleRandom()
        elif strategy.strategytype == TYPE_UNDEFINED:
            handleRandom()
        elif strategy.strategytype == TYPE_SOLVED:
            pass
        elif strategy.strategytype == TYPE_MAGICBYTES:
            if strategy.conttype == PAR_CHGACHG:
                ret_seed, change_inputmap = handleDistanceBytes(opt_seed, st_seed, st_cmploc, cont_list, strategy)
                locmapdet_dict.update(change_inputmap)
            else:
                ret_seed, change_inputmap = handleBytesMagic(st_seed, st_cmploc, strategy.conttype, cont_list)
                locmapdet_dict.update(change_inputmap)
        elif strategy.strategytype == TYPE_MAGICNUMS:
            ret_seed, change_inputmap = handleDistanceNum(opt_seed, st_seed, st_cmploc, cont_list, strategy)
            locmapdet_dict.update(change_inputmap)
        elif strategy.strategytype == TYPE_CHECKCUMS:
            ret_seed, change_inputmap = handleDistanceCheckSums(opt_seed, st_seed, st_cmploc, cont_list, strategy)
            locmapdet_dict.update(change_inputmap)
        elif strategy.strategytype == TYPE_RANDOM:
            handleRandom()

        if ret_seed == opt_seed:
            ret_cmpcov_list = opt_cmpcov_list
        elif ret_seed == st_seed:
            ret_cmpcov_list = st_cmpcov_list

        if st_one[IDX_ARG] == st_one[IDX_ARG + strategy.curloop]:
            exe_status = DIST_FINISH

        LOG(LOG_DEBUG, LOG_FUNCINFO(), strategy.curnum, strategy.endnum, ret_seed.content, ret_cmpcov_list, exe_status,
            locmapdet_dict, showlog=True)
    else:
        sf = strategy.strategytype
        if sf == TYPE_MAGICBYTES or sf == TYPE_MAGICNUMS:
            change_inputmap = gainMagicChangeMap(ret_seed, st_cmploc, strategy)
            locmapdet_dict.update(change_inputmap)
        elif sf == TYPE_CHECKCUMS:
            change_inputmap = gainCheckSumsChangeMap(ret_seed, st_cmploc, strategy)
            locmapdet_dict.update(change_inputmap)
        else:
            pass

    return ret_seed, ret_cmpcov_list, exe_status, locmapdet_dict


'''
Type Inference Module.
'''


# Infer bytes status according bytes change.
def inferFixedOrChanged(ori_one, st_one) -> int:
    ori0, ori1, st0, st1 = ori_one[IDX_ARG], ori_one[IDX_ARG + 1], st_one[IDX_ARG], st_one[IDX_ARG + 1]
    LOG(LOG_DEBUG, LOG_FUNCINFO(), ori0, ori1, st0, st1, showlog=True)
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
        if isinstance(cont_i, bytes) and not cont_i.isdigit():
            return False
    return True


def typeDetect(opt_cmpcov_list, ststart_cmpcov_list, cmporder_num):
    """
    Type identification and speculation.
    @return:
    """
    LOG(LOG_DEBUG, LOG_FUNCINFO(), opt_cmpcov_list, ststart_cmpcov_list, cmporder_num)
    bytes_flag = PAR_UNDEFINED
    strategy_flag = STAT_SUC
    if cmporder_num >= len(opt_cmpcov_list) or cmporder_num >= len(ststart_cmpcov_list):
        # Additional processing required
        strategy_flag = STAT_FAIL
    elif opt_cmpcov_list[cmporder_num][1:][IDX_ARG] == opt_cmpcov_list[cmporder_num][1:][IDX_ARG + 1]:
        bytes_flag = PAR_SOLVED
        strategy_flag = STAT_FIN
    else:
        # Determining the type of comparison instruction
        # Determining byte types
        # Determine the strategy to be executed
        opt_one = opt_cmpcov_list[cmporder_num][1:]
        ststart_one = ststart_cmpcov_list[cmporder_num][1:]
        type_flag = opt_one[IDX_CMPTYPE]
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
                strategy_flag = TYPE_MAGICBYTES
            elif bytes_flag == PAR_CHGACHG:
                strategy_flag = TYPE_CHECKCUMS

        elif type_flag == COV_SWITCH:
            if listIsdigit(opt_one[4: 5 + int(opt_one[2])]):
                strategy_flag = TYPE_MAGICNUMS
            else:
                strategy_flag = TYPE_MAGICBYTES

    return bytes_flag, strategy_flag


def devStrategy(opt_cmpcov_list, cmporder_i, bytes_flag, strategy_flag, st_cmploc):
    """
    Develop a strategy based on type
    """
    # According type flag to determine which one strategy will be executed.
    temp_strategy = StructMutStrategy(strategy_flag, bytes_flag, 0, 0, 0, 0)
    # Determining the executor numbers
    temp_strategy.curnum = 0
    temp_strategy.endnum = len(st_cmploc) * len(MUT_BIT_LIST)
    temp_strategy.curloop = 0
    temp_strategy.endloop = 1

    if cmporder_i < len(opt_cmpcov_list):
        opt_one = opt_cmpcov_list[cmporder_i][1:]
        # Determining the loop type
        if opt_one[IDX_CMPTYPE] == COV_SWITCH:
            temp_strategy.curloop = 0
            temp_strategy.endloop = opt_one[2]

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
