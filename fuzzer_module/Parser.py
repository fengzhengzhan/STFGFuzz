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
            u = u * PAR_BIT_BASE
            u += value[b_i]
        unique_val = u
    else:
        raise Exception("Error ConverUnical Type")
    return unique_val


def univalConverBytes(intvalue, blen):
    cont = b''
    for l_i in range(0, blen):
        rest = intvalue % PAR_BIT_BASE
        intvalue = (intvalue - rest) // PAR_BIT_BASE
        # print(rest, intvalue, chr(rest))
        cont = BYTES_ASCII[rest] + cont

    return cont


def numToBytes(num):
    h = str(hex(num)[2:])
    if len(h) % 2 != 0:
        h = "0" + h

    b = b''
    for i in range(0, len(h), 2):
        b += BYTES_ASCII[int(h[i:i + 2], 16)]

    return b


def getNumDistance(cont_list):
    distance = 0
    # Type of int converse hex characters to compare distance.
    # opt0 = bytesConverUnival(bytes(hex(int(cont_list[0]))[2:], encoding="utf-8"))
    # opt1 = bytesConverUnival(bytes(hex(int(cont_list[1]))[2:], encoding="utf-8"))
    # mut0 = bytesConverUnival(bytes(hex(int(cont_list[2]))[2:], encoding="utf-8"))
    # mut1 = bytesConverUnival(bytes(hex(int(cont_list[3]))[2:], encoding="utf-8"))
    opt0 = cont_list[0]
    opt1 = cont_list[1]
    mut0 = cont_list[2]
    mut1 = cont_list[3]
    # LOG(LOG_DEBUG, LOG_FUNCINFO(), opt0, opt1, mut0, mut1)

    # According distance to return which seed.
    if abs(opt0 - opt1) > abs(mut0 - mut1):  # Distance difference in a constraint.
        distance = 1
    elif abs(opt0 - opt1) < abs(mut0 - mut1):
        distance = -1
    elif abs(opt0 - opt1) == abs(mut0 - mut1):
        distance = 0
    LOG(LOG_DEBUG, LOG_FUNCINFO(), opt0, opt1, mut0, mut1, abs(opt0 - opt1), abs(mut0 - mut1), showlog=True)
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


def gainCheckChangeMap(ret_seed, st_loc, strategy):
    change_inputmap = {}
    if strategy.curnum < strategy.endnum:
        ci = strategy.curnum // 16
        cb = strategy.curnum % 16
        pre = MUT_BIT_LIST[cb]
        while ci >= 0:
            n = ret_seed.content[st_loc[ci]] + pre
            # Add
            if n >= PAR_BIT_BASE:
                now = n % PAR_BIT_BASE
                pre = n // PAR_BIT_BASE
                change_inputmap[st_loc[ci]] = BYTES_ASCII[now]
            # Sub
            elif n < 0:
                now = (n + PAR_BIT_BASE) % PAR_BIT_BASE
                pre = n // PAR_BIT_BASE
                change_inputmap[st_loc[ci]] = BYTES_ASCII[now]
            # Exit
            elif 0 <= n < PAR_BIT_BASE:
                change_inputmap[st_loc[ci]] = BYTES_ASCII[n]
                break
            ci -= 1
    return change_inputmap


def gainRandomChangeMap(st_loc):
    change_inputmap = {}
    r = random.randint(1, len(st_loc))
    for r_i in range(0, r):
        rloc = random.randint(0, len(st_loc) - 1)
        rc = random.randint(0, 255)
        temp = {rloc: BYTES_ASCII[rc]}
        change_inputmap.update(temp)
    return change_inputmap


'''
Multiple comparison type handling functions
'''


def handleMagicNum(st_seed, st_loc, cont_list, strategy):
    change_inputmap = {}
    fixed_cont = cont_list[0]
    if strategy.bytestype == PAR_CHGAFIX:
        fixed_cont = cont_list[1]
    fixed_cont = numToBytes(fixed_cont)

    if strategy.curnum == 0:
        for idx, loc in enumerate(st_loc[::1]):
            change_inputmap[loc] = fixed_cont[idx:idx + 1]
    elif strategy.curnum == 1:
        for idx, loc in enumerate(st_loc[::-1]):
            change_inputmap[loc] = fixed_cont[idx:idx + 1]
    else:
        strategy.strategytype = TYPE_CHECKNUM
        strategy.curnum = 0
        strategy.endnum = len(st_loc) * len(MUT_BIT_LIST)

    return st_seed, change_inputmap


