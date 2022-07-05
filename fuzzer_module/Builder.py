#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import ast
import collections
import re
import json
import networkx as nx
from queue import Queue

from fuzzer_module.Fuzzconfig import *
from .Structures import *

class Graph:
    def __init__(self, dgname, nodes_list, edges_list):
        self.dgname = dgname
        self.dg = nx.DiGraph()
        self.dg.add_nodes_from(nodes_list)
        # self.dg.add_weighted_edges_from(edges_list, stedge={})
        self.dg.add_weighted_edges_from(edges_list)
        self.dgroot = None

    def setdgroot(self, dgroot):
        if self.dgroot == None:
            self.dgroot = dgroot
        # else:
        #     raise Exception("Error dgroot already set.")


def getBinaryInfo(path_graph: str) -> 'dict[str:dict[int:dict[str:str]]]':
    """
    From data_patchloc/binaryline.info file parses strings into dictionaries.
    @return:
    """
    # {'function_name':{line:{'':''},line:{'':''}}, }
    binary_graph = path_graph + BUI_PATCHFILE
    patchline_info = getFileContent(binary_graph)
    # pattern = re.compile(r"\s+")
    # patchline_sub = re.sub(pattern, '', patchline_info)  # Whitespace removed

    # print(patchline_info)
    binline_dict = ast.literal_eval(patchline_info)
    # print(binline_dict['main'])
    LOG(LOG_DEBUG, LOG_FUNCINFO(), patchline_info, binline_dict)
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
        map_func_cgnode = {}
        # Nodes
        nodes_list = []
        for node in data[BUI_NODES]:
            nodes_list.append((node[BUI_NODE_NUM],
                               {BUI_NODE_NUM: node[BUI_NODE_NUM],
                                BUI_NODE_NAME: node[BUI_NODE_NAME],
                                BUI_NODE_DISTANCE: USE_INITNUM,
                                BUI_NODE_FUNCS: set([node[BUI_NODE_LABEL][1:-1]])}))
            LOG(LOG_DEBUG, LOG_FUNCINFO(), node[BUI_NODE_NUM], node[BUI_NODE_NAME], node[BUI_NODE_LABEL])
            map_func_cgnode[node[BUI_NODE_LABEL][1:-1]] = node[BUI_NODE_NAME]
        # Edges
        edges_list = []
        for edge in data[BUI_EDGES]:
            edges_list.append((edge[BUI_EDGE_START],
                               edge[BUI_EDGE_END],
                               BUI_INIT_WEIGHT))
        # print(nodes_list, edges_list)
        LOG(LOG_DEBUG, LOG_FUNCINFO(), nodes_list, edges_list)
        cggraph = Graph(data[BUI_NAME].split(" ")[-1], nodes_list, edges_list)

    return cggraph, map_func_cgnode


