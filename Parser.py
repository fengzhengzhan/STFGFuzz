import struct

from Fuzzconfig import *


def compareBytes(mutseed: StructSeed, init_trace_analysis: 'list[StructTraceReport]', mut_trace_analysis: 'list[StructTraceReport]', cmp_map: dict) -> 'list[StructComparisonReport]':
    '''
    Bytes of change compared to the initial sample.
    '''
    # list[StructTraceReport]
    LOG(LOG_DEBUG, LOG_STR(LOG_FUNCINFO(), init_trace_analysis, mut_trace_analysis))
    comparison_report: 'list[StructComparisonReport]' = []

    # Only differences in mutation are recorded.
    num_i = 0
    num_m = 0
    inittrace_len = len(init_trace_analysis)
    muttrace_len = len(mut_trace_analysis)
    while num_i < inittrace_len and num_m < muttrace_len:
        # Determine if the compare instruction is in the same block.
        if init_trace_analysis[num_i].startguard == mut_trace_analysis[num_m].startguard and \
                init_trace_analysis[num_i].endguard == mut_trace_analysis[num_m].endguard:
            num_st_i = 0
            num_st_m = 0
            initst_len = len(init_trace_analysis[num_i].constraint)
            mutst_len = len(mut_trace_analysis[num_m].constraint)
            while num_st_i < initst_len and num_st_m < mutst_len:
                if init_trace_analysis[num_i].constraint[num_st_i] == mut_trace_analysis[num_m].constraint[num_st_m]:
                    comparison_report.append(StructComparisonReport(mutseed,
                                                                    init_trace_analysis[num_i].stvalue[num_st_i],
                                                                    mut_trace_analysis[num_m].stvalue[num_st_m],
                                                                    init_trace_analysis[num_i].startguard,
                                                                    init_trace_analysis[num_i].endguard,
                                                                    init_trace_analysis[num_i].constraint[num_st_i]))
                    num_st_i += 1
                    num_st_m += 1
                else:
                    if initst_len > mutst_len:
                        comparison_report.append(StructComparisonReport(mutseed,
                                                                        init_trace_analysis[num_i].stvalue[num_st_i],
                                                                        [],
                                                                        init_trace_analysis[num_i].startguard,
                                                                        init_trace_analysis[num_i].endguard,
                                                                        init_trace_analysis[num_i].constraint[num_st_i]))
                        num_st_i += 1
                    elif initst_len < mutst_len:
                        comparison_report.append(StructComparisonReport(mutseed,
                                                                        [],
                                                                        mut_trace_analysis[num_m].stvalue[num_st_m],
                                                                        init_trace_analysis[num_i].startguard,
                                                                        init_trace_analysis[num_i].endguard,
                                                                        mut_trace_analysis[num_m].constraint[num_st_m]))
                        num_st_m += 1
                    elif initst_len == mutst_len:
                        comparison_report.append(StructComparisonReport(mutseed,
                                                                        init_trace_analysis[num_i].stvalue[num_st_i],
                                                                        [],
                                                                        init_trace_analysis[num_i].startguard,
                                                                        init_trace_analysis[num_i].endguard,
                                                                        init_trace_analysis[num_i].constraint[num_st_i]))
                        comparison_report.append(StructComparisonReport(mutseed,
                                                                        [],
                                                                        mut_trace_analysis[num_m].stvalue[num_st_m],
                                                                        init_trace_analysis[num_i].startguard,
                                                                        init_trace_analysis[num_i].endguard,
                                                                        mut_trace_analysis[num_m].constraint[num_st_m]))
                        num_st_i += 1
                        num_st_m += 1

                # Prevent crossing the border.
                if num_st_i >= initst_len and num_st_m < mutst_len:
                    num_st_i = initst_len - 1
                elif num_st_i < initst_len and num_st_m >= mutst_len:
                    num_st_m = mutst_len - 1
            num_i += 1
            num_m += 1


        # Determine that comparison instructions are not in the same block.
        else:
            # Comparative traversal based on length.
            if inittrace_len > muttrace_len:
                num_st_i = 0
                initst_len = len(init_trace_analysis[num_i].constraint)
                while num_st_i < initst_len:
                    comparison_report.append(StructComparisonReport(mutseed,
                                                                    init_trace_analysis[num_i].stvalue[num_st_i],
                                                                    [],
                                                                    init_trace_analysis[num_i].startguard,
                                                                    init_trace_analysis[num_i].endguard,
                                                                    init_trace_analysis[num_i].constraint[num_st_i]))
                    num_st_i += 1
                num_i += 1

            elif inittrace_len < muttrace_len:
                num_st_m = 0
                mutst_len = len(mut_trace_analysis[num_m].constraint)
                while num_st_m < mutst_len:
                    comparison_report.append(StructComparisonReport(mutseed,
                                                                    mut_trace_analysis[num_i].stvalue[num_st_m],
                                                                    [],
                                                                    mut_trace_analysis[num_i].startguard,
                                                                    mut_trace_analysis[num_i].endguard,
                                                                    mut_trace_analysis[num_i].constraint[num_st_m]))
                    num_st_m += 1
                num_m += 1

            elif inittrace_len == muttrace_len:
                num_st_i = 0
                initst_len = len(init_trace_analysis[num_i].constraint)
                while num_st_i < initst_len:
                    comparison_report.append(StructComparisonReport(mutseed,
                                                                    init_trace_analysis[num_i].stvalue[num_st_i],
                                                                    [],
                                                                    init_trace_analysis[num_i].startguard,
                                                                    init_trace_analysis[num_i].endguard,
                                                                    init_trace_analysis[num_i].constraint[num_st_i]))
                    num_st_i += 1

                num_st_m = 0
                mutst_len = len(mut_trace_analysis[num_m].constraint)
                while num_st_m < mutst_len:
                    comparison_report.append(StructComparisonReport(mutseed,
                                                                    mut_trace_analysis[num_i].stvalue[num_st_m],
                                                                    [],
                                                                    mut_trace_analysis[num_i].startguard,
                                                                    mut_trace_analysis[num_i].endguard,
                                                                    mut_trace_analysis[num_i].constraint[num_st_m]))
                    num_st_m += 1

                num_i += 1
                num_m += 1

        # Prevent crossing the border.
        if num_i >= inittrace_len and num_m < muttrace_len:
            num_i = inittrace_len - 1
        elif num_i < inittrace_len and num_m >= muttrace_len:
            num_m = muttrace_len - 1

    return comparison_report


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


