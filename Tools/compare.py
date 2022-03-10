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