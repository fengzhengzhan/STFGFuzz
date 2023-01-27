import os
import ast
import re
import json

binaryline = "data_graph/binaryline.json"
trans_func_symbol = "trans_func_symbol.txt"
trans_symbol_initguard = "trans_symbol_initguard.txt"
track_path = "track_path.txt"
BUI_GUARD_RE = r"@__sanitizer_cov_trace_pc_guard\(i32\*inttoptr\(i64add\(i64ptrtoint\(\[\d*?xi32\]\*@__sancov_gen_.*?toi64\),i64(\d*?)\)toi32\*\)\)"



def readStrDict(filename):
    with open(filename, "r") as f:
        cont = f.readline()
        # print(cont)
    return ast.literal_eval(cont)

def main():
    # Read relation information dict.
    binaryline_dict = readStrDict(binaryline)
    # print(type(binaryline_dict))
    func_symbol_dict = readStrDict(trans_func_symbol)
    # print(type(func_symbol_dict))
    symbol_initguard_dict = readStrDict(trans_symbol_initguard)
    # print(type(symbol_initguard_dict))

    # Deal with track path.  # 102 line enter keyword
    track_list = []
    with open(track_path, 'r') as f:
        trackpath_list = f.readlines()
    for line in trackpath_list:
        if line != "":
            each_list = ast.literal_eval(line[:-2])
            # print(each_list, type(each_list))
            if each_list[1] == 'G':
                track_list.append([each_list[3], each_list[2]])

    # Get the location of track.
    print(track_list)
    for tr in track_list:
        # func guard
        func, guard = tr[0], int(tr[1])
        try:
            symbol = func_symbol_dict[func]
        except Exception as e:
            symbol = func
        initguard = symbol_initguard_dict[symbol]
        # print(func, symbol, initguard)

        # Get json file content.
        json_asm = ""
        json_filename = "data_graph/."+symbol+".dot.json"
        with open(json_filename, 'r') as f:
            data = json.load(f)
        # print(data, type(data))
        for node_j in data["objects"]:
            node_asm = re.sub(r"\s|\\l\.\.\.|\\l|\\", '', node_j["label"])
            pattern = re.compile(BUI_GUARD_RE)
            guard_res = pattern.findall(node_asm)
            cur_guard = str(4 * (guard - initguard))
            if cur_guard in guard_res:
                json_asm = node_asm


        # Line
        # print(json_asm)
        # print(binaryline_dict[symbol])
        for bk, bv in binaryline_dict[symbol].items():
            res = json_asm.find(bv['I'])

            if res != -1:
                print("{}:{}:{}".format(bv['N'],bk,bv['C']))





if __name__ == "__main__":
    main()