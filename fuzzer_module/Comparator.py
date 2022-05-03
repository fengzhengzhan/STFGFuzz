#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import re
from fuzzer_module.Fuzzconfig import *


def getTarget(program_name: str):
    """
    Get the required number of lines of directed functions corresponding to the binary block position.
    There are three types: git patch, sanitizer, manual.
    @return:
    """
    path_patchloc = PROGRAMS + os.sep + program_name + os.sep + DATAPATCHLOC + os.sep
    target_num = 0
    target_dict: 'dict[target_num:StructTarget]' = {}
    for file_i in os.listdir(path_patchloc):
        fname, ext = os.path.splitext(file_i)
        # print(fname, ext)
        if ext == COM_PATCH:  # github patch
            pass

        if ext == COM_SANITIZER:  # sanitizer
            sanitizer_cont = getFileList(path_patchloc + file_i)
            target_dict[target_num] = StructTarget([], [], [])

            for cont_i in sanitizer_cont:
                line = str(cont_i).replace('\n', '')
                re_str = "#(.*?) 0x.*? in (.*?) .*?:(.*?):(.*)"
                re_cont = re.search(re_str, line)
                if re_cont is not None:
                    cont_groups = re_cont.groups()
                    # print(cont_groups)
                    target_dict[target_num].additem(int(cont_groups[0]), delBrackets(cont_groups[1]),
                                                    int(cont_groups[2]))
            target_num += 1

        if ext == COM_MANUAL:  # manual design
            # target:stack:funcname:line
            # A blank line is required between the different targets of the manual mutation target.
            manual_cont = getFileList(path_patchloc + file_i)
            nums = {}
            # Generate a dictionary of targets for easy finding and navigation.
            for cont_i in manual_cont:
                line = str(cont_i).replace('\n', '').split(":")
                if line[0] == '':
                    continue
                numid = int(line[0])
                if numid not in nums:
                    nums[numid] = StructTarget([int(line[1])], [delBrackets(line[2])], [int(line[3])])
                else:
                    nums[numid].additem(int(line[1]), delBrackets(line[2]), int(line[3]))

            for man_k, man_v in nums.items():
                target_dict[target_num] = man_v
                target_num += 1

    # print(target_dict, target_dict[2].ttrace, target_dict[2].tfunc, target_dict[2].tline)
    return target_dict


def getDirectedNodeLoc(binline_dict: dict, target_dict: 'dict[target_num:StructTarget]'):
    map_numTofuncasm: 'dict[targetnum:dict[funcname:list[asm, asm]]]' = {}
    for tar_k, tar_v in target_dict.items():
        # print(tar_v.ttrace, tar_v.tfunc, tar_v.tline)
        funcToasm = {}
        ttrace, tfunc, tline = tar_v.ttrace, tar_v.tfunc, tar_v.tline
        for idx in range(len(ttrace)):
            # Find the real key in CG Symbols.
            temp_binkey = []
            for bin_kj in binline_dict.keys():
                findres = bin_kj.find(tfunc[idx])
                if findres != -1:
                    temp_binkey.append(bin_kj)
                # print(bin_kj, tfunc[idx], findres)
            # Get the asm instruction.
            for tempbin_kj in temp_binkey:
                if tempbin_kj in binline_dict and tline[idx] in binline_dict[tempbin_kj]:
                    # {'I': '', 'F': '_Z3bugv', 'C': '7', 'N': '', 'D': ''}
                    tempfunc = binline_dict[tempbin_kj][tline[idx]][COM_BINFUNC]
                    tempin = binline_dict[tempbin_kj][tline[idx]][COM_BININ]
                    if tempfunc not in funcToasm:
                        funcToasm[tempfunc] = [tempin]
                    elif tempfunc in funcToasm:
                        funcToasm[tempfunc].append(tempin)
        map_numTofuncasm[tar_k] = funcToasm
    LOG(LOG_DEBUG, LOG_FUNCINFO(), map_numTofuncasm)
    return map_numTofuncasm


def reeHistorySTFG():
    """
    Compare functions and reuse the constraint flow graphs used in the history.
    @return:
    """
    pass
