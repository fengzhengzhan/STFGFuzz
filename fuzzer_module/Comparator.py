import re
from fuzzer_module.Fuzzconfig import *


def getDirectedLocation(program_name: str):
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
                    target_dict[target_num].additem(int(cont_groups[0]), cont_groups[1], int(cont_groups[2]))
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
                    nums[numid] = StructTarget([int(line[1])], [line[2]], [int(line[3])])
                else:
                    nums[numid].additem(int(line[1]), line[2], int(line[3]))

            for man_k, man_v in nums.items():
                target_dict[target_num] = man_v
                target_num += 1

    print(target_dict, target_dict[2].ttrace, target_dict[2].tfunc, target_dict[2].tline)
    return target_dict

def reuseHistorySTFG():
    """
    Compare functions and reuse the constraint flow graphs used in the history.
    @return:
    """
    pass
