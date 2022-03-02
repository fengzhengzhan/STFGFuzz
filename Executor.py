import subprocess
import sys
from Fuzzconfig import *


# run cmd to get information from executable files or other tools
def run(cmd: str) -> (int, str, str):
    FUZZLOGGING(DEBUG, LOG_STR(LOG_FUNCINFO(), cmd))
    process = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
    # timeout kill child process
    try:
        std_out, std_err = process.communicate()
    except Exception as e:
        process.kill()
        FUZZLOGGING(ERROR, LOG_STR(LOG_FUNCINFO(), e))
        raise Exception("Error cmd ")
    FUZZLOGGING(DEBUG, LOG_STR(LOG_FUNCINFO(), std_out, std_err))
    ret_code = 128 - process.returncode
    # print(ret_code, std_out, std_err)
    return ret_code, std_out, std_err
