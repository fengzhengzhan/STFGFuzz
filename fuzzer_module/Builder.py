import ast
import re

from fuzzer_module.Fuzzconfig import *


def getPatchInfo(program_name: str):
    """
    From data_patchloc/binaryline.info file parses strings into dictionaries.
    @return:
    """
    # {'function_name':{line:{'':''},line:{'':''}}, }
    temp_patchfile = PROGRAMS + os.sep + program_name + os.sep + PATCHFILE
    patchline_info = getFileContent(temp_patchfile)
    pattern = re.compile(r"\s+")
    patchline_sub = re.sub(pattern, ' ', patchline_info)

    # print(patchline_info)
    patchline_dict = ast.literal_eval(patchline_sub)
    # print(patchline_dict['main'])
    LOG(LOG_DEBUG, LOG_STR(LOG_FUNCINFO(), patchline_info, patchline_sub, patchline_dict))
    



def buildConstraint():
    """
    Constructing constraint graph.
    @return:
    """


if __name__ == "__main__":
    getPatchInfo("demo")

