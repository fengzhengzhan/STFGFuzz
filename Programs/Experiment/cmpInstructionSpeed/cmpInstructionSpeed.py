import os
import time
import subprocess

'''


'''


def runothercmd(cmd: str) -> (int, str, str):
    """
    run cmd to get information from executable files or other tools
    @param cmd:
    @return:
    """
    process = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
    # timeout kill child process
    try:
        stdout, stderr = process.communicate()
    except Exception as e:
        process.kill()
        raise Exception("Error cmd ")
    ret_code = 128 - process.returncode
    # print(ret_code, stdout, stderr)
    return stdout, stderr

def expSpeed(cmd):
    print(cmd, runothercmd(cmd))
    start = time.time()
    for i in range(0, 100):
        runothercmd(cmd)
    end = time.time()
    print("Speed: {}".format((end-start)/100))

def multiProgram():
    expSpeed("cmpInstructionSpeed/lava13796raw CRASH_INPUT")
    expSpeed("cmpInstructionSpeed/lava13796sanitizer CRASH_INPUT")


if __name__ == '__main__':
    multiProgram()


