#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import ast
import re
import json
import networkx as nx
from queue import Queue

from fuzzer_module.Fuzzconfig import *


class Graph:
    def __init__(self, dgname, nodes_list, edges_list):
        self.dgname = dgname
        self.dg = nx.DiGraph()
        self.dg.add_nodes_from(nodes_list)
        # self.dg.add_weighted_edges_from(edges_list, stedge={})
        self.dg.add_weighted_edges_from(edges_list)


def getBinaryInfo(program_name: str) -> 'dict[str:dict[int:dict[str:str]]]':
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
    binline_dict = ast.literal_eval(patchline_sub)
    # print(binline_dict['main'])
    LOG(LOG_DEBUG, LOG_FUNCINFO(), patchline_info, patchline_sub, binline_dict)
    return binline_dict


def getCG(cglist):
    """
    Get the function Call Graph, the most important graph usually has only one.
    @param cglist:
    @return:
    """
    for jsonfile in cglist:
        LOG(LOG_DEBUG, LOG_FUNCINFO(), jsonfile)
        with open(jsonfile, 'r') as f:
            data = json.load(f)
        # for k, v in data.items():
        #     print(k,"->", v)
        # Constructing directed graph.
        map_funcTocgnode = {}
        # Nodes
        nodes_list = []
        for node in data[BUI_NODES]:
            nodes_list.append((node[BUI_NODE_NUM],
                               {BUI_NODE_NUM: node[BUI_NODE_NUM],
                                BUI_NODE_NAME: node[BUI_NODE_NAME],
                                BUI_NODE_LABEL: node[BUI_NODE_LABEL],
                                BUI_NODE_DISTANCE: USE_INITNUM}))
            map_funcTocgnode[node[BUI_NODE_LABEL][1:-1]] = node[BUI_NODE_NAME]
        # Edges
        edges_list = []
        for edge in data[BUI_EDGES]:
            edges_list.append((edge[BUI_EDGE_START],
                               edge[BUI_EDGE_END],
                               BUI_INIT_WEIGHT))
        # print(nodes_list, edges_list)
        LOG(LOG_DEBUG, LOG_FUNCINFO(), nodes_list, edges_list)
        cggraph = Graph(data[BUI_NAME].split(" ")[-1], nodes_list, edges_list)

    return cggraph, map_funcTocgnode


def getCFG(cfglist, map_numTofuncasm):
    """
    Get the
    @param cfglist:
    @return:
    """
    map_guardTocfgnode: 'dict[guardnum:node_j]' = {}
    map_numfuncTotgtnode: 'dict[funcname:node_j]' = {}
    cfggraph_dict = {}
    for jsonfile_i in cfglist:
        # funcname = jsonfile_i.split(os.sep)[-1][1:-9]
        with open(jsonfile_i, 'r') as f:
            data = json.load(f)
            graphname = data[BUI_NAME].split(" ")[-2][1:-1]  # That also is the function name.
            # Excluding the single node_j case.
            if BUI_EDGES not in data:
                continue
            # for k, v in data.items():
            #     print(k,"->", v)
            # print()
            # Constructing directed graph.
            # Nodes
            nodes_list = []
            for node_j in data[BUI_NODES]:
                LOG(LOG_DEBUG, LOG_FUNCINFO(), node_j[BUI_NODE_NAME], node_j[BUI_NODE_LABEL])
                # Find target
                for tarnum_k in map_numTofuncasm:
                    for target_l in map_numTofuncasm[tarnum_k].get(graphname):
                        res = node_j[BUI_NODE_LABEL].find(target_l)
                        if res != -1:
                            if tarnum_k not in map_numfuncTotgtnode:
                                map_numfuncTotgtnode[tarnum_k] = {}
                            if graphname not in map_numfuncTotgtnode[tarnum_k]:
                                map_numfuncTotgtnode[tarnum_k][graphname] = [node_j[BUI_NODE_NAME]]
                            else:
                                map_numfuncTotgtnode[tarnum_k][graphname].append(node_j[BUI_NODE_NAME])

                # Find Guard num node_j
                pattern = re.compile(BUI_GUARD_RE)
                guard_res = pattern.findall(node_j[BUI_NODE_LABEL])
                LOG(LOG_DEBUG, LOG_FUNCINFO(), node_j[BUI_NODE_LABEL], guard_res)
                temp_intlist = []
                for one in guard_res:
                    temp_guardnum = int(int(one, 10) / BUI_LOC_INTERVAL)
                    temp_intlist.append(temp_guardnum)
                    map_guardTocfgnode[temp_guardnum] = node_j[BUI_NODE_NAME]

                nodes_list.append((node_j[BUI_NODE_NUM],
                                   {BUI_NODE_NUM: node_j[BUI_NODE_NUM],
                                    BUI_NODE_NAME: node_j[BUI_NODE_NAME],
                                    BUI_NODE_LABEL: temp_intlist,
                                    BUI_NODE_DISTANCE: USE_INITNUM,
                                    BUI_NODE_ST: []}))
            # Edges
            edges_list = []
            for edge_j in data[BUI_EDGES]:
                edges_list.append((edge_j[BUI_EDGE_START],
                                   edge_j[BUI_EDGE_END],
                                   BUI_INIT_WEIGHT))
            # print(nodes_list, edges_list)
            LOG(LOG_DEBUG, LOG_FUNCINFO(), nodes_list, edges_list)

            cfggraph = Graph(graphname, nodes_list, edges_list)
            cfggraph_dict[graphname] = cfggraph

    return cfggraph_dict, map_guardTocfgnode, map_numfuncTotgtnode


