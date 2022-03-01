import time

from Fuzzconfig import *
import Executor


def mainFuzzer():
    print("----")
    stat_time = time.time()
    for i in range(200):
        ret_code, std_out, std_err = Executor.run("./Programs/Bin/demo -f SeedPool/init_seeds/demo/init.seed")
        print(ret_code, std_out, std_err)
    print(time.time()-stat_time)



if __name__ == "__main__":
    mainFuzzer()