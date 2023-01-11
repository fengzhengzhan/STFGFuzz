import os
import re
import time
import subprocess
import datetime
import signal


import os

cve_list = ['CVE-2014-0160', 'CVE-2015-8540',
            'CVE-2016-4487', 'CVE-2016-4488', 'CVE-2016-4489', 'CVE-2016-4490',
            'CVE-2016-4491', 'CVE-2016-4492', 'CVE-2016-4493', 'CVE-2016-6131', ]

aflgo_dataset_list = ['cxxfilt-CVE-2016-4487', 'giflib-bugs-74', 'jasper-CVE-2015-5221',
                      'KTY_Pretty_Printer', 'libming-CVE-2018-8807', 'libming-CVE-2018-8962',
                      'libxml2_ef709ce2', 'LMS', 'lrzip-CVE-2017-8846', 'lrzip-CVE-2018-11496',
                      'mjs-issues-57', 'mjs-issues-78', 'objdump-CVE-2017-8392',
                      'Palindrome']

uaf_dataset_list = ['CVE-2018-20623', 'yasm-issue-91', 'CVE-2019-6455', 'CVE-2017-10686', 'gifsicle-issue-122', 'CVE-2016-3189', 'CVE-2019-20633']

def createCVEFolder(cve_list):
    for cve in cve_list:
        if not os.path.exists(cve):
            os.makedirs(cve)
            print("Create Successful: {}".format(os.getcwd() + "/" + cve))

def createAFLGoFolder(aflgo_dataset_list):
    for filename in aflgo_dataset_list:
        pwd = "/home/fzz/Desktop/STFGFuzz/Programs/"
        filepath = pwd + filename
        if not os.path.exists(filepath):
            print(filepath)
            os.makedirs(filepath)
            print("Create Successful: {}".format(filepath))

        command = "/home/fzz/Desktop/STFGFuzz/Programs/build.sh -n "+filepath+" clang"
        runTimeLimit(command)
        print("Create Successful: {}".format(command))


def cpSourceFiles():
    cve2016 = ['CVE-2016-4487', 'CVE-2016-4488', 'CVE-2016-4489', 'CVE-2016-4490',
                'CVE-2016-4491', 'CVE-2016-4492', 'CVE-2016-4493', 'CVE-2016-6131', ]
    for dir in cve2016:
        #rmcom = "rm -rf "+dir+"/gcc"
        #os.system(rmcom)
        #print(rmcom)
        cpcom = "cp -r binutils-gdb "+dir
        os.system(cpcom)
        print(cpcom)

def runTimeLimit(cmd) -> (str, str):
    """
    run cmd to get information from executable files or other tools
    @param cmd:
    @return:
    """
    p = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE,
                         shell=True, close_fds=True, start_new_session=True)

    # timeout kill child process
    try:
        stdout, stderr = p.communicate(timeout=20)
        # ret_code = p.poll()
    except subprocess.TimeoutExpired:
        p.kill()
        p.terminate()
        os.killpg(p.pid, signal.SIGTERM)
        stdout, stderr = b'', b'Error Timeout'
    except Exception as e:
        raise Exception("Error cmd: " + cmd)
    # retcode = 128 - p.returncode
    # print(retcode, stdout, stderr)
    return stdout, stderr

# Get time of start time and crash time list
def getFileCreateTime(file):
    # t = os.path.getctime(file)
    stdout, stderr = runTimeLimit("ls -l --full-time " + file)
    data_str = re.search(r'(\d+-\d+-\d+ \d+:\d+:\d+).\d+', str(stdout)).group(1)
    # print(data_str)
    t = datetime.datetime.strptime(data_str, '%Y-%m-%d %H:%M:%S')
    return t

