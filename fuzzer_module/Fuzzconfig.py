import logging
import os
import sys

from fuzzer_module.Structures import *

# Program information.
'''Main Fuzzer'''
FUZZNAME = "STFGFuzzer"
FILEREPLACE = "@@"
INIT = 100
USE_INITNUM = -1
USE_ENDNUM = -2
USE_EXCEPTION = -3
USE_INITSTR = ""

COARSE_STR = "coarse"
FINE_STR = "fine"


# The fisrt character represent the type of compare instruction.
# In order to save space, using one character as the flag to mark.
# The meaning of the parameters following the flags is described in the comments.
# trace
COV_CMP1 = 'a'  # (call_pc, arg1, arg2, arg_len)
COV_CMP2 = 'b'
COV_CMP4 = 'c'
COV_CMP8 = 'd'

COV_CONSTCMP1 = 'e'
COV_CONSTCMP2 = 'f'
COV_CONSTCMP4 = 'g'
COV_CONSTCMP8 = 'h'

TRACECMPSET = {COV_CMP1, COV_CMP2, COV_CMP4, COV_CMP8, COV_CONSTCMP1, COV_CONSTCMP2, COV_CONSTCMP4, COV_CONSTCMP8}

COV_SWITCH = 'i'  # (call_pc, num_case, size_val, case_n...)
COV_DIV4 = 'j'
COV_DIV8 = 'k'
COV_GEP = 'l'

# weak hook
HOOK_MEMCMP = 'm'  # (call_pc, <s1"  "1s>, <s2"  "2s>, size_n, result)
HOOK_STRNCMP = 'n'
HOOK_STRCMP = 'o'
HOOK_STRNCASECMP = 'p'
HOOK_STRCASECMP = 'q'

HOOKCMPSET = {HOOK_MEMCMP, HOOK_STRNCMP, HOOK_STRCMP, HOOK_STRNCASECMP, HOOK_STRCASECMP}

SHMID_FLAG = "D"  # Content show from stdout, that represent the memory share id.
INTERLEN_FLAG = "L"  # The length of array.
INTERLEN_VALUE = 16  # The space bytes in the start of content represents interlen values.
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
IDX_CMP_TYPE = 0
IDX_FUNCPC = 1
IDX_CALLERPC = 2
IDX_ARG1 = 2
IDX_ARG2 = 3
IDX_ARGLEN = 4

IDX_S1 = 2
IDX_S2 = 3
IDX_SIZEN = 4
IDX_RESULT = 5

IDX_NUMCASE = 2
IDX_SIZEVAL = 3

IDX_MUT_TYPE = 0
IDX_MUT_START = 1
IDX_MUT_END = 2


'''Analyzer'''
ANA_ENDPROG_IDX = -2
ANA_MEMSHM_MODE = True
ANA_INTERLEN_SIZE = 16
ANA_SHM_INTERVAL = 1024 * 1024
ANA_CMPCOVSHM_NAME = "cmpcovshm"

'''Builder'''
BUI_PATCHFILE = "binaryline.info"
BUI_NAME = "name"
BUI_NODES = "objects"
BUI_EDGES = "edges"
BUI_NODE_NUM = "_gvid"
BUI_NODE_NAME = "name"
BUI_NODE_LABEL = "label"  # node text
BUI_EDGE_NUM = "_gvid"
BUI_EDGE_START = "tail"  # tail -> head
BUI_EDGE_END = "head"
BUI_EDGE_START_IDX = 0  # tail -> head
BUI_EDGE_END_IDX = 1
BUI_INIT_WEIGHT = 0
BUI_GUARD_RE = "@__sanitizer_cov_trace_pc_guard\(i32\* inttoptr \(i64 add \(i64\\\\l... ptrtoint \(\[15 x i32\]\* @__sancov_gen_.2 to i64\), i64 (.*)\) to i32\*\)\)"
BUI_LOC_INTERVAL = 4
BUI_NODE_ST = "nodest"

