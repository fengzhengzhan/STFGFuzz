from Fuzzconfig import *


# For \x00, that represents hex char in range [0-255].
def traceAyalysis(out_info: str):
    out_info = out_info.decode('UTF-8', 'ignore')
    each_line_list: list[str] = out_info.split("\n")

    start_addr = ""
    end_addr = ""
    call_pc = ""
    num_of_pcguard = 0

    zflag = False
    for each_line in each_line_list:
        each = each_line.split(" ")
        if each[0] == '':
            continue
        elif zflag:
            # An entire string was splited by '\n', then need to add this character for string.
            print(each)
            if each[-1] == END_EACH_FLAG:
                zflag = False
        elif each[0] in FLAG_DICT:
            if each[0] == INIT_PC_GUARD:
                start_addr = each[1]
                end_addr = each[2]
                call_pc = each[3]
            elif each[0] == NUM_PC_GUARD:
                num_of_pcguard = each[1]
            elif each[0] == EACH_PC_GUARD:
                guard_addr = each[1]
                guard_num = each[2]
                call_pc = each[3]
            if each[-1] != END_EACH_FLAG:
                zflag = True
        else:
            # Here content has high possible as the normal program output.
            content = ""






