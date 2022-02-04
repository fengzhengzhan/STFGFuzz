from variable import *

def mutateSeeds(seeds_content, mutate_mode, mutate_location=-1, mutate_content=None):
    # use rules to mutate seeds to produce a array to return
    mutate_str = ""
    ret_mutate_seeds = []
    if mutate_mode == MUTATE_MODE['each_char']:
        for leni in range(len(seeds_content)):
            for chari in range(0, 256):
                mutate_str = seeds_content[:leni] + chr(chari) + seeds_content[(leni + 1):]
                ret_mutate_seeds.append(mutate_str)
    elif mutate_mode == MUTATE_MODE['each_mutN']:
        for leni in range(len(seeds_content)):
            for chari in [0, 64, 128, 192, 255]:
                mutate_str = seeds_content[:leni] + chr(chari) + seeds_content[(leni + 1):]
                ret_mutate_seeds.append(mutate_str)
    elif mutate_mode == MUTATE_MODE['per_each_mutN']:
        for chari in [0, 64, 128, 192, 255]:
            mutate_str = seeds_content[:mutate_location] + chr(chari) + seeds_content[(mutate_location + 1):]
            ret_mutate_seeds.append(mutate_str)
    return ret_mutate_seeds


def gainCmpSetColor(dynamic_cmp_dict, next_dynamic_cmp_dict):
    temp_bytes_map_cmp_dict = {}  # [{cmp_addr:[[type or location], [[value, next_value],[value, next_value]]], cmp_addr:[]},{...}]  using array subscript as bytes location
    temp_cmp_map_bytes_set = set()  # {cmp_addr:[bytes], cmp_addr:[]}
    for nkey, nvalue in next_dynamic_cmp_dict.items():
        if nkey in dynamic_cmp_dict:
            value = dynamic_cmp_dict[nkey]
            # first using len to judge change type, second using operands to judge
            # print(nvalue, value)
            if len(nvalue) > len(value):
                temp_bytes_map_cmp_dict[nkey] = [[NEXT_GREATER], [value, nvalue]]
                temp_cmp_map_bytes_set.add(nkey)
            elif len(nvalue) < len(value):
                temp_bytes_map_cmp_dict[nkey] = [[NEXT_LESS], [value, nvalue]]
                temp_cmp_map_bytes_set.add(nkey)
            else:
                temp = [[],[]]
                fflag = False
                for index in range(len(nvalue)):
                    if value[index] != nvalue[index]:
                        temp[0].append(index)
                        temp[1].append([value[index], nvalue[index]])
                        fflag = True
                if fflag:
                    temp_bytes_map_cmp_dict[nkey] = temp
                    temp_cmp_map_bytes_set.add(nkey)
        else:
            temp_bytes_map_cmp_dict[nkey] = [[NEXT_OVERSETP], [[-1], nvalue]]

    return temp_bytes_map_cmp_dict, temp_cmp_map_bytes_set
