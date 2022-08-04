#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import subprocess
import sys
import os
import signal

from fuzzer_module.Fuzzconfig import *

def run(cmd: str) -> (str, str):
    """
    run cmd to get information from executable files or other tools
    @param cmd:
    @return:
    """
    LOG(DEBUG, LOC(), cmd)
    p = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.STDOUT,
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
    if stdout == None:
        stdout = b''
    if stderr == None:
        stderr = b''
    return stdout, stderr
