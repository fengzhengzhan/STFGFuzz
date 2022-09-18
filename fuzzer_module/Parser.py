#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import random

from fuzzer_module.Fuzzconfig import *
from .Structures import *

# Convert bytes to a corresponding PAR_CONVER_BIT-bit integer
def bytesConverNum(value) -> int:
    unique_val = value
    if isinstance(value, bytes):
        u = 0
        for b_i in range(0, len(value)):
            u = u * PAR_BIT_BASE
            u += value[b_i]
        unique_val = u
    return unique_val


def numConverBytes(intvalue, blen):
    cont = b''
    for l_i in range(0, blen):
        rest = intvalue % PAR_BIT_BASE
        intvalue = (intvalue - rest) // PAR_BIT_BASE
        # print(rest, intvalue, chr(rest))
        cont = BYTES_ASCII[rest] + cont

    return cont


def converNumList(cont_list):
    """
    According hex to conver numbers.
    @return:
    """
    temp = []
    for one in cont_list:
        if isinstance(one, bytes):
            temp.append(b)
        elif isinstance(one, int):
            b = bytes(hex(int(one))[2:], encoding="utf-8")
        else:
            raise Exception("Error converNum")
        temp.append(b)
    return temp


def numToBytes(num, nlen, mode):
    b = b''
    if type(num) == int:
        h = str(hex(int(num))[2:])
        if mode == PAR_CONVSINGLE:
            if len(h) < nlen:
                h = "0"*(nlen-len(h)) + h
            for i in range(0, len(h)):
                b += BYTES_ASCII[ord(h[i:i+1])]
        elif mode == PAR_CONVDOUBLE:
            # if len(h) < nlen * 2:
            #     h = "0" * (nlen * 2 - len(h)) + h
            if len(h) % 2 == 1:
                h = "0" + h
            for i in range(0, len(h), 2):
                b += BYTES_ASCII[int(h[i:i + 2], 16)]
    elif type(num) == bytes:
        b = num
    else:
        raise Exception(num)
    return b


def getDistance(cont_list):
    # Type of int converse hex characters to compare distance.
    opt0, opt1, mut0, mut1 = cont_list[0], cont_list[1], cont_list[2], cont_list[3]
    if isinstance(opt0, bytes) or isinstance(opt1, bytes) or isinstance(mut0, bytes) or isinstance(mut1, bytes):
        opt0, opt1, mut0, mut1 = bytesConverNum(opt0), bytesConverNum(opt1), \
                                 bytesConverNum(mut0), bytesConverNum(mut1)

    distance = 0
    # LOG(LOG_DEBUG, LOG_FUNCINFO(), opt0, opt1, mut0, mut1)

    # According distance to return which seed.
    if abs(opt0 - opt1) > abs(mut0 - mut1):  # Distance difference in a constraint.
        distance = 1
    elif abs(opt0 - opt1) < abs(mut0 - mut1):
        distance = -1
    elif abs(opt0 - opt1) == abs(mut0 - mut1):
        distance = 0
    LOG(DEBUG, LOC(), opt0, opt1, mut0, mut1, abs(opt0 - opt1), abs(mut0 - mut1))
    return distance


def getRetSeed(distance, opt_seed, mut_seed):
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
        # Directions may fail at this point
        ret_seed = mut_seed if random.randint(0, 1) == 1 else opt_seed
    return ret_seed


'''
Multiple comparison type handling functions
'''


def handleMagicNum(st_cmploc, cont_list, strategy):
    change_inputmap = {}
    fixed_cont = cont_list[0]
    if strategy.bytestype == PAR_CHGAFIX:
        fixed_cont = cont_list[1]

    if strategy.curnum == 0:
        fixed_cont = numToBytes(fixed_cont, len(st_cmploc), PAR_CONVSINGLE)
        for idx, loc in enumerate(st_cmploc[::1]):
            change_inputmap[loc] = fixed_cont[idx:idx + 1]
    elif strategy.curnum == 1:
        fixed_cont = numToBytes(fixed_cont, len(st_cmploc), PAR_CONVSINGLE)
        for idx, loc in enumerate(st_cmploc[::-1]):
            change_inputmap[loc] = fixed_cont[idx:idx + 1]
    elif strategy.curnum == 2:
        fixed_cont = numToBytes(fixed_cont, len(st_cmploc), PAR_CONVDOUBLE)
        LOG(DEBUG, LOC(), fixed_cont)
        for idx, loc in enumerate(st_cmploc[::1]):
            change_inputmap[loc] = fixed_cont[idx:idx + 1]
    elif strategy.curnum == 3:
        fixed_cont = numToBytes(fixed_cont, len(st_cmploc), PAR_CONVDOUBLE)
        for idx, loc in enumerate(st_cmploc[::-1]):
            change_inputmap[loc] = fixed_cont[idx:idx + 1]
    else:
        strategy.strategytype = TYPE_CHECKNUM
        strategy.curnum = 0
        # strategy.endnum = len(st_cmploc) * len(MUT_BIT_LIST)
        strategy.endnum = len(st_cmploc) * MUT_BIT_LEN

    LOG(DEBUG, LOC(), strategy.curnum, change_inputmap, show=True)

    return change_inputmap


