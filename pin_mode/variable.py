INS_IP = "I"  #"->FuncIP"
CMP_INS = "C"
IMG_BASE_ADDR = "M"  #"->MainExecutable"
OPERAND_VALUE = "O"  #"->Regs"
OTHER_CMP_INS = "OC"

# config
PROGRAM_FILENAME  = "fuzzer_program/base64"
STATIC_FILENAME = "info_data/static_info.pkl"
DYNAMIC_INIT_FILENAME = "dynamic_info.out"
DYNAMIC_SAVE_PATH = "info_data/"
INITSEEDS_FILENAME = "fuzzer_program/fuzzer_input/rand.b64"
MUTATESEEDS_FILEPATH = "fuzzer_program/fuzzer_mutate/"
CRASH_FILEPATH = "fuzzer_program/fuzzer_crash/"
MUTATE_SAVE_PATH = "fuzzer_program/fuzzer_mutate/"

GRAPH_DIR = "graph_data"
GRAPH_FILENAME = "static_graph"
DYNAMIC_GRAPH_FILENAME = "dynamic_graph_"

# each ID numbers
STATIC_POS = {'START_EA':0, 'END_EA':1, 'BLOCK_NUM':2, 'BLOCKS_DICT':3, 'ROOT_ARR':4, 'NODE_ARR':5}  # static information IDs number
INTERESTING_OPERATE = ['call', 'cmp', 'lea', 'test', 'xor']
MUTATE_MODE = {'each_char':1000, 'each_mutN':1001, 'self_change':1002, 'per_each_mutN':1003}
# select which function to dynamic draw
DRAW_FUNC = {'main':'main', 'do_decode':'do_decode', 'base64_decode_ctx':'base64_decode_ctx', 'decode_4':'decode_4'}

# bytes_map_cmp flag
NEXT_GREATER = 101
NEXT_EQUAL = 102
NEXT_LESS = 103
NEXT_OVERSETP = 104