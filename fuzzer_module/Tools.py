#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import datetime
import re
import subprocess
import time
import os


def saveAsFile(content: str, filename: str):
    """
    Store mutated strings as files for easy reading by test programs.
    @param content:
    @param filename:
    @return:
    """
    with open(filename, "w") as f:
        f.write(content)


def getMutfilename(label: str) -> str:
    return str(datetime.datetime.now().strftime('%Y%m%d%H%M%S%f')) + "_" + str(label) + ".seed"


def getFileList(filepathname: str) -> list:
    """
    Get the content list of the file for each lines.
    @param filepathname:
    @return:
    """
    with open(filepathname, 'r', encoding="UTF-8") as f:
        file_list = f.readlines()
    return file_list

def getTimeStr():
    t = str(time.strftime("%Y%m%d%H%M%S", time.localtime(time.time())))
    return t

def getFileContent(filepathname: str) -> str:
    """
    Get the content of the file.
    @param filepathname:
    @return:
    """
    file_cont = ""
    file_list = getFileList(filepathname)
    for each in file_list:
        file_cont += each
    return file_cont

def delBrackets(source_str: str) -> str:
    restr = r"\(.*?\)"
    replace_str = re.sub(restr, "", source_str)
    return str(replace_str)

def getTimestampStr(days, seconds):
    h = seconds // 3600
    m = (seconds - h * 3600) // 60
    s = seconds - h * 3600 - m * 60
    timestr = "{}:{}:{}:{}".format(days, h, m, s)
    return timestr

def getProjectPath():
    project_path = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))
    return project_path

def runothercmd(cmd: str) -> (int, str, str):
    """
    run cmd to get information from executable files or other tools
    @param cmd:
    @return:
    """
    process = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
    # timeout kill child process
    try:
        std_out, std_err = process.communicate()
    except Exception as e:
        process.kill()
        raise Exception("Error cmd ")
    ret_code = 128 - process.returncode
    # print(ret_code, std_out, std_err)
    return std_out, std_err


if __name__ == "__main__":
    print(delBrackets("bug"))


