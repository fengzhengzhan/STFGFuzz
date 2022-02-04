import logging
import sys
from graphviz import Digraph

from variable import *

# before draw dynamic graph to execute this function, use return dict as the draw node
def gainDynamicInfo(static_info_dict, dynamic_info_dict, draw_funcname):
    static_info = static_info_dict[draw_funcname]

    sorted_static = sorted(static_info[STATIC_POS['BLOCKS_DICT']].items(), key=lambda item: item[0])
    sorted_dynamic = sorted(dynamic_info_dict.items(), key=lambda item: item[0])
    dynamic_path = []
    draw_dynamic_dict = {}

    # print(static_info_dict, dynamic_info_dict)
    # draw all nodes to graph
    num_block = 0
    for key, value in sorted_static:
        draw_value_str = ""
        block_color = "#000000"
        num_block += 1

        # gain the interesting operate, get regs value and more infor',mation
        for index in range(len(value[0])):
            if value[0][index] in dynamic_info_dict:
                block_color = "#ff0000"
                temp_operate = str(value[1][index]).replace(",", "").replace(";", "").split(" ")
                # Determine if interesting operations are included
                if temp_operate[0] in INTERESTING_OPERATE:
                    draw_value_str += value[1][index]

                    dynamic_path.append(value[0][index])
                    draw_value_str += " <" + str(value[0][index]) + "> "
                    # iterator each operate to gain the rags
                    if len(dynamic_info_dict[value[0][index]]) > 1:
                        for each in range(len(dynamic_info_dict[value[0][index]])):
                            draw_value_str += " >" + dynamic_info_dict[value[0][index]][each]
                    draw_value_str += "\n"

        if num_block == 1:
            block_color = "#0000ff"
        logging.debug("{}-> value:{}".format(sys._getframe().f_code.co_name, value))
        draw_dynamic_dict[key] = [key + "\n" + draw_value_str, block_color]
    return dynamic_path, draw_dynamic_dict

# before draw dynamic graph for cmp instructions this function, use return dict as the draw node
def gainCmpInfo(static_info_dict, bytes_map_cmp_dict, draw_funcname):
    static_info = static_info_dict[draw_funcname]

    sorted_static = sorted(static_info[STATIC_POS['BLOCKS_DICT']].items(), key=lambda item: item[0])
    sorted_cmp = sorted(bytes_map_cmp_dict.items(), key=lambda item: item[0])
    draw_dynamic_dict = {}

    # print(static_info_dict, dynamic_info_dict)
    # draw all nodes to graph
    for key, value in sorted_static:
        draw_value_str = ""
        block_color = "#000000"

        # gain the interesting operate, get regs value and more infor',mation
        for index in range(len(value[0])):
            if value[0][index] in bytes_map_cmp_dict:
                block_color = "#ff0000"
                # Decide whether to include operations of interest
                draw_value_str += value[1][index]

                draw_value_str += " <" + str(value[0][index]) + "> "
                # iterator each operate to gain the rags
                draw_value_str += " >" + str(bytes_map_cmp_dict[value[0][index]][1])
                draw_value_str += "\n"

        logging.debug("{}-> value:{}".format(sys._getframe().f_code.co_name, value))
        draw_dynamic_dict[key] = [key + "\n" + draw_value_str, block_color]
    return draw_dynamic_dict



def drawDynamicGraph(static_info_dict, draw_dynamic_dict, draw_funcname, draw_dynamic_filename):
    static_info = static_info_dict[draw_funcname]
    dot = Digraph(str(draw_funcname))
    for key, value in draw_dynamic_dict.items():
        dot.node(key, value[0], color=value[1])

    # draw edges for all nodes
    for i in range(len(static_info[STATIC_POS['ROOT_ARR']])):
        dot.edge(static_info[STATIC_POS['ROOT_ARR']][i], static_info[STATIC_POS['NODE_ARR']][i])
    dot.view(filename=DYNAMIC_GRAPH_FILENAME+draw_dynamic_filename, directory=GRAPH_DIR)
    # dot.render(DYNAMIC_GRAPH_FILENAME+draw_dynamic_filename+".gv", view=True)

