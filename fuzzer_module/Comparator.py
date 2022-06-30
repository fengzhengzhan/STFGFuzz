#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import re
from fuzzer_module.Fuzzconfig import *
from .Structures import *


def getTarget(path_patchloc, patchtype: list):
    """
    Get the required number of lines of directed functions corresponding to the binary block position.
    There are three types: git patch, sanitizer, manual.
    @return:
    """
    target_num = -1
    # [[0, 'bug', 18], [1, 'main', 109], [2, '__libc_start_main', 308]]
    target_dict: 'dict[target_num:[[ttrace, tfunc, tline]]]' = {}  # The first line determine the type of patch
    for file_i in os.listdir(path_patchloc):
        file_split = file_i.split(".")
        fname, ext = file_split[0], file_split[-1]
        LOG(LOG_DEBUG, LOG_FUNCINFO(), fname, ext, showlog=True)

        if ext == COM_PATCH and ext in patchtype:  # github diff as patch
            pass

        if ext == COM_SANITIZER and ext in patchtype:  # clang sanitizer
            sanitizer_cont = getFileList(path_patchloc + file_i)

            for cont_i in sanitizer_cont:
                line = str(cont_i).replace('\n', '')
                re_str = "#(.*?) 0x.*? in (.*?) .*?:(.*?):(.*)"
                re_cont = re.search(re_str, line)
                # print(re_cont)
                if re_cont is not None:
                    cont_groups = re_cont.groups()
                    if int(cont_groups[0]) == 0:
                        target_num += 1
                        target_dict[target_num] = []
                        target_dict[target_num].append([COM_SANITIZER, file_i, target_num])
                    # print(cont_groups)
                    target_dict[target_num].append([int(cont_groups[0]), delBrackets(cont_groups[1]),
                                                    int(cont_groups[2])])
            # print(target_dict[0])

        if ext == COM_MANUAL and ext in patchtype:  # manual design
            # filename:line
            # A blank line is required between the different targets of the manual mutation target.
            manual_cont = getFileList(path_patchloc + file_i)
            target_num += 1
            target_dict[target_num] = []
            target_dict[target_num].append([COM_MANUAL, file_i, target_num])

            # Generate a dictionary of targets for easy finding and navigation.
            idx = -1
            for cont_i in manual_cont:
                line = str(cont_i).replace('\n', '').split(":")
                if line[0] == '':
                    continue
                idx += 1
                target_dict[target_num].append([idx, line[0], int(line[1])])

    LOG(LOG_DEBUG, LOG_FUNCINFO(), target_dict, showlog=True)
    raise Exception
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
        func_asm = {}
        for each in tgt_v:
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
                    if tempfunc not in func_asm:
                        func_asm[tempfunc] = [[ttrace, tempins]]
                    elif tempfunc in func_asm:
                        func_asm[tempfunc].append([ttrace, tempins])
        map_numTofuncasm[tgt_k] = func_asm
    # LOG(LOG_DEBUG, LOG_FUNCINFO(), map_numTofuncasm, showlog=True)
    return map_numTofuncasm


def compareTargetDiff(before_path, target_dict):
    """
    If the targets are different that return True.
    @return:
    """
    LOG(LOG_DEBUG, LOG_FUNCINFO(), before_path, showlog=True)
    cmptgt = True
    before_target_file = before_path + B4TGT_FILE
    if os.path.exists(before_target_file):
        before_target_dict = loadFromPkl(before_target_file)
        if before_target_dict == target_dict:
            cmptgt = False
    saveAsPkl(before_target_file, target_dict)
    return cmptgt


def reeHistorySTFG():
    """
    Compare functions and reuse the constraint flow graphs used in the history.
    @return:
    """
    pass
