import logging
import sys

from Tools import *

# Program information.
BTFUZZ = "BTFuzzer"
FILEREPLACE = "@@"
INIT = 100


# Struct
# The structure stores information about the seed file.
class StructSeed:
    def __init__(self, filename: str, content: str, seedtype: int, location: list):
        self.filename = filename
        if content == "":
            self.content = getSeedContent(filename)
        else:
            self.content = content
        self.seedtype = seedtype  # INIT MUT_TYPE_SUB MUT_TYPE_INSERT
        self.location = location


# The structure stores information about trace report.
class StructTraceReport:
    def __init__(self, startguard: int, endguard: int, constraint: 'list[str]', stvalue: 'list[list[str, str]]', programcontent: 'list[str]'):
        self.startguard = startguard
        self.endguard = endguard
        self.constraint = constraint
        self.stvalue = stvalue
        self.progcontent = programcontent


class StructComparisonReport:
    def __init__(self, mutseed: StructSeed, sttype: str, init_sttrace: list, mut_sttrace: list, startguard: int, endguard: int, stpcguard: str):
        self.mutseed = mutseed
        self.sttype = sttype
        self.init_sttrace = init_sttrace
        self.mut_sttrace = mut_sttrace
        self.startguard = startguard
        self.endguard = endguard
        self.stpcguard = stpcguard


# This is the global compare command mapping.
class StructCmpMap:
    def __init__(self):
        self.cmpmap: 'dict[StructCmpInfo]' = {}


class StructCmpInfo:
    def __init__(self, cmptype, startguard, endguard, inputmap: list):
        self.cmptype = cmptype
        self.startguard = startguard
        self.endguard = endguard
        self.inputmap = inputmap  # Compare the input bytes involved in the instruction.


# This is the global constraint graph.
class StructConstraintGraph:
    def __init__(self):
        self.constraintgraph = []

# The fisrt character represent the type of compare instruction.
# In order to save space, using one character as the flag to mark.
# The meaning of the parameters following the flags is described in the comments.
COV_TRACE_CMP1 = 'a'  # (call_pc, arg1, arg2, arg_len)
COV_TRACE_CMP2 = 'b'
COV_TRACE_CMP4 = 'c'
COV_TRACE_CMP8 = 'd'

COV_TRACE_CONST_CMP1 = 'e'
COV_TRACE_CONST_CMP2 = 'f'
COV_TRACE_CONST_CMP4 = 'g'
COV_TRACE_CONST_CMP8 = 'h'

TRACECMPLIST = [COV_TRACE_CMP1, COV_TRACE_CMP2,
           COV_TRACE_CMP4, COV_TRACE_CMP8,
           COV_TRACE_CONST_CMP1, COV_TRACE_CONST_CMP2,
           COV_TRACE_CONST_CMP4, COV_TRACE_CONST_CMP8]

COV_TRACE_SWITCH = 'i'  # (call_pc, num_case, size_val, case_n...)
COV_TRACE_DIV4 = 'j'
COV_TRACE_DIV8 = 'k'
COV_TRACE_GEP = 'l'

WEAK_HOOK_MEMCMP = 'm'  # (call_pc, <s1"  "1s>, <s2"  "2s>, size_n, result)
WEAK_HOOK_STRNCMP = 'n'
WEAK_HOOK_STRCMP = 'o'
WEAK_HOOK_STRNCASECMP = 'p'
WEAK_HOOK_STRCASECMP = 'q'

HOOKCMPLIST = [WEAK_HOOK_MEMCMP, WEAK_HOOK_STRNCMP,
               WEAK_HOOK_STRCMP, WEAK_HOOK_STRNCASECMP,
               WEAK_HOOK_STRCASECMP]

END_EACH_FLAG = "Z"  # End of each line.
INIT_PC_GUARD = "I"  # (call_pc, start, end)
NUM_PC_GUARD = "S"  # (call_pc, nums) Numbers of pc guard, from 1 to number.
EACH_PC_GUARD = "G"  # (call_pc, guard_addr, guard_num)

PROGRAM_END = "E"  # end