# Turn single-byte variants into +1 -1 operations on the total length
def handleCheckNum(opt_seed, mut_seed, st_loc, cont_list, strategy):
    # According distance to return which seed.
    distance = getNumDistance(cont_list)
    ret_seed = gainRetSeed(distance, opt_seed, mut_seed)
    # According bytes location to mutation seed location.
    change_inputmap = gainCheckChangeMap(ret_seed, st_loc, strategy)

    return ret_seed, change_inputmap


def handleMagicBytes(st_seed, st_loc, cont_list, strategy):
    change_inputmap = {}
    fixed_cont = cont_list[0]
    if strategy.bytestype == PAR_CHGAFIX:
        fixed_cont = cont_list[1]

    if strategy.curnum == 0:
        for idx, loc in enumerate(st_loc[::1]):
            change_inputmap[loc] = fixed_cont[idx:idx + 1]
    elif strategy.curnum == 1:
        for idx, loc in enumerate(st_loc[::-1]):
            change_inputmap[loc] = fixed_cont[idx:idx + 1]
    else:
        strategy.strategytype = TYPE_CHECKBYTES
        strategy.curnum = 0
        strategy.endnum = len(st_loc) * len(MUT_BIT_LIST)

    return st_seed, change_inputmap


def handleCheckBytes(opt_seed, mut_seed, st_loc, cont_list, strategy):
    # According distance to return which seed.
    distance = getBytesDistance(cont_list)
    ret_seed = gainRetSeed(distance, opt_seed, mut_seed)
    # According bytes location to mutation seed location.
    change_inputmap = gainCheckChangeMap(ret_seed, st_loc, strategy)

    return ret_seed, change_inputmap


def handleRandom(opt_seed, mut_seed, st_loc, cont_list):
    # According distance to return which seed.
    distance = getNumDistance(cont_list)
    ret_seed = gainRetSeed(distance, opt_seed, mut_seed)
    # According bytes location to mutation seed location.
    change_inputmap = gainRandomChangeMap(st_loc)
    LOG(LOG_DEBUG, LOG_FUNCINFO(), st_loc, ret_seed.content, change_inputmap)
    return change_inputmap


# def handleChecksums():
#     pass
#
#
# def handleUndefined():
#     pass


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
    change_inputmap = {}
    opt_one = opt_cmpcov_list[cmporder_num][1:]
    if opt_one[IDX_CMPTYPE] == COV_SWITCH:
        cont_list = [opt_one[4], opt_one[4 + strategy.curloop]]
    else:
        cont_list = [opt_one[IDX_ARG], opt_one[IDX_ARG + 1]]

    if cmporder_num < len(opt_cmpcov_list) and cmporder_num < len(st_cmpcov_list):
        st_one = st_cmpcov_list[cmporder_num][1:]
        if opt_one[IDX_CMPTYPE] == COV_SWITCH:
            cont_list += [st_one[4], st_one[4 + strategy.curloop]]
        else:
            cont_list += [st_one[IDX_ARG], st_one[IDX_ARG + 1]]
        LOG(LOG_DEBUG, LOG_FUNCINFO(),
            strategy.strategytype, opt_cmpcov_list[cmporder_num], st_cmpcov_list[cmporder_num], cont_list, showlog=True)

        if strategy.strategytype == TYPE_DEFAULT:
            change_inputmap = handleRandom(opt_seed, st_seed, st_cmploc, cont_list)
        elif strategy.strategytype == TYPE_UNDEFINED:
            change_inputmap = handleRandom(opt_seed, st_seed, st_cmploc, cont_list)
        elif strategy.strategytype == TYPE_SOLVED:
            pass

        elif strategy.strategytype == TYPE_MAGICNUM:
            ret_seed, change_inputmap = handleMagicNum(st_seed, st_cmploc, cont_list, strategy)
        elif strategy.strategytype == TYPE_CHECKNUM:
            ret_seed, change_inputmap = handleCheckNum(opt_seed, st_seed, st_cmploc, cont_list, strategy)

        elif strategy.strategytype == TYPE_MAGICBYTES:
            ret_seed, change_inputmap = handleMagicBytes(st_seed, st_cmploc, cont_list, strategy)
        elif strategy.strategytype == TYPE_CHECKBYTES:
            ret_seed, change_inputmap = handleCheckBytes(opt_seed, st_seed, st_cmploc, cont_list, strategy)

        elif strategy.strategytype == TYPE_RANDOM:
            change_inputmap = handleRandom(opt_seed, st_seed, st_cmploc, cont_list)

        locmapdet_dict.update(change_inputmap)

        if ret_seed == opt_seed:
            ret_cmpcov_list = opt_cmpcov_list
        elif ret_seed == st_seed:
            ret_cmpcov_list = st_cmpcov_list

        if st_one[IDX_ARG] == st_one[IDX_ARG + strategy.curloop]:
            exe_status = DIST_FINISH

        LOG(LOG_DEBUG, LOG_FUNCINFO(), strategy.curnum, strategy.endnum, ret_seed.content, ret_cmpcov_list, exe_status,
            locmapdet_dict, showlog=True)
    # There is no corresponding constraint in st seed.
    else:
        sf = strategy.strategytype
        if sf == TYPE_MAGICNUM:
            change_inputmap = handleMagicNum(ret_seed, st_cmploc, cont_list, strategy)
        elif sf == TYPE_MAGICBYTES:
            change_inputmap = handleMagicBytes(ret_seed, st_cmploc, cont_list, strategy)
        elif sf == TYPE_CHECKNUM or sf == TYPE_CHECKBYTES:
            change_inputmap = gainCheckChangeMap(ret_seed, st_cmploc, strategy)
        else:
            change_inputmap = gainRandomChangeMap(st_cmploc)

        locmapdet_dict.update(change_inputmap)

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
    strategy_flag = STAT_SUC
    cmp_flag = UNDEFINE
    bytes_flag = PAR_UNDEFINED
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
        cmp_flag = opt_one[IDX_CMPTYPE]
        if cmp_flag in TRACENUMCMPSET:
            # Determining the type of variables
            bytes_flag = inferFixedOrChanged(opt_one, ststart_one)
            # Speculative change type
            if bytes_flag == TYPE_SOLVED:
                strategy_flag = STAT_FIN
            elif bytes_flag == PAR_FIXAFIX:
                strategy_flag = TYPE_RANDOM
            elif bytes_flag == PAR_FIXACHG or bytes_flag == PAR_CHGAFIX:
                strategy_flag = TYPE_MAGICNUM
            else:  # bytes_flag == PAR_CHGACHG
                strategy_flag = TYPE_CHECKNUM

        elif cmp_flag in HOOKSTRCMPSET:
            # Determining the type of variables
            bytes_flag = inferFixedOrChanged(opt_one, ststart_one)
            # Speculative change type
            if bytes_flag == TYPE_SOLVED:
                strategy_flag = STAT_FIN
            elif bytes_flag == PAR_FIXAFIX:
                strategy_flag = TYPE_RANDOM
            elif bytes_flag == PAR_FIXACHG or bytes_flag == PAR_CHGAFIX:
                strategy_flag = TYPE_MAGICBYTES
            else:  # bytes_flag == PAR_CHGACHG
                strategy_flag = TYPE_CHECKBYTES

        elif cmp_flag == COV_SWITCH:
            if listIsdigit(opt_one[4: 5 + int(opt_one[2])]):
                strategy_flag = TYPE_CHECKNUM
            else:
                strategy_flag = TYPE_CHECKBYTES

    return strategy_flag, cmp_flag, bytes_flag


