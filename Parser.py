import struct

from Fuzzconfig import *


def traceBack(init_trace, mut_trace, lcstable, i, m, init_list, mut_list):
    '''
    Backtracking to find a location
    '''
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
    '''
    Find the longest common subsequence.
    '''
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
    '''
    Bytes of change compared to the initial sample.
    '''
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
        
        st_lcs_len, st_init_list, st_mut_list = compareLCS(init_trace_analysis[guard_init_list[gi]].constraint, mut_trace_analysis[guard_mut_list[gi]].constraint)
        # Same part of the constraint.
        for sti in range(len(st_init_list)):
            comparison_diffreport.append(
                StructComparisonReport(
                    mutseed,
                    init_trace_analysis[guard_init_list[gi]].stvalue[st_init_list[sti]][IND_CMP_TYPE],
                    init_trace_analysis[guard_init_list[gi]].stvalue[st_init_list[sti]],
                    mut_trace_analysis[guard_mut_list[gi]].stvalue[st_mut_list[sti]],
                    init_trace_analysis[guard_init_list[gi]].startguard,
                    init_trace_analysis[guard_init_list[gi]].endguard,
                    init_trace_analysis[guard_init_list[gi]].constraint[st_init_list[sti]],
                )
            )

        # Different parts of the initial constraint
        for ii in range(len(init_trace_analysis[guard_init_list[gi]].constraint)):
            if ii not in st_init_list:
                comparison_onereport.append(
                    StructComparisonReport(
                        mutseed,
                        init_trace_analysis[guard_init_list[gi]].stvalue[ii][IND_CMP_TYPE],
                        init_trace_analysis[guard_init_list[gi]].stvalue[ii],
                        [],
                        init_trace_analysis[guard_init_list[gi]].startguard,
                        init_trace_analysis[guard_init_list[gi]].endguard,
                        init_trace_analysis[guard_init_list[gi]].constraint[ii]
                    )
                )

        # Different parts of the variation constraint
        for mi in range(len(mut_trace_analysis[guard_mut_list[gi]].constraint)):
            if mi not in st_mut_list:
                comparison_onereport.append(
                    StructComparisonReport(
                        mutseed,
                        mut_trace_analysis[guard_mut_list[gi]].stvalue[mi][IND_CMP_TYPE],
                        [],
                        mut_trace_analysis[guard_mut_list[gi]].stvalue[mi],
                        mut_trace_analysis[guard_mut_list[gi]].startguard,
                        mut_trace_analysis[guard_mut_list[gi]].endguard,
                        mut_trace_analysis[guard_mut_list[gi]].constraint[mi]

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


def inferFixedOrChanged(ini1, ini2, mut1, mut2):
    temp_infer: list[list, list] = [[0, 0], ["", ""]]
    if ini1 == mut1:
        temp_infer[0][0] = PAR_FIXED
        temp_infer[1][0] = ini1
    else:
        temp_infer[0][0] = PAR_CHANGED
        temp_infer[1][0] = mut1

    if ini2 == mut2:
        temp_infer[0][1] = PAR_FIXED
        temp_infer[1][1] = ini2
    else:
        temp_infer[0][1] = PAR_CHANGED
        temp_infer[1][1] = mut2

    return temp_infer


def typeSpeculation(comparison_diffreport: 'list[StructComparisonReport]', comparison_onereport: 'list[StructComparisonReport]', cmp_map: dict) -> dict:
    '''
    Type identification and speculation.
    '''
    # print(comparison_report)
    LOG(LOG_DEBUG, LOG_STR(LOG_FUNCINFO(), comparison_diffreport, comparison_onereport))
    eachloop_change_inputmap = {}

    for each in comparison_diffreport:
        mutseed = each.mutseed
        if len(each.init_sttrace) != 0 and len(each.mut_sttrace) != 0:
            if mutseed.seedtype == MUT_TYPE_SUB:
                if each.sttype in TRACECMPLIST:
                    ini_arg1 = each.init_sttrace[IND_ARG1]
                    ini_arg2 = each.init_sttrace[IND_ARG2]
                    mut_arg1 = each.mut_sttrace[IND_ARG1]
                    mut_arg2 = each.mut_sttrace[IND_ARG2]
                    infer_bytes = inferFixedOrChanged(ini_arg1, ini_arg2, mut_arg1, mut_arg2)

                elif each.sttype in HOOKCMPLIST:
                    ini_s1 = each.init_sttrace[IND_S1]
                    ini_s2 = each.init_sttrace[IND_S2]
                    mut_s1 = each.mut_sttrace[IND_S1]
                    mut_s2 = each.mut_sttrace[IND_S2]
                    infer_bytes = inferFixedOrChanged(ini_s1, ini_s2, mut_s1, mut_s2)
                    # Find fixed bytes and changed bytes.
                    if PAR_FIXED in infer_bytes[0]:
                        if infer_bytes[0][0] == PAR_FIXED:
                            fixed_bytes = infer_bytes[1][0]
                            changed_bytes = infer_bytes[1][1]
                        elif infer_bytes[0][1] == PAR_FIXED:
                            fixed_bytes = infer_bytes[1][1]
                            changed_bytes = infer_bytes[1][0]

                        # Using characters to match location of the input bytes.
                        start_match = changed_bytes.find(MUT_STR[0:MUT_MATCH])
                        end_match = changed_bytes.find(MUT_STR[len(MUT_STR)-MUT_MATCH:len(MUT_STR)])
                        # Direct byte matching requires only one copy of the string.
                        if mutseed.location[0]-start_match not in eachloop_change_inputmap:
                            if start_match != -1:
                                input_start_loc = mutseed.location[0] - start_match
                                for l in range(0, len(fixed_bytes)):
                                    eachloop_change_inputmap[input_start_loc+l] = fixed_bytes[l]
                            elif end_match != -1:
                                pass
                            else:
                                # This case requires the use of single-byte probes.
                                pass
                    else:
                        pass

                elif each.sttype == COV_TRACE_SWITCH:
                    pass
            elif mutseed.seedtype == MUT_TYPE_INSERT:
                pass

        elif len(each.init_sttrace) != 0 and len(each.mut_sttrace) == 0:
            pass
        elif len(each.init_sttrace) == 0 and len(each.mut_sttrace) != 0:
            pass
        elif len(each.init_sttrace) == 0 and len(each.mut_sttrace) == 0:
            pass


    return eachloop_change_inputmap


if __name__ == "__main__":
    a = ['A', 'B', 'C', 'B', 'D', 'A', 'B']
    b = ['B', 'D', 'C', 'A', 'B', 'A']
    # a = ['A']
    # b = ['A']
    compareLCS(a, b)