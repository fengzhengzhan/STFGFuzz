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
        self.deleteq: Queue[StructSeed] = Queue(maxsize=0)
        self.strategyq: Queue[StructStrategy] = Queue(maxsize=0)

        self.loc_coarse_list: 'list[int]' = []
        self.slid_window: int = SCH_SLID_WINDOW
        self.freeze_bytes = set()
        self.skip_cmpidset = set()  # freeze or ignore

        self.coveragepath = set()

        self.expandnums = 0
        self.expand_size = SCH_EXPAND_SIZE

        self.recunique_crash = set()
        self.recsol_cmpset = set()  # Record data, do not use

        self.file_crash_csv = None
        self.path_crashseeds = None

    def initEachloop(self, vis):
        self.loc_coarse_list = []
        self.slid_window = SCH_SLID_WINDOW
        self.mutlocnums = 0
        vis.cmpnum, vis.cmptotal = 0, 0
        self.expand_size *= SCH_EXPAND_MULTI

    def selectOneSeed(self, mode: int, mutseed=None) -> StructSeed:
        temp_one = None
        if mode == SCH_LOOP_SEED:
            if not self.seedq.empty():
                temp_one = self.seedq.get()
        elif mode == SCH_MUT_SEED:
            if not self.mutateq.empty():
                temp_one = self.mutateq.get()
        elif mode == SCH_THIS_SEED:
            temp_one = mutseed

        if temp_one == None:
            raise Exception("Error: seed None.")
        if SCH_SAVEASFILE:
            saveAsFile(temp_one.content, temp_one.filename)
        self.addDeleteq(temp_one)
        return temp_one

    def addq(self, mode: int, struct_list: 'list[StructSeed]'):
        for each in struct_list:
            if mode == SCH_LOOP_SEED:
                self.seedq.put(each)
            elif mode == SCH_MUT_SEED:
                self.mutateq.put(each)

    def addDeleteq(self, temp_one):
        self.deleteq.put(temp_one)

    def deleteSeeds(self):
        """
        Delete mutated intermediate files.
        @return:
        """
        while not self.deleteq.empty():
            temp_one = self.deleteq.get()
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
                                  + str(stdout).replace(',', 'comma') + "," + str(stderr).replace(',', 'comma') + ",\n"
                        cf.write(linestr)
                    # write seed
                    saveAsFile(seed.content, self.path_crashseeds + name)
        else:
            raise Exception(LOG_FUNCINFO() + "Error Path")

    def quitFuzz(self):
        self.deleteSeeds()
        sys.exit(0)
