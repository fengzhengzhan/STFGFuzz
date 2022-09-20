#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import subprocess
import sys
import os
import signal

from fuzzer_module.Fuzzconfig import *

def runTimeLimit(cmd: str, vis) -> (str, str):
    """
    run cmd to get information from executable files or other tools
    @param cmd:
    @return:
    """
    LOG(DEBUG, LOC(), cmd)
    vis.total += 1
    p = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE,
                         shell=True, close_fds=True, start_new_session=True)

    # timeout kill child process
    try:
        stdout, stderr = p.communicate(timeout=EXE_TIMEOUT)
        # ret_code = p.poll()
    except subprocess.TimeoutExpired:
        p.kill()
        p.terminate()
        os.killpg(p.pid, signal.SIGTERM)
        stdout, stderr = b'', b'Error Timeout'
    except Exception as e:
        raise Exception("Error cmd ")
    # retcode = 128 - p.returncode
    # print(retcode, stdout, stderr)
    return stdout, stderr

def runNoLimit(cmd: str) -> (int, str, str):
    """
    run cmd to get information from executable files or other tools
    @param cmd:
    @return:
    """
    LOG(DEBUG, LOC(), cmd)
    process = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
    # timeout kill child process
    try:
        stdout, stderr = process.communicate()
    except Exception as e:
        process.kill()
        LOG(ERROR, LOC(), e)
        raise Exception("Error cmd ")
    LOG(DEBUG, LOC(), stdout, stderr)
    retcode = 128 - process.returncode
    # print(retcode, stdout, stderr)
    return stdout, stderr
