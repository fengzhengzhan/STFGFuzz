import re
import json
from ctypes import *

from fuzzer_module.Fuzzconfig import *


class Analyzer:
    def __init__(self):
        self.num_pcguard: int = -1
        try:
            self.rt = CDLL('librt.so')
        except:
            self.rt = CDLL('librt.so.1')

    def traceAyalysis(self, out_info: str):
        """
        Analysis of trace reports generated by documents.
        @param out_info:
        @return:
        """
        if ANA_MEMSHM_MODE:
            return self.memoryTrace(out_info)
        else:
            return self.terminalTrace(out_info)  # fixme

    def memoryTrace(self, out_info: str):
        re_str = SHMID_FLAG + "(.*?)" + END_EACH_FLAG
        shm_key = int(re.search(re_str, str(out_info)).group(1))
        # print(shm_key)

        shmget = self.rt.shmget
        shmget.argtypes = [c_int, c_size_t, c_int]
        shmget.restype = c_int

        shmat = self.rt.shmat
        shmat.argtypes = [c_int, POINTER(c_void_p), c_int]
        shmat.restype = c_void_p

        shmid = shmget(shm_key, 512 * 1024 * 1024, 0o666)
        if shmid < 0:
            raise Exception("Error System not infected.")

        addr = shmat(shmid, None, 0)
        # Get the length of cmpcovshm contents.
        interlen_str = string_at(addr, ANA_INTERLEN_SIZE).decode("utf-8")
        re_str = INTERLEN_FLAG + "(.*?)" + END_EACH_FLAG
        interlen = int(re.search(re_str, interlen_str).group(1))

        # Read content in pieces
        pieces = interlen // ANA_SHM_INTERVAL
        over = interlen % ANA_SHM_INTERVAL

        cmpcovshm_str = ""
        for each in range(0, pieces):
            cmpcovshm_str += string_at(addr + ANA_SHM_INTERVAL * each, ANA_SHM_INTERVAL).decode("utf-8")
        # fixme .decode("utf-8", "ignore")
        cmpcovshm_str += string_at(addr + ANA_SHM_INTERVAL * pieces, over).decode("utf-8")
        cmpcovshm_str = cmpcovshm_str[16:-1]
        self.rt.shmctl(shmid, 0, 0)

        # Content to json
        cmpcovshm_str = '{"' + ANA_CMPCOVSHM_NAME + '":[' + cmpcovshm_str + ']}'
        cmpcovshm_json = json.loads(cmpcovshm_str)
        cmpcovshm_list = cmpcovshm_json[ANA_CMPCOVSHM_NAME]
        # print(type(cmpcovshm_json[ANA_CMPCOVSHM_NAME]), cmpcovshm_json[ANA_CMPCOVSHM_NAME])
        LOG(LOG_DEBUG, LOG_STR(LOG_FUNCINFO(), cmpcovshm_list))

        # Iterate through the trace report to get the corresponding information
        cmprpt_dict: 'dict[cmpid:[StructCmpIns]]' = {}  # According cmp instruction to genetator dict.
        cmpid_list = []
        content_list = []
        args_list = []
        pre_guard_num = USE_INITNUM  # before
        end_guard_num = USE_ENDNUM
        exception_guard_num = USE_EXCEPTION
        for each in cmpcovshm_list:
            typeflag = each[0]
            if typeflag == INIT_PC_GUARD:
                pass
            elif typeflag == NUM_PC_GUARD:
                self.num_pcguard = int(each[2])
            elif typeflag == EACH_PC_GUARD:
                type = typeflag
                guard_num = int(each[1], 16)
                for idx, oneid in enumerate(cmpid_list):
                    if idx not in cmprpt_dict:
                        cmprpt_dict[oneid] = [StructCmpIns(oneid, pre_guard_num, guard_num, content_list[idx], args_list[idx]), ]
                    else:
                        cmprpt_dict[oneid].append(StructCmpIns(oneid, pre_guard_num, guard_num, content_list[idx], args_list[idx]))
                pre_guard_num = guard_num
                cmpid_list = []
                content_list = []
                args_list = []
            elif typeflag == PROGRAM_END:
                end = True
                for idx, oneid in enumerate(cmpid_list):
                    if idx not in cmprpt_dict:
                        cmprpt_dict[oneid] = [StructCmpIns(oneid, pre_guard_num, end_guard_num, content_list[idx], args_list[idx]), ]
                    else:
                        cmprpt_dict[oneid].append(StructCmpIns(oneid, pre_guard_num, end_guard_num, content_list[idx], args_list[idx]))
                cmpid_list = []
                content_list = []
                args_list = []

            elif typeflag in TRACECMPSET:
                # type, func_pc, caller_pc, arg1, arg2, arg_len
                cmpid_list.append(str(each[1][2:]+each[2][2:]))
                content_list.append([typeflag, each[1], each[2], each[5]])
                args_list.append([each[3], each[4]])
            elif typeflag == COV_SWITCH:
                # type, func_pc, caller_pc, num_case, size_val
                cmpid_list.append(str(each[1][2:] + each[2][2:]))
                content_list.append([typeflag, each[1], each[2], int(each[3]), each[4]])
                temp_args = []
                for i in range(int(each[3])):
                    temp_args.append(each[i + 5])
                args_list.append(temp_args)
            elif typeflag == COV_DIV4 or typeflag == COV_DIV8 or typeflag == COV_GEP:
                pass
            elif typeflag in HOOKCMPSET:
                # type, func_pc, caller_pc, s1, s2, size_n, result
                cmpid_list.append(str(each[1][2:]+each[2][2:]))
                content_list.append([typeflag, each[1], each[2], int(each[5]), int(each[6])])
                args_list.append([each[3], each[4]])

        if len(cmpid_list) > 0:
            for idx, oneid in enumerate(cmpid_list):
                if idx not in cmprpt_dict:
                    cmprpt_dict[oneid] = [StructCmpIns(oneid, pre_guard_num, end_guard_num, content_list[idx], args_list[idx]), ]
                else:
                    cmprpt_dict[oneid].append(StructCmpIns(oneid, pre_guard_num, end_guard_num, content_list[idx], args_list[idx]))

        cmprpt_set: 'cmpid' = set(cmprpt_dict)
        return cmprpt_dict, cmprpt_set


    def terminalTrace(self, out_info: str):
        # For \x00, that represents hex char in range [0-255].
        out_info = out_info.decode('UTF-8', 'ignore')
        each_line_list: list[str] = out_info.split("\n")

        struct_report_list: 'list[StructTraceReport]' = []

        call_pc_list = []
        content_list = []

        exist_z = True
        before_guard_num = USE_INITNUM
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
                combine_line += '\n'  # An entire string was splited by '\n',then need to add this character for string.
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
            LOG(LOG_DEBUG, LOG_STR(LOG_FUNCINFO(), combine_line))

            # Matching Symbols.
            each = combine_line.split(" ")
            typeflag = each[0]
            if typeflag in FLAG_DICT and each[-1] == END_EACH_FLAG:
                # Matching trace identifier.
                if typeflag == INIT_PC_GUARD:
                    type = typeflag
                    call_pc = each[1]
                    start_addr = each[2]
                    end_addr = each[3]
                elif typeflag == NUM_PC_GUARD:
                    type = typeflag
                    call_pc = each[1]
                    self.num_pcguard = int(each[2])
                elif typeflag == EACH_PC_GUARD:
                    type = typeflag
                    call_pc = each[1]
                    guard_addr = each[2]
                    guard_num = int(each[3], 16)
                    struct_report_list.append(StructTraceReport(before_guard_num, guard_num, call_pc_list, content_list, []))
                    before_guard_num = guard_num
                    call_pc_list = []
                    content_list = []
                elif typeflag == PROGRAM_END:
                    type = typeflag
                    call_pc = each[1]
                    end = True
                    struct_report_list.append(StructTraceReport(before_guard_num, ANA_ENDPROG_IDX, call_pc_list, content_list, []))
                # Matching comparison identifier.
                elif typeflag in TRACECMPSET:
                    type = typeflag
                    call_pc = each[1]
                    arg1 = each[2]
                    arg2 = each[3]
                    arg_len = each[4]
                    call_pc_list.append(call_pc)
                    temp_content = [type, call_pc, arg1, arg2, arg_len]
                    content_list.append(temp_content)
                elif typeflag == COV_SWITCH:
                    type = typeflag
                    call_pc = each[1]
                    num_case = int(each[2])
                    size_val = each[3]

                    call_pc_list.append(call_pc)
                    temp_content = [type, call_pc, num_case, size_val]
                    for i in range(num_case):
                        temp_content.append(each[i+4])
                    content_list.append(temp_content)
                elif typeflag == COV_DIV4 or typeflag == COV_DIV8 or typeflag == COV_GEP:
                    pass
                elif typeflag in HOOKCMPSET:
                    type = typeflag
                    call_pc = each[1]
                    s1 = re.search(r'<s1"(.*)"1s>', combine_line, flags=re.S).group(1)
                    s2 = re.search(r'<s2"(.*)"2s>', combine_line, flags=re.S).group(1)
                    size_n = int(each[-3])
                    result = int(each[-2])

                    call_pc_list.append(call_pc)
                    temp_content = [type, call_pc, s1, s2, size_n, result]
                    content_list.append(temp_content)

                    # print(type, call_pc, s1.encode(), s2.encode(), size_n, result)
                    LOG(LOG_DEBUG, LOG_STR(LOG_FUNCINFO(), type, call_pc, s1.encode(), s2.encode(), size_n, result))

            else:
                # Here content has high possible as the normal program output.
                content = combine_line

        # print(struct_report_list)
        LOG(LOG_DEBUG, LOG_STR(LOG_FUNCINFO(), struct_report_list))

        # print(trace_analysis)
        return struct_report_list

    def getNumOfPcguard(self):
        if self.num_pcguard == -1:
            raise Exception("Error: Number of tracks not acquired.")
        return self.num_pcguard

