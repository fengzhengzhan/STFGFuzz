import os
import random
import subprocess
import logging
import pickle
import sys
import datetime
import time
from multiprocessing import Process, Manager
from graphviz import Digraph

from variable import *
from readfile import *
from savefile import *
from dynamicanalysis import *
from fuzzeroperat import *
from fuzzertools import *

LOG_FORMAT = "%(asctime)s - %(levelname)s - %(message)s"
logging.basicConfig(filename='log_data/mainFuzzer.log', level=logging.WARNING, format=LOG_FORMAT)
logging.debug("-------------------------")


def dynamicExecute(seeds_content, indexlen, static_info_dict, dynamic_info_dict, dynamic_cmp_dict, BYTES_MAP_CMP):
    ret_mutate_seeds = mutateSeeds(seeds_content, MUTATE_MODE['per_each_mutN'], mutate_location=indexlen)
    for each_mutseed in ret_mutate_seeds:
        save_path = MUTATE_SAVE_PATH
        mutate_name = "mutate" + datetime.datetime.now().strftime("%Y%m%d%H%M%S") + str(indexlen) + str(random.randint(0, 10000))
        mutate_dynamicout_filename = DYNAMIC_SAVE_PATH + mutate_name + ".out"
        mutate_filename = save_path + mutate_name + ".b64"

        saveSeeds(each_mutseed, mutate_filename)

        # try to execute the program to find the bugs return
        file_run_cmd = "./fuzzer_program/base64 -d " + mutate_filename
        file_retcode, file_stdout, file_stderr = run(file_run_cmd)

        # try to execute "pin" to get the dynamic information file (this execute spend more time)
        dynamic_run_cmd = "./../pin320/pin -t info_data/MyPinTool.so -o " + mutate_dynamicout_filename + " -- ./fuzzer_program/base64 -d " + mutate_filename
        dynamic_retcode, dynamic_stdout, dynamic_stderr = run(dynamic_run_cmd)

        img_base_ip, next_dynamic_cmp_dict, next_dynamic_info_dict = openDynamicFile(mutate_dynamicout_filename)
        temp_bytes_map_cmp_dict, temp_cmp_map_bytes_set = gainCmpSetColor(dynamic_cmp_dict, next_dynamic_cmp_dict)

        BYTES_MAP_CMP[indexlen] = temp_bytes_map_cmp_dict

        # each_dynamic_path, draw_dynamic_dict = gainDynamicInfo(static_info_dict, dynamic_info_dict, DRAW_FUNC['main'])

        os.remove(mutate_dynamicout_filename)
        os.remove(mutate_filename)

        # print(indexlen, each_mutseed[0])


