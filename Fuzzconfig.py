import logging


# The fisrt character represent the type of compare instruction.
# In order to save space, using one character as the flag to mark.
COV_TRACE_CMP1 = 'a'
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


LOG_FORMAT = "%(asctime)s - %(levelname)s - %(message)s"
logging.basicConfig(filename='InfoData/log_data/BTFuzzer.log', level=logging.WARNING, format=LOG_FORMAT)
logging.debug("-------------------------")

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


