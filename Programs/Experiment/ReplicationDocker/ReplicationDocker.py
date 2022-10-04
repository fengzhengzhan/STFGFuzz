import os
import re
import time
import subprocess
import datetime

program_name = "CVE2016"
dir_program = "dataset/" + program_name
dir_datain = "dataset/" + program_name + "_dataset/in/in"
dir_dataout = "dataset/" + program_name + "_dataset/out/crashes"
dir_csv = "dataset/" + program_name + ".csv"


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

def saveToCSV(program_name, id, create_time, duration_time, stderr, stdout):
    with open(dir_csv, "a+", encoding="utf-8") as cf:
        # GEN_CSV_HEADERS = "filename,time,duration,content,stdout,stderr\n"
        linestr = str(program_name) + "," \
                  + str(id).replace(',', 'comma') + "," \
                  + str(create_time) + "," \
                  + str(duration_time) + "," \
                  + str(stderr).replace(',', 'comma') + "," \
                  + str(stdout).replace(',', 'comma') + ",,,\n"
        cf.write(linestr)


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
        saveToCSV(program_name, each, create_time, duration_time, stderr, stdout)
    except Exception as e:
        # raise Exception(e)
        print("Error "+str(e))
    #
    # print()
