#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import logging
import os
import sys

from fuzzer_module.Tools import *

# Program information.
'''Main Fuzzer'''
FUZZNAME = "STFGFuzzer"
FUZZPRINTLOG = FUZZNAME + "_show.log"
FILEREPLACE = "@@"
USE_INITNUM = -1
USE_INITMAXNUM = 0x7fffffff
USE_ENDNUM = -2
USE_EXCEPTION = -3
USE_INITSTR = ""
USE_INITCONTENT = b'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX'
QUIT_FUZZ = 11
LIMITER = 100000
FUZZ_DIRECTED = 60
FUZZ_GERYBOX = 61


EXP_MODE = False
# EXP_MODE = True
VIS_TERM = True
# VIS_TERM = False
# VIS_SHOWGRAPH = True
VIS_SHOWGRAPH = False

AUTO_SEED = "auto.seed"
EXPAND_SEED = "expand.seed"

COARSE_STR = "coarse"
FINE_STR = "fine"
ST_STR = "st"
REPEAT_STR = "repeat"
LENGTH_STR = "length"
LD_EXPAND = 128

STG_LD = "LengthDetect"
STG_SD = "SlidingDetect"
STG_BD = "ByteDetect"
STG_ST = "Strategy"

SLID_GAP = 2

B4TGT_FILE = ".before_target_dict.pkl"

# The fisrt character represent the type of compare instruction.
# In order to save space, using one character as the flag to mark.
# The meaning of the parameters following the flags is described in the comments.
# trace
# dict has no call_pc(cmpid) to save storage space
COV_CMP1 = 'a'  # (info, cmpid, arg1, arg2, arg_len)  dict.pop(cmpid)
COV_CMP2 = 'b'
COV_CMP4 = 'c'
COV_CMP8 = 'd'

COV_CONSTCMP1 = 'e'
COV_CONSTCMP2 = 'f'
COV_CONSTCMP4 = 'g'
COV_CONSTCMP8 = 'h'

TRACENUMCMPSET = {COV_CMP1, COV_CMP2, COV_CMP4, COV_CMP8, COV_CONSTCMP1, COV_CONSTCMP2, COV_CONSTCMP4, COV_CONSTCMP8}
NUMCMPBIT_DICT = {COV_CMP1: 1, COV_CMP2: 2, COV_CMP4: 4, COV_CMP8: 8,
                  COV_CONSTCMP1: 1, COV_CONSTCMP2: 2, COV_CONSTCMP4: 4, COV_CONSTCMP8: 8}

COV_SWITCH = 'i'  # (info, call_pc, num_case, size_val, val, case_n...)  dict.pop(cmpid)
COV_DIV4 = 'j'
COV_DIV8 = 'k'
COV_GEP = 'l'

# weak hook
HOOK_MEMCMP = 'm'  # (info, call_pc, s1, s2, size_n, result)  dict.pop(cmpid)
HOOK_STRNCMP = 'n'
HOOK_STRCMP = 'o'
HOOK_STRNCASECMP = 'p'
HOOK_STRCASECMP = 'q'

HOOKSTRCMPSET = {HOOK_MEMCMP, HOOK_STRNCMP, HOOK_STRCMP, HOOK_STRNCASECMP, HOOK_STRCASECMP}

CMPSET = {COV_CMP1, COV_CMP2, COV_CMP4, COV_CMP8, COV_CONSTCMP1, COV_CONSTCMP2, COV_CONSTCMP4, COV_CONSTCMP8,
          HOOK_MEMCMP, HOOK_STRNCMP, HOOK_STRCMP, HOOK_STRNCASECMP, HOOK_STRCASECMP,
          COV_SWITCH, COV_DIV4, COV_DIV8, COV_GEP}

UNDEFINE = 'z'

SHMID_FLAG = 'D'  # Content show from stdout, that represent the memory share id.
INTERLEN_FLAG = 'L'  # The length of array.
INTERLEN_VALUE = 16  # The space bytes in the start of content represents interlen values.
END_EACH_FLAG = 'Z'  # End of each line.
INIT_PC_GUARD = 'I'  # (info, call_pc, nums, start, end) Numbers of pc guard, from 1 to number.
COVERAGE_NUM = 'C'  # Get rough code coverage.
EACH_PC_GUARD = 'G'  # (info, call_pc, guard_num)  dict.pop(cmpid)

PROGRAM_END = 'E'  # end

# Reverse Correspondence
FLAG_DICT = {
    'a': "COV_TRACE_CMP1",
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
    'G': "EACH_PC_GUARD",
    'E': "PROGRAM_END",
}