def getCFG(cfglist, map_num_asm, target_dict):
    """
    Get the
    @param cfglist:
    @return:
    """
    # dot_list = []
    # G = nx.DiGraph()
    # for dot in dot_list:
    #     G.update(nx.DiGraph(nx.drawing.nx_pydot.read_dot(dot)))

    map_guard_gvid: '{funcname:{guardnum:node_j}}' = {}
    map_target: '{funcname:[id,nodeid,node_j]}' = {}
    cfggraph_dict = {}
    for jsonfile_i in cfglist:
        # funcname = jsonfile_i.split(os.sep)[-1][1:-9]
        with open(jsonfile_i, 'r') as f:
            data = json.load(f)
            # print(data)
            # LOG(LOG_DEBUG, LOG_FUNCINFO(), data[BUI_NAME], showlog=True)
            graphname = data[BUI_NAME].split(" ")[-2][1:-1]  # That also is the function name.
            if graphname not in map_guard_gvid:
                map_guard_gvid[graphname] = {}

            # for k, v in data.items():
            #     print(k,"->", v)
            # print()
            # Constructing directed graph.
            # Nodes
            nodes_list = []
            for node_j in data[BUI_NODES]:
                node_asm = re.sub(r"\s|\\l|\\", '', node_j[BUI_NODE_LABEL])
                LOG(LOG_DEBUG, LOG_FUNCINFO(), node_j[BUI_NODE_NAME], node_asm)

                # Find function callgraph.
                pattern = re.compile(BUI_FUNCS)
                callfuncs = set(pattern.findall(node_asm))
                callfuncs = callfuncs - BUI_FILTER_FUNCS
                LOG(LOG_DEBUG, LOG_FUNCINFO(), callfuncs)

                # Find Guard num node_j
                pattern = re.compile(BUI_GUARD_RE)
                guard_res = pattern.findall(node_asm)
                # if graphname == "_Z3bugv":
                #     print("_Z3bugv", node_j[BUI_NODE_LABEL])
                if len(guard_res) == 0:
                    pattern = re.compile(BUI_GUARD2_RE)
                    guard_res = pattern.findall(node_asm)
                    # if len(guard_res) == 0:
                    #     LOG(LOG_DEBUG, LOG_FUNCINFO(), node_j[BUI_NODE_LABEL], showlog=True)

                LOG(LOG_DEBUG, LOG_FUNCINFO(), guard_res)
                temp_guardlist = []
                for one in guard_res:
                    temp_guardnum = int(int(one, 10) / BUI_LOC_INTERVAL)
                    temp_guardlist.append(temp_guardnum)
                    map_guard_gvid[graphname][temp_guardnum] = node_j[BUI_NODE_NUM]

                nodes_list.append((node_j[BUI_NODE_NUM],
                                   {BUI_NODE_NUM: node_j[BUI_NODE_NUM],
                                    BUI_NODE_NAME: node_j[BUI_NODE_NAME],
                                    BUI_NODE_LABEL: temp_guardlist,
                                    BUI_NODE_DISTANCE: USE_INITNUM,
                                    BUI_NODE_FUNCS: callfuncs,
                                    BUI_NODE_ST: []}))
                LOG(LOG_DEBUG, LOG_FUNCINFO(), node_j[BUI_NODE_NUM], node_j[BUI_NODE_NAME], temp_guardlist)

                # Find target
                for tarnum_k in map_num_asm:  # target nums
                    if len(map_num_asm[tarnum_k]) == 0:
                        # Greybox
                        map_target[tarnum_k] = {}
                        continue

                    patchflag = target_dict[tarnum_k][0][0]
                    if patchflag == COM_SANITIZER or patchflag == COM_MANUAL or patchflag == COM_PATCH:
                        # print(map_numTofuncasm[0], graphname)
                        # if graphname == "file_magicfind" or graphname == "match":
                        #     print(graphname, node_j[BUI_NODE_LABEL])
                        if graphname in map_num_asm[tarnum_k]:
                            for target_l in map_num_asm[tarnum_k].get(graphname):  # [tgtnumid, asm]
                                tgtid = target_l[0]
                                LOG(LOG_DEBUG, LOG_FUNCINFO(), node_asm, target_l[1])
                                # res = node_j[BUI_NODE_LABEL].replace(' ', '').replace('\\l', '') \
                                #     .find(target_l[1].replace(' ', ''))
                                res = node_asm.find(target_l[1])

                                if res != -1:
                                    if tarnum_k not in map_target:
                                        map_target[tarnum_k] = {}
                                    if graphname not in map_target[tarnum_k]:
                                        map_target[tarnum_k][graphname] = [
                                            [tgtid, temp_guardlist, node_j[BUI_NODE_NUM]]]
                                    else:
                                        map_target[tarnum_k][graphname].append(
                                            [tgtid, temp_guardlist, node_j[BUI_NODE_NUM]])

            # Excluding the single node_j case.
            if BUI_EDGES not in data:
                continue
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

    return cfggraph_dict, map_guard_gvid, map_target


def getPredecessorsGvid(G, nodegvid):
    predis_dict = {}
    predq = Queue(maxsize=0)
    # print(G.nodes, type(G.nodes))
    # print(list(G.predecessors(nodegvid)))
    # for n in G.nodes:
    #     print(n, list(G.predecessors(n)))
    #     for x in G.predecessors(n):
    #         print(G.nodes(data=True)[x])
    # print(G.nodes(data=True)[nodegvid])
    predq.put(nodegvid)
    predis_dict[nodegvid] = 0
    while not predq.empty():
        curgvid = predq.get()
        for x in G.predecessors(curgvid):
            if x not in predis_dict:
                predq.put(x)
                predis_dict[x] = predis_dict[curgvid] + 1

    return predis_dict

