import random

from fuzzer_module.Fuzzconfig import *


'''
Multiple comparison type handling functions
'''
def handleStrMagic(seed_loc, bytes_infer) -> dict:
    change_inputmap = {}
    if bytes_infer.var0_type == PAR_FIXED:
        fixed_cont = bytes_infer.var0_cont[0]
    elif bytes_infer.var1_type == PAR_FIXED:
        fixed_cont = bytes_infer.var1_cont[0]

    for fix_i in range(len(fixed_cont)):
        change_inputmap[seed_loc[fix_i]] = fixed_cont[fix_i]
    return change_inputmap

def strConverUnival(value):
    unique_val = USE_INITNUM
    if isinstance(value, int):  # Type of int converse hex characters to compare distance.
        value = str(hex(value)[2:])

    if isinstance(value, str):
        u = 0
        for str_i in range(0, len(value)):
            u = u * PAR_CONVER_BIT
            u += ord(value[str_i])
        unique_val = u
    return unique_val

def handleDistanceNum(opt_seed, mut_seed, st_loc, bytes_infer, sch) -> dict:
    ret_seed = mut_seed
    change_inputmap = {}

    val00 = strConverUnival(int(bytes_infer.var0_cont[0]))
    val01 = strConverUnival(int(bytes_infer.var0_cont[1]))
    val10 = strConverUnival(int(bytes_infer.var1_cont[0]))
    val11 = strConverUnival(int(bytes_infer.var1_cont[1]))
    LOG(LOG_DEBUG, LOG_FUNCINFO(), opt_seed.content, mut_seed.content)
    # According distance to return which seed.
    if abs(val00-val10) > abs(val01-val11):  # Distance difference in a constraint.
        ret_seed = mut_seed
    elif abs(val00-val10) < abs(val01-val11):
        ret_seed = opt_seed
    elif abs(val00-val10) == abs(val01-val11):
        ret_seed = mut_seed if random.randint(0, 1) == 1 else opt_seed

    # According bytes location to mutation seed location.
    if sch.mutlocnums < len(st_loc) * 16:
        chari = sch.mutlocnums // 16
        charb = sch.mutlocnums % 16
        sch.mutlocnums += 1
        c = abs(ord(ret_seed.content[st_loc[chari]]) + MUT_BIT_LIST[charb]) % 256
        c = chr(c)
        change_inputmap[st_loc[chari]] = c
        LOG(LOG_DEBUG, LOG_FUNCINFO(), chari, charb, st_loc, opt_seed.content, mut_seed.content, change_inputmap)
        LOG(LOG_DEBUG, LOG_FUNCINFO(), val00, val01, val10, val11, abs(val00-val10), abs(val01-val11), ret_seed.content)
    return ret_seed, change_inputmap

def handleDistanceStr(opt_seed, mut_seed, st_loc, bytes_infer, sch) -> dict:
    ret_seed = mut_seed
    change_inputmap = {}

    val00 = strConverUnival(bytes_infer.var0_cont[0])
    val01 = strConverUnival(bytes_infer.var0_cont[1])
    val10 = strConverUnival(bytes_infer.var1_cont[0])
    val11 = strConverUnival(bytes_infer.var1_cont[1])
    LOG(LOG_DEBUG, LOG_FUNCINFO(), opt_seed.content, mut_seed.content)
    # According distance to return which seed.
    if abs(val00-val10) > abs(val01-val11):  # Distance difference in a constraint.
        ret_seed = mut_seed
    elif abs(val00-val10) < abs(val01-val11):
        ret_seed = opt_seed
    elif abs(val00-val10) == abs(val01-val11):
        ret_seed = mut_seed if random.randint(0, 1) == 1 else opt_seed

    # According bytes location to mutation seed location.
    if sch.mutlocnums < len(st_loc) * 16:
        chari = sch.mutlocnums // 16
        charb = sch.mutlocnums % 16
        sch.mutlocnums += 1
        c = abs(ord(ret_seed.content[st_loc[chari]]) + MUT_BIT_LIST[charb]) % 256
        c = chr(c)
        change_inputmap[st_loc[chari]] = c
        LOG(LOG_DEBUG, LOG_FUNCINFO(), chari, charb, st_loc,
            opt_seed.content, mut_seed.content, change_inputmap, showlog=True)
        LOG(LOG_DEBUG, LOG_FUNCINFO(), val00, val01, val10, val11,
            abs(val00-val10), abs(val01-val11), ret_seed.content, showlog=True)
    return ret_seed, change_inputmap

def handleChecksums():
    pass

def handleUndefined():
    pass


'''
Type Inference Module.
'''
# Infer bytes status according bytes change.
def inferFixedOrChanged(ori0, ori1, st0, st1) -> (int, StructCmpInfer):
    # Original group <-> Control group
    if st0 == st1:
        temp_bytesflag = PAR_SOLVED
        temp_infer = None
    elif ori0 == st0 and ori1 == st1:
        temp_bytesflag = PAR_FIXAFIX
        temp_infer = StructCmpInfer(PAR_FIXED, [ori0, st0], PAR_FIXED, [ori1, st1])
    elif ori0 == st0 and ori1 != st1:
        temp_bytesflag = PAR_FIXACHG
        temp_infer = StructCmpInfer(PAR_FIXED, [ori0, st0], PAR_CHANGED, [ori1, st1])
    elif ori0 != st0 and ori1 == st1:
        temp_bytesflag = PAR_CHGAFIX
        temp_infer = StructCmpInfer(PAR_CHANGED, [ori0, st0], PAR_FIXED, [ori1, st1])
    elif ori0 != st0 and ori1 != st1:
        temp_bytesflag = PAR_CHGACHG
        temp_infer = StructCmpInfer(PAR_CHANGED, [ori0, st0], PAR_CHANGED, [ori1, st1])
    return temp_bytesflag, temp_infer

