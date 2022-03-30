import struct

from fuzzer_module.Fuzzconfig import *


'''
Tracking Comparison Module.
'''
def traceBack(init_trace, mut_trace, lcstable, i, m, init_list, mut_list):
    """
    Backtracking to find a location
    @param init_trace:
    @param mut_trace:
    @param lcstable:
    @param i:
    @param m:
    @param init_list:
    @param mut_list:
    @return:
    """
    while i > 0 and m > 0:
        if init_trace[i - 1] == mut_trace[m - 1]:
            init_list.append(i - 1)
            mut_list.append(m - 1)
            i -= 1
            m -= 1
        else:
            if lcstable[i - 1][m] > lcstable[i][m - 1]:
                i -= 1
            elif lcstable[i - 1][m] < lcstable[i][m - 1]:
                m -= 1
            else:
                traceBack(init_trace, mut_trace, lcstable, i - 1, m, init_list, mut_list)
                break


def compareLCS(init_trace: list, mut_trace: list):
    """
    Find the longest common subsequence.
    @param init_trace:
    @param mut_trace:
    @return: Return to coordinate position.
    """
    init_len = len(init_trace)
    mut_len = len(mut_trace)
    lcstable = [[0 for _ in range(mut_len+1)] for _ in range(init_len+1)]

    # Constructing the state transfer matrix.
    for i in range(1, init_len+1):
        for j in range(1, mut_len+1):
            if init_trace[i-1] == mut_trace[j-1]:
                lcstable[i][j] = lcstable[i-1][j-1] + 1
            else:
                lcstable[i][j] = max(lcstable[i-1][j], lcstable[i][j-1])
    # for each in lcstable:
    #     print(each)
    lcs_len = lcstable[init_len][mut_len]

    # Backtracking to find a location.
    init_list = []
    mut_list = []
    traceBack(init_trace, mut_trace, lcstable, init_len, mut_len, init_list, mut_list)
    init_list.reverse()
    mut_list.reverse()
    # print(init_list, mut_list)

    return lcs_len, init_list, mut_list


def compareRpt(seed: StructSeed, initrpt_dict: 'dict[str:StructCmpIns]', initrpt_set: set, mutrpt_dict, mutrpt_set):
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



def typeDetect(comparison_diffreport: 'list[StructCmpReport]', comparison_onereport: 'list[StructCmpReport]', cmp_map: dict, mutate_loc: StructMutLoc) -> dict:
    """
    Type identification and speculation.
    @param comparison_diffreport:
    @param comparison_onereport:
    @param cmp_map:
    @param mutate_loc:
    @return:
    """
    # print(comparison_report)
    LOG(LOG_DEBUG, LOG_STR(LOG_FUNCINFO(), comparison_diffreport, comparison_onereport))
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

    # The loop traverses the case where only a single variant exists for the initial and variant.
    for each in comparison_onereport:
        pass

    # print(each_change_inputmap)
    return each_change_inputmap


if __name__ == "__main__":
    a = ['A', 'B', 'C', 'B', 'D', 'A', 'B']
    b = ['B', 'D', 'C', 'A', 'B', 'A']
    # a = ['A']
    # b = ['A']
    compareLCS(a, b)