def searchCGFuncNode(graph, funcname):
    """
    According funcname to find which function to call target function.
    @return:
    """
    ref_dict = {}  # {'_Z3bugv': 0, 'main': 1}

    # According funcname find which function call target.
    cgnode_list = []
    for node in graph.dg.nodes(data=True):
        LOG(LOG_DEBUG, LOG_FUNCINFO(), node[0], node[1])
        if funcname in node[1][BUI_NODE_FUNCS]:
            cgnode_list.append(node[0])
    LOG(LOG_DEBUG, LOG_FUNCINFO(), cgnode_list, showlog=True)

    # Find call functions.
    for one in cgnode_list:
        predis_dict = getPredecessorsGvid(graph.dg, one)
        LOG(LOG_DEBUG, LOG_FUNCINFO(), predis_dict)
        for pregvid_j, predis_j in predis_dict.items():
            for callfunc_k in graph.dg.nodes[pregvid_j][BUI_NODE_FUNCS]:
                if callfunc_k not in ref_dict:
                    ref_dict[callfunc_k] = predis_j
                elif callfunc_k > predis_j:
                    ref_dict[callfunc_k] = predis_j

    LOG(LOG_DEBUG, LOG_FUNCINFO(), ref_dict, showlog=True)
    return ref_dict


def searchCFGFuncNode():
    pass


def getTargetPredecessorsGuard(cggraph, cfggraph_dict, map_guard_gvid, map_target, target_dict):
    LOG(LOG_DEBUG, LOG_FUNCINFO(), cfggraph_dict, map_target, showlog=True)
    map_tgtpredgvid = {}
    for tgtnum_i in map_target:  # Select target numbers.
        patchflag = target_dict[tgtnum_i][0][0]
        if patchflag == COM_SANITIZER:
            LOG(LOG_DEBUG, LOG_FUNCINFO(), patchflag, map_target[tgtnum_i], showlog=True)
            map_tgtpredgvid[tgtnum_i] = {}
            for tgtfunc_j in map_target[tgtnum_i]:
                if tgtfunc_j not in cfggraph_dict or tgtfunc_j not in map_guard_gvid:
                    map_tgtpredgvid[tgtnum_i][tgtfunc_j] = {0:0, }
                else:
                    for tgtlist_k in map_target[tgtnum_i][tgtfunc_j]:
                        tgtidx = tgtlist_k[0]
                        tgtloc_list = tgtlist_k[1]
                        tgtnodegvid = tgtlist_k[2]
                        predis_dict = getPredecessorsGvid(
                            cfggraph_dict[tgtfunc_j].dg, tgtnodegvid)
                        LOG(LOG_DEBUG, LOG_FUNCINFO(),
                            tgtfunc_j, tgtidx, tgtloc_list, tgtnodegvid, predis_dict, map_guard_gvid, showlog=True)
                        # for k, v in predis_dict.items():
                        #     print(k, cfggraph_dict[tgtfunc_j].dg.nodes(data=True)[k], v)
                        if tgtfunc_j not in map_tgtpredgvid[tgtnum_i]:
                            map_tgtpredgvid[tgtnum_i][tgtfunc_j] = {}
                        map_tgtpredgvid[tgtnum_i][tgtfunc_j].update(predis_dict)
                        # print(predis_dict)
        elif patchflag == COM_MANUAL or patchflag == COM_PATCH:
            LOG(LOG_DEBUG, LOG_FUNCINFO(), patchflag, map_target[tgtnum_i], showlog=True)

            # Find which function call target function and get the distance for target.
            callfuncs_dict = {}
            for tgtfunc_i in map_target[tgtnum_i]:
                ref_dict = searchCGFuncNode(cggraph, tgtfunc_i)
                for ref_k, dis_v in ref_dict.items():
                    if ref_k not in callfuncs_dict.items():
                        callfuncs_dict[ref_k] = dis_v
                    elif callfuncs_dict[ref_k] > dis_v:
                        callfuncs_dict[ref_k] = dis_v

            # Reverse traversal to build map_tgtpredgvid.
            # Find which gvid(node) include callfuncs.


        elif patchflag == COM_GREYBOX:
            map_tgtpredgvid[tgtnum_i] = {}

    # print(map_tgtpredgvid)
    return map_tgtpredgvid