def typeSpeculation(comparison_report: list, eachloop_input_map: dict, cmp_map: dict) -> dict:
    '''
    Type identification and speculation.
    '''
    # print(comparison_report)
    LOG(LOG_DEBUG, LOG_STR(LOG_FUNCINFO(), comparison_report))

    for each in comparison_report:
        seed, ini, mut = each
        cmp_callpc = ini[IND_CALLPC]
        if seed.seedtype == MUT_TYPE_SUB:
            if mut[IND_CMP_TYPE] in TRACECMPLIST:
                ini_arg1 = ini[IND_ARG1]
                ini_arg2 = ini[IND_ARG2]
                mut_arg1 = mut[IND_ARG1]
                mut_arg2 = mut[IND_ARG2]
                infer_bytes = inferFixedOrChanged(ini_arg1, ini_arg2, mut_arg1, mut_arg2)

            elif mut[IND_CMP_TYPE] in HOOKCMPLIST:
                ini_s1 = ini[IND_S1]
                ini_s2 = ini[IND_S2]
                mut_s1 = mut[IND_S1]
                mut_s2 = mut[IND_S2]
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
                    if seed.location[0]-start_match not in eachloop_input_map:
                        if start_match != -1:
                            input_start_loc = seed.location[0] - start_match
                            for l in range(0, len(fixed_bytes)):
                                eachloop_input_map[input_start_loc+l] = fixed_bytes[l]
                        elif end_match != -1:
                            pass
                        else:
                            # This case requires the use of single-byte probes.
                            pass
                else:
                    pass

            elif mut[IND_CMP_TYPE] == COV_TRACE_SWITCH:
                pass
        elif seed.seedtype == MUT_TYPE_INSERT:
            pass

    return eachloop_input_map