def handleMagicBytes(st_cmploc, cont_list, strategy):
    change_inputmap = {}
    fixed_cont = cont_list[0]
    if strategy.bytestype == PAR_CHGAFIX:
        fixed_cont = cont_list[1]
    LOG(DEBUG, LOC(), st_cmploc, cont_list, fixed_cont, show=True)
    if type(fixed_cont) == int:
        fixed_cont = fixed_cont % MUT_BIT_LEN
        fixed_cont = fixed_cont.to_bytes(1, byteorder='little')

    if strategy.curnum == 0:
        for idx, loc in enumerate(st_cmploc[::1]):
            # LOG(DEBUG, LOC(), change_inputmap, idx, loc, show=True)
            change_inputmap[loc] = fixed_cont[idx:idx + 1]
            # LOG(DEBUG, LOC(), change_inputmap[loc], show=True)
            # LOG(DEBUG, LOC(), fixed_cont[idx:idx + 1], show=True)
    elif strategy.curnum == 1:
        for idx, loc in enumerate(st_cmploc[::-1]):
            change_inputmap[loc] = fixed_cont[idx:idx + 1]
    else:
        strategy.strategytype = TYPE_CHECKBYTES
        strategy.curnum = 0
        # strategy.endnum = len(st_cmploc) * len(MUT_BIT_LIST)
        strategy.endnum = len(st_cmploc) * MUT_BIT_LEN

    return change_inputmap


# def handleChecksums(ret_seed, st_loc, strategy):
#     change_inputmap = {}
#     if strategy.curnum < strategy.endnum:
#         ci = strategy.curnum // 16
#         cb = strategy.curnum % 16
#         pre = MUT_BIT_LIST[cb]
#         while ci >= 0:
#             if ci < len(st_loc) and st_loc[ci] < len(ret_seed.content):
#                 n = ret_seed.content[st_loc[ci]] + pre
#                 LOG(DEBUG, LOC(), ret_seed.content[st_loc[ci]], pre, n)
#                 stloc = st_loc[ci]
#             else:
#                 n = pre
#                 stloc = st_loc[-1] + ci - len(st_loc) + 1
#             # Add
#             if n >= PAR_BIT_BASE:
#                 now = n % PAR_BIT_BASE
#                 pre = n // PAR_BIT_BASE
#                 change_inputmap[stloc] = BYTES_ASCII[now]
#             # Sub
#             elif n < 0:
#                 now = (n + PAR_BIT_BASE) % PAR_BIT_BASE
#                 pre = n // PAR_BIT_BASE
#                 change_inputmap[stloc] = BYTES_ASCII[now]
#             # Exit
#             elif 0 <= n < PAR_BIT_BASE:
#                 change_inputmap[stloc] = BYTES_ASCII[n]
#                 break
#             ci -= 1
#     return change_inputmap

def handleChecksums(ret_seed, st_loc, strategy):
    change_inputmap = {}
    if strategy.curnum < strategy.endnum:
        ci = strategy.curnum // MUT_BIT_LEN
        cb = strategy.curnum % MUT_BIT_LEN
        change_inputmap[st_loc[ci]] = BYTES_ASCII[cb]
    return change_inputmap


def handleRandom(st_loc):
    change_inputmap = {}
    if len(st_loc) > 0:
        r = random.randint(1, len(st_loc))
        for r_i in range(0, r):
            rloc = random.randint(0, len(st_loc) - 1)
            rc = random.randint(0, 255)
            temp = {rloc: BYTES_ASCII[rc]}
            change_inputmap.update(temp)
    return change_inputmap


# def handleUndefined():
#     pass


'''
Try to solve the constraint according to the distance
'''


def solveChangeMap(strategy, st_cmploc, opt_seed, opt_cmpcov_list, cmporder_num):
    """
    Get the strategy change map
    @return:
    """
    LOG(DEBUG, LOC(), st_cmploc, opt_seed.content, opt_cmpcov_list, cmporder_num)

    locmapdet_dict = {}
    change_inputmap = {}
    if cmporder_num < len(opt_cmpcov_list):
        opt_one = opt_cmpcov_list[cmporder_num][1:]
        if opt_one[IDX_CMPTYPE] == COV_SWITCH:
            cont_list = [opt_one[4], opt_one[4 + strategy.curloop]]
        else:
            cont_list = [opt_one[IDX_ARG], opt_one[IDX_ARG + 1]]

        LOG(DEBUG, LOC(), cont_list)
        if strategy.strategytype == TYPE_DEFAULT:
            change_inputmap = handleRandom(st_cmploc)
        elif strategy.strategytype == TYPE_UNDEFINED:
            change_inputmap = handleRandom(st_cmploc)
        elif strategy.strategytype == TYPE_SOLVED:
            pass

        elif strategy.strategytype == TYPE_MAGICNUM:
            change_inputmap = handleMagicNum(st_cmploc, cont_list, strategy)
        elif strategy.strategytype == TYPE_CHECKNUM:
            change_inputmap = handleChecksums(opt_seed, st_cmploc, strategy)

        elif strategy.strategytype == TYPE_MAGICBYTES:
            change_inputmap = handleMagicBytes(st_cmploc, cont_list, strategy)
        elif strategy.strategytype == TYPE_CHECKBYTES:
            change_inputmap = handleChecksums(opt_seed, st_cmploc, strategy)

        elif strategy.strategytype == TYPE_RANDOM:
            change_inputmap = handleRandom(st_cmploc)

        locmapdet_dict.update(change_inputmap)

    return locmapdet_dict


