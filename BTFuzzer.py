import sys
import subprocess
import time
from multiprocessing import Process
import threading
from datetime import datetime


from fuzzconfig import *


# run cmd to get information from executable files or other tools
def run(cmd):
    FUZZLOGGING("DEBUG", "{}-> cmd:{}".format(sys._getframe().f_code.co_name, cmd))
    process = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
    # timeout kill child process
    try:
        std_out, std_err = process.communicate()
    except Exception as e:
        process.kill()
        logging.error("{}-> error:{} ".format(sys._getframe().f_code.co_name, e))
        raise Exception("Error cmd ")
    logging.debug("{}-> stdout:{}, stderr:{} ".format(sys._getframe().f_code.co_name, std_out, std_err))
    ret_code = 128 - process.returncode
    # print(ret_code, std_out, std_err)
    return ret_code, std_out, std_err

def mainFuzzer():
    print("----")
    stat_time = time.time()
    # print()
    # for i in range(200):
    #     ret_code, std_out, std_err = run("./llvm_mode/Programs/Bin/demo -f SeedPool/init_seeds/demo/init.seed")
    #     print(ret_code, std_out, std_err)
    # process_list = []
    # for i in range(1000):  # 开启5个子进程执行fun1函数
    #     p = Process(target=run, args=("./llvm_mode/Programs/Bin/demo -f SeedPool/init_seeds/demo/init.seed",))  # 实例化进程对象
    #     p.start()
    #     process_list.append(p)
    #
    # for i in process_list:
    #     p.join()

    threads = []
    for _ in range(1000):  # 循环创建10个线程
        t = threading.Thread(target=run, args=("./llvm_mode/Programs/Bin/demo -f SeedPool/init_seeds/demo/init.seed",))
        threads.append(t)
    for t in threads:  # 循环启动10个线程
        t.start()
    print(time.time()-stat_time)



if __name__ == "__main__":
    mainFuzzer()