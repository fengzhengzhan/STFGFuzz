import time
import pickle
import logging
import sys

LOG_FORMAT = "%(asctime)s - %(levelname)s - %(message)s"
logging.basicConfig(filename='log_data/wasm.log', level=logging.WARNING, format=LOG_FORMAT)
logging.debug("-------------------------")

STATIC_FILENAME = "wasm/static_info.pkl"
DYNAMIC_FILENAME = ""
SEEDS_FILENAME = "wasm/archives/run/out"
EXECUTE_FILENAME = "wasm/archives/wfuzzer/wasm3/build/wasm3"


TIME = lambda: time.strftime("%H:%M:%S", time.localtime(time.time()))  # return time

# Read files.
# open static file to get static information
def openStaticFile(filename=STATIC_FILENAME):
    with open(filename, 'rb') as file:
        static_info_dict = pickle.load(file)
    static_main_addr = int(static_info_dict['main'][0], 16)
    static_cmp_dict = static_info_dict["static_cmp_dict"]
    logging.debug("{}-> {} : {}".format(sys._getframe().f_code.co_name, type(static_info_dict), static_info_dict))
    return static_main_addr, static_info_dict, static_cmp_dict


# This function returns the final result used to analyze the seed file.
def finalresults(static_info_dict, dynamic_info_dict):
    pass


if __name__ == "__main__":
    print("[{}] Welcome to use analysis tool for seeds execution path ...".format(TIME()))
    static_main_addr, static_info_dict, static_cmp_dict = openStaticFile()
    # print(static_main_addr, static_info_dict, static_cmp_dict)
    for k, v in static_info_dict.items():
        print(k, v)
