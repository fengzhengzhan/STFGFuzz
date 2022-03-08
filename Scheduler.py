import os
from queue import Queue

from Fuzzconfig import *

class Scheduler:
    def __init__(self):
        self.seedq: Queue[StructSeed] = Queue(maxsize=0)
        self.mutateTestq: Queue[StructSeed] = Queue(maxsize=0)
        self.importantq: Queue[StructSeed] = Queue(maxsize=0)
        self.deleteq: Queue[StructSeed] = Queue(maxsize=0)

    def selectOneSeed(self) -> StructSeed:
        temp_one = self.seedq.get()
        self.deleteq.put(temp_one)
        return temp_one

    def selectMutOneSeed(self) -> StructSeed:
        temp_one = self.mutateTestq.get()
        self.deleteq.put(temp_one)
        return temp_one

    def addSeeds(self, seeds_path: str, seeds_filename: list):
        for eachseed in seeds_filename:
            self.seedq.put(StructSeed(seeds_path + eachseed, "", INIT, []))

    def addMutSeeds(self, structseed_list: list[StructSeed]):
        for each in structseed_list:
            self.mutateTestq.put(each)

    def mutateTestqEmpty(self):
        return self.mutateTestq.empty()

    def deleteSeeds(self):
        '''
        Delete mutated intermediate files.
        '''
        while not self.deleteq.empty():
            os.remove(self.deleteq.get().filename)