def devStrategy(opt_cmpcov_list, cmporder_i, strategy_flag, cmp_flag, bytes_flag, st_cmploc):
    """
    Develop a strategy based on type
    """
    # According type flag to determine which one strategy will be executed.
    temp_stgy = StructStrategy(strategy_flag, cmp_flag, bytes_flag, 0, 0, 0, 0)
    # Determining the executor numbers
    temp_stgy.curnum = 0
    if strategy_flag == TYPE_MAGICNUM or strategy_flag == TYPE_MAGICBYTES:
        temp_stgy.endnum = 3
    else:
        temp_stgy.endnum = len(st_cmploc) * len(MUT_BIT_LIST)

    temp_stgy.curloop = 0
    temp_stgy.endloop = 1

    if cmporder_i < len(opt_cmpcov_list):
        opt_one = opt_cmpcov_list[cmporder_i][1:]
        # Determining the loop type
        if opt_one[IDX_CMPTYPE] == COV_SWITCH:
            temp_stgy.curloop = 0
            temp_stgy.endloop = opt_one[2]

    return temp_stgy


if __name__ == "__main__":
    # opt_seed = StructSeed("path", "AAAC", MUT_SEED_SUB, set([0, 1]))
    # mut_seed = StructSeed("path", "AAAD", MUT_SEED_SUB, set([0, 1]))
    # st_loc = [1, 2, 3]
    # cont_list = ["AAAC", "BEBF", "AAAD", "BEBF"]
    # for i in range(0, 100):
    #     strategy = StructMutStrategy(TYPE_DEFAULT, PAR_FIXACHG, i, 3, 0, 2)
    #     ret_seed, change_inputmap = handleDistanceCheckSums(opt_seed, mut_seed, st_loc, cont_list, strategy)
    #     print(ret_seed.content, change_inputmap)

    # handleDistanceNum()

    print(bytes(hex(int(1818326624))[2:], encoding="utf-8"))
    print(bytesConverUnival(bytes(hex(int(1818326624))[2:], encoding="utf-8")))