def execFuzz():
    '''
    1. read seeds
    2. collect information, try to execute the new seed
    3. mutate seeds and collect dynamic information (multiprocess)
    4. using rules to mutate seeds
    5. find bugs
    :return:
    '''
    # keep MyPinTool.cpp in sync
    run("cp /root/Desktop/fuzz_article/AsFuzzer/pin320/source/tools/MyPinTool/obj-intel64/MyPinTool.so /root/Desktop/fuzz_article/AsFuzzer/AsFuzzerProj/info_data")

    # collection static dynamic init_seed information
    dynamic_path_set = set()
    static_main_addr, static_info_dict, static_cmp_dict = openStaticFile()
    dynamic_run_cmd = "./../pin320/pin -t info_data/MyPinTool.so -o " + DYNAMIC_SAVE_PATH+DYNAMIC_INIT_FILENAME  + " -- ./fuzzer_program/base64 -d fuzzer_program/fuzzer_input/AAAB.b64"
    dynamic_retcode, dynamic_stdout, dynamic_stderr = run(dynamic_run_cmd)
    img_base_ip, dynamic_cmp_dict, dynamic_info_dict = openDynamicFile(DYNAMIC_SAVE_PATH+DYNAMIC_INIT_FILENAME)
    seeds_content = openFuzzSeeds()
    seed_len = len(seeds_content)

    manager = Manager()
    BYTES_MAP_CMP = manager.list(range(seed_len))  # using array subscript as bytes location
    CMP_MAP_BYTES = {}
    process_list = []

    start_time = time.time()
    # iterate seed length, exec fuzzer, gain relation information
    for indexlen in range(0, seed_len):
    # for indexlen in range(0, 1):
        p = Process(target=dynamicExecute, args=(seeds_content, indexlen, static_info_dict, dynamic_info_dict, dynamic_cmp_dict, BYTES_MAP_CMP))
        p.start()
        process_list.append(p)

    num = 0
    print("Fuzzer Loop: {}/{}".format(num, seed_len))
    for pl in process_list:
        pl.join()
        num += 1
        if num % 10 == 0:
            print("Fuzzer Loop: {}/{}".format(num, seed_len))

    print(time.time() - start_time)

    for indexlen in range(0, seed_len):
        for k, _ in BYTES_MAP_CMP[indexlen].items():
            if k in CMP_MAP_BYTES:
                CMP_MAP_BYTES[k].append(indexlen)
            else:
                CMP_MAP_BYTES[k] = [indexlen, ]

    manualAnalysisCmp(BYTES_MAP_CMP, CMP_MAP_BYTES, static_cmp_dict)

    # print(BYTES_MAP_CMP[0])
    # print(CMP_MAP_BYTES)

        # each_dynamic_path_set = set(each_dynamic_path)
        # union_dynamic_path_set = dynamic_path_set | each_dynamic_path_set
        #
        # if len(union_dynamic_path_set - dynamic_path_set) == 0:
        #     os.remove(mutate_filename)
        # else:
        #     dynamic_path_set = union_dynamic_path_set
        # drawDynamicGraph(static_info_dict, draw_dynamic_dict, DRAW_FUNC['main'], "mutatename")


def debugDraw():
    # static_main_addr, static_info_dict, static_cmp_dict = openStaticFile()
    # dynamic_run_cmd = "./../pin320/pin -t ../pin320/source/tools/MyPinTool/obj-intel64/MyPinTool.so -- ./fuzzer_program/base64 -d fuzzer_program/fuzzer_input/rand.b64"
    # dynamic_retcode, dynamic_stdout, dynamic_stderr = run(dynamic_run_cmd)

    # dynamic_run_cmd = "./../pin320/pin -t info_data/MyPinTool.so -- ./fuzzer_program/base64 -d fuzzer_program/fuzzer_input/rand.b64"
    # dynamic_retcode, dynamic_stdout, dynamic_stderr = run(dynamic_run_cmd)
    # print(dynamic_stdout)

    # img_base_ip, dynamic_info_dict = openRebaseDynamicFile(static_main_addr)
    # img_base_ip, dynamic_cmp_dict, dynamic_info_dict = openDynamicFile("info_data/dynamic_info.out")
    # each_dynamic_path, draw_dynamic_dict = gainDynamicInfo(static_info_dict, dynamic_info_dict, DRAW_FUNC['main'])
    # drawDynamicGraph(static_info_dict, draw_dynamic_dict, DRAW_FUNC['main'], "debugm")
    # print(dynamic_cmp_dict)

    static_main_addr, static_info_dict, static_cmp_dict = openStaticFile()
    dynamic_run_cmd = "./../pin320/pin -t info_data/MyPinTool.so -o " + DYNAMIC_SAVE_PATH + DYNAMIC_INIT_FILENAME + " -- ./fuzzer_program/base64 -d fuzzer_program/fuzzer_input/rand.b64"
    dynamic_retcode, dynamic_stdout, dynamic_stderr = run(dynamic_run_cmd)
    img_base_ip, dynamic_cmp_dict, dynamic_info_dict = openDynamicFile(DYNAMIC_SAVE_PATH + DYNAMIC_INIT_FILENAME)
    print(dynamic_info_dict)
    seeds_content = openFuzzSeeds()

    seed_len = len(seeds_content)
    indexlen = 0
    dynamicExecute(seeds_content, indexlen, static_info_dict, dynamic_info_dict, dynamic_cmp_dict)


def main():
    print("-------------------------")
    print("start fuzzing test")
    execFuzz()
    print("end fuzzing test")
    print("-------------------------")

if __name__ == '__main__':
    main()
    # debugDraw()


