#!/usr/bin/env python3
# -*- coding: utf-8 -*-


'''Key Structure'''
# map_funcTocgname
# map_guardTofuncname
from fuzzer_module.Fuzzconfig import *

'''Struct'''
class StructPath:
    def __init__(self, program_name):
        self.code_Bin = PROGRAMS + os.sep + program_name + os.sep + CODEBIN + os.sep
        self.code_IR = PROGRAMS + os.sep + program_name + os.sep + CODEIR + os.sep
        self.code_sources = PROGRAMS + os.sep + program_name + os.sep + CODESOURCES + os.sep
        self.data_graph = PROGRAMS + os.sep + program_name + os.sep + DATAGRAPH + os.sep
        self.data_patchloc = PROGRAMS + os.sep + program_name + os.sep + DATAPATCHLOC + os.sep
        self.seeds_crash = PROGRAMS + os.sep + program_name + os.sep + SEEDSCRASH + os.sep
        self.seeds_init = PROGRAMS + os.sep + program_name + os.sep + SEEDSINIT + os.sep
        self.seeds_mutate = PROGRAMS + os.sep + program_name + os.sep + SEEDSMUTATE + os.sep


class StructTarget:
    def __init__(self, tgttrace: list, tgtinfo: int):
        self.tgttrace: list = tgttrace
        self.tgtinfo: int = tgtinfo

    def addone(self, ttrace, tfunc, tline):
        self.tgttrace.append([ttrace, tfunc, tline])

    def additem(self, ttrace, tfunc, tline):
        for one_i in range(0, len(ttrace)):
            self.tgttrace.append([ttrace[one_i], tfunc[one_i], tline[one_i]])


# The structure stores information about the seed file.
class StructSeed:
    def __init__(self, filename: str, content: bytes, seedtype: int, location: set, priority=0):
        self.filename = filename
        self.content = content
        self.seedtype = seedtype  # INIT MUT_TYPE_SUB MUT_TYPE_INSERT
        self.location = location  # -1 as the init seed
        self.priority = priority


# class StructCmpIns:
#     def __init__(self, stcmpid, startguard, endguard, stvalue:list, stargs):
#         self.cmpid = stcmpid
#         self.startguard = startguard
#         self.endguard = endguard
#         self.stvalue = stvalue  # type, func_pc, caller_pc ...
#         self.stargs = stargs  # arg1, arg2, arg3 ...

class StructCmpInfo:
    def __init__(self, cmptype, inputmap: list, ansvalue, startguard, endguardtrue, endguardfalse):
        self.cmptype = cmptype
        self.inputmap = inputmap  # Compare the input bytes involved in the instruction.
        self.ansvalue = ansvalue
        self.startguard = startguard
        self.endguardtrue = endguardtrue
        self.endguardfalse = endguardfalse


class StructStrategy:
    def __init__(self, strategytype, cmptype, bytestype, curnum, endnum, curloop, endloop):
        self.strategytype = strategytype
        self.cmptype = cmptype
        self.bytestype = bytestype
        self.curnum = curnum
        self.endnum = endnum
        self.curloop = curloop
        self.endloop = endloop


# Key: cmpid  Value: branch_order cmp_type input_bytes branches
class StructMapCmpid:
    def __init__(self, cmpid, cmp_branch_order, cmptype: set, inputmapval: 'dict[loc:value]',
                 branch_true: set, branch_false: set):
        self.cmpid = cmpid
        self.cmporder = cmp_branch_order
        self.cmptype = cmptype
        self.inputmapval = inputmapval
        self.branch_true = branch_true
        self.branch_false = branch_false


class StructMapInpus:
    def __init__(self, inputloc, valuerange: set,
                 cmpset, cmpval: 'dict[cmpid:valuerangeset]',
                 branchset, branchval: 'dict[branchid:valuerangeset]'):
        self.inputloc = inputloc
        self.valuerange = valuerange
        self.cmpset = cmpset
        self.cmpval = cmpval
        self.branchset = branchset
        self.branchval = branchval


class StructMapBranches:
    def __init__(self, branchid, cmplist, inputmap):
        self.branchid = branchid
        self.cmplist = cmplist
        self.inputmap = inputmap
