import os
import time
import subprocess
import xlrd
import xlwt
from xlutils.copy import copy
import matplotlib

matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
import numpy as np
import ast
import random
import re
import json
from ctypes import *

'''
Experiment of SpeedCmpInstruction.
'''

USE_INITNUM = -1
SHMID_FLAG = 'D'  # Content show from stdout, that represent the memory share id.
INTERLEN_FLAG = 'L'  # The length of array.
INTERLEN_VALUE = 16  # The space bytes in the start of content represents interlen values.
END_EACH_FLAG = 'Z'  # End of each line.
INIT_PC_GUARD = 'I'  # (info, call_pc, nums, start, end) Numbers of pc guard, from 1 to number.
COVERAGE_NUM = 'C'  # Get rough code coverage.
EACH_PC_GUARD = 'G'  # (info, call_pc, guard_num)  dict.pop(cmpid)
ANA_ENDPROG_IDX = -2
ANA_MEMSHM_MODE = True
ANA_FILTER_SIZE = 128
ANA_INTERLEN_SIZE = 16
ANA_COVERNUM_SIZE = 16
ANA_START_SIZE = ANA_FILTER_SIZE + ANA_INTERLEN_SIZE + ANA_COVERNUM_SIZE
ANA_SHM_INTERVAL = 1024 * 1024
ANA_SHM_SIZE = 2147483648
# Trace level
TRACE_NULL = 'O'
TRACE_GUARDFAST = 'P'
TRACE_GUARD = 'Q'
TRACE_GUARDSYMBOL = 'R'
TRACE_CMPFILTER = 'S'
TRACE_CMP = 'T'
TRACE_CMPGUARD = 'U'
TRACE_CMPGUARDSYMBOL = 'V'


class Analyzer:
    def __init__(self):
        self.shm_key = USE_INITNUM
        self.addr = None
        try:
            self.rt = CDLL('librt.so')
        except:
            self.rt = CDLL('librt.so.1')
        self.shmget = self.rt.shmget
        self.shmget.argtypes = [c_int, c_size_t, c_int]
        self.shmget.restype = c_int

        self.shmat = self.rt.shmat
        self.shmat.argtypes = [c_int, POINTER(c_void_p), c_int]
        self.shmat.restype = c_void_p

    # Combination Functions
    # getAddr()
    # getInterlen()
    # getRpt()
    # traceAyalysis()

    def getShm(self, out_info: str):
        """
        Get the memory share address.
        """
        try:
            re_str = SHMID_FLAG + "(.*?)" + END_EACH_FLAG
            shm_key = int(re.search(re_str, str(out_info)).group(1))
            # print(shm_key)
        except Exception as e:
            shm_key = 124816
            # if self.shm_key == USE_INITNUM:
            #     raise Exception("Error shm_key {}".format(e))

        if shm_key != self.shm_key:
            self.shm_key = shm_key

            shmid = self.shmget(shm_key, ANA_SHM_SIZE, 0o1000 | 0o666)  # 2*1024*1024*1024 2GB
            if shmid < 0:
                raise Exception("Error System not shared.")

            self.addr = self.shmat(shmid, None, 0)

        # Get the length of cmpcovshm contents.
        interlen_str = string_at(self.addr + ANA_FILTER_SIZE, ANA_INTERLEN_SIZE).decode("utf-8")
        re_str = INTERLEN_FLAG + "(.*?)" + END_EACH_FLAG
        interlen = int(re.search(re_str, interlen_str).group(1))

        covernum_str = string_at(self.addr + ANA_FILTER_SIZE + ANA_INTERLEN_SIZE, ANA_COVERNUM_SIZE).decode("utf-8")
        re_str = COVERAGE_NUM + "(.*?)" + END_EACH_FLAG
        covernum = int(re.search(re_str, covernum_str).group(1))
        return interlen, covernum

    def sendCmpid(self, cmpid):
        """
        Send cmpid to save the cmpid information.
        @param cmpid:
        @return:
        """
        if self.addr is None:
            raise Exception("Error Memory share space not create.")

        cmpid = str(cmpid) + "\0"
        memmove(self.addr, cmpid.encode(), len(cmpid))


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


def expSpeed(cmd, count):
    print(cmd, runothercmd(cmd))
    start = time.time()
    for i in range(0, count):
        runothercmd(cmd)
    end = time.time()
    et = (end - start) / count
    print("Speed: {}".format(et))
    print()
    return et


def saveToexcel(path, value):
    print(path, value)
    index = len(value)  # 获取需要写入数据的行数
    workbook = xlrd.open_workbook(path)  # 打开工作簿
    sheets = workbook.sheet_names()  # 获取工作簿中的所有表格
    worksheet = workbook.sheet_by_name(sheets[1])  # 获取工作簿中所有表格中的的第一个表格
    rows_old = worksheet.nrows  # 获取表格中已存在的数据的行数
    print(rows_old, index)
    new_workbook = copy(workbook)  # 将xlrd对象拷贝转化为xlwt对象
    new_worksheet = new_workbook.get_sheet(1)  # 获取转化后工作簿中的第一个表格
    for i in range(0, index):
        for j in range(0, len(value[i])):
            new_worksheet.write(i + rows_old, j, value[i][j])  # 追加写入数据，注意是从i+rows_old行开始写入
    new_workbook.save(path)  # 保存工作簿


