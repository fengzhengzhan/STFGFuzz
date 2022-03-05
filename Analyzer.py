import re

from Fuzzconfig import *

# Get the content of the seed file.
def getSeedContent():
    


# For \x00, that represents hex char in range [0-255].
def traceAyalysis(out_info: str) -> (int, list):
    out_info = out_info.decode('UTF-8', 'ignore')
    each_line_list: list[str] = out_info.split("\n")

    num_of_pcguard: int = 0
    trace_analysis: list[list[int], list[list[str]], list[list[list]]] = []
    guard_list = []
    guard_callpc_list = []
    guard_content_list = []

    call_pc_list = []
    content_list = []

    exist_z = True
    nofirst_g = False
    combine_line = ""
    for each_line in each_line_list:
        # Handling blank lines.
        if exist_z and each_line == '':
            continue
        # Handling normal lines.
        elif each_line[0] in FLAG_DICT and each_line[1] == ' ' and each_line[-2] == ' ' and each_line[-1] == END_EACH_FLAG:
            combine_line = ""
            combine_line = each_line
        # Handling discontinuous lines.
        elif each_line[0] in FLAG_DICT and each_line[1] == ' ' and each_line[-1] != END_EACH_FLAG:
            combine_line = ""
            combine_line += each_line
            exist_z = False
            continue
        elif not exist_z and each_line == '':
            combine_line += '\n'  # An entire string was splited by '\n', then need to add this character for string.
            continue
        elif not exist_z and each_line[-1] != END_EACH_FLAG:
            combine_line += '\n' + each_line
            continue
        elif not exist_z and each_line[-2] == ' ' and each_line[-1] == END_EACH_FLAG:
            combine_line += '\n' + each_line
            exist_z = True
        # Other cases remain as they are.
        else:
            combine_line = ""
            combine_line = each_line

        # print(combine_line.encode())
        FUZZLOGGING(DEBUG, LOG_STR(LOG_FUNCINFO(), combine_line))

        # Matching Symbols.
        each = combine_line.split(" ")
        if each[0] in FLAG_DICT and each[-1] == END_EACH_FLAG:
            # Matching trace identifier.
            if each[0] == INIT_PC_GUARD:
                type = each[0]
                call_pc = each[1]
                start_addr = each[2]
                end_addr = each[3]
            elif each[0] == NUM_PC_GUARD:
                type = each[0]
                call_pc = each[1]
                num_of_pcguard = int(each[2])
            elif each[0] == EACH_PC_GUARD:
                type = each[0]
                call_pc = each[1]
                guard_addr = each[2]
                guard_num = int(each[3], 16)
                guard_list.append(guard_num)
                if nofirst_g:
                    guard_callpc_list.append(call_pc_list)
                    guard_content_list.append(content_list)
                    call_pc_list = []
                    content_list = []
                nofirst_g = True
            elif each[0] == PROGRAM_END:
                type = each[0]
                call_pc = each[1]
                end = True
                guard_callpc_list.append(call_pc_list)
                guard_content_list.append(content_list)
                trace_analysis.append(guard_list)
                trace_analysis.append(guard_callpc_list)
                trace_analysis.append(guard_content_list)
            # Matching comparison identifier.
            elif each[0] == COV_TRACE_CMP1 or each[0] == COV_TRACE_CMP2 \
                    or each[0] == COV_TRACE_CMP4 or each[0] == COV_TRACE_CMP8 \
                    or each[0] == COV_TRACE_CONST_CMP1 or each[0] == COV_TRACE_CONST_CMP2 \
                    or each[0] == COV_TRACE_CONST_CMP4 or each[0] == COV_TRACE_CONST_CMP8:
                type = each[0]
                call_pc = each[1]
                arg1 = each[2]
                arg2 = each[3]
                arg_len = each[4]
                call_pc_list.append(call_pc)
                temp_content = [call_pc, arg1, arg2, arg_len]
                content_list.append(temp_content)
            elif each[0] == COV_TRACE_SWITCH:
                type = each[0]
                call_pc = each[1]
                num_case = int(each[2])
                size_val = each[3]

                call_pc_list.append(call_pc)
                temp_content = [call_pc, num_case, size_val]
                for i in range(num_case):
                    temp_content.append(each[i+4])
                content_list.append(temp_content)
            elif each[0] == COV_TRACE_DIV4 or each[0] == COV_TRACE_DIV8 or each[0] == COV_TRACE_GEP:
                pass
            elif each[0] == WEAK_HOOK_MEMCMP or each[0] == WEAK_HOOK_STRNCMP \
                    or each[0] == WEAK_HOOK_STRCMP or each[0] == WEAK_HOOK_STRNCASECMP \
                    or each[0] == WEAK_HOOK_STRCASECMP:
                type = each[0]
                call_pc = each[1]
                s1 = re.search(r'<s1"(.*)"1s>', combine_line, flags=re.S).group(1)
                s2 = re.search(r'<s2"(.*)"2s>', combine_line, flags=re.S).group(1)
                size_n = int(each[-3])
                result = int(each[-2])

                call_pc_list.append(call_pc)
                temp_content = [call_pc, s1, s2, size_n, result]
                content_list.append(temp_content)

                # print(type, call_pc, s1.encode(), s2.encode(), size_n, result)
                FUZZLOGGING(DEBUG, LOG_STR(LOG_FUNCINFO(), type, call_pc, s1.encode(), s2.encode(), size_n, result))

        else:
            # Here content has high possible as the normal program output.
            content = combine_line

    print(trace_analysis)
    return num_of_pcguard, trace_analysis