'''Comparator'''
COM_PATCH = 'patch'
COM_SANITIZER = 'sanitizer'
COM_MANUAL = 'manual'
COM_PATCHSET = {USE_INITNUM, COM_PATCH, COM_SANITIZER, COM_MANUAL}

COM_PATCH_FILE = 'errors_patch.info'
COM_SANITIZER_FILE = 'errors_sanitizer.info'
COM_MANUAL_FILE = "errors_manual.info"

'''Generator'''
PROGRAMS = "Programs"
CODESOURCES = "code_sources"
CODEBIN = "code_Bin"
CODEIR = "code_IR"
DATAGRAPH = "data_graph"
DATAPATCHLOC = "data_patchloc"
SEEDSINIT = "seeds_init"
SEEDSMUTATE = "seeds_mutate"
SEEDSCRASH = "seeds_crash"
# clang $1.c -emit-llvm -S
# opt -dot-cfg $1.ll > /dev/null   // get CFG
# opt -dot-callgraph $1.ll > /dev/null   // get CG
# dot -Tpng -o $1.png cfg.main.dot
# dot -Tpng -o $1.callgraph.png callgraph.dot
GEN_DOTCALLGRAPH = "opt -dot-callgraph "
GEN_DOTCFG = "opt -dot-cfg "
GEN_CG_SUFFIX = ".callgraph.dot"
GEN_CFG_SUFFIX = ".dot"
GEN_DOTJSON = "dot -Tdot_json "
GEN_OVERLAY = " > "
GEN_APPEND = " >> "
GEN_TRACEBC_SUFFIX = "_trace.bc"



'''Mutator'''
MUT_STR = "AAABAAAC"
MUT_MATCH = 4  # Truncate 4 bytes as a fast variant flag for fast matching.
MUT_STEP = 4  # step size of mutant seeds
MUT_TYPE_SUB = 101
MUT_TYPE_INSERT = 102

'''Parser'''
PAR_FIXED = 201
PAR_CHANGED = 202

PAR_MAGIC1_TYPE = 181  # fixed changed
PAR_MAGIC2_TYPE = 182  # changed fixed
PAR_CHECKSUMS_TYPE = 183  # changed changed
PAR_FIX_TYPE = 184  # fixed fixed

PAR_VARINIT = 0
PAR_VARMUT = 1


'''Scheduler'''
SCH_INIT_SEED = 221
SCH_MUT_SEED = 222
SCH_THIS_SEED = 223

SCH_SAVEASFILE = True

SCH_SLID_WINDOW = 8

'''Visualizer'''
# Red for frozen bytes.
# Yellow is the change bytes.
# _ is the confirmation bytes.
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
VIS_N = 110
VIS_P = 112
VIS_Q = 113
VIS_S = 115
VIS_SEED_LINE = 16

VIS_MAX_LINE = 25

VIS_TERMINAL = False
VIS_SHOWGRAPH = True
VIS_CG_NAME = "CG.gv"
VIS_CFG_NAME = "CFG.gv"
VIS_DPI = 300

'''Logging'''
# Logging the information during the fuzzing.
# LOG(LOG_DEBUG, LOG_STR(LOG_FUNCINFO(), arg1, arg2, arg3))
LOG_FORMAT = "%(asctime)s - %(levelname)s - %(message)s"
try:
    logging.basicConfig(filename='Programs/{}.log'.format(FUZZNAME), level=logging.WARNING, format=LOG_FORMAT)
except:
    logging.basicConfig(filename='{}.log'.format(FUZZNAME), level=logging.WARNING, format=LOG_FORMAT)
logging.debug("{} -------------------------".format(FUZZNAME))

LOG_FUNCINFO = lambda : str(sys._getframe(1).f_code.co_name) + ":" + str(sys._getframe(1).f_lineno)

LOG_DEBUG = 251
LOG_INFO = 252
LOG_WARNING = 253
LOG_ERROR = 254
LOG_CRITICAL = 255


def LOG_STR(funcinfo, *args, print_mode=False):
    logstr = "{}-> ".format(funcinfo)
    for content in args:
        logstr += "{} || ".format(content)
    if print_mode:
        print(logstr)
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


