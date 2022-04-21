#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import ast
import random
import re
import json
from ctypes import *

from fuzzer_module.Fuzzconfig import *

# The operation of Memory Shared.
# 1. Find the memory share id
# ipcs -lm
# ipcs -m
# ipcs -m | grep shmid
# 2. Delete memory share.
# ipcrm -m shmid

# Change the number of SHMMAX (8GB)
# echo "8589934592" > /proc/sys/kernel/shmmax  OR  sysctl -w kernel.shmmax=2147483648
# echo "kernel.shmmax=8589934592" >> /etc/sysctl.conf

class Analyzer:
    def __init__(self):
        self.num_pcguard: int = USE_INITNUM
        self.global_shm_key = USE_INITNUM
        self.addr = None
        self.sendaddr = None
        try:
            self.rt = CDLL('librt.so')
        except:
            self.rt = CDLL('librt.so.1')
        self.shmget = self.rt.shmget
        self.shmget.argtypes = [c_int, c_size_t, c_int]
        self.shmget.restype = c_int

        self.shmat = self.rt.shmat
        self.shmat.argtypes = [c_int, POINTER(c_void_p), c_int]
        self.shmat.restype = c_void_p

    def getNumOfPcguard(self):
        if self.num_pcguard == -1:
            raise Exception("Error: Number of tracks not acquired.")
        return self.num_pcguard

    # Combination Functions
    # getAddr()
    # getInterlen()
    # getRpt()
    # traceAyalysis()

    def getAddr(self, out_info: str):
        """
        Get the memory share address.
        @param out_info:
        @return:
        """
        try:
            re_str = SHMID_FLAG + "(.*?)" + END_EACH_FLAG
            shm_key = int(re.search(re_str, str(out_info)).group(1))
            # print(shm_key)
        except Exception as e:
            raise Exception("Error shm_key {}".format(e))

        LOG(LOG_DEBUG, LOG_FUNCINFO(), shm_key, self.global_shm_key)
        if shm_key != self.global_shm_key:
            self.global_shm_key = shm_key

            shmid = self.shmget(shm_key, ANA_SHM_SIZE, 0o1000 | 0o666)  # 2*1024*1024*1024 2GB
            if shmid < 0:
                raise Exception("Error System not shared.")

            self.addr = self.shmat(shmid, None, 0)

        return self.addr

    def getInterlen(self, addr):
        """
        Get the length of rpt.
        @param addr:
        @return:
        """
        # Get the length of cmpcovshm contents.
        interlen_str = string_at(addr, ANA_INTERLEN_SIZE).decode("utf-8")
        re_str = INTERLEN_FLAG + "(.*?)" + END_EACH_FLAG
        interlen = int(re.search(re_str, interlen_str).group(1))
        return interlen

    def getRpt(self, interlen, addr):
        """
        Get the list of cmp information.
        @param interlen:
        @param addr:
        @return:
        """
        # Read content in pieces
        pieces = interlen // ANA_SHM_INTERVAL
        over = interlen % ANA_SHM_INTERVAL

        cmpcovshm_str = "["
        if pieces > 0:
            cmpcovshm_str += string_at(addr + ANA_INTERLEN_SIZE, ANA_SHM_INTERVAL-ANA_INTERLEN_SIZE).decode("utf-8")
            for each in range(1, pieces):
                cmpcovshm_str += string_at(addr + ANA_SHM_INTERVAL * each, ANA_SHM_INTERVAL).decode("utf-8")
            # fixme .decode("utf-8", "ignore")
            cmpcovshm_str += string_at(addr + ANA_SHM_INTERVAL * pieces, over).decode("utf-8")
        else:
            cmpcovshm_str += string_at(addr + ANA_INTERLEN_SIZE, over-ANA_INTERLEN_SIZE).decode("utf-8")
        cmpcovshm_str += "]"

        # Make the fuzz loop block.
        # self.rt.shmctl(shmid, 0, 0)

        # Content to json
        cmpcov_list = ast.literal_eval(cmpcovshm_str)
        LOG(LOG_DEBUG, LOG_FUNCINFO(), cmpcovshm_str, cmpcov_list)
        del cmpcovshm_str
        return cmpcov_list

    def traceAyalysis(self, cmpcov_list, freezeid_rpt, type_info):
        """
        # Analysis of trace reports generated by documents. memoryTrace
        # Iterate through the trace list to generates the corresponding cmpid dictionary.
        @param cmpcov_list:
        @param freezeid_rpt:
        @param type_info:
        @return:
        """
        cmp_dict = {}  # According cmp instruction to genetator dict.
        for each_i in cmpcov_list:
            if each_i[0] in type_info and each_i[1] not in freezeid_rpt:
                cmpid = each_i[1]
                if cmpid not in cmp_dict:
                    cmp_dict[cmpid] = [each_i[0:1] + each_i[2:]]
                else:
                    cmp_dict[cmpid].append(each_i[0:1] + each_i[2:])
        return cmp_dict

    def traceGuardAyalysis(self, cmpcovcont_list, cmpcov_content, freezeid_rpt, sch: 'Scheduler'):
        """
        Perform a trace of the compare instruction execution path if necessary.
        @param cmpcovcont_list:
        @param cmpcov_content:
        @param freezeid_rpt:
        @param sch:
        @return:
        """
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
                # if cmpid in freezeid_rpt:
                #     continue
            if typeflag == INIT_PC_GUARD:
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
    def compareRptToLoc(self, b4cmp_dict, cmp_dict):
        b4cmpset = set(b4cmp_dict)
        cmpset = set(cmp_dict)
        interset = b4cmpset & cmpset  # Intersection set
        symdiffset = b4cmpset ^ cmpset  # Symmetric Difference set
        diffcmp_set = set()
        LOG(LOG_DEBUG, LOG_FUNCINFO(), interset, symdiffset)

        # Intersection set
        # compare whether the parameters of the same constraint are different.
        # Faster comparisons can be achieved by using arrays instead of structures.
        for key_i in interset:
            if b4cmp_dict[key_i] != cmp_dict[key_i]:
                diffcmp_set.add(key_i)

        # Symmetric Difference set
        for key_i in symdiffset:
            diffcmp_set.add(key_i)

        return diffcmp_set


    def sendCmpid(self, cmpid):
        """
        Send cmpid to save the cmpid information.
        @param cmpid:
        @return:
        """
        if self.sendaddr is None:
            shmid = self.shmget(ANA_SEND_KEY, ANA_SEND_SIZE, 0o1000 | 0o666)  # IPC_CREAT | Permission
            while shmid < 0:
                randkey = random.randint(100000, 999999)
                shmid = self.shmget(randkey, ANA_SEND_SIZE, 0o1000 | 0o666)  # IPC_CREAT | Permission
                with open(ANA_SEND_FILE, "w") as f:
                    f.write(str(randkey))
            self.sendaddr = self.shmat(shmid, None, 0)

        memmove(self.sendaddr, cmpid.encode(), len(cmpid))


if __name__ == "__main__":
    vis = Analyzer()
    while True:
        addr = vis.getAddr("D124816Z\n")
        interlen = vis.getInterlen(addr)
        print(interlen)
        cmpcovshm_list = vis.getRpt(interlen, addr)
    # print(cmpcovshm_list)
