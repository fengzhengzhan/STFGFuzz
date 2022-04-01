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
def handleStrMagic(mutseed, fixed_list, changed_list, mutate_loc) -> dict:
    change_inputmap = {}
    fixed_bytes = fixed_list[PAR_VARINIT]
    changed_bytes = changed_list[PAR_VARMUT]
    # Using characters to match location of the input bytes.
    start_match = changed_bytes.find(MUT_STR[0:MUT_MATCH])
    end_match = changed_bytes.find(MUT_STR[len(MUT_STR)-MUT_MATCH : len(MUT_STR)])
    # Direct byte matching requires only one copy of the string.
    if start_match != -1:
        input_start_loc = min(mutseed.location) - start_match
        for l in range(0, len(fixed_bytes)):
            change_inputmap[input_start_loc + l] = fixed_bytes[l]
    else:
        # This case requires the use of single-byte probes.
        for one in mutseed.location:
            mutate_loc.mutonelist.append(one)
    return change_inputmap


def handleNumMagic(mutseed, fixed_list, changed_list, mutate_loc) -> dict:
    change_inputmap = {}
    fixed_bytes = fixed_list[PAR_VARINIT]
    changed_bytes = changed_list[PAR_VARMUT]
    # Using characters to match location of the input bytes.
    start_match = changed_bytes.find(MUT_STR[0:MUT_MATCH])
    # end_match = changed_bytes.find(MUT_STR[len(MUT_STR) - MUT_MATCH: len(MUT_STR)])
    # Direct byte matching requires only one copy of the string.
    if start_match != -1:
        input_start_loc = mutseed.location[0] - start_match
        for l in range(0, len(fixed_bytes)):
            change_inputmap[input_start_loc + l] = fixed_bytes[l]
    else:
        # This case requires the use of single-byte probes.
        pass
    return change_inputmap


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
        temp_infer = StructCmpInfer(PAR_FIXED, [ori1, con1], PAR_CHANGED, [ori0, con0])
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
        type_infer.append(TYPE_UNDEFINED)
    elif bytes_type == PAR_FIXACHG or bytes_type == PAR_CHGAFIX:
        if cmpins.stvalue[0] in HOOKSTRCMPSET:
            type_infer.append(TYPE_MAGICSTR)
        elif cmpins.stvalue[0] in TRACENUMCMPSET:
            type_infer.append(TYPE_MAGICNUMS)
    elif bytes_type == PAR_CHGACHG:
        type_infer.append(TYPE_UNDEFINED)

    return type_infer

# According type flag to determine which one strategy will be executed.
def exeTypeStrategy(seed, type_infer_list, bytes_infer):
    loc = list(seed.location)
    loc.sort()
    locmapdet_dict = {}
    for inf_i in type_infer_list:
        if inf_i == TYPE_SOLVED:
            return {}
        elif inf_i == TYPE_MAGICSTR:
            for fix_i in range(len(bytes_infer.var0_cont[0])):
                locmapdet_dict[loc[fix_i]] = bytes_infer.var0_cont[0][fix_i]
        elif inf_i == TYPE_MAGICNUMS:
            pass

    return locmapdet_dict

def typeDetect(seed: 'StructSeed', st_key: 'cmpid', initrpt_dict: 'dict[cmpid:[StructCmpIns]]', strpt_dict):
    """
    Type identification and speculation.
    @param comparison_diffreport:
    @param comparison_onereport:
    @param cmp_map:
    @param mutate_loc:
    @return:
    """
    LOG(LOG_DEBUG, LOG_FUNCINFO(), seed.location, st_key, initrpt_dict, strpt_dict)

    type_infer_list = []
    locmapdet_dict = {}
    # Single Constraint Resolution
    if (st_key in initrpt_dict) and (st_key in strpt_dict):  # Handling mutually corresponding constraints after mutation
        for len_i in range(min(len(initrpt_dict[st_key]), len(strpt_dict[st_key]))):
            ini = initrpt_dict[st_key][len_i].stargs
            st = strpt_dict[st_key][len_i].stargs
            bytes_flag, bytes_infer = inferFixedOrChanged(ini[0], ini[1], st[0], st[1])  # Determining the type of variables
            type_infer_list = type_infer_list + detectCmpType(bytes_flag, strpt_dict[st_key][len_i])  # Speculative change type
            locmapdet_dict = exeTypeStrategy(seed, type_infer_list, bytes_infer)

            LOG(LOG_DEBUG, LOG_FUNCINFO(), bytes_flag, bytes_infer, ini[0], ini[1], st[0], st[1])

    elif (st_key in initrpt_dict) and (st_key not in strpt_dict):
        pass
    elif (st_key not in initrpt_dict) and (st_key in strpt_dict):
        pass
    else:
        handleUndefined()

    return set(type_infer_list), locmapdet_dict


