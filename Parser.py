import struct

from Fuzzconfig import *


def compareBytes(mutseed: StructSeed, init_trace_analysis: 'list[StructTraceReport]', mut_trace_analysis: 'list[StructTraceReport]') -> 'list[StructComparisonReport]':
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
                    comparison_report.append(
                        StructComparisonReport(
                            mutseed,
                            init_trace_analysis[num_i].stvalue[num_st_i][IND_CMP_TYPE],
                            init_trace_analysis[num_i].stvalue[num_st_i],
                            mut_trace_analysis[num_m].stvalue[num_st_m],
                            init_trace_analysis[num_i].startguard,
                            init_trace_analysis[num_i].endguard,
                            init_trace_analysis[num_i].constraint[num_st_i]
                        )
                    )
                    num_st_i += 1
                    num_st_m += 1
                else:
                    if initst_len > mutst_len:
                        comparison_report.append(
                            StructComparisonReport(
                                mutseed,
                                init_trace_analysis[num_i].stvalue[num_st_i][IND_CMP_TYPE],
                                init_trace_analysis[num_i].stvalue[num_st_i],
                                [],
                                init_trace_analysis[num_i].startguard,
                                init_trace_analysis[num_i].endguard,
                                init_trace_analysis[num_i].constraint[num_st_i]
                            )
                        )
                        num_st_i += 1
                    elif initst_len < mutst_len:
                        comparison_report.append(
                            StructComparisonReport(
                                mutseed,
                                mut_trace_analysis[num_m].stvalue[num_st_m][IND_CMP_TYPE],
                                [],
                                mut_trace_analysis[num_m].stvalue[num_st_m],
                                mut_trace_analysis[num_i].startguard,
                                mut_trace_analysis[num_i].endguard,
                                mut_trace_analysis[num_m].constraint[num_st_m]
                            )
                        )
                        num_st_m += 1
                    elif initst_len == mutst_len:
                        comparison_report.append(
                            StructComparisonReport(
                                mutseed,
                                init_trace_analysis[num_i].stvalue[num_st_i][IND_CMP_TYPE],
                                init_trace_analysis[num_i].stvalue[num_st_i],
                                [],
                                init_trace_analysis[num_i].startguard,
                                init_trace_analysis[num_i].endguard,
                                init_trace_analysis[num_i].constraint[num_st_i]
                            )
                        )
                        comparison_report.append(
                            StructComparisonReport(
                                mutseed,
                                mut_trace_analysis[num_m].stvalue[num_st_m][IND_CMP_TYPE],
                                [],
                                mut_trace_analysis[num_m].stvalue[num_st_m],
                                mut_trace_analysis[num_i].startguard,
                                mut_trace_analysis[num_i].endguard,
                                mut_trace_analysis[num_m].constraint[num_st_m]
                            )
                        )
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
                    comparison_report.append(
                        StructComparisonReport(
                            mutseed,
                            init_trace_analysis[num_i].stvalue[num_st_i][IND_CMP_TYPE],
                            init_trace_analysis[num_i].stvalue[num_st_i],
                            [],
                            init_trace_analysis[num_i].startguard,
                            init_trace_analysis[num_i].endguard,
                            init_trace_analysis[num_i].constraint[num_st_i]
                        )
                    )
                    num_st_i += 1
                num_i += 1

            elif inittrace_len < muttrace_len:
                num_st_m = 0
                mutst_len = len(mut_trace_analysis[num_m].constraint)
                while num_st_m < mutst_len:
                    comparison_report.append(
                        StructComparisonReport(
                            mutseed,
                            mut_trace_analysis[num_m].stvalue[num_st_m][IND_CMP_TYPE],
                            [],
                            mut_trace_analysis[num_i].stvalue[num_st_m],
                            mut_trace_analysis[num_i].startguard,
                            mut_trace_analysis[num_i].endguard,
                            mut_trace_analysis[num_i].constraint[num_st_m]
                        )
                    )
                    num_st_m += 1
                num_m += 1

            elif inittrace_len == muttrace_len:
                num_st_i = 0
                initst_len = len(init_trace_analysis[num_i].constraint)
                while num_st_i < initst_len:
                    comparison_report.append(
                        StructComparisonReport(
                            mutseed,
                            init_trace_analysis[num_i].stvalue[num_st_i][IND_CMP_TYPE],
                            init_trace_analysis[num_i].stvalue[num_st_i],
                            [],
                            init_trace_analysis[num_i].startguard,
                            init_trace_analysis[num_i].endguard,
                            init_trace_analysis[num_i].constraint[num_st_i]
                        )
                    )
                    num_st_i += 1

                num_st_m = 0
                mutst_len = len(mut_trace_analysis[num_m].constraint)
                while num_st_m < mutst_len:
                    comparison_report.append(
                        StructComparisonReport(
                            mutseed,
                            mut_trace_analysis[num_m].stvalue[num_st_m][IND_CMP_TYPE],
                            [],
                            mut_trace_analysis[num_i].stvalue[num_st_m],
                            mut_trace_analysis[num_i].startguard,
                            mut_trace_analysis[num_i].endguard,
                            mut_trace_analysis[num_i].constraint[num_st_m]
                        )
                    )
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


def typeSpeculation(comparison_report: 'list[StructComparisonReport]', cmp_map: dict) -> dict:
    '''
    Type identification and speculation.
    '''
    # print(comparison_report)
    LOG(LOG_DEBUG, LOG_STR(LOG_FUNCINFO(), comparison_report))
    eachloop_change_inputmap = {}

    for each in comparison_report:
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


