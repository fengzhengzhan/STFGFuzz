import sys
import subprocess
import time
import queue

from classqueue import Test


# run cmd to get information from executable files or other tools
def run(cmd: str) -> (int, str, str):
    process = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
    # timeout kill child process
    try:
        std_out, std_err = process.communicate()
    except Exception as e:
        process.kill()
        raise Exception("Error cmd ")
    ret_code = 128 - process.returncode
    # print(ret_code, std_out, std_err)
    return ret_code, std_out, std_err


def mainFuzzer():
    print("----")
    stat_time = time.time()
    for i in range(200):
        ret_code, std_out, std_err = run("./../Programs/Bin/demo -f ../SeedPool/init_seeds/demo/init.seed")
        print(ret_code, std_out, std_err)
    print(time.time()-stat_time)



if __name__ == "__main__":
    # mainFuzzer()

    q = queue.Queue(maxsize=0)
    q.put(Test(0, [1, 2, ]))
    q.put(Test(1, [3, 4]))

    tt = q.get()
    print(tt.s, tt.b)
    tt = q.get()
    print(tt.s, tt.b)
