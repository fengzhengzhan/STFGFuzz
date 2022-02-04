import pickle
import logging
import sys

from variable import *

# open static file to get static information
def openStaticFile(filename=STATIC_FILENAME):
    with open(filename, 'rb') as file:
        static_info_dict = pickle.load(file)
    static_main_addr = int(static_info_dict['main'][0], 16)
    static_cmp_dict = static_info_dict["static_cmp_dict"]
    logging.debug("{}-> {} : {}".format(sys._getframe().f_code.co_name, type(static_info_dict), static_info_dict))
    return static_main_addr, static_info_dict, static_cmp_dict
# open dynamic file
def openDynamicFile(filename):
    dynamic_info_dict = {}
    dynamic_cmp_dict = {}
    img_base_ip = ""
    with open(filename, 'r') as file:
        for eachline in file.readlines():
            split_line = eachline.split(" ")
            eachline_flag = split_line[0]
            # gain dynamic information from eachline, using the first content to distinguish type
            if eachline_flag == INS_IP:
                # ipaddr = hex(int(split_line[1], 16) - int(img_base_ip, 16))
                ipaddr = hex(int(split_line[1], 16))
                dynamic_info_dict[ipaddr] = [INS_IP, ]
            elif eachline_flag == CMP_INS:
                ipaddr = hex(int(split_line[1], 16))
                if ipaddr in dynamic_info_dict:
                    dynamic_info_dict[ipaddr].append(hex(int(split_line[-2], 16)))
                    dynamic_info_dict[ipaddr].append(hex(int(split_line[-1], 16)))
                    dynamic_cmp_dict[ipaddr].append(hex(int(split_line[-2], 16)))
                    dynamic_cmp_dict[ipaddr].append(hex(int(split_line[-1], 16)))
                else:
                    dynamic_info_dict[ipaddr] = [hex(int(split_line[-2], 16)), hex(int(split_line[-1], 16))]
                    dynamic_cmp_dict[ipaddr] = [hex(int(split_line[-2], 16)), hex(int(split_line[-1], 16))]
            elif eachline_flag == OTHER_CMP_INS:
                ipaddr = hex(int(split_line[1], 16))
                dynamic_info_dict[ipaddr] = ['oc_unknown', 'oc_unknown']
            elif eachline_flag == IMG_BASE_ADDR:
                img_base_ip = split_line[2]
            else:
                logging.error("{}-> Error Dynamic information".format(sys._getframe().f_code.co_name))
                raise Exception("Error Dynamic information")
    logging.debug("{}-> {} : {}".format(sys._getframe().f_code.co_name, img_base_ip, dynamic_info_dict))
    return img_base_ip, dynamic_cmp_dict, dynamic_info_dict
# open fuzz seeds
def openFuzzSeeds(filename=INITSEEDS_FILENAME):
    seeds_content = ""
    with open(filename, 'r') as file:
        for each in file.readlines():
            seeds_content += each
    return seeds_content