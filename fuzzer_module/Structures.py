#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from fuzzer_module.Tools import *

'''Key Structure'''
# map_funcTocgname
# map_guardTofuncname

'''Struct'''
class StructTarget:
    def __init__(self, ttrace:list, tfunc:list, tline:list):
        self.ttrace: list = ttrace
        self.tfunc: list = tfunc
        self.tline: list = tline

    def additem(self, ttrace, tfunc, tline):
        self.ttrace.append(ttrace)
        self.tfunc.append(tfunc)
        self.tline.append(tline)

# The structure stores information about the seed file.
class StructSeed:
    def __init__(self, filename: str, content: str, seedtype: int, location: set):
        self.filename = filename
        if content == "":
            self.content = getFileContent(filename)
        else:
            self.content = content
        self.seedtype = seedtype  # INIT MUT_TYPE_SUB MUT_TYPE_INSERT
        self.location = location  # -1 as the init seed



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

class StructMutStrategy:
    def __init__(self, type, curnum, endlen, curloop, endloop):
        self.type = type
        self.curnum = curnum
        self.endlen = endlen
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