def saveToCSV(dir_csv, program_name, id, create_time, duration_time, stderr, stdout, cmpflag):
    with open(dir_csv, "a+", encoding="utf-8") as cf:
        # GEN_CSV_HEADERS = "filename,time,duration,content,stdout,stderr\n"
        linestr = str(program_name) + "," \
                  + str(id).replace(',', 'comma') + "," \
                  + str(create_time) + "," \
                  + str(duration_time) + "," \
                  + str(stderr).replace(',', 'comma') + "," \
                  + str(stdout).replace(',', 'comma') + "," \
                  + str(cmpflag).replace(',', 'comma') + ",,,\n"
        cf.write(linestr)

def compareCrash(stderr, dir_patchloc):
    # print(stderr, dir_patchloc)
    errlist = []
    for err_i in str(stderr).split("\\n"):
        re_str = r"\#(\d*).*/(.*?):(\d*?):"
        re_crash = re.findall(re_str, str(err_i))
        # print(str(err_i))
        # print(re_crash)
        if len(re_crash) > 0:
            errlist.append(re_crash)

    patchlist = []
    with open(dir_patchloc, "r") as f:
        cont = f.readlines()
    # print(cont)
    for cont_i in cont:
        re_str = r"\#(\d*).*/(.*?):(\d*?):"
        re_crash = re.findall(re_str, cont_i)
        # print(cont_i)
        # print(re_crash)
        if len(re_crash) > 0:
            patchlist.append(re_crash)

    if errlist == patchlist:
        return "yes"

    return ""

def createFolder():
    lavalist = [292, 357, 660, 1199, 2285, 2543, 3089, 3377, 4049, 4383, 4961, 7002, 7700, 9763, 13796, 14324, 16689, 17222]
    for lavaid in lavalist:
        path = "dataset/lava1_dataset/angora_lava1_"+str(lavaid)
        print(path)
        folder = os.path.exists(path)

        if not folder:
            os.makedirs(path)
            # print(path)

def CVE2016():
    program_name = "CVE2016"
    dir = "dataset/cve2016/aflgo/"
    dir_program = dir + program_name
    dir_datain = dir + program_name + "_dataset/in/in"
    dir_dataout = dir + program_name + "_dataset/out/crashes"
    dir_csv = dir + program_name + ".csv"

    start_time = getFileCreateTime(dir_datain)
    print(start_time)

    # Get crash list
    crashes = os.listdir(dir_dataout)
    crashes.sort()
    # print(crashes)
    for each in crashes:
        each_crash = dir_dataout + "/" + each
        print(each_crash)
        # print(getFileCreateTime(each_crash))
        create_time = getFileCreateTime(each_crash)
        duration_time = create_time - start_time
        # print("./" + dir_program + " @" + each_crash)
        try:
            stdout, stderr = runTimeLimit("./" + dir_program + " @" + each_crash)
            # re_flag = re.search(r'AddressSanitizer', str(stderr))
            # if re_flag != None:
            #     saveToCSV(program_name, each, create_time, duration_time, stderr, stdout)
            saveToCSV(dir_csv, program_name, each, create_time, duration_time, stderr, stdout, "None Compare")
        except Exception as e:
            # raise Exception(e)
            print("Error " + str(e))
        #
        # print()

