#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import re
from fuzzer_module.Fuzzconfig import *


def getTarget(path_patchloc, patchtype:list):
    """
    Get the required number of lines of directed functions corresponding to the binary block position.
    There are three types: git patch, sanitizer, manual.
    @return:
    """
    target_num = 0
    target_dict: 'dict[target_num:StructTarget]' = {}
    for file_i in os.listdir(path_patchloc):
        file_split = file_i.split(".")
        fname, ext = file_split[0], file_split[-1]
        LOG(LOG_DEBUG, LOG_FUNCINFO(), fname, ext)
        if ext == COM_PATCH and ext in patchtype:  # github patch
            pass

        if ext == COM_SANITIZER and ext in patchtype:  # sanitizer
            sanitizer_cont = getFileList(path_patchloc + file_i)
            target_dict[target_num] = StructTarget([], 3)

            for cont_i in sanitizer_cont:
                line = str(cont_i).replace('\n', '')
                re_str = "#(.*?) 0x.*? in (.*?) .*?:(.*?):(.*)"
                re_cont = re.search(re_str, line)
                # print(re_cont)
                if re_cont is not None:
                    cont_groups = re_cont.groups()
                    # print(cont_groups)
                    target_dict[target_num].addone(int(cont_groups[0]), delBrackets(cont_groups[1]),
                                                    int(cont_groups[2]))
            target_num += 1
            # print(target_dict[0].tgttrace)

        if ext == COM_MANUAL and ext in patchtype:  # manual design
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
                    nums[numid] = StructTarget([], 3).addone(int(line[1]), delBrackets(line[2]), int(line[3]))
                else:
                    nums[numid].addone(int(line[1]), delBrackets(line[2]), int(line[3]))

            for man_k, man_v in nums.items():
                target_dict[target_num] = man_v
                target_num += 1

    # print(target_dict, target_dict[2].ttrace, target_dict[2].tfunc, target_dict[2].tline)
    return target_dict


def getDirectedNodeLoc(binline_dict: dict, target_dict: 'dict[target_num:StructTarget]'):
    """
    Get the IR of the target position
    @return:
    """
    # print(binline_dict.keys())
    map_numTofuncasm: '{targetnum:{funcname:[[id,asm],[id,asm],...]}}' = {}
    for tgt_k, tgt_v in target_dict.items():
        # print(tgt_v.ttrace, tgt_v.tfunc, tgt_v.tline)
        functo_asm = {}
        tgttrace = tgt_v.tgttrace
        for each in tgttrace:
            ttrace, tfunc, tline = each[0], each[1], each[2]
            # print(ttrace, tfunc, tline)
            # Find the real key in CG Symbols.
            temp_binkey = []
            for bin_kj in binline_dict.keys():
                findres = bin_kj.find(tfunc)
                if findres != -1:
                    temp_binkey.append(bin_kj)
                # print(bin_kj, tfunc[each], findres)
            # Get the asm instruction.
            for tempbin_kj in temp_binkey:
                if tempbin_kj in binline_dict and tline in binline_dict[tempbin_kj]:
                    # {'I': '', 'F': '_Z3bugv', 'C': '7', 'N': '', 'D': ''}
                    tempfunc = binline_dict[tempbin_kj][tline][COM_BINFUNC]
                    tempins = binline_dict[tempbin_kj][tline][COM_BININS]
                    if tempfunc not in functo_asm:
                        functo_asm[tempfunc] = [[ttrace, tempins]]
                    elif tempfunc in functo_asm:
                        functo_asm[tempfunc].append([ttrace, tempins])
        map_numTofuncasm[tgt_k] = functo_asm
    LOG(LOG_DEBUG, LOG_FUNCINFO(), map_numTofuncasm, showlog=True)
    return map_numTofuncasm


def reeHistorySTFG():
    """
    Compare functions and reuse the constraint flow graphs used in the history.
    @return:
    """
    pass
