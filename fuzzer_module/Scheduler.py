#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import re
from queue import Queue

from fuzzer_module.Fuzzconfig import *


class Scheduler:
    def __init__(self):
        self.seedq: Queue[StructSeed] = Queue(maxsize=0)
        self.mutateq: Queue[StructSeed] = Queue(maxsize=0)
        self.importantq: Queue[StructSeed] = Queue(maxsize=0)
        self.delq: Queue[StructSeed] = Queue(maxsize=0)
        self.delmutq: Queue[StructSeed] = Queue(maxsize=0)
        self.strategyq: Queue[StructStrategy] = Queue(maxsize=0)

        self.loc_coarse_list: 'list[int]' = []
        self.slid_window: int = SCH_SLID_WINDOW
        self.freeze_bytes = set()
        self.skip_cmpidset = set()  # freeze or ignore

        self.coverage_path = set()

        self.expandnums = 0
        self.expand_size = SCH_EXPAND_SIZE

        self.recunique_crash = set()
        self.recsol_cmpset = set()  # Record data, do not use

        self.file_crash_csv = None
        self.path_crashseeds = None

        self.cur_target = 0
        self.all_target = USE_INITNUM

        self.map_functo_guard = {}
        self.map_functo_symbol = {}

    def initEachloop(self, vis):
        self.loc_coarse_list = []
        self.slid_window = SCH_SLID_WINDOW
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

    def saveCrash(self, seed: StructSeed, stdout, stderr, start_time, last_time):
        """
        To facilitate analysis, save all the crash seed information in a csv file
        @return:
        """
        if self.file_crash_csv != None and self.path_crashseeds != None:
            path, name = os.path.split(seed.filename)
            if not os.path.exists(self.path_crashseeds + name) and len(stderr) != 0:
                try:
                    re_str = "#0 (.*?) in"
                    crashid = re.search(re_str, str(stderr)).group(1)
                except Exception as e:
                    crashid = str(stderr)[-16:-3]  #
                if crashid not in self.recunique_crash:
                    self.recunique_crash.add(crashid)
                    # write csv
                    with open(self.file_crash_csv, "a+", encoding="utf-8") as cf:
                        # GEN_CSV_HEADERS = "filename,time,duration,content,stdout,stderr\n"
                        linestr = str(name) + "," + datetime.datetime.strftime(start_time, "%Y-%m-%d_%H:%M:%S") + "," \
                                  + last_time + "," + str(seed.content).replace(',', 'comma') + "," \
                                  + str(stdout).replace(',', 'comma') + "," + str(stderr).replace(',',
                                                                                                  'comma') + ",,,\n"
                        cf.write(linestr)
                    # write seed
                    saveAsFile(seed.content, self.path_crashseeds + name)
        else:
            raise Exception(LOG_FUNCINFO() + "Error Path")

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
                guard_funcname = delBrackets(trace[1])
                guard_num = trace[2]
                # Map execute function name to symbol function name.
                if guard_funcname not in self.map_functo_symbol:
                    for bin_kj in self.map_functo_guard.keys():
                        findres = bin_kj.find(guard_funcname)
                        if findres != -1:
                            self.map_functo_symbol[guard_funcname] = bin_kj

                # Change guard start number from symbol function name which use execute function name map it.
                if guard_funcname in self.map_functo_symbol:
                    if guard_num < self.map_functo_guard[self.map_functo_symbol[guard_funcname]]:
                        self.map_functo_guard[self.map_functo_symbol[guard_funcname]] = guard_num

    def selectConstraint(self, guardcov_list, map_functo_tgtguard, map_tgtpredgvid_dis):
        """
        Perform a trace of the compare instruction execution path if necessary.
        """
        # If map location is empty, then first to run it to collect information.
        # If map is not empty, then run it when can not find in map.
        if len(self.map_functo_symbol) == 0 or len(self.map_functo_guard) == 0:
            self.updateGuardSymbol(guardcov_list)

        # Select compare and add it to priority queue.
        # According target number to determine the direction of mutation.
        maptgt_functo_tgtguard = map_functo_tgtguard[self.cur_target]
        maptgt_tgtpredgvid_dis = map_tgtpredgvid_dis[self.cur_target]

        LOG(LOG_DEBUG, LOG_FUNCINFO(), maptgt_functo_tgtguard, maptgt_tgtpredgvid_dis, showlog=True)

        LOG(LOG_DEBUG, LOG_FUNCINFO(), self.map_functo_symbol, self.map_functo_guard, showlog=True)
        return {}