# Trace level
TRACE_NULL = 'O'
TRACE_GUARDFAST = 'P'
TRACE_GUARD = 'Q'
TRACE_GUARDSYMBOL = 'R'
TRACE_CMPFILTER = 'S'
TRACE_CMP = 'T'
TRACE_CMPGUARD = 'U'
TRACE_CMPGUARDSYMBOL = 'V'

# Hex for visible characters
# bytes.fromhex(HEX_ASCII[n])
# bytes.fromhex("".join(HEX_ASCII[n1:n2])
# bytes[0:1] Get the one byte character. b'a'
BYTES_ASCII = [b'\x00', b'\x01', b'\x02', b'\x03', b'\x04', b'\x05', b'\x06', b'\x07', b'\x08', b'\t', b'\n', b'\x0b',
               b'\x0c', b'\r', b'\x0e', b'\x0f', b'\x10', b'\x11', b'\x12', b'\x13', b'\x14', b'\x15', b'\x16', b'\x17',
               b'\x18', b'\x19', b'\x1a', b'\x1b', b'\x1c', b'\x1d', b'\x1e', b'\x1f', b' ', b'!', b'"', b'#', b'$',
               b'%', b'&', b"'", b'(', b')', b'*', b'+', b',', b'-', b'.', b'/', b'0', b'1', b'2', b'3', b'4', b'5',
               b'6', b'7', b'8', b'9', b':', b';', b'<', b'=', b'>', b'?', b'@', b'A', b'B', b'C', b'D', b'E', b'F',
               b'G', b'H', b'I', b'J', b'K', b'L', b'M', b'N', b'O', b'P', b'Q', b'R', b'S', b'T', b'U', b'V', b'W',
               b'X', b'Y', b'Z', b'[', b'\\', b']', b'^', b'_', b'`', b'a', b'b', b'c', b'd', b'e', b'f', b'g', b'h',
               b'i', b'j', b'k', b'l', b'm', b'n', b'o', b'p', b'q', b'r', b's', b't', b'u', b'v', b'w', b'x', b'y',
               b'z', b'{', b'|', b'}', b'~', b'\x7f', b'\x80', b'\x81', b'\x82', b'\x83', b'\x84', b'\x85', b'\x86',
               b'\x87', b'\x88', b'\x89', b'\x8a', b'\x8b', b'\x8c', b'\x8d', b'\x8e', b'\x8f', b'\x90', b'\x91',
               b'\x92', b'\x93', b'\x94', b'\x95', b'\x96', b'\x97', b'\x98', b'\x99', b'\x9a', b'\x9b', b'\x9c',
               b'\x9d', b'\x9e', b'\x9f', b'\xa0', b'\xa1', b'\xa2', b'\xa3', b'\xa4', b'\xa5', b'\xa6', b'\xa7',
               b'\xa8', b'\xa9', b'\xaa', b'\xab', b'\xac', b'\xad', b'\xae', b'\xaf', b'\xb0', b'\xb1', b'\xb2',
               b'\xb3', b'\xb4', b'\xb5', b'\xb6', b'\xb7', b'\xb8', b'\xb9', b'\xba', b'\xbb', b'\xbc', b'\xbd',
               b'\xbe', b'\xbf', b'\xc0', b'\xc1', b'\xc2', b'\xc3', b'\xc4', b'\xc5', b'\xc6', b'\xc7', b'\xc8',
               b'\xc9', b'\xca', b'\xcb', b'\xcc', b'\xcd', b'\xce', b'\xcf', b'\xd0', b'\xd1', b'\xd2', b'\xd3',
               b'\xd4', b'\xd5', b'\xd6', b'\xd7', b'\xd8', b'\xd9', b'\xda', b'\xdb', b'\xdc', b'\xdd', b'\xde',
               b'\xdf', b'\xe0', b'\xe1', b'\xe2', b'\xe3', b'\xe4', b'\xe5', b'\xe6', b'\xe7', b'\xe8', b'\xe9',
               b'\xea', b'\xeb', b'\xec', b'\xed', b'\xee', b'\xef', b'\xf0', b'\xf1', b'\xf2', b'\xf3', b'\xf4',
               b'\xf5', b'\xf6', b'\xf7', b'\xf8', b'\xf9', b'\xfa', b'\xfb', b'\xfc', b'\xfd', b'\xfe', b'\xff']
HEX_ASCII = [b'0', b'1', b'2', b'3', b'4', b'5', b'6', b'7', b'8', b'9', b'A', b'B', b'C', b'D', b'E', b'F', b'G', b'H',
             b'I', b'J', b'K', b'L', b'M', b'N', b'O', b'P', b'Q', b'R', b'S', b'T', b'U', b'V', b'W', b'X', b'Y', b'Z',
             b'a', b'b', b'c', b'd', b'e', b'f', b'g', b'h', b'i', b'j', b'k', b'l', b'm', b'n', b'o', b'p', b'q', b'r',
             b's', b't', b'u', b'v', b'w', b'x', b'y', b'z']