def LAVA1():
    # lavalist = [292, 357, 660, 1199, 2285, 2543, 3089, 3377, 4049, 4383, 4961, 7002, 7700, 9763, 13796, 14324, 16689, 17222]
    lavalist = [14324]
    for lavaid in lavalist:
        lavaid = str(lavaid)
        program_name = "lava"+lavaid
        dir = "dataset/lava1_dataset/angora_lava1_"+lavaid+"/"
        dir_program = "../../"+program_name+"/code_Bin/"+program_name
        dir_patchloc = "../../" + program_name + "/data_patchloc/crash0.sanitize"
        dir_datain = dir + "seeds"
        dir_dataout = dir + "output/crashes"
        dir_csv = dir + program_name + ".csv"

        start_time = getFileCreateTime(dir_datain)
        print(start_time)

        # Get crash list
        crashes = os.listdir(dir_dataout)
        crashes.sort()
        # print(crashes)
        for each in crashes:
            each_crash = dir_dataout + "/" + each
            print(each_crash)
            # print(getFileCreateTime(each_crash))
            create_time = getFileCreateTime(each_crash)
            duration_time = create_time - start_time
            print(create_time, duration_time)
            # print("./" + dir_program + " @" + each_crash)
            try:
                cmd = "./" + dir_program + " " + each_crash
                # print(cmd)
                stdout, stderr = runTimeLimit(cmd)
                # print(stdout, stderr)
                # re_flag = re.search(r'AddressSanitizer', str(stderr))
                # if re_flag != None:
                #     saveToCSV(program_name, each, create_time, duration_time, stderr, stdout)
                cmpflag = compareCrash(stderr, dir_patchloc)
                saveToCSV(dir_csv, program_name, each, create_time, duration_time, stderr, stdout, cmpflag)
            except Exception as e:
                # raise Exception(e)
                print("Error " + str(e))
            #
            # print()


def gainAFLGoCsv(program_name, sanitize_location):
    dir = "dataset/aflgo/"
    dir_program = sanitize_location
    dir_datain = dir + program_name + "/in"
    dir_dataout = dir + program_name + "/out/crashes"
    dir_csv = dir + program_name + ".csv"

    start_time = getFileCreateTime(dir_datain)
    # start_time = datetime.datetime.strptime("2022-12-04 17:41:27", '%Y-%m-%d %H:%M:%S')
    # print(start_time)

    # Get crash list
    crashes = os.listdir(dir_dataout)
    crashes.sort()
    # print(crashes)
    for each in crashes:
        each_crash = dir_dataout + "/" + each
        print(each_crash)
        # print(getFileCreateTime(each_crash))
        create_time = getFileCreateTime(each_crash)
        duration_time = create_time - start_time
        # print("./" + dir_program + " @" + each_crash)
        try:
            # swftophp
            # command = dir_program + " " + each_crash
            # jasper
            command = dir_program + " -f "+each_crash +" -t mif -F /tmp/out -T jpg"
            stdout, stderr = runTimeLimit(command)
            # re_flag = re.search(r'AddressSanitizer', str(stderr))
            # if re_flag != None:
            #     saveToCSV(program_name, each, create_time, duration_time, stderr, stdout)
            saveToCSV(dir_csv, program_name, each, create_time, duration_time, stderr, stdout, "None Compare")
        except Exception as e:
            # raise Exception(e)
            print("Error " + str(e))
        #
        # print()

def gainAngoraCsv(program_name, sanitize_location):
    dir = "dataset/angora/"
    dir_program = sanitize_location
    dir_datain = dir + program_name + "/seeds"
    dir_dataout = dir + program_name + "/output/crashes"
    dir_csv = dir + program_name + ".csv"

    start_time = getFileCreateTime(dir_datain)
    # start_time = datetime.datetime.strptime("2022-12-04 17:41:27", '%Y-%m-%d %H:%M:%S')
    # print(start_time)

    # Get crash list
    crashes = os.listdir(dir_dataout)
    crashes.sort()
    # print(crashes)
    for each in crashes:
        each_crash = dir_dataout + "/" + each
        print(each_crash)
        # print(getFileCreateTime(each_crash))
        create_time = getFileCreateTime(each_crash)
        duration_time = create_time - start_time
        # print("./" + dir_program + " @" + each_crash)
        try:
            # swftophp
            command = dir_program + " " + each_crash
            print("command:{}".format(command))
            stdout, stderr = runTimeLimit(command)
            # re_flag = re.search(r'AddressSanitizer', str(stderr))
            # if re_flag != None:
            #     saveToCSV(program_name, each, create_time, duration_time, stderr, stdout)
            saveToCSV(dir_csv, program_name, each, create_time, duration_time, stderr, stdout, "None Compare")
        except Exception as e:
            # raise Exception(e)
            print("Error " + str(e))
        #
        # print()

