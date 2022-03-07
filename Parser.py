import struct

from Fuzzconfig import *


def inferFixedOrChanged(ini1, ini2, mut1, mut2):
    temp_infer: list[list, list] = [[0, 0], ["", ""]]
    if ini1 == mut1:
        temp_infer[0][0] = PAR_FIXED
        temp_infer[1][0] = ini1
    else:
        temp_infer[0][0] = PAR_CHANGED

    if ini2 == mut2:
        temp_infer[0][1] = PAR_FIXED
        temp_infer[1][1] = ini2
    else:
        temp_infer[0][1] = PAR_CHANGED

    return temp_infer


def typeSpeculation(comparison_report: list) -> list:
    '''
    Type identification and speculation.
    '''
    LOG(LOG_DEBUG, LOG_STR(LOG_FUNCINFO(), comparison_report))

    fixed_bytes = ""
    changed_bytes = ""
    for each in comparison_report:
        loc, ini, mut = each
        if loc[IND_MUT_TYPE] == MUT_TYPE_SUB:
            if mut[IND_CMP_TYPE] in TRACECMPLIST:
                ini_arg1 = ini[IND_ARG1]
                ini_arg2 = ini[IND_ARG2]
                mut_arg1 = mut[IND_ARG1]
                mut_arg2 = mut[IND_ARG2]
            elif mut[IND_CMP_TYPE] in HOOKCMPLIST:
                ini_s1 = ini[IND_S1]
                ini_s2 = ini[IND_S2]
                mut_s1 = mut[IND_S1]
                mut_s2 = mut[IND_S2]
                inferFixedOrChanged(ini_s1, ini_s2, mut_s1, mut_s2)


            elif mut[IND_CMP_TYPE] == COV_TRACE_SWITCH:
                pass
        elif loc[IND_MUT_TYPE] == MUT_TYPE_INSERT:
            pass
