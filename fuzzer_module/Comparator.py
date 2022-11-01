#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import random
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
        LOG(DEBUG, LOC(), fname, ext)

        # patch, manual each line as a target.
        # sanitizer has trace information.
        if ext == COM_PATCH and ext in patchtype:  # github diff as patch
            patch_cont = getFileList(path_patchloc + file_i)

            # diff --git a/Modules/demo.cc b/Modules/demo.cc
            # index 5d295d3..79da8ba 100644
            # --- a/Modules/demo.cc
            # +++ b/Modules/demo.cc
            # @@ -123,3 +123,3 @@ int main(int argc, char *argv[]) {
            # -    // bug();
            # -    bug("123");
            # -    bug(123);
            # +    bug();
            # +    // bug("123");
            # +    // bug(123);
            # diff --git a/Modules/test.txt b/Modules/test.txt
            # new file mode 100644
            # index 0000000..e69de29
            patch_list = []
            idx = -1
            for cont_i in patch_cont:
                # line = str(cont_i).replace('\n', '')
                # re_diffstartstr = r"diff --git .*"
                # re_diffstart = re.search(re_diffstartstr, line)
                # LOG(LOG_DEBUG, LOG_FUNCINFO(), line, re_diffstart, showlog=True)
                # if re_diffstart is not None:
                #     target_num += 1
                #     target_dict[target_num] = []
                #     target_dict[target_num].append([COM_PATCH, file_i, target_num])

                # re_funcfile_str = r"\+\+\+ (.*)"
                # re_funcfile = re.findall(re_funcfile_str, line)
                # if len(re_funcfile) != 0:
                #     funcfile = re_funcfile[0]

                re_funcline_str = r"@@ -\d*?,\d*? \+(\d*?),\d*? @@"
                re_funcline = re.findall(re_funcline_str, cont_i)
                if len(re_funcline) != 0:
                    funcline = int(re_funcline[0])
                    re_funcname_str = r"@@.*?@@.* (.*?)\(.*"
                    re_funcname = re.findall(re_funcname_str, cont_i)
                    if len(re_funcname) != 0:
                        idx += 1
                        patch_list.append([idx, re_funcname[0], funcline])

            LOG(DEBUG, LOC(), patch_list, show=True)
            for patch_i in patch_list:
                target_num += 1
                target_dict[target_num] = []
                target_dict[target_num].append([COM_PATCH, file_i, target_num])
                target_dict[target_num].append(patch_i)

        if ext == COM_SANITIZER and ext in patchtype:  # clang sanitizer
            sanitizer_cont = getFileList(path_patchloc + file_i)
            # LOG(DEBUG, LOC(), sanitizer_cont, show=True)

            for cont_i in sanitizer_cont:
                line = delBrackets(str(cont_i).replace('\n', ''))
                re_str = r"#(.*?) 0x.*? in (.*?) .*?:(.*?):(.*)"
                re_cont = re.search(re_str, line)
                # print(re_cont)
                if re_cont is not None:
                    cont_groups = re_cont.groups()
                    if int(cont_groups[0]) == 0:
                        target_num += 1
                        target_dict[target_num] = []
                        target_dict[target_num].append([COM_SANITIZER, file_i, target_num])
                    # print(cont_groups)
                    LOG(DEBUG, LOC(), line, int(cont_groups[0]), cont_groups[1],
                        cont_groups[2])
                    target_dict[target_num].append([int(cont_groups[0]), cont_groups[1],
                                                    int(cont_groups[2])])
            # print(target_dict[0])

        if ext == COM_MANUAL and ext in patchtype:  # manual design
            # filename:line
            # A blank line is required between the different targets of the manual mutation target.
            manual_cont = getFileList(path_patchloc + file_i)

            # Generate a dictionary of targets for easy finding and navigation.
            idx = -1
            for cont_i in manual_cont:
                line = str(cont_i).replace('\n', '').split(":")
                if line[0] == '':
                    continue
                target_num += 1
                target_dict[target_num] = []
                target_dict[target_num].append([COM_MANUAL, file_i, target_num])
                idx += 1
                target_dict[target_num].append([idx, line[0], int(line[1])])

    # Add Greybox fuzzing.
    target_num += 1
    target_dict[target_num] = []
    target_dict[target_num].append([COM_GREYBOX, COM_GREYBOX, target_num])

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
        patchflag = tgt_v[0][0]
        if patchflag == COM_SANITIZER or patchflag == COM_PATCH:
            for each in tgt_v[1:]:  # Skip the first line for information describe.
                ttrace, tfunc, tline = each[0], each[1], each[2]
                # print(ttrace, tfunc, tline)
                # Find the real key in CG Symbols.
                binkey = []
                for bin_kj in binline_dict.keys():
                    findres = bin_kj.find(tfunc)
                    if findres != -1:
                        binkey.append(bin_kj)
                    # print(bin_kj, tfunc[each], findres)
                # Get the asm instruction.
                for bin_kj in binkey:
                    if tline in binline_dict[bin_kj]:
                        # {'I': '', 'F': '_Z3bugv', 'C': '7', 'N': '', 'D': ''}
                        tempfunc = binline_dict[bin_kj][tline][COM_BINFUNC]
                        tempins = binline_dict[bin_kj][tline][COM_BININS]
                        if tempfunc not in func_asm:
                            func_asm[tempfunc] = [[ttrace, tempins]]
                        elif tempfunc in func_asm:
                            func_asm[tempfunc].append([ttrace, tempins])
        elif patchflag == COM_MANUAL:
            for each in tgt_v[1:]:
                ttrace, tfile, tline = each[0], each[1], each[2]
                for binfunc_ki, binlineasm_vi in binline_dict.items():
                    LOG(DEBUG, LOC(), binfunc_ki, binlineasm_vi)
                    if len(binlineasm_vi) == 0:
                        continue
                    bininfo_dict = binlineasm_vi[random.sample(binlineasm_vi.keys(), 1)[0]]
                    LOG(DEBUG, LOC(), bininfo_dict[COM_BINFUNC], bininfo_dict[COM_BINFILE], show=True)
                    if tfile == bininfo_dict[COM_BINFILE]:
                        if tline in binlineasm_vi:
                            # {'I': '', 'F': '_Z3bugv', 'C': '7', 'N': '', 'D': ''}
                            tempfunc = binlineasm_vi[tline][COM_BINFUNC]
                            tempins = binlineasm_vi[tline][COM_BININS]
                            if tempfunc not in func_asm:
                                func_asm[tempfunc] = [[ttrace, tempins]]
                            elif tempfunc in func_asm:
                                func_asm[tempfunc].append([ttrace, tempins])

        map_numTofuncasm[tgt_k] = func_asm
    LOG(DEBUG, LOC(), map_numTofuncasm, show=True)
    return map_numTofuncasm


def compareTargetDiff(before_path, target_dict):
    """
    If the targets are different that return True.
    @return:
    """
    LOG(DEBUG, LOC(), before_path, show=True)
    cmptgt = True
    before_target_file = before_path + B4TGT_FILE
    if os.path.exists(before_target_file):
        before_target_dict = loadFromPkl(before_target_file)
        if before_target_dict == target_dict:
            cmptgt = False
    return cmptgt


def reeHistorySTFG():
    """
    Compare functions and reuse the constraint flow graphs used in the history.
    @return:
    """
    pass
