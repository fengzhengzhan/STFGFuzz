import ast
import re
import json
import networkx as nx


from fuzzer_module.Fuzzconfig import *


class Graph:
    def __init__(self, dgname, nodes_list, edges_list):
        self.dgname = dgname
        self.dg = nx.DiGraph()
        self.dg.add_nodes_from(nodes_list)
        # self.dg.add_weighted_edges_from(edges_list, stedge={})
        self.dg.add_weighted_edges_from(edges_list)


def getPatchInfo(program_name: str) -> 'dict[str:dict[int:dict[str:str]]]':
    """
    From data_patchloc/binaryline.info file parses strings into dictionaries.
    @return:
    """
    # {'function_name':{line:{'':''},line:{'':''}}, }
    temp_patchfile = PROGRAMS + os.sep + program_name + os.sep + DATAGRAPH + os.sep + BUI_PATCHFILE
    patchline_info = getFileContent(temp_patchfile)
    pattern = re.compile(r"\s+")
    patchline_sub = re.sub(pattern, ' ', patchline_info)

    # print(patchline_info)
    patchline_dict = ast.literal_eval(patchline_sub)
    # print(patchline_dict['main'])
    LOG(LOG_DEBUG, LOG_FUNCINFO(), patchline_info, patchline_sub, patchline_dict)
    return patchline_dict


def getCG(cglist) -> (Graph, dict):
    """
    Get the function Call Graph, the most important graph usually has only one.
    @param cglist:
    @return:
    """
    for jsonfile in cglist:
        with open(jsonfile, 'r') as f:
            data = json.load(f)
        # for k, v in data.items():
        #     print(k,"->", v)
        # Constructing directed graph.
        map_funcTocgname = {}
        # Nodes
        nodes_list = []
        for node in data[BUI_NODES]:
            nodes_list.append((node[BUI_NODE_NUM],
                               {BUI_NODE_NUM: node[BUI_NODE_NUM],
                                BUI_NODE_NAME: node[BUI_NODE_NAME],
                                BUI_NODE_LABEL: node[BUI_NODE_LABEL]}))
            map_funcTocgname[node[BUI_NODE_LABEL][1:-1]] = node[BUI_NODE_NAME]
        # Edges
        edges_list = []
        for edge in data[BUI_EDGES]:
            edges_list.append((edge[BUI_EDGE_START],
                               edge[BUI_EDGE_END],
                               BUI_INIT_WEIGHT))
        # print(nodes_list, edges_list)
        LOG(LOG_DEBUG, LOG_FUNCINFO(), nodes_list, edges_list)
        cggraph = Graph(data[BUI_NAME].split(" ")[-1], nodes_list, edges_list)

    return cggraph, map_funcTocgname


def getCFG(cfglist) -> 'dict[str:Graph]':
    """
    Get the
    @param cfglist:
    @return:
    """
    map_guardTocfgname: dict[str:str] = {}
    cfggraph_dict = {}
    for jsonfile in cfglist:
        # funcname = jsonfile.split(os.sep)[-1][1:-9]
        with open(jsonfile, 'r') as f:
            data = json.load(f)
            # Excluding the single node case.
            if BUI_EDGES not in data:
                continue
            # for k, v in data.items():
            #     print(k,"->", v)
            # print()
            # Constructing directed graph.
            # Nodes
            nodes_list = []
            for node in data[BUI_NODES]:
                pattern = re.compile(BUI_GUARD_RE)
                results = pattern.findall(node[BUI_NODE_LABEL])
                temp_intlist = []
                for one in results:
                    temp_guardnum = int(int(one, 10) / BUI_LOC_INTERVAL)
                    temp_intlist.append(temp_guardnum)
                    map_guardTocfgname[temp_guardnum] = node[BUI_NODE_NAME]

                nodes_list.append((node[BUI_NODE_NUM],
                                   {BUI_NODE_NUM: node[BUI_NODE_NUM],
                                    BUI_NODE_NAME: node[BUI_NODE_NAME],
                                    BUI_NODE_LABEL: temp_intlist,
                                    BUI_NODE_ST: []}))
            # Edges
            edges_list = []
            for edge in data[BUI_EDGES]:
                edges_list.append((edge[BUI_EDGE_START],
                                   edge[BUI_EDGE_END],
                                   BUI_INIT_WEIGHT))
            # print(nodes_list, edges_list)
            LOG(LOG_DEBUG, LOG_FUNCINFO(), nodes_list, edges_list)
            temp_graphname = data[BUI_NAME].split(" ")[-2][1:-1]
            cfggraph = Graph(temp_graphname, nodes_list, edges_list)
            cfggraph_dict[temp_graphname] = cfggraph

    return cfggraph_dict, map_guardTocfgname


def buildConstraint(start_node, end_node, st_list):
    """
    Constructing constraint graph.
    Record only important constraints.
    Add important constraints text to each node.
    Use color labels for key nodes.
    @return:
    """




if __name__ == "__main__":
    getPatchInfo("demo")