def getFuncOffset(map_tgtpredgvid_dis, map_target):
    """

    @return:
    """
    LOG(LOG_DEBUG, LOG_FUNCINFO(), map_tgtpredgvid_dis, map_target)
    tgtpred_offset = {}
    for tgtnum_ki, func_vi in map_tgtpredgvid_dis.items():
        if tgtnum_ki not in tgtpred_offset:
            tgtpred_offset[tgtnum_ki] = {}
        for func_kj, preddict_vj in func_vi.items():
            if func_kj not in tgtpred_offset[tgtnum_ki]:
                tgtpred_offset[tgtnum_ki][func_kj] = len(preddict_vj)
    LOG(LOG_DEBUG, LOG_FUNCINFO(), tgtpred_offset, showlog=True)

    for tgtnum_ki, func_ki in tgtpred_offset.items():
        if tgtnum_ki not in map_target:
            continue
        tgtnode = {}
        for func_kj, orderlist_vj in map_target[tgtnum_ki].items():
            for node_k in map_target[tgtnum_ki][func_kj]:
                nid = int(node_k[0]) * BUI_ORDER_MULTI
                if nid not in tgtnode:
                    tgtnode[nid] = func_kj
                else:
                    while nid in tgtnode:
                        nid += 1
                    tgtnode[nid] = func_kj

        ordernode = list(tgtnode.keys())
        ordernode.sort()
        LOG(LOG_DEBUG, LOG_FUNCINFO(), tgtnode, ordernode)
        offset = 0
        for order in ordernode:
            func = tgtnode[order]
            temp = tgtpred_offset[tgtnum_ki][func]
            tgtpred_offset[tgtnum_ki][func] = offset
            offset += temp
    LOG(LOG_DEBUG, LOG_FUNCINFO(), tgtpred_offset)
    return tgtpred_offset


def printTargetSeq(map_target):
    copy_map = map_target.copy()
    tgtnum = list(copy_map.keys())
    tgtnum.sort()
    trace_orderdict = {}
    for tgtnum_i in tgtnum:
        print("=={}==".format(tgtnum_i))
        if tgtnum_i not in trace_orderdict:
            trace_orderdict[tgtnum_i] = collections.OrderedDict()
        funcs = copy_map[tgtnum_i].keys()
        tgtnode = {}
        for func_j in funcs:
            for node_k in copy_map[tgtnum_i][func_j]:
                nid = int(node_k[0]) * BUI_ORDER_MULTI
                if nid not in tgtnode:
                    tgtnode[nid] = [int(node_k[0]), func_j, node_k[1], node_k[2]]
                else:
                    while nid in tgtnode:
                        nid += 1
                    tgtnode[nid] = [int(node_k[0]), func_j, node_k[1], node_k[2]]

        ordernode = list(tgtnode.keys())
        ordernode.sort(reverse=True)
        for order_j in ordernode:
            # 8 main guard:[91]  gvid:94
            print("# {} {} {} {}".format(tgtnode[order_j][0], tgtnode[order_j][1],
                                         tgtnode[order_j][2], tgtnode[order_j][3]))
            trace_orderdict[tgtnum_i][tgtnode[order_j][1]] = [tgtnode[order_j][0], tgtnode[order_j][2], USE_INITMAXNUM, ]

        print()
        # print(tgtnode)
    return trace_orderdict


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
                    layerq.put(curlayer + 1)
                else:
                    G.nodes[node_j][BUI_NODE_DISTANCE] = min(tdis, curlayer)

    LOG(LOG_DEBUG, LOG_FUNCINFO(), root, G.nodes(data=True))


def buildBFSdistance(cggraph, cfggraph_dict) -> dict:
    """
    An incoming graph is traversed breadth-first to determine the mutual position of nodes.
    @return:
    """
    LOG(LOG_DEBUG, LOG_FUNCINFO(), cggraph, cfggraph_dict)
    # CG BFS
    # print(cggraph.dgname, cggraph.dg)
    cgroot = searchRoot(cggraph.dg)
    cggraph.setdgroot(cgroot)
    addDistanceGraph(cggraph.dg, cgroot)

    # CFG BFS
    # print(cfggraph_dict)
    for cfgname_ik, cfgG_iv in cfggraph_dict.items():
        cfgroot = searchRoot(cfgG_iv.dg)
        cfgG_iv.setdgroot(cfgroot)
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


if __name__ == '__main__':
    testmap = {0: {'mget': [[1, [238], 'Node0x55abc9b6b560']], 'mget2': [[1, [238], 'Node0x55abc9b6b560']],
                   'file_softmagic': [[3, [4], 'Node0x55abc9b06a10']], 'process': [[7, [14], 'Node0x55abc96ae500']],
                   'match': [[2, [72], 'Node0x55abc9b0df60']], 'file_or_fd': [[5, [46], 'Node0x55abc96d34f0']],
                   'file_buffer': [[4, [26], 'Node0x55abc9a2b810']], 'magic_file': [[6, [2], 'Node0x55abc96ee670']],
                   'main': [[8, [91], 'Node0x55abc9677d20']], 'file_magicfind': [[0, [0], 'Node0x55abc9916c00']]}}
    printTargetSeq(testmap)
