import logging
import sys

# Program information.
BTFUZZ = "BTFuzzer"
FILEREPLACE = "@@"

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
MUTATE_STR = "aaabaaac"
STEP = 4  # step size of mutant seeds
TYPE_SUB = 101
TYPE_INSERT = 102

# Logging the information during the fuzzing.
LOG_FORMAT = "%(asctime)s - %(levelname)s - %(message)s"
logging.basicConfig(filename='InfoData/log_data/BTFuzzer.log', level=logging.WARNING, format=LOG_FORMAT)
logging.debug("-------------------------")

LOG_FUNCINFO = lambda : str(sys._getframe(1).f_code.co_name) + ":" + str(sys._getframe(1).f_lineno)

def LOG_STR(funcinfo, *args):
    logstr = "{}-> ".format(funcinfo)
    for content in args:
        logstr += "{} || ".format(content)
    return logstr

DEBUG = 101
INFO = 102
WARNING = 103
ERROR = 104
CRITICAL = 105

def FUZZLOGGING(loggingtype: str, infomation: str) -> None:
    if loggingtype == DEBUG:
        logging.debug(infomation)
    elif loggingtype == INFO:
        logging.info(infomation)
    elif loggingtype == WARNING:
        logging.warning(infomation)
    elif loggingtype == ERROR:
        logging.error(infomation)
    elif loggingtype == CRITICAL:
        logging.critical(infomation)
    else:
        raise Exception("Error logging.")


