#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import datetime
import pickle
import re
import time
import os


def saveAsFile(content: bytes, filename: str):
    """
    Store mutated strings as files for easy reading by test programs.
    @param content:
    @param filename:
    @return:
    """
    with open(filename, "wb") as f:
        f.write(content)


def saveAsPkl(filename, data):
    with open(filename, 'wb') as f:
        pickle.dump(data, f)


def loadFromPkl(filename):
    with open(filename, 'rb') as f:
        data = pickle.load(f)
    return data


def readContent(filename: str) -> bytes:
    """
    Get the content of the file.
    @param filepathname:
    @return:
    """
    with open(filename, "rb") as f:
        cont = f.read()
    return cont


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


def getTime():
    t = str(time.strftime("[%H:%M:%S]", time.localtime(time.time())))
    return t


def getTimeStr():
    t = str(time.strftime("%Y%m%d%H%M%S", time.localtime(time.time())))
    return t


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


def getCmpidOrder(cmpid, order):
    return str(cmpid) + "+" + str(order)


def getLocInputValue(content, location):
    loc_input = {}
    for one_loc in location:
        loc_input[one_loc] = content[one_loc:one_loc + 1]
    return loc_input


if __name__ == "__main__":
    # print(delBrackets("bug"))
    # std_out, std_err = run("./Programs/base64/code_Bin/base64 -d Programs/base64/seeds_crash/validate_inputs/utmp-fuzzed-222.b64")
    # print(std_out, std_err)
    # cont = readContent("/home/fzz/Desktop/STFGFuzz/Programs/base64/seeds_init/rand.seed")
    # print(cont)
    print(delBrackets("bug(args)"))
