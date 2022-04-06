import re
import json
from ctypes import *

from fuzzer_module.Fuzzconfig import *


class Analyzer:
    def __init__(self):
        self.num_pcguard: int = USE_INITNUM
        self.shm_key = USE_INITNUM
        try:
            self.rt = CDLL('librt.so')
        except:
            self.rt = CDLL('librt.so.1')


    def gainTraceRpt(self, out_info: str):
        """
        Analysis of trace reports generated by documents.
        @param out_info:
        @return:
        """
        if ANA_MEMSHM_MODE:
            return self.memoryTrace(out_info)
        else:
            return self.terminalTrace(out_info)  # Not recommended

    def memoryTrace(self, out_info: str):
        try:
            re_str = SHMID_FLAG + "(.*?)" + END_EACH_FLAG
            self.shm_key = int(re.search(re_str, str(out_info)).group(1))
            # print(self.shm_key)
        except Exception as e:
            pass

        shmget = self.rt.shmget
        shmget.argtypes = [c_int, c_size_t, c_int]
        shmget.restype = c_int

        shmat = self.rt.shmat
        shmat.argtypes = [c_int, POINTER(c_void_p), c_int]
        shmat.restype = c_void_p

        shmid = shmget(self.shm_key, 4294967296, 0o777)  # 4*1024*1024*1024 4GB
        if shmid < 0:
            raise Exception("Error System not shared.")

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
        LOG(LOG_DEBUG, LOG_FUNCINFO(), cmpcovshm_list)
        return cmpcovshm_list, out_info

    def terminalTrace(self, out_info: str):
        # For \x00, that represents hex char in range [0-255].
        out_info = out_info.decode('UTF-8', 'ignore')
        each_line_list: list[str] = out_info.split("\n")

        exist_z = True
        cmpcovcont_list = []
        content = ""
        for each_line in each_line_list:
            combine_line = ""
            # Handling blank lines.
            if exist_z and each_line == '':
                continue
            # Handling normal lines.
            elif each_line[0] in FLAG_DICT \
                    and each_line[1] == ' ' and each_line[-2] == ' ' \
                    and each_line[-1] == END_EACH_FLAG:
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

            LOG(LOG_DEBUG, LOG_FUNCINFO(), combine_line)

            # Matching Symbols.
            each = combine_line.split(" ")
            typeflag = each[0]
            if typeflag in FLAG_DICT and each[-1] == END_EACH_FLAG:
                cmpcovcont_list.append(each)
            else:
                # Here content has high possible as the normal program output.
                content += combine_line

        return cmpcovcont_list, content

    def traceAyalysis(self, cmpcovcont_list, cmpcov_content, freezeid_rpt, sch: 'Scheduler'):
        # Iterate through the trace report to get the corresponding information
        cmprpt_dict: 'dict[cmpid:[StructCmpIns]]' = {}  # According cmp instruction to genetator dict.
        cmpid_list = []
        flagid_list = []
        args_list = []
        pre_guard_num = USE_INITNUM  # before
        end_guard_num = USE_ENDNUM
        exception_guard_num = USE_EXCEPTION
        for each in cmpcovcont_list:
            typeflag = each[0]
            if typeflag in CMPSET:
                cmpid = str(each[1][2:]+each[2][2:])
                if cmpid in freezeid_rpt:
                    continue
            if typeflag == INIT_PC_GUARD:
                pass
            elif typeflag == NUM_PC_GUARD:
                self.num_pcguard = int(each[2])
            elif typeflag == EACH_PC_GUARD:
                type = typeflag
                guard_num = int(each[1], 16)
                sch.coveragepath.add(guard_num)
                for i, oneid in enumerate(cmpid_list):
                    if oneid not in cmprpt_dict:
                        cmprpt_dict[oneid] = [
                            StructCmpIns(oneid, pre_guard_num, guard_num, flagid_list[i], args_list[i]),
                        ]
                    else:
                        cmprpt_dict[oneid].append(
                            StructCmpIns(oneid, pre_guard_num, guard_num, flagid_list[i], args_list[i])
                        )
                pre_guard_num = guard_num
                cmpid_list = []
                flagid_list = []
                args_list = []
            elif typeflag == PROGRAM_END:
                end = True
                for i, oneid in enumerate(cmpid_list):
                    if oneid not in cmprpt_dict:
                        cmprpt_dict[oneid] = [
                            StructCmpIns(oneid, pre_guard_num, end_guard_num, flagid_list[i], args_list[i]),
                        ]
                    else:
                        cmprpt_dict[oneid].append(
                            StructCmpIns(oneid, pre_guard_num, end_guard_num, flagid_list[i], args_list[i])
                        )
                cmpid_list = []
                flagid_list = []
                args_list = []

            elif typeflag in TRACENUMCMPSET:
                # type, func_pc, caller_pc, arg1, arg2, arg_len
                cmpid_list.append(cmpid)
                flagid_list.append([typeflag, each[1], each[2], each[5]])
                args_list.append([each[3], each[4]])
            elif typeflag == COV_SWITCH:
                # type, func_pc, caller_pc, num_case, size_val
                cmpid_list.append(cmpid)
                flagid_list.append([typeflag, each[1], each[2], int(each[3]), each[4]])
                temp_args = []
                temp_args.append(each[5])
                for i in range(int(each[3])):
                    temp_args.append(each[i + 6])
                args_list.append(temp_args)
            elif typeflag == COV_DIV4 or typeflag == COV_DIV8 or typeflag == COV_GEP:
                pass
            elif typeflag in HOOKSTRCMPSET:
                # type, func_pc, caller_pc, s1, s2, size_n, result
                cmpid_list.append(cmpid)
                flagid_list.append([typeflag, each[1], each[2], int(each[5]), int(each[6])])
                args_list.append([each[3], each[4]])

        if len(cmpid_list) > 0:
            for i, oneid in enumerate(cmpid_list):
                if oneid not in cmprpt_dict:
                    cmprpt_dict[oneid] = [
                        StructCmpIns(oneid, pre_guard_num, end_guard_num, flagid_list[i], args_list[i]),
                    ]
                else:
                    cmprpt_dict[oneid].append(
                        StructCmpIns(oneid, pre_guard_num, end_guard_num, flagid_list[i], args_list[i])
                    )

        LOG(LOG_DEBUG, LOG_FUNCINFO(), cmprpt_dict)
        cmprpt_set: 'cmpid' = set(cmprpt_dict)
        return cmprpt_dict, cmprpt_set

    '''
    Tracking Comparison Module.
    '''

    def compareRptToLoc(self, seed: StructSeed,
                        initrpt_dict: 'dict[str:StructCmpIns]', initrpt_set: set, mutrpt_dict, mutrpt_set):
        interset = initrpt_set & mutrpt_set  # Intersection set
        symdiffset = initrpt_set ^ mutrpt_set  # Symmetric Difference set
        cmpmaploc_rptdict = {}
        LOG(LOG_DEBUG, LOG_FUNCINFO(), seed.location, interset, symdiffset)

        if len(interset) > 0:
            # compare whether the parameters of the same constraint are different
            for key_i in interset:
                if len(initrpt_dict[key_i]) != len(mutrpt_dict[key_i]):
                    cmpmaploc_rptdict[key_i] = seed.location
                else:
                    for l_j in range(len(initrpt_dict[key_i])):
                        for larg_k in range(len(initrpt_dict[key_i][l_j].stargs)):
                            if initrpt_dict[key_i][l_j].stargs[larg_k] != mutrpt_dict[key_i][l_j].stargs[larg_k]:
                                cmpmaploc_rptdict[key_i] = seed.location
        if len(symdiffset) > 0:
            for key_i in symdiffset:
                cmpmaploc_rptdict[key_i] = set(seed.location)

        return cmpmaploc_rptdict

    def getNumOfPcguard(self):
        if self.num_pcguard == -1:
            raise Exception("Error: Number of tracks not acquired.")
        return self.num_pcguard