# Detect bytes type from bytes status and bytes contents.
def detectCmpType(bytes_type, bytes_infer, cmpins: StructCmpIns) -> list:
    type_infer = []
    if bytes_type == PAR_SOLVED:
        type_infer.append(TYPE_SOLVED)
    elif bytes_type == PAR_FIXAFIX:
        if cmpins.stvalue[0] in TRACENUMCMPSET:
            type_infer.append(TYPE_MAGICNUMS)
        elif cmpins.stvalue[0] == COV_SWITCH:
            if bytes_infer.var0_isdigit and bytes_infer.var1_isdigit:
                type_infer.append(TYPE_MAGICNUMS)
            else:
                type_infer.append(TYPE_MAGICSTR)

    elif bytes_type == PAR_FIXACHG or bytes_type == PAR_CHGAFIX:
        if cmpins.stvalue[0] in HOOKSTRCMPSET:
            type_infer.append(TYPE_MAGICSTR)
        elif cmpins.stvalue[0] in TRACENUMCMPSET:
            type_infer.append(TYPE_MAGICNUMS)
        elif cmpins.stvalue[0] == COV_SWITCH:
            if bytes_infer.var0_isdigit and bytes_infer.var1_isdigit:
                type_infer.append(TYPE_MAGICNUMS)
            else:
                type_infer.append(TYPE_MAGICSTR)

    elif bytes_type == PAR_CHGACHG:
        type_infer.append(TYPE_UNDEFINED)

    return type_infer

# According type flag to determine which one strategy will be executed.
def exeTypeStrategy(opt_seed, seed, st_loc, type_infer_list, bytes_infer, sch):
    ret_seed = seed
    locmapdet_dict = {}
    LOG(LOG_DEBUG, LOG_FUNCINFO(), type_infer_list)
    for inf_i in type_infer_list:
        if inf_i == TYPE_SOLVED:
            ret_seed = seed
            locmapdet_dict = {}
            break
        elif inf_i == TYPE_MAGICSTR:
            change_inputmap = handleStrMagic(st_loc, bytes_infer)
            locmapdet_dict.update(change_inputmap)
        elif inf_i == TYPE_MAGICNUMS:
            ret_seed, change_inputmap = handleDistanceNum(opt_seed, seed, st_loc, bytes_infer, sch)
            locmapdet_dict.update(change_inputmap)
    LOG(LOG_DEBUG, LOG_FUNCINFO(), ret_seed.content)
    return ret_seed, locmapdet_dict

def typeDetect(opt_seed, seed: 'StructSeed', st_loc, st_key: 'cmpid',
               optrpt_dict: 'dict[cmpid:[StructCmpIns]]', strpt_dict, sch: 'Scheduler'):
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
        # Get the first comparison and determine the parameter type.
        if optrpt_dict[st_key][0].stvalue[0] in (TRACENUMCMPSET | HOOKSTRCMPSET):
            # Double operand type comparison
            for len_i in range(min(len(optrpt_dict[st_key]), len(strpt_dict[st_key]))):
                ini = optrpt_dict[st_key][len_i].stargs
                st = strpt_dict[st_key][len_i].stargs
                # Determining the type of variables
                bytes_flag, bytes_infer = inferFixedOrChanged(ini[0], ini[1], st[0], st[1])
                # Speculative change type
                type_infer_list = detectCmpType(bytes_flag, bytes_infer, strpt_dict[st_key][len_i])
                ret_seed, locmapdet_dict = exeTypeStrategy(opt_seed, seed, st_loc, type_infer_list, bytes_infer, sch)

                LOG(LOG_DEBUG, LOG_FUNCINFO(), ret_seed.content, locmapdet_dict)
                LOG(LOG_DEBUG, LOG_FUNCINFO(), bytes_flag, bytes_infer, ini[0], ini[1], st[0], st[1])
        elif optrpt_dict[st_key][0].stvalue[0] == COV_SWITCH:
            for len_i in range(min(len(optrpt_dict[st_key]), len(strpt_dict[st_key]))):
                ini = optrpt_dict[st_key][len_i].stargs
                st = strpt_dict[st_key][len_i].stargs
                # Determining the type of variables
                bytes_flag, bytes_infer = inferFixedOrChanged(ini[0], ini[sch.switchnums], st[0], st[sch.switchnums])
                # Speculative change type
                type_infer_list = detectCmpType(bytes_flag, bytes_infer, strpt_dict[st_key][len_i])
                ret_seed, locmapdet_dict = exeTypeStrategy(opt_seed, seed, st_loc, type_infer_list, bytes_infer, sch)
                LOG(LOG_DEBUG, LOG_FUNCINFO(), bytes_flag, bytes_infer,
                    ini[0], ini[sch.switchnums], st[0], st[sch.switchnums])

    elif (st_key in optrpt_dict) and (st_key not in strpt_dict):
        pass
    elif (st_key not in optrpt_dict) and (st_key in strpt_dict):
        pass
    else:
        handleUndefined()

    return ret_seed, set(type_infer_list), locmapdet_dict