# strategy STGY
# Status || Detect cmp types
STAT_FAIL = -1
STAT_SUC = 1
STAT_FIN = 2
TYPE_DEFAULT = 50
TYPE_UNDEFINED = 51
TYPE_SOLVED = 52
TYPE_MAGICNUM = 53
TYPE_CHECKNUM = 54
TYPE_MAGICBYTES = 55
TYPE_CHECKBYTES = 56
TYPE_RANDOM = 57

DIST_FINISH = 80  # distance
DIST_CONTINUE = 81
DIST_FAIL = 82

# Parameter Location Index
IDX_CMPID = 0  # n0x1230x123
IDX_CMPTYPE = 0  # n   Remove cmpid
IDX_BLOCKNUM = 1  # 10_0

IDX_ARG = 2

'''Analyzer'''
ANA_ENDPROG_IDX = -2
ANA_MEMSHM_MODE = True
ANA_FILTER_SIZE = 128
ANA_INTERLEN_SIZE = 16
ANA_COVERNUM_SIZE = 16
ANA_START_SIZE = ANA_FILTER_SIZE + ANA_INTERLEN_SIZE + ANA_COVERNUM_SIZE
ANA_SHM_INTERVAL = 1024 * 1024
ANA_SHM_SIZE = 2147483648

'''Builder'''
BUI_PATCHFILE = "binaryline.info"
BUI_NAME = "name"
BUI_NODES = "objects"
BUI_EDGES = "edges"
BUI_NODE_NUM = "_gvid"
BUI_NODE_NAME = "name"
BUI_NODE_LABEL = "label"  # pc_guard num
BUI_NODE_DISTANCE = "distance"
BUI_EDGE_NUM = "_gvid"
BUI_EDGE_START = "tail"  # tail -> head
BUI_EDGE_END = "head"
BUI_EDGE_START_IDX = 0  # tail -> head
BUI_EDGE_END_IDX = 1
BUI_INIT_WEIGHT = 0
# @__sanitizer_cov_trace_pc_guard(i32* inttoptr (i64 add (i64\l... ptrtoint ([78 x i32]* @__sancov_gen_.147 to i64), i64 56) to i32*))
BUI_GUARD_RE = "@__sanitizer_cov_trace_pc_guard\(i32\* inttoptr \(i64 add \(i64\\\\l\.\.\. " \
               "ptrtoint \(\[\d*? x i32\]\* @__sancov_gen_.\d*? to i64\), i64 (\d*?)\) to i32\*\)\)"
# @__sanitizer_cov_trace_pc_guard(i32* getelementptr inbounds ([20 x\l... i32], [20 x i32]* @__sancov_gen_.127, i32 0, i32 0))
BUI_GUARD2_RE = "@__sanitizer_cov_trace_pc_guard\(i32\* getelementptr inbounds \(\[.*?\\\\l\.\.\. .*?i32\], " \
                "\[\d*? x i32\]\* @__sancov_gen_\.\d*?, i32 (\d*?), i32 \d*?\)\)"
BUI_LOC_INTERVAL = 4
BUI_NODE_ST = "nodest"

BUI_ORDER_MULTI = 10

'''Comparator'''
COM_PATCH = 'patch'
COM_SANITIZER = 'sanitizer'
COM_MANUAL = 'manual'
COM_PATCHSET = {USE_INITNUM, COM_PATCH, COM_SANITIZER, COM_MANUAL}

COM_BININS = 'I'
COM_BINFUNC = 'F'
COM_BINCOL = 'C'
COM_BINFILE = 'N'
COM_BINDIR = 'D'

'''Generator'''
PROGRAMS = "Programs"
CODEBIN = "code_Bin"
CODEIR = "code_IR"
CODESOURCES = "code_sources"
DATAGRAPH = "data_graph"
DATAPATCHLOC = "data_patchloc"
SEEDSINIT = "seeds_init"
SEEDSMUTATE = "seeds_mutate"
SEEDSCRASH = "seeds_crash"
CRASH_CSVFILENAME = "crashes.csv"
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
GEN_CSV_HEADERS = "filename,time,duration,content,stdout,stderr\n"

'''Mutator'''
MUT_STR = b'AAABAAAC'
MUT_MATCH = 4  # Truncate 4 bytes as a fast variant flag for fast matching.
MUT_STEP = 4  # step size of mutant seeds
SEED_INIT = 100
MUT_SEED_SUB = 101
MUT_SEED_INSERT = 102

MUT_BIT_LIST = [128, -128, 64, -64, 32, -32, 16, -16, 8, -8, 4, -4, 2, -2, 1, -1]

