import subprocess
import sys

from fuzzer_module.Fuzzconfig import *


def run(cmd: str) -> (int, str, str):
    """
    run cmd to get information from executable files or other tools
    @param cmd:
    @return:
    """
    LOG(LOG_DEBUG, LOG_STR(LOG_FUNCINFO(), cmd))
    process = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
    # timeout kill child process
    try:
        std_out, std_err = process.communicate()
    except Exception as e:
        process.kill()
        LOG(LOG_ERROR, LOG_STR(LOG_FUNCINFO(), e))
        raise Exception("Error cmd ")
    LOG(LOG_DEBUG, LOG_STR(LOG_FUNCINFO(), std_out, std_err))
    ret_code = 128 - process.returncode
    # print(ret_code, std_out, std_err)
    return ret_code, std_out, std_err