def execProgram(program, count, excel):
    data = []
    data.append(program)
    data.append(expSpeed("dataset/" + program + "_gcc @rand.seed", count))
    data.append(expSpeed("dataset/" + program + "_clang @rand.seed", count))
    data.append(expSpeed("dataset/" + program + "_aflgo @rand.seed", count))
    data.append(expSpeed("dataset/" + program + "_sanitize @rand.seed", count))
    ana = Analyzer()
    ana.getShm("D124816Z\n")

    ana.sendCmpid(TRACE_GUARDFAST)
    print("TRACE_GUARDFAST")
    data.append(expSpeed("dataset/" + program + "_CFDGF @rand.seed", count))

    ana.sendCmpid("xx")
    print("TRACE_CMPFILTER")
    data.append(expSpeed("dataset/" + program + "_CFDGF @rand.seed", count))

    ana.sendCmpid(TRACE_CMPGUARDSYMBOL)
    print("TRACE_CMPGUARDSYMBOL")
    data.append(expSpeed("dataset/" + program + "_CFDGF @rand.seed", count))
    print()

    saveToexcel(excel, [data])


def experiment():
    execProgram("cxxfilt", 100, "SpeedCmpInstruction.xlsx")


'''
Matplotlib get picture
'''


def readExcel(filename) -> list:
    xlsx = xlrd.open_workbook(filename)
    excel_data = []
    for shidx, sh in enumerate(xlsx.sheets()):
        if shidx != 0:
            continue
        for r in range(sh.nrows):
            temp_data = sh.row_values(r)
            excel_data.append(temp_data)
    # print(excel_data)
    return excel_data


def splitValue(data, col):
    """
    According column split the excel.
    @return:
    """
    col_list = []
    for line in data:
        col_list.append(line[col])
    return col_list


def genPicture(filename, ):
    excel_data = readExcel(filename)
    # print(excel_data)

    labels = splitValue(excel_data[1:], 0)
    gcc_list = splitValue(excel_data[1:], 1)
    clang_list = splitValue(excel_data[1:], 2)
    aflgo_list = splitValue(excel_data[1:], 3)
    sanitize_list = splitValue(excel_data[1:], 4)
    CFDGF_guard_list = splitValue(excel_data[1:], 5)
    CFDGF_filter_list = splitValue(excel_data[1:], 6)
    CFDGF_symbol_list = splitValue(excel_data[1:], 7)
    print(gcc_list, clang_list, aflgo_list, sanitize_list, CFDGF_guard_list, CFDGF_filter_list, CFDGF_symbol_list)

    x = np.arange(len(labels))  # the label locations
    width = 0.2  # the width of the bars

    fig, ax = plt.subplots()
    # rects1 = ax.bar(x - 3 * width, gcc_list, width, label='gcc')
    # rects2 = ax.bar(x - 2 * width, clang_list, width, label='clang')
    # rects3 = ax.bar(x - 1 * width, aflgo_list, width, label='aflgo')
    # rects4 = ax.bar(x, sanitize_list, width, label='sanitize')
    # rects5 = ax.bar(x + 1 * width, CFDGF_guard_list, width, label='CFDGF_guard')
    # rects6 = ax.bar(x + 2 * width, CFDGF_filter_list, width, label='CFDGF_filter')
    # rects7 = ax.bar(x + 3 * width, CFDGF_symbol_list, width, label='CFDGF_symbol')

    rects1 = ax.bar(x - 2.5*width, gcc_list, width, label='gcc')
    rects2 = ax.bar(x - 1.5*width, clang_list, width, label='clang')
    rects3 = ax.bar(x - 0.5*width, aflgo_list, width, label='aflgo')
    rects4 = ax.bar(x + 0.5*width, sanitize_list, width, label='sanitize')
    rects5 = ax.bar(x + 1.5*width, CFDGF_guard_list, width, label='CFDGF_guard')
    rects6 = ax.bar(x + 2.5*width, CFDGF_filter_list, width, label='CFDGF_filter')

    # Add some text for labels, title and custom x-axis tick labels, etc.
    ax.set_ylabel('Time')
    ax.set_title('Speed of compare instruction')
    ax.set_xticks(x, labels)
    ax.legend()

    ax.bar_label(rects1, padding=0, fmt="", fontsize=0)
    ax.bar_label(rects2, padding=0, fmt="", fontsize=0)
    ax.bar_label(rects3, padding=0, fmt="", fontsize=0)
    ax.bar_label(rects4, padding=0, fmt="", fontsize=0)
    ax.bar_label(rects5, padding=0, fmt="", fontsize=0)
    ax.bar_label(rects6, padding=0, fmt="", fontsize=0)
    # ax.bar_label(rects7, padding=0, fmt="", fontsize=0)

    fig.tight_layout()

    plt.savefig('./cmpInstructionSpeed.jpg')
    plt.show()


if __name__ == '__main__':
    # experiment()
    genPicture("SpeedCmpInstruction.xlsx")