'''Parser'''
PAR_SOLVED = 200
PAR_FIXAFIX = 201
PAR_FIXACHG = 202
PAR_CHGAFIX = 203
PAR_CHGACHG = 204
PAR_UNDEFINED = 205

PAR_FIXED = 205
PAR_CHANGED = 206

PAR_MAGIC1_TYPE = 181  # fixed changed
PAR_MAGIC2_TYPE = 182  # changed fixed
PAR_CHECKSUMS_TYPE = 183  # changed changed
PAR_FIX_TYPE = 184  # fixed fixed

PAR_VARINIT = 0
PAR_VARMUT = 1

PAR_BIT_BASE = 256

PAR_CONVSINGLE = 210
PAR_CONVDOUBLE = 211

'''Scheduler'''
SCH_LOOP_SEED = 221
SCH_MUT_SEED = 222
SCH_THIS_SEED = 223
SCH_THISMUT_SEED = 224

SCH_SAVEASFILE = True

SCH_EXPAND_MULTI = 2  # Seed expansion factor per round
SCH_EXPAND_SIZE = 64 // SCH_EXPAND_MULTI

# The count of sliding windows is multiple of SCH_SLID_COUNT.
# Recommond 1024/16 = 64
SCH_SLID_MIN = 8  # 8 bit
SCH_SLID_SLICE = 4  # 16 slices.

# Determine the number of similar comparison instructions skipped.
SCH_SKIP_COUNT = 3
# Determine the position of the loop comparison instruction
SCH_EXLOC = 0
# Determine the similarity to the target-triggered Sanitizer
# high:0   low:infinite
SCH_CRASH_SIMI = 2



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
VIS_D = 100
VIS_F = 102
VIS_N = 110
VIS_P = 112
VIS_Q = 113
VIS_S = 115
VIS_X = 120
VIS_Z = 122
VIS_SEED_LINE = 16

VIS_MAX_LINE = 16

VIS_MAX_OUT = 10
VIS_MAX_ERR = 10

VIS_CG_NAME = "CG.gv"
VIS_CFG_NAME = "CFG.gv"
VIS_DPI = 300

VIS_LEN = 76
VIS_STDLEN = VIS_LEN * 3

'''Logging'''
# Logging the information during the fuzzing.
# LOG(LOG_DEBUG, LOG_FUNCINFO(), arg1, arg2, arg3)
LOG_FORMAT = "%(asctime)s - %(levelname)s - %(message)s"

LOG_DEBUG = logging.DEBUG
LOG_INFO = logging.INFO
LOG_WARNING = logging.WARNING
LOG_ERROR = logging.ERROR
LOG_CRITICAL = logging.CRITICAL

LOG_LEVEL = LOG_WARNING

try:
    print(getTime() + ' ' + getProjectPath() + '/Programs/{}.log'.format(FUZZNAME))
    logging.basicConfig(filename=getProjectPath() + '/Programs/{}.log'.format(FUZZNAME), level=LOG_LEVEL,
                        format=LOG_FORMAT)
except:
    print('{} {}.log'.format(getTime(), FUZZNAME))
    logging.basicConfig(filename='{}.log'.format(FUZZNAME), level=LOG_LEVEL, format=LOG_FORMAT)
logging.debug("{} -------------------------".format(FUZZNAME))

LOG_FUNCINFO = lambda: str(sys._getframe(1).f_code.co_name) + ":" + str(sys._getframe(1).f_lineno)


def retLogStr(funcinfo, *args):
    logstr = "|>>| {}-> ".format(funcinfo)
    for content in args:
        logstr += "{} || ".format(content)
    logstr += "|<<|"
    return logstr


def LOG(loggingtype, funcinfo, *args, showlog=False) -> None:
    if not EXP_MODE and showlog:
        logstr = retLogStr(funcinfo, *args)
        with open(PROGRAMS + os.sep + FUZZPRINTLOG, "a+") as f:
            f.write("\n" + logstr + "\n")
        if not VIS_TERM:
            print("\n" + logstr + "\n", end="")

    # logging
    if LOG_LEVEL == LOG_DEBUG and loggingtype == LOG_DEBUG:
        logstr = retLogStr(funcinfo, *args)
        logging.debug(logstr)
    elif loggingtype == LOG_INFO:
        logstr = retLogStr(funcinfo, *args)
        logging.info(logstr)
    elif loggingtype == LOG_WARNING:
        logstr = retLogStr(funcinfo, *args)
        logging.warning(logstr)
    elif loggingtype == LOG_ERROR:
        logstr = retLogStr(funcinfo, *args)
        logging.error(logstr)
    elif loggingtype == LOG_CRITICAL:
        logstr = retLogStr(funcinfo, *args)
        logging.critical(logstr)
