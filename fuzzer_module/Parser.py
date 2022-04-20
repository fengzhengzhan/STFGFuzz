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
        change_inputmap[seed_loc[fix_i]] = fixed_cont[fix_i]
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
    cont = ""
    for l_i in range(0, strlen):
        rest = intvalue % 256
        intvalue = (intvalue-rest) // 256
        # print(rest, intvalue, chr(rest))
        cont = chr(rest) + cont

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
    if abs(opt0-opt1) > abs(mut0-mut1):  # Distance difference in a constraint.
        ret_seed = mut_seed
    elif abs(opt0-opt1) < abs(mut0-mut1):
        ret_seed = opt_seed
    elif abs(opt0-opt1) == abs(mut0-mut1):
        ret_seed = mut_seed if random.randint(0, 1) == 1 else opt_seed

    # According bytes location to mutation seed location.
    if strategy.curnum < strategy.endlen * 16:
        chari = strategy.curnum // 16
        charb = strategy.curnum % 16
        strategy.curnum += 1
        c = abs(ord(ret_seed.content[st_loc[chari]]) + MUT_BIT_LIST[charb]) % 256
        c = chr(c)
        change_inputmap[st_loc[chari]] = c
        LOG(LOG_DEBUG, LOG_FUNCINFO(), chari, charb, st_loc, opt_seed.content, mut_seed.content, change_inputmap)
        LOG(LOG_DEBUG, LOG_FUNCINFO(), opt0, mut0, opt1, mut1, abs(opt0-opt1), abs(mut0-mut1), ret_seed.content)
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
    if abs(opt0-opt1) > abs(mut0-mut1):  # Distance difference in a constraint.
        ret_seed = mut_seed
    elif abs(opt0-opt1) < abs(mut0-mut1):
        ret_seed = opt_seed
    elif abs(opt0-opt1) == abs(mut0-mut1):
        ret_seed = mut_seed if random.randint(0, 1) == 1 else opt_seed

    # According bytes location to mutation seed location.
    if strategy.curnum < strategy.endlen * 16:
        chari = strategy.curnum // 16
        charb = strategy.curnum % 16
        strategy.curnum += 1
        c = abs(ord(ret_seed.content[st_loc[chari]]) + MUT_BIT_LIST[charb]) % 256
        c = chr(c)
        change_inputmap[st_loc[chari]] = c
        LOG(LOG_DEBUG, LOG_FUNCINFO(), chari, charb, st_loc,
            opt_seed.content, mut_seed.content, change_inputmap, showlog=True)
        LOG(LOG_DEBUG, LOG_FUNCINFO(), opt0, mut0, opt1, mut1,
            abs(opt0-opt1), abs(mut0-mut1), ret_seed.content, showlog=True)
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
    if strategy.curnum < strategy.endlen * 16:
        st_len = len(st_loc)
        bit_len = st_len * 8 - 1
        # Return full string.
        cont = ""
        for loc_i in st_loc:
            cont += ret_seed.content[loc_i]
        cont_num = strConverUnival(cont)
        addnum = ((-1) ** (strategy.curnum%2)) * (2 ** (bit_len - (strategy.curnum)//2))
        cont_num = cont_num + addnum
        # print(addnum, cont_num)
        cont = univalConverStr(cont_num, st_len)
        for loc_idx, loc_i in enumerate(st_loc):
            change_inputmap[loc_i] = cont[loc_idx]
        strategy.curnum += 1

    return ret_seed, change_inputmap

def handleChecksums():
    pass

def handleUndefined():
    pass


'''
Type Inference Module.
'''
# Infer bytes status according bytes change.
def inferFixedOrChanged(cont_list) -> int:
    # Original group <-> Control group
    ori0, ori1, st0, st1 = cont_list[0], cont_list[1], cont_list[2], cont_list[3]
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
        if not cont_i.isdigit():
            return False
    return True

# Detect bytes type from bytes status and bytes contents.
def detectCmpType(bytes_type, cont_list, cmpins: StructCmpIns) -> list:
    type_infer = []
    if bytes_type == PAR_SOLVED:
        type_infer.append(TYPE_SOLVED)
    elif bytes_type == PAR_FIXAFIX:
        if cmpins.stvalue[0] in TRACENUMCMPSET:
            type_infer.append(TYPE_MAGICNUMS)
        elif cmpins.stvalue[0] == COV_SWITCH:
            if listIsdigit(cont_list):
                type_infer.append(TYPE_MAGICNUMS)
            else:
                type_infer.append(TYPE_MAGICSTR)

    elif bytes_type == PAR_FIXACHG or bytes_type == PAR_CHGAFIX:
        if cmpins.stvalue[0] in HOOKSTRCMPSET:
            type_infer.append(TYPE_MAGICSTR)
        elif cmpins.stvalue[0] in TRACENUMCMPSET:
            type_infer.append(TYPE_MAGICNUMS)
        elif cmpins.stvalue[0] == COV_SWITCH:
            if listIsdigit(cont_list):
                type_infer.append(TYPE_MAGICNUMS)
            else:
                type_infer.append(TYPE_MAGICSTR)

    elif bytes_type == PAR_CHGACHG:
        type_infer.append(TYPE_CHECKCUMS)

    return type_infer

# According type flag to determine which one strategy will be executed.
def exeTypeStrategy(opt_seed, seed, st_loc, type_infer_list, bytes_flag, cont_list, strategy):
    ret_seed = seed
    locmapdet_dict = {}
    LOG(LOG_DEBUG, LOG_FUNCINFO(), type_infer_list)
    for inf_i in type_infer_list:
        if inf_i == TYPE_SOLVED:
            ret_seed = seed
            locmapdet_dict = {}
            break
        elif inf_i == TYPE_MAGICSTR:
            change_inputmap = handleStrMagic(st_loc, bytes_flag, cont_list)
            locmapdet_dict.update(change_inputmap)
        elif inf_i == TYPE_MAGICNUMS:
            ret_seed, change_inputmap = handleDistanceNum(opt_seed, seed, st_loc, cont_list, strategy)
            locmapdet_dict.update(change_inputmap)
        elif inf_i == TYPE_CHECKCUMS:
            ret_seed, change_inputmap = handleDistanceCheckSums(opt_seed, seed, st_loc, cont_list, strategy)
            locmapdet_dict.update(change_inputmap)
    LOG(LOG_DEBUG, LOG_FUNCINFO(), ret_seed.content)
    return ret_seed, locmapdet_dict

def typeDetect(opt_seed, seed: 'StructSeed', st_loc, st_key: 'cmpid',
               optrpt_dict: 'dict[cmpid:[StructCmpIns]]', strpt_dict, strategy: 'StructMutStrategy', sch):
    """
    Type identification and speculation.
    @return:
    """
    LOG(LOG_DEBUG, LOG_FUNCINFO(), seed.location, st_loc, st_key, optrpt_dict, strpt_dict)
    type_infer_list = []
    locmapdet_dict = {}
    ret_seed = seed
    # Both parties report the existence of a single binding solution
    if (st_key in optrpt_dict) and (st_key in strpt_dict):  # Handling mutually corresponding constraints after mutation
        if len(optrpt_dict[st_key]) == len(strpt_dict[st_key]):
            # Get the first comparison and determine the parameter type.
            if optrpt_dict[st_key][0].stvalue[0] in (TRACENUMCMPSET | HOOKSTRCMPSET):
                # Double operand type comparison
                for len_i in range(min(len(optrpt_dict[st_key]), len(strpt_dict[st_key]))):
                    ini = optrpt_dict[st_key][len_i].stargs
                    st = strpt_dict[st_key][len_i].stargs
                    cont_list = [ini[0], ini[1], st[0], st[1]]
                    # Determining the type of variables
                    bytes_flag = inferFixedOrChanged(cont_list)
                    # Speculative change type
                    type_infer_list = detectCmpType(bytes_flag, cont_list, strpt_dict[st_key][len_i])
                    ret_seed, locmapdet_dict = exeTypeStrategy(opt_seed, seed, st_loc,
                                                               type_infer_list, bytes_flag, cont_list, strategy)

                    LOG(LOG_DEBUG, LOG_FUNCINFO(), ret_seed.content, locmapdet_dict)
                    LOG(LOG_DEBUG, LOG_FUNCINFO(), bytes_flag, cont_list, ini[0], ini[1], st[0], st[1])
            elif optrpt_dict[st_key][0].stvalue[0] == COV_SWITCH:
                strategy.endloop = optrpt_dict[st_key][0].stvalue[3]
                for len_i in range(min(len(optrpt_dict[st_key]), len(strpt_dict[st_key]))):
                    ini = optrpt_dict[st_key][len_i].stargs
                    st = strpt_dict[st_key][len_i].stargs
                    cont_list = [ini[0], ini[strategy.curloop], st[0], st[strategy.curloop]]
                    # Determining the type of variables
                    bytes_flag = inferFixedOrChanged(cont_list)
                    # Speculative change type
                    type_infer_list = detectCmpType(bytes_flag, cont_list, strpt_dict[st_key][len_i])
                    ret_seed, locmapdet_dict = exeTypeStrategy(opt_seed, seed, st_loc,
                                                               type_infer_list, bytes_flag, cont_list, strategy)
                    LOG(LOG_DEBUG, LOG_FUNCINFO(), bytes_flag, cont_list, strategy.curloop, ini)

    elif (st_key in optrpt_dict) and (st_key not in strpt_dict):
        pass
    elif (st_key not in optrpt_dict) and (st_key in strpt_dict):
        pass
    else:
        handleUndefined()

    return ret_seed, set(type_infer_list), locmapdet_dict


if __name__ == "__main__":
    opt_seed = StructSeed("path", "AAAC", MUT_SEED_SUB, set([0,1]))
    mut_seed = StructSeed("path", "AAAD", MUT_SEED_SUB, set([0,1]))
    st_loc = [1,2,3]
    cont_list = ["AAAC", "BEBF", "AAAD", "BEBF"]
    for i in range(0, 100):
        strategy = StructMutStrategy(TYPE_DEFAULT, i, 3, 0, 2)
        ret_seed, change_inputmap = handleDistanceCheckSums(opt_seed, mut_seed, st_loc, cont_list, strategy)
        print(ret_seed.content, change_inputmap)