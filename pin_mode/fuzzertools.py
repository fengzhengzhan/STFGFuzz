import subprocess
import sys
import logging


# Manual Analysis functions
def manualAnalysisCmp(BYTES_MAP_CMP, CMP_MAP_BYTES, static_cmp_dict):
    with open("analyse.txt", "w+") as f:
        for cmpk, cmpv in CMP_MAP_BYTES.items():
            f.write(str(cmpk))
            f.write("\n")
            f.write(str(cmpv))
            f.write("\n")
            for x in cmpv:
                f.write(str(BYTES_MAP_CMP[x][cmpk]))
                f.write(" ")
            f.write("\n")
            f.write(str(static_cmp_dict[cmpk]))
            f.write("\n")
            f.write("--------------------")

# run cmd to get information from pin or other tools
def run(cmd):
    logging.debug("{}-> cmd:{}".format(sys._getframe().f_code.co_name, cmd))
    process = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
    # timeout kill child process
    try:
        std_out, std_err = process.communicate()
    except Exception as e:
        process.kill()
        logging.error("{}-> error:{} ".format(sys._getframe().f_code.co_name, e))
        raise Exception("Error cmd ")
    logging.debug("{}-> stdout:{}, stderr:{} ".format(sys._getframe().f_code.co_name, std_out, std_err))
    ret_code = 128 - process.returncode
    return ret_code, std_out, std_err