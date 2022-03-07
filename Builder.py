
from Fuzzconfig import *


def compareBytes(init_trace_analysis: list, mut_trace_analysis: list, location: list) -> list:
    '''
    Bytes of change compared to the initial sample.
    '''
    # list[list[int], list[list[str]], list[list[list]]]
    LOG(LOG_DEBUG, LOG_STR(LOG_FUNCINFO(), init_trace_analysis, mut_trace_analysis))
    comparison_report: list[list[list, list, list]] = []

    # Only differences in mutation are recorded.
    max_i = max(len(init_trace_analysis[0]), len(mut_trace_analysis[0]))
    for i in range(0, max_i):
        if init_trace_analysis[0][i] == mut_trace_analysis[0][i]:
            max_j = max(len(init_trace_analysis[1][i]), len(mut_trace_analysis[1][i]))
            for j in range(0, max_j):
                if init_trace_analysis[1][i][j] == mut_trace_analysis[1][i][j]:
                    max_k = len(mut_trace_analysis[2][i][j])
                    for k in range(0, max_k):
                        if init_trace_analysis[2][i][j][k] == mut_trace_analysis[2][i][j][k]:
                            pass
                        else:
                            comparison_report.append([location, init_trace_analysis[2][i][j], mut_trace_analysis[2][i][j]])
                            LOG(LOG_DEBUG, LOG_STR(LOG_FUNCINFO(), location, str(init_trace_analysis[2][i][j]).encode(), str(mut_trace_analysis[2][i][j]).encode()))
                else:
                    pass
        else:
            pass

    return comparison_report



def buildConstraint():
    '''
    Constructing constraint graph.
    '''


