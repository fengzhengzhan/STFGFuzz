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
# Compile the program
cd ${PROGRAMS}/${PROGRAMNAME}
# clang++ -g -emit-llvm -c code_sources/demo.cc -o code_sources/demo.bc
# clang -g -emit-llvm -c ${SOURCES}/${PROGRAMNAME}.cc -o ${IR}/${PROGRAMNAME}.${SUFFIX} # IR
# -fsanitize-recover=address -fsanitize=address,memory -fsanitize-coverage=bb,no-prune,trace-pc-guard  -fsanitize-coverage=edge,trace-pc-guard (default)
${COMPILER} -fsanitize=address -fsanitize-coverage=bb,no-prune,trace-pc-guard,trace-cmp -emit-llvm -c ${SOURCES}/${PROGRAMNAME}.${SUFFIX} -o ${IR}/${PROGRAMNAME_TRACE}.${SUFFIX} 
rm -f ${LINE_SAVE}
echo "{" >> ${LINE_SAVE}
opt -load ../../${LLVMPASSPATH} -line -S ${IR}/${PROGRAMNAME_TRACE}.${SUFFIX} -o ${IR}/${PROGRAMNAME_PASS}.${SUFFIX} >> ${LINE_SAVE}
echo "}" >> ${LINE_SAVE}
llc -filetype=obj ${IR}/${PROGRAMNAME_PASS}.${SUFFIX} -o ${IR}/${PROGRAMNAME}.o  # Object file
${COMPILER} -lz -fsanitize=address -Wl,--whole-archive -L../../${SANPATH} -lcmpcov -Wl,--no-whole-archive ${IR}/${PROGRAMNAME}.o -o ${BIN}/${PROGRAMNAME}  # Link
# ${COMPILER} -fsanitize=address -Wl,--whole-archive -L../../${SANPATH} -lcmpcov -Wl,--no-whole-archive ${IR}/${PROGRAMNAME}.o -o ${BIN}/${PROGRAMNAME}  # Link
# clang -fsanitize=address -Wl,--whole-archive -L../../${SANPATH} -lcmpcov -Wl,--no-whole-archive -L/usr/local/lib/ -lhiredis ${IR}/${PROGRAMNAME}.o -o ${BIN}/${PROGRAMNAME}  # Link
cd ../..
'''


def compilerCmd(dir, file):
    # pass
    clang_cmd = "clang -fsanitize=address -fsanitize-coverage=bb,no-prune,trace-pc-guard,trace-cmp -emit-llvm -c " \
                + dir + "/" + file + " -o " + dir + "/" + file[:-3] + "_trace.bc"
    llc_cmd = "llc -filetype=obj " + dir + "/" + file[:-3] + "_trace.bc" + " -o " + dir + "/" + file[:-3] + ".o"
    clangsan_cmd = "clang -lz -fsanitize=address -Wl,--whole-archive -L/home/fzz/Desktop/STFGFuzz/llvm_mode/ClangSanitizer -lcmpcov -Wl,--no-whole-archive " \
                   + dir + "/" + file[:-3] + ".o" + " -o experiment_dataset/" + file[:-3]

    os.system(clang_cmd)
    os.system(llc_cmd)
    os.system(clangsan_cmd)

    print(clang_cmd)
    print(llc_cmd)
    print(clangsan_cmd)
    print()
    print()


def compilerProgram(data_list):
    for dir in data_list:
        # print(dir)
        for file in os.listdir(dir):
            # print(file)
            ext = file.split(".")[-1]
            # print(ext)
            if ext == "bc":
                fext = file.split("_")[-1]
                # print(fext)
                if fext != "trace.bc":
                    print(file)
                    compilerCmd(dir, file)


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
    # print(cmd, runothercmd(cmd))
    start = time.time()
    for i in range(0, count):
        runothercmd(cmd)
    end = time.time()
    et = (end - start) / count
    print("Speed: {}".format(et))
    # print()
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


# program = ['base64', 'md5sum', 'uniq', 'who', 'addr2line', 'ar', 'as', 'c++filt', 'gprof', 'nm',
#            'objcopy', 'objdump', 'ranlib', 'readelf', 'size', 'strings', 'strip']
# args = ['-d ', '', '', '', '', '', '', ' @', '', '', '', '', '', '', '', '', '']
program = ['as', 'base64', 'c++filt', 'md5sum', 'readelf', 'strings', 'uniq']
args = ['', '-d ', ' @', '', '', '', '']
dir_prog = "experiment_dataset/"
dir_seed = "seeds/"
seeds_list = ['1KB', '2KB', '4KB', '8KB', '16KB', '32KB', '64KB', '128KB', '256KB', '512KB', '1MB']


# seeds_list = ['1KB', '2KB']


def testSpeed():
    for idx in range(0, len(program)):
        data = []
        data.append(program[idx])
        for each in seeds_list:
            cmd = dir_prog + program[idx] + " " + args[idx] + dir_seed + each
            et = expSpeed(cmd, 3)
            print(cmd, et)
            data.append(et)
        saveToexcel("SeedLengthSpeed.xlsx", [data])


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


def genPicture(filename, ):
    excel_data = readExcel(filename)
    print(excel_data)

    x = ['1', '2', '4', '8', '16', '32', '64', '128', '256', '512', '1024']  # 点的横坐标
    k1 = excel_data[1][1:]  # 线的纵坐标
    k2 = excel_data[2][1:]  # 线的纵坐标
    k3 = excel_data[3][1:]  # 线的纵坐标
    k4 = excel_data[4][1:]  # 线的纵坐标
    k5 = excel_data[5][1:]  # 线的纵坐标
    k6 = excel_data[6][1:]  # 线的纵坐标
    k7 = excel_data[7][1:]  # 线的纵坐标
    # k8 = excel_data[8][1:]  # 线的纵坐标
    # k9 = excel_data[9][1:]  # 线的纵坐标
    # k10 = excel_data[10][1:]  # 线的纵坐标
    # k11 = excel_data[11][1:]  # 线的纵坐标
    # k12 = excel_data[12][1:]  # 线的纵坐标
    # k13 = excel_data[13][1:]  # 线的纵坐标
    # k14 = excel_data[14][1:]  # 线的纵坐标
    # k15 = excel_data[15][1:]  # 线的纵坐标
    # k16 = excel_data[16][1:]  # 线的纵坐标
    # k17 = excel_data[17][1:]  # 线的纵坐标
    # plt.plot(x, k1, 's-', color='r', label="base64")  # s-:方形
    # plt.plot(x, k2, 'o-', color='g', label="md5sum")  # o-:圆形
    plt.plot(x, k1, 'o-', label=program[0])
    plt.plot(x, k2, 'o-', label=program[1])
    plt.plot(x, k3, 'o-', label=program[2])
    plt.plot(x, k4, 'o-', label=program[3])
    plt.plot(x, k5, 'o-', label=program[4])
    plt.plot(x, k6, 'o-', label=program[5])
    plt.plot(x, k7, 'o-', label=program[6])
    # plt.plot(x, k8, 'o-', label=program[7])
    # plt.plot(x, k9, 'o-', label=program[8])
    # plt.plot(x, k10, 'o-', label=program[9])
    # plt.plot(x, k11, 'o-', label=program[10])
    # plt.plot(x, k12, 'o-', label=program[11])
    # plt.plot(x, k13, 'o-', label=program[12])
    # plt.plot(x, k14, 'o-', label=program[13])
    # plt.plot(x, k15, 'o-', label=program[14])
    # plt.plot(x, k16, 'o-', label=program[15])
    # plt.plot(x, k17, 'o-', label=program[16])
    plt.xlabel("input size (kb)")  # 横坐标名字
    plt.ylabel("execution time (s)")  # 纵坐标名字
    # plt.title("Relationship between input size and execution speed")
    plt.legend(loc="best")  # 图例
    plt.savefig('./SeedLengthSpeed.png', dpi=300)
    plt.show()


if __name__ == '__main__':
    cur_path = os.getcwd()
    os.chdir(cur_path + "/dataset")
    print(os.getcwd())
    # compilerProgram(['binutils_gdb_bin', 'coreutils_bin'])
    # testSpeed()
    genPicture("SeedLengthSpeed.xlsx")
