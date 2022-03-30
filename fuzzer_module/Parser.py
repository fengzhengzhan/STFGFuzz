from fuzzer_module.Fuzzconfig import *


'''
Tracking Comparison Module.
'''
def compareRptToLoc(seed: StructSeed, initrpt_dict: 'dict[str:StructCmpIns]', initrpt_set: set, mutrpt_dict, mutrpt_set):
    interset = initrpt_set & mutrpt_set  # Intersection
    symdiffset = initrpt_set ^ mutrpt_set  # Symmetric Difference set
    cmpmaploc_rptdict = {}
    LOG(LOG_DEBUG, LOG_STR(LOG_FUNCINFO(), seed.location, interset, symdiffset))

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
            cmpmaploc_rptdict[key] = seed.location

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


'''
Type Inference Module.
'''
def inferFixedOrChanged(ini1, ini2, mut1, mut2) -> StructCmpInfer:
    temp_infer = StructCmpInfer(USE_INITNUM, USE_INITSTR, USE_INITNUM, USE_INITSTR)
    if ini1 == mut1:
        temp_infer.var1_type = PAR_FIXED
        temp_infer.var1_cont = [ini1, mut1]
    else:
        temp_infer.var1_type = PAR_CHANGED
        temp_infer.var1_cont = [ini1, mut1]

    if ini2 == mut2:
        temp_infer.var2_type = PAR_FIXED
        temp_infer.var2_cont = [ini2, mut2]
    else:
        temp_infer.var2_type = PAR_CHANGED
        temp_infer.var2_cont = [ini2, mut2]

    return temp_infer


def varChangeSpeculation(infer_bytes: StructCmpInfer):
    temp_flag = USE_INITNUM
    if infer_bytes.var1_type == PAR_FIXED and infer_bytes.var2_type == PAR_CHANGED:
        temp_flag = PAR_MAGIC1_TYPE
    elif infer_bytes.var1_type == PAR_CHANGED and infer_bytes.var2_type == PAR_FIXED:
        temp_flag = PAR_MAGIC2_TYPE
    elif infer_bytes.var1_type == PAR_CHANGED and infer_bytes.var2_type == PAR_CHANGED:
        temp_flag = PAR_CHECKSUMS_TYPE
    elif infer_bytes.var1_type == PAR_FIXED and infer_bytes.var2_type == PAR_FIXED:
        temp_flag = PAR_FIX_TYPE

    return temp_flag



def typeDetect(execute_seed: 'StructSeed', st_k: 'cmpid', initrpt_dict: 'dict[cmpid:[StructCmpIns]]', mutrpt_dict):
    """
    Type identification and speculation.
    @param comparison_diffreport:
    @param comparison_onereport:
    @param cmp_map:
    @param mutate_loc:
    @return:
    """
    LOG(LOG_DEBUG, LOG_STR(LOG_FUNCINFO(), execute_seed.location, st_k, initrpt_dict, mutrpt_dict, print_mode=True))

    comparison_diffreport = None
    each_change_inputmap = {}  # Determine the changed bytes.
    # Loop through the cases where the initial and variant correspond to each other.
    for each in comparison_diffreport:
        mutseed = each.mutseed
        change_inputmap = {}
        if mutseed.seedtype == MUT_TYPE_SUB:
            if each.sttype in TRACECMPSET:
                infer_bytes = inferFixedOrChanged(
                    each.init_sttrace[IDX_ARG1], each.init_sttrace[IDX_ARG2],
                    each.mut_sttrace[IDX_ARG1], each.mut_sttrace[IDX_ARG2]
                )
                # Find fixed bytes and changed bytes.
                var_flag = varChangeSpeculation(infer_bytes)
                if var_flag == PAR_MAGIC1_TYPE:
                    change_inputmap = handleNumMagic(mutseed, infer_bytes.var1_cont, infer_bytes.var2_cont, mutate_loc)
                elif var_flag == PAR_MAGIC2_TYPE:
                    change_inputmap = handleNumMagic(mutseed, infer_bytes.var2_cont, infer_bytes.var1_cont, mutate_loc)
                elif var_flag == PAR_CHECKSUMS_TYPE:
                    pass
                elif var_flag == PAR_FIX_TYPE:
                    pass

            elif each.sttype in HOOKCMPSET:
                infer_bytes = inferFixedOrChanged(
                    each.init_sttrace[IDX_S1], each.init_sttrace[IDX_S2],
                    each.mut_sttrace[IDX_S1], each.mut_sttrace[IDX_S2]
                )
                # Find fixed bytes and changed bytes.
                var_flag = varChangeSpeculation(infer_bytes)
                if var_flag == PAR_MAGIC1_TYPE:
                    change_inputmap = handleStrMagic(mutseed, infer_bytes.var1_cont, infer_bytes.var2_cont, mutate_loc)
                elif var_flag == PAR_MAGIC2_TYPE:
                    change_inputmap = handleStrMagic(mutseed, infer_bytes.var2_cont, infer_bytes.var1_cont, mutate_loc)
                elif var_flag == PAR_CHECKSUMS_TYPE:
                    pass
                elif var_flag == PAR_FIX_TYPE:
                    pass

            elif each.sttype == COV_SWITCH:
                pass
        elif mutseed.seedtype == MUT_TYPE_INSERT:
            pass

        # Handling input change mapping.
        mergeMapReport(change_inputmap, each_change_inputmap)


    # print(each_change_inputmap)
    return each_change_inputmap


