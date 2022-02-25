import sys
import subprocess
import time


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
    for i in range(200):
        ret_code, std_out, std_err = run("./llvm_mode/Programs/Bin/demo -f SeedPool/init_seeds/demo/init.seed")
        print(ret_code, std_out, std_err)
    print(time.time()-stat_time)

if __name__ == "__main__":
    mainFuzzer()