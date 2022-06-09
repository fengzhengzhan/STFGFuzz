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
        self.shm_key = USE_INITNUM
        self.addr = None
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

    # Combination Functions
    # getAddr()
    # getInterlen()
    # getRpt()
    # traceAyalysis()

    def getShm(self, out_info: str):
        """
        Get the memory share address.
        """
        try:
            re_str = SHMID_FLAG + "(.*?)" + END_EACH_FLAG
            shm_key = int(re.search(re_str, str(out_info)).group(1))
            # print(shm_key)
        except Exception as e:
            shm_key = 124816
            # if self.shm_key == USE_INITNUM:
            #     raise Exception("Error shm_key {}".format(e))

        LOG(LOG_DEBUG, LOG_FUNCINFO(), shm_key, self.shm_key)
        if shm_key != self.shm_key:
            self.shm_key = shm_key

            shmid = self.shmget(shm_key, ANA_SHM_SIZE, 0o1000 | 0o666)  # 2*1024*1024*1024 2GB
            if shmid < 0:
                raise Exception("Error System not shared.")

            self.addr = self.shmat(shmid, None, 0)

        # Get the length of cmpcovshm contents.
        LOG(LOG_DEBUG, LOG_FUNCINFO(), out_info, self.addr)
        interlen_str = string_at(self.addr + ANA_FILTER_SIZE, ANA_INTERLEN_SIZE).decode("utf-8")
        re_str = INTERLEN_FLAG + "(.*?)" + END_EACH_FLAG
        interlen = int(re.search(re_str, interlen_str).group(1))

        covernum_str = string_at(self.addr + ANA_FILTER_SIZE + ANA_INTERLEN_SIZE, ANA_COVERNUM_SIZE).decode("utf-8")
        re_str = COVERAGE_NUM + "(.*?)" + END_EACH_FLAG
        covernum = int(re.search(re_str, covernum_str).group(1))
        return interlen, covernum

    def sendCmpid(self, cmpid):
        """
        Send cmpid to save the cmpid information.
        @param cmpid:
        @return:
        """
        if self.addr is None:
            raise Exception("Error Memory share space not create.")

        cmpid = str(cmpid) + "\0"
        memmove(self.addr, cmpid.encode(), len(cmpid))

    def getRpt(self, interlen):
        """
        Get the list of cmp information.
        @param interlen:
        @return:
        """
        # Read content in pieces
        pieces = interlen // ANA_SHM_INTERVAL
        over = interlen % ANA_SHM_INTERVAL

        # print(string_at(self.addr+128+16, 4096))
        cmpcovshm_str = "["
        if pieces > 0:
            cmpcovshm_str += string_at(self.addr + ANA_START_SIZE, ANA_SHM_INTERVAL - ANA_START_SIZE) \
                .decode("utf-8", "ignore")
            for each in range(1, pieces):
                cmpcovshm_str += string_at(self.addr + ANA_SHM_INTERVAL * each, ANA_SHM_INTERVAL) \
                    .decode("utf-8", "ignore")
            # fixme .decode("utf-8", "ignore")
            cmpcovshm_str += string_at(self.addr + ANA_SHM_INTERVAL * pieces, over).decode("utf-8", "ignore")
        else:
            cmpcovshm_str += string_at(self.addr + ANA_START_SIZE, over - ANA_START_SIZE).decode("utf-8", "ignore")
        cmpcovshm_str += "]"

        # Make the fuzz loop block.
        # self.rt.shmctl(shmid, 0, 0)

        # Content to json
        # LOG(LOG_DEBUG, LOG_FUNCINFO(), cmpcovshm_str, showlog=True)
        cmpcov_list = ast.literal_eval(cmpcovshm_str)
        del cmpcovshm_str
        return cmpcov_list

    def traceAyalysis(self, cmpcov_list, freezeid_rpt):
        """
        # Analysis of trace reports generated by documents. memoryTrace
        # Iterate through the trace list to generates the corresponding cmpid dictionary.
        @param cmpcov_list:
        @param freezeid_rpt:
        @return:
        """
        cmp_dict = {}  # According cmp instruction to genetator dict.
        for each_i in cmpcov_list:
            if each_i[IDX_CMPTYPE + 1] in FLAG_DICT and each_i[IDX_CMPID] not in freezeid_rpt:
                cmpid = each_i[IDX_CMPID]
                if cmpid not in cmp_dict:
                    cmp_dict[cmpid] = [each_i[1:]]
                else:
                    cmp_dict[cmpid].append(each_i[1:])
        return cmp_dict

    def getGuardNum(self, guardcov_list):
        """
        Get all pc_guard numbers.
        """
        guard_set = set()
        guard_total = USE_INITNUM
        for trace_i in guardcov_list:
            trace = trace_i[1:]
            if trace[IDX_CMPTYPE] == EACH_PC_GUARD:
                guard_set.add(trace[1])
            elif trace[IDX_CMPTYPE] == INIT_PC_GUARD:
                guard_total = trace[2]
        return guard_set, guard_total

    def updateGuardSymbol(self, guardcov_list, sch):
        # Iterate through the trace report to get the corresponding information
        for trace_i in guardcov_list:
            trace = trace_i[1:]
            if trace[IDX_CMPTYPE] == EACH_PC_GUARD:
                guard_funcname = delBrackets(trace[1])
                guard_num = trace[2]
                # Map execute function name to symbol function name.
                if guard_funcname not in sch.map_functo_symbol:
                    for bin_kj in sch.map_functo_guard.keys():
                        findres = bin_kj.find(guard_funcname)
                        if findres != -1:
                            sch.map_functo_symbol[guard_funcname] = bin_kj

                # Change guard start number from symbol function name which use execute function name map it.
                if guard_funcname in sch.map_functo_symbol:
                    if guard_num < sch.map_functo_guard[sch.map_functo_symbol[guard_funcname]]:
                        sch.map_functo_guard[sch.map_functo_symbol[guard_funcname]] = guard_num

    def traceGuardAnalysis(self, guardcov_list, sch):
        """
        Perform a trace of the compare instruction execution path if necessary.
        """
        if len(sch.map_functo_symbol) == 0 or len(sch.map_functo_guard) == 0:
            self.updateGuardSymbol(guardcov_list, sch)




        LOG(LOG_DEBUG, LOG_FUNCINFO(), sch.map_functo_symbol, sch.map_functo_guard, showlog=True)
        return

    '''
    Tracking Comparison Module.
    '''

    def compareRptToLoc(self, b4cmp_dict, cmp_dict):
        b4cmpset = set(b4cmp_dict)
        cmpset = set(cmp_dict)
        interset = b4cmpset & cmpset  # Intersection set
        # symdiffset = b4cmpset ^ cmpset  # Symmetric Difference set
        symdiffset = cmpset - b4cmpset  # Symmetric Difference set
        diffcmp_set = set()
        LOG(LOG_DEBUG, LOG_FUNCINFO(), interset, symdiffset)

        # Intersection set
        # compare whether the parameters of the same constraint are different.
        # Faster comparisons can be achieved by using arrays instead of structures.
        for key_i in interset:
            if len(b4cmp_dict[key_i]) != len(cmp_dict[key_i]):
                diffcmp_set.add(key_i)
            else:
                for idx in range(0, len(b4cmp_dict[key_i])):
                    if b4cmp_dict[key_i][idx][IDX_ARG:] != cmp_dict[key_i][idx][IDX_ARG:]:
                        diffcmp_set.add(key_i)
                        break

        # Symmetric Difference set
        for key_i in symdiffset:
            diffcmp_set.add(key_i)

        return diffcmp_set

    def compareRptDiff(self, b4_cmpcov_list, cmpcov_list, pos: int):
        """
        @return: Same or cmpcov_list==null is False, Different is True.
        """
        if len(cmpcov_list) == 0:
            return False
        if pos == -1:
            if b4_cmpcov_list != cmpcov_list:
                return True
        else:
            if pos < len(b4_cmpcov_list) and pos < len(cmpcov_list) \
                    and b4_cmpcov_list[pos] != cmpcov_list[pos]:
                return True
        return False


if __name__ == "__main__":
    ana = Analyzer()
    ana.getShm("D124816Z\n")

    # ana.sendCmpid("abcde")
    # ana.sendCmpid("None")
    ana.sendCmpid("Guard")
    # ana.sendCmpid("m0x49e319")
    # while True:
    #     addr = ana.getAddr("D124816Z\n")
    #     interlen = ana.getInterlen(addr)
    #     print(interlen)
    #     cmpcovshm_list = ana.getRpt(interlen, addr)
    interlen, covernum = ana.getShm("D124816Z\n")
    print(interlen, covernum)
    cmpcovshm_list = ana.getRpt(interlen)
    with open("../Programs/TrackCrash/crashinfo/info", "w") as f:
        f.write(str(cmpcovshm_list))
    # print(cmpcovshm_list)
    print(interlen, covernum)
    # print(cmpcovshm_list)
