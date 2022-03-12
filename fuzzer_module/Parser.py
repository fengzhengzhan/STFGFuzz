import struct

from Fuzzconfig import *

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


def compareBytes(mutseed: StructSeed, init_trace_analysis: 'list[StructTraceReport]', mut_trace_analysis: 'list[StructTraceReport]') -> ('list[StructComparisonReport]', 'list[StructComparisonReport]'):
    """
    Bytes of change compared to the initial sample.
    @param mutseed:
    @param init_trace_analysis:
    @param mut_trace_analysis:
    @return:
    """
    # list[StructTraceReport]
    LOG(LOG_DEBUG, LOG_STR(LOG_FUNCINFO(), init_trace_analysis, mut_trace_analysis))
    comparison_diffreport: 'list[StructComparisonReport]' = []
    comparison_onereport: 'list[StructComparisonReport]' = []


    # Only differences in mutation are recorded.
    inittrace_len = len(init_trace_analysis)
    muttrace_len = len(mut_trace_analysis)

    temp_inittrace = []
    for ti in range(inittrace_len):
        temp_inittrace.append(str(init_trace_analysis[ti].startguard) + "_" + str(init_trace_analysis[ti].endguard))
    temp_muttrace = []
    for ti in range(muttrace_len):
        temp_muttrace.append(str(mut_trace_analysis[ti].startguard) + "_" + str(mut_trace_analysis[ti].endguard))
    guard_lcs_len, guard_init_list, guard_mut_list = compareLCS(temp_inittrace, temp_muttrace)

    # Common subsequence comparison constraints are different.
    for gi in range(len(guard_init_list)):
        igi = guard_init_list[gi]
        mgi = guard_mut_list[gi]
        st_lcs_len, st_init_list, st_mut_list = compareLCS(init_trace_analysis[igi].constraint, mut_trace_analysis[mgi].constraint)
        # Same part of the constraint.
        for sti in range(len(st_init_list)):
            comparison_diffreport.append(
                StructComparisonReport(
                    mutseed,
                    init_trace_analysis[igi].stvalue[st_init_list[sti]][IND_CMP_TYPE],
                    init_trace_analysis[igi].stvalue[st_init_list[sti]],
                    mut_trace_analysis[mgi].stvalue[st_mut_list[sti]],
                    init_trace_analysis[igi].startguard,
                    init_trace_analysis[igi].endguard,
                    init_trace_analysis[igi].constraint[st_init_list[sti]],
                )
            )

        # Different parts of the initial constraint
        for ii in range(len(init_trace_analysis[igi].constraint)):
            if ii not in st_init_list:
                comparison_onereport.append(
                    StructComparisonReport(
                        mutseed,
                        init_trace_analysis[igi].stvalue[ii][IND_CMP_TYPE],
                        init_trace_analysis[igi].stvalue[ii],
                        [],
                        init_trace_analysis[igi].startguard,
                        init_trace_analysis[igi].endguard,
                        init_trace_analysis[igi].constraint[ii]
                    )
                )

        # Different parts of the variation constraint
        for mi in range(len(mut_trace_analysis[mgi].constraint)):
            if mi not in st_mut_list:
                comparison_onereport.append(
                    StructComparisonReport(
                        mutseed,
                        mut_trace_analysis[mgi].stvalue[mi][IND_CMP_TYPE],
                        [],
                        mut_trace_analysis[mgi].stvalue[mi],
                        mut_trace_analysis[mgi].startguard,
                        mut_trace_analysis[mgi].endguard,
                        mut_trace_analysis[mgi].constraint[mi]

                    )
                )

    # Different parts of the initial trace
    for i in range(inittrace_len):
        if i not in guard_init_list:
            for st_i in range(len(init_trace_analysis[i].constraint)):
                comparison_onereport.append(
                    StructComparisonReport(
                        mutseed,
                        init_trace_analysis[i].stvalue[st_i][IND_CMP_TYPE],
                        init_trace_analysis[i].stvalue[st_i],
                        [],
                        init_trace_analysis[i].startguard,
                        init_trace_analysis[i].endguard,
                        init_trace_analysis[i].constraint[st_i]
                    )
                )

    # Different parts of the variation tracking
    for m in range(muttrace_len):
        if m not in guard_mut_list:
            for st_m in range(len(mut_trace_analysis[m].constraint)):
                comparison_onereport.append(
                    StructComparisonReport(
                        mutseed,
                        mut_trace_analysis[m].stvalue[st_m][IND_CMP_TYPE],
                        [],
                        mut_trace_analysis[m].stvalue[st_m],
                        mut_trace_analysis[m].startguard,
                        mut_trace_analysis[m].endguard,
                        mut_trace_analysis[m].constraint[st_m]
                    )
                )

    return comparison_diffreport, comparison_onereport


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
        input_start_loc = mutseed.location[0] - start_match
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



def typeSpeculation(comparison_diffreport: 'list[StructComparisonReport]', comparison_onereport: 'list[StructComparisonReport]', cmp_map: dict, mutate_loc: StructMutateLocation) -> dict:
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
            if each.sttype in TRACECMPLIST:
                infer_bytes = inferFixedOrChanged(
                    each.init_sttrace[IND_ARG1], each.init_sttrace[IND_ARG2],
                    each.mut_sttrace[IND_ARG1], each.mut_sttrace[IND_ARG2]
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

            elif each.sttype in HOOKCMPLIST:
                infer_bytes = inferFixedOrChanged(
                    each.init_sttrace[IND_S1], each.init_sttrace[IND_S2],
                    each.mut_sttrace[IND_S1], each.mut_sttrace[IND_S2]
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

            elif each.sttype == COV_TRACE_SWITCH:
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