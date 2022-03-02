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

COV_TRACE_SWITCH = 'i'
COV_TRACE_DIV4 = 'j'
COV_TRACE_DIV8 = 'k'
COV_TRACE_GEP = 'l'

WEAK_HOOK_MEMCMP = 'm'
WEAK_HOOK_STRNCMP = 'n'
WEAK_HOOK_STRCMP = 'o'
WEAK_HOOK_STRNCASECMP = 'p'
WEAK_HOOK_STRCASECMP = 'q'

START_PC_GUARD = "I"  # (start, end, call_pc)
NUM_PC_GUARD = "S"  # (nums) Numbers of pc guard.
EACH_PC_GUARD = "G"  # (guard, num, call_pc)

END_OF_PROGRAM = "E"  # end


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


