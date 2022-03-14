import ast
import re
import json

from fuzzer_module.Fuzzconfig import *


class Graph:
    def __init__(self):
        pass


def getPatchInfo(program_name: str) -> 'dict[str:dict[int:dict[str:str]]]':
    """
    From data_patchloc/binaryline.info file parses strings into dictionaries.
    @return:
    """
    # {'function_name':{line:{'':''},line:{'':''}}, }
    temp_patchfile = PROGRAMS + os.sep + program_name + os.sep + DATAGRAPH + os.sep + PATCHFILE
    patchline_info = getFileContent(temp_patchfile)
    pattern = re.compile(r"\s+")
    patchline_sub = re.sub(pattern, ' ', patchline_info)

    # print(patchline_info)
    patchline_dict = ast.literal_eval(patchline_sub)
    # print(patchline_dict['main'])
    LOG(LOG_DEBUG, LOG_STR(LOG_FUNCINFO(), patchline_info, patchline_sub, patchline_dict))
    return patchline_dict


def getCG(cglist):
    # print(cglist)
    for jsonfile in cglist:
        with open(jsonfile, 'r') as f:
            data = json.load(f)
        for k, v in data.items():
            print(k, v)
        # print(data)
        # print(data['objects'])
        # print(len(data))


def getCFG(cfglist):
    for jsonfile in cfglist:
        with open(jsonfile, 'r') as f:
            data = json.load(f)



def buildConstraint():
    """
    Constructing constraint graph.
    @return:
    """


if __name__ == "__main__":
    getPatchInfo("demo")