def solveDistence(strategy, opt_seed, st_seed, opt_cmpcov_list, st_cmpcov_list, cmporder_num):
    """
    Resolving the distance between constraints
    strategy: StructMutStrategy
    @return:
    """
    # There is no corresponding constraint in st seed.
    ret_seed = opt_seed
    ret_cmpcov_list = opt_cmpcov_list
    exe_status = DIST_CONTINUE

    LOG(DEBUG, LOC(), cmporder_num, len(opt_cmpcov_list), len(st_cmpcov_list))
    if cmporder_num < len(opt_cmpcov_list) and cmporder_num < len(st_cmpcov_list):
        LOG(DEBUG, LOC(), opt_cmpcov_list[cmporder_num], st_cmpcov_list, show=True)
        opt_one = opt_cmpcov_list[cmporder_num][1:]
        st_one = st_cmpcov_list[cmporder_num][1:]
        if opt_one[IDX_CMPTYPE] == COV_SWITCH:
            cont_list = [opt_one[4], opt_one[4 + strategy.curloop],
                         st_one[4], st_one[4 + strategy.curloop]]
        else:
            cont_list = [opt_one[IDX_ARG], opt_one[IDX_ARG + 1],
                         st_one[IDX_ARG], st_one[IDX_ARG + 1]]

        if strategy.curloop == 2:
            cont_list = converNumList(cont_list)
            distance = getDistance(cont_list)
            ret_seed = getRetSeed(distance, opt_seed, st_seed)
        else:
            distance = getDistance(cont_list)
            ret_seed = getRetSeed(distance, opt_seed, st_seed)

        if ret_seed == st_seed:
            ret_cmpcov_list = st_cmpcov_list

        LOG(DEBUG, LOC(), cont_list, show=True)
        if cont_list[2] == cont_list[3]:
            exe_status = DIST_FINISH
            ret_seed = st_seed
        if cont_list[0] == cont_list[1]:
            exe_status = DIST_FINISH
            ret_seed = opt_seed
        # LOG(LOG_DEBUG, LOG_FUNCINFO(), exe_status, st_one[IDX_ARG], st_one[IDX_ARG + strategy.curloop], showlog=True)

    return ret_seed, ret_cmpcov_list, exe_status


'''
Type Inference Module.
'''


# Infer bytes status according bytes change.
def inferFixedOrChanged(ori_one, st_one) -> int:
    ori0, ori1, st0, st1 = ori_one[IDX_ARG], ori_one[IDX_ARG + 1], st_one[IDX_ARG], st_one[IDX_ARG + 1]
    LOG(DEBUG, LOC(), ori0, ori1, st0, st1)
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
    LOG(DEBUG, LOC(), opt_cmpcov_list, ststart_cmpcov_list, cmporder_num)
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
            bytes_flag = PAR_CHGAFIX
            # LOG(DEBUG, LOC(), listIsdigit(opt_one[4: 5 + int(opt_one[2])]), opt_one[4: 5 + int(opt_one[2])], show=True)
            if listIsdigit(opt_one[4: 5 + int(opt_one[2])]):
                # strategy_flag = TYPE_CHECKNUM
                strategy_flag = TYPE_MAGICNUM
            else:
                # strategy_flag = TYPE_CHECKBYTES
                strategy_flag = TYPE_MAGICBYTES

    return strategy_flag, cmp_flag, bytes_flag


def devStrategy(opt_cmpcov_list, cmporder_i, strategy_flag, cmp_flag, bytes_flag, st_cmploc):
    """
    Develop a strategy based on type
    """
    # According type flag to determine which one strategy will be executed.
    temp_stgy = StructStrategy(strategy_flag, cmp_flag, bytes_flag, 0, 0, 0, 0)
    # Determining the executor numbers
    temp_stgy.curnum = 0
    if strategy_flag == TYPE_MAGICNUM:
        temp_stgy.endnum = 5
    elif strategy_flag == TYPE_MAGICBYTES:
        temp_stgy.endnum = 3
    else:
        # temp_stgy.endnum = len(st_cmploc) * len(MUT_BIT_LIST)  # Can't reach.
        temp_stgy.endnum = len(st_cmploc) * MUT_BIT_LEN  # Can't reach.

    temp_stgy.curloop = 0
    temp_stgy.endloop = 1
    # Use curnum to adjust the selection mutation stage, instead of curloop .
    # if strategy_flag == TYPE_MAGICNUM or strategy_flag == TYPE_CHECKNUM:
    #     temp_stgy.endloop = 1
    # else:
    #     temp_stgy.endloop = 1

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
    print(bytesConverNum(bytes(hex(int(1818326624))[2:], encoding="utf-8")))
