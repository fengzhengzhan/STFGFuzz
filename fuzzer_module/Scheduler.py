import re
from queue import Queue

from fuzzer_module.Fuzzconfig import *


class Scheduler:
    def __init__(self):
        self.seedq: Queue[StructSeed] = Queue(maxsize=0)
        self.mutateq: Queue[StructSeed] = Queue(maxsize=0)
        self.importantq: Queue[StructSeed] = Queue(maxsize=0)
        self.deleteq: Queue[StructSeed] = Queue(maxsize=0)

        self.loc_coarse_list: 'list[int]' = []
        self.loc_fine_list: 'list[int]' = []
        self.slid_window: int = SCH_SLID_WINDOW
        self.freeze_bytes: set = set()
        self.freezeid_rpt = set()
        self.solved_cmpset = set()

        self.mutlocnums = 0
        self.switchnums = 1

        self.unique_crash = set()

    def initEachloop(self):
        self.loc_coarse_list = []
        self.loc_fine_list = []
        self.slid_window = SCH_SLID_WINDOW
        self.mutlocnums = 0

    def selectOneSeed(self, mode: int, mutseed=None) -> StructSeed:
        if mode == SCH_LOOP_SEED:
            temp_one = self.seedq.get()
        elif mode == SCH_MUT_SEED:
            temp_one = self.mutateq.get()
        elif mode == SCH_THIS_SEED:
            temp_one = mutseed
        else:
            raise Exception("Error: mode type.")
        if SCH_SAVEASFILE:
            saveAsFile(temp_one.content, temp_one.filename)
        self.addDeleteq(temp_one)
        return temp_one


    def addSeeds(self, mode: int, structseed_list: 'list[StructSeed]'):
        for each in structseed_list:
            if mode == SCH_LOOP_SEED:
                self.seedq.put(each)
            elif mode == SCH_MUT_SEED:
                self.mutateq.put(each)

    def addDeleteq(self, temp_one):
        self.deleteq.put(temp_one)

    def isEmpty(self, mode) -> bool:
        temp_flag = False
        if mode == SCH_LOOP_SEED:
            temp_flag = self.seedq.empty()
        elif mode == SCH_MUT_SEED:
            temp_flag = self.mutateq.empty()
        return temp_flag

    def deleteSeeds(self):
        """
        Delete mutated intermediate files.
        @return:
        """
        while not self.deleteq.empty():
            temp_one = self.deleteq.get()
            if SCH_SAVEASFILE:
                os.remove(temp_one.filename)

    def saveCrash(self, file_crash_csv, path_crashseeds, seed: StructSeed, stdout, stderr):
        """
        To facilitate analysis, save all the crash seed information in a csv file
        @return:
        """
        path, name = os.path.split(seed.filename)
        if not os.path.exists(path_crashseeds + name) and len(stderr) != 0:
            re_str = "#0 (.*?) in"
            crashid = re.search(re_str, str(stderr)).group(1)
            if crashid not in self.unique_crash:
                self.unique_crash.add(crashid)
                # write csv
                with open(file_crash_csv, "a+", encoding="utf-8") as cf:
                    linestr = str(name) + "," + str(seed.content.encode("utf-8")) + "," + str(stdout) + "," + str(stderr) + "\n"
                    cf.write(linestr)
                # write seed
                with open(path_crashseeds + name, "w", encoding="utf-8") as sf:
                    sf.write(seed.content)

    def quitFuzz(self):
        self.deleteSeeds()
        sys.exit(0)