def searchRoot(G):
    """
    Traverse all nodes to find which node has no parent nodes, that is considered root node.
    @return:
    """
    root_list = []
    # for n in G.nodes(data=True):
    #     predecessors = G.predecessors(n[0])
    #     print(n, n[0], predecessors)
    #     if len(list(predecessors)) == 0:
    #         print(n)

    for n in G.nodes(data=False):
        predecessors = G.predecessors(n)
        if len(list(predecessors)) == 0:
            root_list.append(n)

    return root_list


def addDistanceGraph(G, root):
    # print(G.nodes[0][BUI_NODE_DISTANCE])
    # G.nodes[0][BUI_NODE_DISTANCE] = 10
    # print(G.nodes[0][BUI_NODE_DISTANCE])
    # print(G.nodes[1][BUI_NODE_DISTANCE])
    LOG(LOG_DEBUG, LOG_FUNCINFO(), root, G.nodes(data=True))
    nodeidq = Queue(maxsize=0)
    layerq = Queue(maxsize=0)
    for r_i in root:
        nodeidq.put(r_i)
        layerq.put(0)
        while not nodeidq.empty() and not layerq.empty():
            curnodeid = nodeidq.get()
            curlayer = layerq.get()
            G.nodes[curnodeid][BUI_NODE_DISTANCE] = curlayer
            # print(curnodeid, G.nodes[curnodeid][BUI_NODE_LABEL])
            for node_j in G.successors(curnodeid):
                # print("  ", node_j, )
                tdis = G.nodes[node_j][BUI_NODE_DISTANCE]
                if tdis == -1:
                    nodeidq.put(node_j)
                    layerq.put(curlayer+1)
                else:
                    G.nodes[node_j][BUI_NODE_DISTANCE] = min(tdis, curlayer)

    LOG(LOG_DEBUG, LOG_FUNCINFO(), root, G.nodes(data=True), showlog=True)


def buildBFSdistance(cggraph, cfggraph_dict) -> dict:
    """
    An incoming graph is traversed breadth-first to determine the mutual position of nodes.
    @return:
    """
    LOG(LOG_DEBUG, cggraph, cfggraph_dict, showlog=True)
    # CG BFS
    # print(cggraph.dgname, cggraph.dg)
    cgroot = searchRoot(cggraph.dg)
    addDistanceGraph(cggraph.dg, cgroot)

    # CFG BFS
    print(cfggraph_dict)
    for cfgname_ik, cfgG_iv in cfggraph_dict.items():
        cfgroot = searchRoot(cfgG_iv.dg)
        addDistanceGraph(cfgG_iv.dg, cfgroot)


def buildConstraint(start_node, end_node, st_list):
    """
    Constructing constraint graph.
    Record only important constraints.
    Add important constraints text to each node.
    Use color labels for key nodes.
    @return:
    """
    pass
