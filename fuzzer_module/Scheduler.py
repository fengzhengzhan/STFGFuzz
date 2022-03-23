import os
from queue import Queue

from fuzzer_module.Fuzzconfig import *


class Scheduler:
    def __init__(self):
        self.seedq: Queue[StructSeed] = Queue(maxsize=0)
        self.locCoarseq: Queue[int] = Queue(maxsize=0)
        self.locFineq: Queue[int] = Queue(maxsize=0)
        self.slidWindow: int = SCH_SLID_WINDOW
        self.freezebytes: dict = {}
        self.mutateTestq: Queue[StructSeed] = Queue(maxsize=0)
        self.importantq: Queue[StructSeed] = Queue(maxsize=0)
        self.deleteq: Queue[StructSeed] = Queue(maxsize=0)


    def selectOneSeed(self, mode: int) -> StructSeed:
        if mode == SCH_INIT_SEED:
            temp_one = self.seedq.get()
        elif mode == SCH_MUT_SEED:
            temp_one = self.mutateTestq.get()
        else:
            raise Exception("Error: mode type.")
        self.addDeleteq(temp_one)
        return temp_one

    def addSeeds(self, mode: int, structseed_list: 'list[StructSeed]'):
        for each in structseed_list:
            if mode == SCH_INIT_SEED:
                self.seedq.put(each)
            elif mode == SCH_MUT_SEED:
                self.mutateTestq.put(each)

    def isEmpty(self, mode) -> bool:
        temp_flag = False
        if mode == SCH_INIT_SEED:
            temp_flag = self.seedq.empty()
        elif mode == SCH_MUT_SEED:
            temp_flag = self.mutateTestq.empty()
        elif mode == SCH_LOC_COARSE_SEED:
            temp_flag = self.locCoarseq.empty()
        elif mode == SCH_LOC_FINE_SEED:
            temp_flag = self.locFineq.empty()
        return temp_flag

    def getValue(self, mode):
        temp_value = 0
        if mode == SCH_LOC_COARSE_SEED:
            temp_value = self.locCoarseq.get()
        elif mode == SCH_LOC_FINE_SEED:
            temp_value = self.locFineq.get()
        return temp_value

    def addDeleteq(self, temp_one):
        self.deleteq.put(temp_one)

    def deleteSeeds(self):
        """
        Delete mutated intermediate files.
        @return:
        """
        while not self.deleteq.empty():
            os.remove(self.deleteq.get().filename)
