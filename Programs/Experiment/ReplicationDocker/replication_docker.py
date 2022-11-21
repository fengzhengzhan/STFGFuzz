import os
import re
import time
import subprocess
import datetime


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


def createFolder():
    lavalist = [292, 357, 660, 1199, 2285, 2543, 3089, 3377, 4049, 4383, 4961, 7002, 7700, 9763, 13796, 14324, 16689, 17222]
    for lavaid in lavalist:
        path = "dataset/lava1_dataset/angora_lava1_"+str(lavaid)
        print(path)
        folder = os.path.exists(path)

        if not folder:
            os.makedirs(path)
            # print(path)

def main():
    # CVE2016()
    LAVA1()
    # createFolder()


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