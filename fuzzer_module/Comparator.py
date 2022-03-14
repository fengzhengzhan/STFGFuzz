
from fuzzer_module.Fuzzconfig import *


def getDirectedLocation(programe_name: str, filetype: str, filename=[]):
    """
    Get the required number of lines of directed functions corresponding to the binary block position.
    There are three types: git patch, sanitizer, manual.
    @return:
    """
    target_dict: 'dict[target:[StructTarget, ]]' = {}
    if filetype == COM_PATCH:
        pass

    if filetype == COM_SANITIZER:
        pass

    if filetype == COM_MANUAL:
        # target:stack:funcname:line
        # A blank line is required between the different targets of the manual mutation target.
        temp_manualfile = PROGRAMS + os.sep + programe_name + os.sep + DATAPATCHLOC + os.sep + COM_MANUAL_FILE
        manual_cont = getFileList(temp_manualfile)

        # Generate a dictionary of targets for easy finding and navigation.
        for each in manual_cont:
            if each == '\n':
                continue
            line = str(each).replace('\n', '').split(":")
            target_num = int(line[0])
            if target_num not in target_dict:
                target_dict[target_num] = [StructTarget(
                    target_num,
                    int(line[1], 10),
                    line[2],
                    int(line[3])
                )]
            else:
                target_dict[target_num].append(
                    StructTarget(
                        target_num,
                        int(line[1], 10),
                        line[2],
                        int(line[3])
                    )
                )

        # print(target_dict[1][1].__dict__)

    return target_dict


def reuseHistorySTFG():
    """
    Compare functions and reuse the constraint flow graphs used in the history.
    @return:
    """
    pass

