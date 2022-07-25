#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import subprocess
import sys

from fuzzer_module.Fuzzconfig import *


def run(cmd: str) -> (str, str):
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