def main():
    # CVE2016()
    # LAVA1()
    # createFolder()


    # gainAFLGoCsv("swftophp048", "/home/fzz/Desktop/STFGFuzz/Programs/swftophp/code_Bin/swftophp")
    # gainAFLGoCsv("swftophp2864", "/home/fzz/Desktop/STFGFuzz/Programs/swftophp/code_Bin/swftophp")
    # gainAFLGoCsv("swftophp1042864", "/home/fzz/Desktop/STFGFuzz/Programs/swftophp/code_Bin/swftophp")
    # gainAFLGoCsv("swftophpother", "/home/fzz/Desktop/STFGFuzz/Programs/swftophp/code_Bin/swftophp")
    # gainAFLGoCsv("lava229", "/home/fzz/Desktop/STFGFuzz/Programs/lava292/code_Bin/lava229")
    # gainAFLGoCsv("listswf", "/home/fzz/Desktop/STFGFuzz/Programs/listswf/code_Bin/listswf")
    # gainAFLGoCsv("listswf1226", "/home/fzz/Desktop/STFGFuzz/Programs/listswf/code_Bin/listswf")
    # gainAFLGoCsv("jasper-CVE-2015-5221", "/home/fzz/Desktop/STFGFuzz/Programs/jasper-CVE-2015-5221/code_Bin/jasper-CVE-2015-5221")


    # gainAngoraCsv("swftophp048", "/home/fzz/Desktop/STFGFuzz/Programs/swftophp/code_Bin/swftophp")
    # gainAngoraCsv("listswf048", "/home/fzz/Desktop/STFGFuzz/Programs/listswf/code_Bin/listswf")
    # gainAngoraCsv("angora_listswf", "/home/fzz/Desktop/STFGFuzz/Programs/listswf/code_Bin/listswf")
    # gainAngoraCsv("listswf1226", "/home/fzz/Desktop/STFGFuzz/Programs/listswf/code_Bin/listswf")

    # createCVEFolder(cve_list)
    # cpSourceFiles()

    # createAFLGoFolder(aflgo_dataset_list)
    createAFLGoFolder(uaf_dataset_list)




if __name__ == '__main__':
    main()


#
# import os
# import time
#
#
# dir_crash = "/root/datav5/Angora-1.2.2/lava1/lava_corpus/LAVA-1/output/crashes"
# dir_seeds = "/root/datav5/Angora-1.2.2/lava1/lava_corpus/LAVA-1/seeds"
# file_seeds = dir_seeds + "/" + "seed.txt"
# file_sanitize = "sanitize.txt"
#
# def TimeStampToTime(timestamp):
#     timeStruct = time.localtime(timestamp)
#     return time.strftime('%Y-%m-%d %H:%M:%S',timeStruct)
#
# def getFileTime(filepath):
#     # filepath = unicode(filepath, 'utf8')
#     t = os.path.getctime(filepath)
#     timestamp = time.localtime(t)
#     timestamp = time.strftime('%Y-%m-%d %H:%M:%S', timestamp)
#     return timestamp
#
# def getFilesFromDir(directory):
#     dir_list = []
#     for file in os.listdir(directory):
#         filename = dir_crash + "/" + file
#         if os.path.isfile(filename):
#             dir_list.append(filename)
#     # for file in dir_list:
#     #     print(file)
#     return dir_list
#
#
# def main():
#     print("gain_crash_experiment:")
#     # Get list of all crashes.
#     dir_list = getFilesFromDir(dir_crash)
#     # Get file time.
#     print(file_seeds, getFileTime(file_seeds))
#     for file in dir_list:
#         print(file, getFileTime(file))
#
#
# if __name__ == '__main__':
#     main()
