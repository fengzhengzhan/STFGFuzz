from fuzzer_module.Fuzzconfig import *


'''
Tracking Comparison Module.
'''
def compareRptToLoc(seed: StructSeed, initrpt_dict: 'dict[str:StructCmpIns]', initrpt_set: set, mutrpt_dict, mutrpt_set):
    interset = initrpt_set & mutrpt_set  # Intersection
    symdiffset = initrpt_set ^ mutrpt_set  # Symmetric Difference set
    cmpmaploc_rptdict = {}
    LOG(LOG_DEBUG, LOG_FUNCINFO(), seed.location, interset, symdiffset)

    if len(interset) > 0:
        # compare whether the parameters of the same constraint are different
        for key in interset:
            if len(initrpt_dict[key]) != len(mutrpt_dict[key]):
                cmpmaploc_rptdict[key] = seed.location
            else:
                for l in range(len(initrpt_dict[key])):
                    for larg in range(len(initrpt_dict[key][l].stargs)):
                        if initrpt_dict[key][l].stargs[larg] != mutrpt_dict[key][l].stargs[larg]:
                            cmpmaploc_rptdict[key] = seed.location
    if len(symdiffset) > 0:
        for key in symdiffset:
            cmpmaploc_rptdict[key] = set(seed.location)

    return cmpmaploc_rptdict


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
    if isinstance(value, int):
        unique_val = value
    elif isinstance(value, str):
        u = 0
        for str_i in range(0, len(value)):
            u = u * PAR_CONVER_BIT
            u += ord(value[str_i])
        unique_val = u
    return unique_val

def handleDistanceNum(before_seed, mut_seed, st_loc, bytes_infer, sch) -> dict:
    ret_seed = mut_seed
    change_inputmap = {}
    LOG(LOG_DEBUG, LOG_FUNCINFO(), bytes_infer.var0_cont[0], bytes_infer.var0_cont[1], bytes_infer.var1_cont[0], bytes_infer.var1_cont[1])

    fixed_val0 = strConverUnival(bytes_infer.var0_cont[0])
    fixed_val1 = strConverUnival(bytes_infer.var0_cont[1])
    change_val0 = strConverUnival(bytes_infer.var1_cont[0])
    change_val1 = strConverUnival(bytes_infer.var1_cont[1])
    # According distance to return which seed.
    if abs(fixed_val0-change_val0) >= abs(fixed_val1-change_val1):
        ret_seed = mut_seed
    elif abs(fixed_val0-change_val0) < abs(fixed_val1-change_val1):
        ret_seed = before_seed

    # According bytes location to mutation seed location.
    if sch.mutlocnums < len(st_loc) * 16:
        chari = sch.mutlocnums // 16
        charb = sch.mutlocnums % 16
        sch.mutlocnums += 1
        c = abs(ord(ret_seed.content[st_loc[chari]]) + MUT_BIT_LIST[charb]) % 256
        c = chr(c)
        change_inputmap[st_loc[chari]] = c

    return ret_seed, change_inputmap


def handleChecksums():
    pass

def handleUndefined():
    pass

'''
Type Inference Module.
'''
# Infer bytes status according bytes change.
def inferFixedOrChanged(ori0, ori1, con0, con1) -> (int, StructCmpInfer):
    # Original group <-> Control group
    if con0 == con1:
        temp_bytesflag = PAR_SOLVED
        temp_infer = None
    elif ori0 == con0 and ori1 == con1:
        temp_bytesflag = PAR_FIXAFIX
        temp_infer = StructCmpInfer(PAR_FIXED, [ori0, con0], PAR_FIXED, [ori1, con1])
    elif ori0 == con0 and ori1 != con1:
        temp_bytesflag = PAR_FIXACHG
        temp_infer = StructCmpInfer(PAR_FIXED, [ori0, con0], PAR_CHANGED, [ori1, con1])
    elif ori0 != con0 and ori1 == con1:
        temp_bytesflag = PAR_CHGAFIX
        temp_infer = StructCmpInfer(PAR_CHANGED, [ori0, con0], PAR_FIXED, [ori1, con1])
    elif ori0 != con0 and ori1 != con1:
        temp_bytesflag = PAR_CHGACHG
        temp_infer = StructCmpInfer(PAR_CHANGED, [ori0, con0], PAR_CHANGED, [ori1, con1])
    return temp_bytesflag, temp_infer

# Detect bytes type from bytes status and bytes contents.
def detectCmpType(bytes_type, cmpins: StructCmpIns) -> list:
    type_infer = []
    if bytes_type == PAR_SOLVED:
        type_infer.append(TYPE_SOLVED)
    elif bytes_type == PAR_FIXAFIX:
        type_infer.append(TYPE_MAGICNUMS)
    elif bytes_type == PAR_FIXACHG or bytes_type == PAR_CHGAFIX:
        if cmpins.stvalue[0] in HOOKSTRCMPSET:
            type_infer.append(TYPE_MAGICSTR)
        elif cmpins.stvalue[0] in TRACENUMCMPSET:
            type_infer.append(TYPE_MAGICNUMS)
    elif bytes_type == PAR_CHGACHG:
        type_infer.append(TYPE_UNDEFINED)

    return type_infer

# According type flag to determine which one strategy will be executed.
def exeTypeStrategy(before_seed, seed, st_loc, type_infer_list, bytes_infer, sch):
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
            ret_seed, change_inputmap = handleDistanceNum(before_seed, seed, st_loc, bytes_infer, sch)
            locmapdet_dict.update(change_inputmap)

    return ret_seed, locmapdet_dict

def typeDetect(before_seed, seed: 'StructSeed', st_loc, st_key: 'cmpid', initrpt_dict: 'dict[cmpid:[StructCmpIns]]', strpt_dict, sch: 'Scheduler'):
    """
    Type identification and speculation.
    @param comparison_diffreport:
    @param comparison_onereport:
    @param cmp_map:
    @param mutate_loc:
    @return:
    """
    LOG(LOG_DEBUG, LOG_FUNCINFO(), seed.location, st_loc, st_key, initrpt_dict, strpt_dict)

    type_infer_list = []
    locmapdet_dict = {}
    ret_seed = seed
    # Single Constraint Resolution
    if (st_key in initrpt_dict) and (st_key in strpt_dict):  # Handling mutually corresponding constraints after mutation
        for len_i in range(min(len(initrpt_dict[st_key]), len(strpt_dict[st_key]))):
            ini = initrpt_dict[st_key][len_i].stargs
            st = strpt_dict[st_key][len_i].stargs
            bytes_flag, bytes_infer = inferFixedOrChanged(ini[0], ini[1], st[0], st[1])  # Determining the type of variables
            type_infer_list = detectCmpType(bytes_flag, strpt_dict[st_key][len_i])  # Speculative change type
            ret_seed, locmapdet_dict = exeTypeStrategy(before_seed, seed, st_loc, type_infer_list, bytes_infer, sch)
            if st_key == "4fc28a4fc7e7":
                LOG(LOG_DEBUG, LOG_FUNCINFO(), ret_seed.content, locmapdet_dict, print_mode=True)

            LOG(LOG_DEBUG, LOG_FUNCINFO(), bytes_flag, bytes_infer, ini[0], ini[1], st[0], st[1])

    elif (st_key in initrpt_dict) and (st_key not in strpt_dict):
        pass
    elif (st_key not in initrpt_dict) and (st_key in strpt_dict):
        pass
    else:
        handleUndefined()

    return ret_seed, set(type_infer_list), locmapdet_dict


