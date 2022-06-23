#!/usr/bin/env python3
# -*- coding: utf-8 -*-
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
        self.slid_window: int = SCH_SLID_COUNT
        self.freeze_bytes = set()
        self.pass_cmp_dict:dict = {}  # Though cmpid, record information with dict

        self.coverage_set = set()

        self.expandnums = 0
        self.expand_size = SCH_EXPAND_SIZE

        self.recunique_crash = set()

        self.file_crash_csv = None
        self.path_crashseeds = None

        self.cur_tgtnum = 0
        self.all_tgtnum = USE_INITNUM
        self.targetcmp_pq = PriorityQueue()

        self.cur_nearlydis = USE_INITMAXNUM

        self.trans_symbol_initguard = {}
        self.trans_func_symbol = {}

        self.target_dict:'{tgtnum:{funcline,funcline}}' = {}
        self.target_crashinfo = []

    def initEachloop(self, vis):
        self.loc_coarse_list = []
        self.slid_window = SCH_SLID_COUNT
        self.mutlocnums = 0
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
                    re_str = "#0 (.*?) in"
                    crashid = re.search(re_str, str(stderr)).group(1)
                    # Compare sanitizer similarity
                    re_str = "#(.*?) 0x.*? in (.*?) .*?:(.*?):"
                    re_cont = re.findall(re_str, str(stderr))
                    LOG(LOG_DEBUG, LOG_FUNCINFO(), re_cont, showlog=True)
                    cinfo_num = 0
                    crash_infostr = ""
                    for c in re_cont:
                        LOG(LOG_DEBUG, LOG_FUNCINFO(), delBrackets(c[1])+c[2], self.target_dict[self.cur_tgtnum], showlog=True)
                        if delBrackets(c[1])+c[2] in self.target_dict[self.cur_tgtnum]:
                            crash_infostr += delBrackets(c[1])+c[2] + " -> "
                            cinfo_num += 1

                    LOG(LOG_DEBUG, LOG_FUNCINFO(), cinfo_num, len(self.target_dict[self.cur_tgtnum]), showlog=True)
                    if len(self.target_dict[self.cur_tgtnum]) - cinfo_num < SCH_CRASH_SIMI:
                        tgtsan = True
                        self.cur_tgtnum += 1
                        self.target_crashinfo.append(crash_infostr)
                    LOG(LOG_DEBUG, LOG_FUNCINFO(), tgtsan, self.cur_tgtnum, showlog=True)
                except Exception as e:
                    crashid = str(stderr)[-16:-3]  #

                if crashid not in self.recunique_crash:
                    vis.crash_num += 1
                    vis.last_crash_time = vis.last_time
                    self.recunique_crash.add(crashid)
                    # write csv
                    with open(self.file_crash_csv, "a+", encoding="utf-8") as cf:
                        # GEN_CSV_HEADERS = "filename,time,duration,content,stdout,stderr\n"
                        linestr = str(name) + "," + datetime.datetime.strftime(vis.start_time, "%Y-%m-%d_%H:%M:%S") + "," \
                                  + vis.last_time + "," + str(seed.content).replace(',', 'comma') + "," \
                                  + str(stdout).replace(',', 'comma') + "," + str(stderr).replace(',',
                                                                                                  'comma') + ",,,\n"
                        cf.write(linestr)
                    # write seed
                    saveAsFile(seed.content, self.path_crashseeds + name)
        else:
            raise Exception(LOG_FUNCINFO() + "Error Path")

        return tgtsan

    def quitFuzz(self):
        self.deleteSeeds(SCH_THIS_SEED)
        self.deleteSeeds(SCH_THISMUT_SEED)
        sys.exit(0)

    '''
    Cmp Operation
    '''

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
        LOG(LOG_DEBUG, LOG_FUNCINFO(), map_tgtpredgvid_dis, trans_guard_gvid)
        # If map location is empty, then first to run it to collect information.
        # If map is not empty, then run it when can not find in map.
        if len(self.trans_func_symbol) == 0 or len(self.trans_symbol_initguard) == 0:
            self.updateGuardSymbol(guardcov_list)

        # Update vis.trace_orderdict trace information
        # vis.trace_orderdict[self.cur_tgtnum]

        # Select compare and add it to priority queue.
        # According target number to determine the direction of mutation.
        curtgtpred_offset = tgtpred_offset[self.cur_tgtnum]
        map_curtgtpredgvid_dis = map_tgtpredgvid_dis[self.cur_tgtnum]
        LOG(LOG_DEBUG, LOG_FUNCINFO(), map_curtgtpredgvid_dis)
        distance = USE_INITMAXNUM
        disdup_cmpidset = set()

        for trace_i in guardcov_list:
            LOG(LOG_DEBUG, LOG_FUNCINFO(), trace_i)
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
                symbol = self.trans_func_symbol[func]
                if symbol not in trans_guard_gvid:
                    continue

                # Transform the pc_guard to sub the value.
                transguard = int(realguard) - self.trans_symbol_initguard[symbol]
                LOG(LOG_DEBUG, LOG_FUNCINFO(), trace_i, symbol, transguard, trans_guard_gvid[symbol], self.trans_symbol_initguard[symbol])
                if transguard not in trans_guard_gvid[symbol]:
                    continue
                # Get the networkx node gvid to get it.
                gvid = trans_guard_gvid[symbol][transguard]
                if symbol in map_curtgtpredgvid_dis and gvid in map_curtgtpredgvid_dis[symbol]:
                    # Set distance for priority queue.
                    distance = curtgtpred_offset[symbol] + map_curtgtpredgvid_dis[symbol][gvid]
                    # Update visualizer's trace_orderdict
                    # print(vis.trace_orderdict[self.cur_tgtnum])
                    if str(symbol) in vis.trace_orderdict[self.cur_tgtnum]:
                        vis.trace_orderdict[self.cur_tgtnum][symbol][2] = \
                            min(vis.trace_orderdict[self.cur_tgtnum][symbol][2], map_curtgtpredgvid_dis[symbol][gvid])
                elif symbol in map_curtgtpredgvid_dis and gvid not in map_curtgtpredgvid_dis[symbol]:
                    distance = USE_INITMAXNUM
                LOG(LOG_DEBUG, LOG_FUNCINFO(), trace_i, symbol, transguard, gvid, distance)
            else:
                # func, realguard, cmpnum = trace_i[2].split("+")
                # if func == '':
                #     continue
                if distance != USE_INITMAXNUM and cmpid not in disdup_cmpidset:
                    # The smaller the distance, the higher the priority.
                    # self.target_cmp.put((distance - vis.loop, cmpid))
                    vis.cur_min_dis = min(vis.cur_min_dis, distance)
                    self.targetcmp_pq.put((distance, cmpid))
                    disdup_cmpidset.add(cmpid)
                    LOG(LOG_DEBUG, LOG_FUNCINFO(), distance-vis.loop, cmpid, trace_i)
        LOG(LOG_DEBUG, LOG_FUNCINFO(), map_tgtpredgvid_dis, self.trans_symbol_initguard, showlog=True)
        LOG(LOG_DEBUG, LOG_FUNCINFO(), tgtpred_offset, trans_guard_gvid, showlog=True)
        del disdup_cmpidset


    def selectBranch(self):
        pass

    def findNearDistance(self, trace_guard_list, map_tgtpredgvid_dis, tgtpred_offset, map_guard_gvid):
        """
        From pc_guard set find the BFS location.
        @return:
        """
        near_dis = USE_INITMAXNUM
        trace_guard_set = set(trace_guard_list)
        self.coverage_set = self.coverage_set | trace_guard_set
        map_curtgtpredgvid_dis = map_tgtpredgvid_dis[self.cur_tgtnum]
        curtgtpred_offset = tgtpred_offset[self.cur_tgtnum]
        reverseto_gvid_guard = {}
        for func_ki, map_kj in map_guard_gvid.items():
            reverseto_gvid_guard[func_ki] = {v: k for k, v in map_kj.items()}

        # Traverse to find the shortest distance.
        for func_ki, disdict_vi in map_curtgtpredgvid_dis.items():
            for gvid_kj, dis_vj in disdict_vi.items():
                if reverseto_gvid_guard[func_ki][gvid_kj] in trace_guard_set:
                    distance = curtgtpred_offset[func_ki] + dis_vj
                    near_dis = min(near_dis, distance)

        return near_dis