# Reverse Correspondence
FLAG_DICT = {'a': "COV_TRACE_CMP1",
             'b': "COV_TRACE_CMP2",
             'c': "COV_TRACE_CMP4",
             'd': "COV_TRACE_CMP8",
             'e': "COV_TRACE_CONST_CMP1",
             'f': "COV_TRACE_CONST_CMP2",
             'g': "COV_TRACE_CONST_CMP4",
             'h': "COV_TRACE_CONST_CMP8",
             'i': "COV_TRACE_SWITCH",
             'j': "COV_TRACE_DIV4",
             'k': "COV_TRACE_DIV8",
             'l': "COV_TRACE_GEP",
             'm': "WEAK_HOOK_MEMCMP",
             'n': "WEAK_HOOK_STRNCMP",
             'o': "WEAK_HOOK_STRCMP",
             'p': "WEAK_HOOK_STRNCASECMP",
             'q': "WEAK_HOOK_STRCASECMP",
             'Z': "END_EACH_FLAG",
             'I': "INIT_PC_GUARD",
             'S': "NUM_PC_GUARD",
             'G': "EACH_PC_GUARD",
             'E': "PROGRAM_END",
             }

# Parameter Location Index
IND_CMP_TYPE = 0
IND_CALLPC = 1
IND_ARG1 = 2
IND_ARG2 = 3
IND_ARGLEN = 4

IND_S1 = 2
IND_S2 = 3
IND_SIZEN = 4
IND_RESULT = 5

IND_NUMCASE = 2
IND_SIZEVAL = 3

IND_MUT_TYPE = 0
IND_MUT_START = 1
IND_MUT_END = 2

# Analyzer
ANA_STARTPROG_IND = -1
ANA_ENDPROG_IND = -2

# Generator
SEEDPOOL = "SeedPool"
INITSEEDS = "init_seeds"
CRASHSEEDS = "crash_seeds"
MUTATESEEDS = "mutate_seeds"
INFODATA = "InfoData"
GRAPHDATA = "graph_data"
# clang $1.c -emit-llvm -S
# opt -dot-cfg $1.ll > /dev/null   // get CFG
# opt -dot-callgraph $1.ll > /dev/null   // get CG
# dot -Tpng -o $1.png cfg.main.dot
# dot -Tpng -o $1.callgraph.png callgraph.dot
DOTCALLGRAPH = "opt -dot-callgraph "
DOTCFG = "opt -dot-cfg "
CG_SUFFIX = ".callgraph.dot"
CFG_SUFFIX = ".dot"

# Mutator
MUT_STR = "aaabaaac"
MUT_MATCH = 4  # Truncate 4 bytes as a fast variant flag for fast matching.
MUT_STEP = 4  # step size of mutant seeds
MUT_TYPE_SUB = 101
MUT_TYPE_INSERT = 102

# Parser
PAR_FIXED = 201
PAR_CHANGED = 202

# Scheduler
SCH_INIT_SEED = 221
SCH_MUT_SEED = 222

# Visualizer
# Red for frozen bytes.
# Yellow is the confirmation bytes.
# White is undetected bytes.
# Blue is the raw bytes.
VIS_BLACK = 1
VIS_BLUE = 2
VIS_CYAN = 3
VIS_GREEN = 4
VIS_MAGENTA = 5
VIS_RED = 6
VIS_WHITE = 7
VIS_YELLOW = 8

VIS_A = 97
VIS_P = 112
VIS_Q = 113
VIS_S = 115
VIS_SEED_LINE = 16


# Logging the information during the fuzzing.
LOG_FORMAT = "%(asctime)s - %(levelname)s - %(message)s"
logging.basicConfig(filename='InfoData/log_data/BTFuzzer.log', level=logging.WARNING, format=LOG_FORMAT)
logging.debug("-------------------------")

LOG_FUNCINFO = lambda : str(sys._getframe(1).f_code.co_name) + ":" + str(sys._getframe(1).f_lineno)

LOG_DEBUG = 251
LOG_INFO = 252
LOG_WARNING = 253
LOG_ERROR = 254
LOG_CRITICAL = 255


def LOG_STR(funcinfo, *args):
    logstr = "{}-> ".format(funcinfo)
    for content in args:
        logstr += "{} || ".format(content)
    return logstr


def LOG(loggingtype: str, infomation: str) -> None:
    if loggingtype == LOG_DEBUG:
        logging.debug(infomation)
    elif loggingtype == LOG_INFO:
        logging.info(infomation)
    elif loggingtype == LOG_WARNING:
        logging.warning(infomation)
    elif loggingtype == LOG_ERROR:
        logging.error(infomation)
    elif loggingtype == LOG_CRITICAL:
        logging.critical(infomation)
    else:
        raise Exception("Error logging.")


