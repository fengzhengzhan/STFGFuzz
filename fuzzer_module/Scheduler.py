#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import random
import re
from queue import Queue
from queue import PriorityQueue

from fuzzer_module.Fuzzconfig import *
from .Structures import *


class Scheduler:
    def __init__(self):
        self.seedq: Queue[StructSeed] = Queue()
        self.mutateq: Queue[StructSeed] = Queue()
        self.importantq: Queue[StructSeed] = Queue()
        self.delq: Queue[StructSeed] = Queue()
        self.delmutq: Queue[StructSeed] = Queue()
        self.strategyq: Queue[StructStrategy] = Queue()

        self.loc_coarse_list: 'list[int]' = []
        self.freeze_bytes = set()
        self.pass_cmp_dict: dict = {}  # Though cmpid, record information with dict

        self.coverage_set = set()

        self.expandnums = 0
        self.expand_size = SCH_EXPAND_SIZE

        self.recunique_crash = set()

        self.file_crash_csv = None
        self.path_crashseeds = None

        self.cur_tgtnum = 0
        self.all_tgtnum = USE_INITNUM
        self.targetcmp_pq = PriorityQueue()
        self.skipcmp_dict = {}

        self.cur_nearlydis = USE_INITMAXNUM

        self.trans_symbol_initguard = {}
        self.trans_func_symbol = {}

        self.target_dict: '{tgtnum:{funcline,funcline}}' = {}
        self.target_crashinfo = []

    def initEachloop(self, vis):
        vis.cmpnum, vis.cmptotal = 0, 0
        self.expand_size *= SCH_EXPAND_MULTI

    '''
    Seed Operation
    '''

    def selectOneSeed(self, mode: int, mutseed=None) -> StructSeed:
        temp_one = None
        if mode == SCH_LOOP_SEED:
            if not self.seedq.empty():
                temp_one = self.seedq.get()
            self.delq.put(temp_one)
        elif mode == SCH_MUT_SEED:
            if not self.mutateq.empty():
                temp_one = self.mutateq.get()
            self.delmutq.put(temp_one)
        elif mode == SCH_THIS_SEED:
            temp_one = mutseed
            self.delq.put(temp_one)
        elif mode == SCH_THISMUT_SEED:
            temp_one = mutseed
            self.delmutq.put(temp_one)

        if temp_one == None:
            raise Exception("Error: seed None.")
        if SCH_SAVEASFILE:
            saveAsFile(temp_one.content, temp_one.filename)

        return temp_one

    def addq(self, mode: int, struct_list: 'list[StructSeed]'):
        for each in struct_list:
            if mode == SCH_LOOP_SEED:
                self.seedq.put(each)
            elif mode == SCH_MUT_SEED:
                self.mutateq.put(each)

    def deleteSeeds(self, mode):
        """
        Delete mutated intermediate files.
        @return:
        """
        if mode == SCH_THIS_SEED:
            while not self.delq.empty():
                temp_one = self.delq.get()
                if SCH_SAVEASFILE:
                    try:
                        os.remove(temp_one.filename)
                    except Exception as e:
                        pass
        elif mode == SCH_THISMUT_SEED:
            while not self.delmutq.empty():
                temp_one = self.delmutq.get()
                if SCH_SAVEASFILE:
                    try:
                        os.remove(temp_one.filename)
                    except Exception as e:
                        pass

    def saveCrash(self, seed: StructSeed, stdout, stderr, vis):
        """
        To facilitate analysis, save all the crash seed information in a csv file
        @return:
        """
        tgtsan = False
        if self.file_crash_csv != None and self.path_crashseeds != None:
            path, name = os.path.split(seed.filename)
            if not os.path.exists(self.path_crashseeds + name) and len(stderr) != 0:
                try:
                    re_str = "==ERROR: (.*?): "
                    crashtype = re.search(re_str, str(stderr)).group(1)
                    if crashtype in SCH_SKIPCRASH_SET:
                        return tgtsan
                    re_str = "#0 (.*?) in"
                    crashid = re.search(re_str, str(stderr)).group(1)
                    # Compare sanitizer similarity
                    re_str = "#(.*?) 0x.*? in (.*?) .*?:(.*?):"
                    re_cont = re.findall(re_str, str(stderr))
                    LOG(DEBUG, LOC(), crashtype, crashid, re_cont, show=True)
                    cinfo_num = 0
                    crash_infostr = ""
                    for c in re_cont:
                        LOG(DEBUG, LOC(), delBrackets(c[1]) + c[2], self.target_dict[self.cur_tgtnum])
                        if delBrackets(c[1]) + c[2] in self.target_dict[self.cur_tgtnum]:
                            crash_infostr += delBrackets(c[1]) + ":" + c[2] + " >> "
                            cinfo_num += 1

                    LOG(DEBUG, LOC(), len(self.target_dict[self.cur_tgtnum]))
                    # fixme set value can not fixed.
                    if 'greybox0' not in self.target_dict[self.cur_tgtnum] and len(
                            self.target_dict[self.cur_tgtnum]) - cinfo_num <= SCH_CRASH_SIMI:
                        tgtsan = True
                        # self.cur_tgtnum += 1
                        self.target_crashinfo.append(crash_infostr)
                    LOG(DEBUG, LOC(), tgtsan, self.cur_tgtnum)
                except Exception as e:
                    crashid = str(stderr)[-16:-3]  #

                if crashid not in self.recunique_crash:
                    vis.crash_num += 1
                    vis.last_crash_time = vis.last_time
                    self.recunique_crash.add(crashid)
                    # write csv
                    with open(self.file_crash_csv, "a+", encoding="utf-8") as cf:
                        # GEN_CSV_HEADERS = "filename,time,duration,content,stdout,stderr\n"
                        linestr = str(name) + "," \
                                  + datetime.datetime.strftime(vis.start_time, "%Y-%m-%d_%H:%M:%S") + "," \
                                  + vis.last_time + "," + str(seed.content).replace(',', 'comma') + "," \
                                  + str(stdout).replace(',', 'comma') + "," \
                                  + str(stderr).replace(',', 'comma') + ",,,\n"
                        cf.write(linestr)
                    # write seed
                    saveAsFile(seed.content, self.path_crashseeds + name)
        else:
            raise Exception(LOC() + "Error Path")

        return tgtsan

    def quitFuzz(self):
        self.deleteSeeds(SCH_THIS_SEED)
        self.deleteSeeds(SCH_THISMUT_SEED)
        sys.exit(0)

    '''
    Cmp Operation
    '''

    def extensionLocation(self, location, cmp_len):
        exloc_list = []
        exloc_list.append(location)
        for outside in range(1, SCH_EXLOC + 1):

            left_side = location - outside
            if 0 <= left_side < cmp_len:
                exloc_list.append(left_side)

            right_side = location + outside
            if 0 <= right_side < cmp_len:
                exloc_list.append(right_side)

        # exloc_list.sort()
        return exloc_list

    def updateGuardSymbol(self, guardcov_list):
        # Iterate through the trace report to get the corresponding information
        for trace_i in guardcov_list:
            trace = trace_i[1:]
            if trace[IDX_CMPTYPE] == EACH_PC_GUARD:
                guard_num = int(trace[1])
                guard_funcname = delBrackets(trace[2])
                # Map execute function name to symbol function name.
                if guard_funcname not in self.trans_func_symbol:
                    for bin_kj in self.trans_symbol_initguard.keys():
                        if guard_funcname == bin_kj:
                            self.trans_func_symbol[guard_funcname] = bin_kj
                            break
                        else:
                            findres = bin_kj.find(guard_funcname)
                            if findres != -1:
                                self.trans_func_symbol[guard_funcname] = bin_kj

                # Change guard start number from symbol function name which use execute function name map it.
                if guard_funcname in self.trans_func_symbol:
                    if guard_num < self.trans_symbol_initguard[self.trans_func_symbol[guard_funcname]]:
                        self.trans_symbol_initguard[self.trans_func_symbol[guard_funcname]] = guard_num

    def selectConstraint(self, guardcov_list, map_tgtpredgvid_dis, tgtpred_offset, trans_guard_gvid, vis):
        """
        Perform a trace of the compare instruction execution path if necessary.
        """
        LOG(DEBUG, LOC(), map_tgtpredgvid_dis, trans_guard_gvid)

        # If map location is empty, then first to run it to collect information.
        # If map is not empty, then run it when can not find in map.
        if len(self.trans_func_symbol) == 0 or len(self.trans_symbol_initguard) == 0:
            self.updateGuardSymbol(guardcov_list)

        # Update vis.trace_orderdict trace information
        # vis.trace_orderdict[self.cur_tgtnum]

        # Select compare and add it to priority queue.
        # According target number to determine the direction of mutation.
        map_curtgtpredgvid_dis = map_tgtpredgvid_dis[self.cur_tgtnum]
        disdup_cmpiddict = {}
        if len(map_curtgtpredgvid_dis) == 0:  # Greybox
            for trace_i in guardcov_list:
                cmpid = trace_i[0]
                cmptype = trace_i[1]
                if cmptype in CMPSET:
                    if cmpid not in disdup_cmpiddict:
                        disdup_cmpiddict[cmpid] = 0
                    else:
                        disdup_cmpiddict[cmpid] += 1
                    self.targetcmp_pq.put((random.randint(0, LIMITER), cmpid, disdup_cmpiddict[cmpid]))

        else:  # Directed
            curtgtpred_offset = tgtpred_offset[self.cur_tgtnum]
            LOG(DEBUG, LOC(), map_curtgtpredgvid_dis)
            distance = USE_INITMAXNUM

            for trace_i in guardcov_list:
                LOG(DEBUG, LOC(), trace_i)
                cmpid = trace_i[0]
                cmptype = trace_i[1]
                if cmptype == EACH_PC_GUARD:
                    # pc_guard to update the Calibration Distance.
                    realguard = trace_i[2]
                    func = delBrackets(trace_i[3])
                    # According offset to determine the distance.
                    if func not in curtgtpred_offset:
                        continue
                    # Lazy to update
                    if func not in self.trans_func_symbol:
                        self.updateGuardSymbol(guardcov_list)
                    # Get the static symbol function name.
                    # todo Symbol inconsistency  file_strncmp<->file_strncmp16
                    symbol = self.trans_func_symbol[func]
                    LOG(DEBUG, LOC(), func, symbol, self.trans_func_symbol)
                    if symbol not in trans_guard_gvid:
                        continue

                    # Transform the pc_guard to sub the value.
                    transguard = int(realguard) - self.trans_symbol_initguard[symbol]
                    LOG(DEBUG, LOC(), trace_i, symbol, transguard, trans_guard_gvid[symbol],
                        self.trans_symbol_initguard[symbol])
                    if transguard not in trans_guard_gvid[symbol]:
                        continue
                    # Get the networkx node gvid to get it.
                    gvid = trans_guard_gvid[symbol][transguard]
                    if symbol in map_curtgtpredgvid_dis and gvid in map_curtgtpredgvid_dis[symbol]:
                        # Set distance for priority queue.
                        distance = curtgtpred_offset[symbol] + map_curtgtpredgvid_dis[symbol][gvid]
                        # Update visualizer's trace_orderdict
                        # print(vis.trace_orderdict[self.cur_tgtnum])
                        if symbol in vis.trace_orderdict[self.cur_tgtnum]:
                            vis.trace_orderdict[self.cur_tgtnum][symbol][2] = \
                                min(vis.trace_orderdict[self.cur_tgtnum][symbol][2],
                                    map_curtgtpredgvid_dis[symbol][gvid])
                    elif symbol in map_curtgtpredgvid_dis and gvid not in map_curtgtpredgvid_dis[symbol]:
                        distance = USE_INITMAXNUM
                    LOG(DEBUG, LOC(), trace_i, symbol, transguard, gvid, distance)
                else:
                    # func, realguard, cmpnum = trace_i[2].split("+")
                    # if func == '':
                    #     continue

                    if cmpid not in disdup_cmpiddict:
                        disdup_cmpiddict[cmpid] = 0
                    else:
                        disdup_cmpiddict[cmpid] += 1
                    # if distance != USE_INITMAXNUM and cmpid not in disdup_cmpiddict:
                    if distance != USE_INITMAXNUM:
                        # The smaller the distance, the higher the priority.
                        # self.target_cmp.put((distance - vis.loop, cmpid))
                        vis.cur_min_dis = min(vis.cur_min_dis, distance)
                        if distance <= LIMITER:
                            self.targetcmp_pq.put((distance, cmpid, disdup_cmpiddict[cmpid]))
                        LOG(DEBUG, LOC(), distance - vis.loop, cmpid, trace_i)
            LOG(DEBUG, LOC(), map_tgtpredgvid_dis, self.trans_symbol_initguard)
            LOG(DEBUG, LOC(), tgtpred_offset, trans_guard_gvid)
            del disdup_cmpiddict

    def selectBranch(self):
        pass

    def findNearDistance(self, trace_guard_list, map_tgtpredgvid_dis, tgtpred_offset, map_guard_gvid):
        """
        From pc_guard set find the BFS location.
        @return:
        """
        near_dis = USE_INITMAXNUM

        if self.cur_tgtnum not in map_tgtpredgvid_dis or len(map_tgtpredgvid_dis[self.cur_tgtnum]) == 0:
            near_dis = USE_INITNUM
        else:
            # pc_guard numbers.
            map_curtgtpredgvid_dis = map_tgtpredgvid_dis[self.cur_tgtnum]
            trace_guard_set = set(trace_guard_list)
            self.coverage_set = self.coverage_set | trace_guard_set
            curtgtpred_offset = tgtpred_offset[self.cur_tgtnum]
            reverseto_gvid_guard = {}
            for func_ki, map_kj in map_guard_gvid.items():
                reverseto_gvid_guard[func_ki] = {v: k for k, v in map_kj.items()}

            # Traverse to find the shortest distance.
            for func_ki, disdict_vi in map_curtgtpredgvid_dis.items():
                for gvid_kj, dis_vj in disdict_vi.items():
                    # If pc_guard in trace_guard dynamic, then update it to near_dis.
                    if reverseto_gvid_guard[func_ki][gvid_kj] in trace_guard_set:
                        distance = curtgtpred_offset[func_ki] + dis_vj
                        near_dis = min(near_dis, distance)

        return near_dis

    '''
    Scheduler constraint.
    '''

    def skipInvalidState(self, stcmpid, cmpmaploc_dict):
        ret_flag = False
        # Cyclic independent comparison
        # Invalid compare instruction.
        if stcmpid in self.skipcmp_dict and self.skipcmp_dict[stcmpid] >= SCH_SKIP_COUNT:
            ret_flag = True

        # Length of location
        # len(cmpmaploc_dict[stcmpid_ki]) == len(init_seed.content)
        if stcmpid not in cmpmaploc_dict:
            ret_flag = True
        elif len(cmpmaploc_dict[stcmpid]) > SCH_SKIP_LEN:
            ret_flag = True

        return ret_flag

    def updateInvalidCmp(self, stcmpid):
        if stcmpid not in self.skipcmp_dict:
            self.skipcmp_dict[stcmpid] = 1
        else:
            self.skipcmp_dict[stcmpid] += 1

    def clearInvalidCmp(self, stcmpid):
        if stcmpid in self.skipcmp_dict:
            self.skipcmp_dict[stcmpid] = 0
