from fuzzer_module.Tools import *

'''Key Structure'''
# map_funcTocgname
# map_guardTofuncname

'''Struct'''
class StructTarget:
    def __init__(self, tnum, ttrace, tfunc, tline):
        self.tnum: int = tnum
        self.ttrace: int = ttrace
        self.tfunc: str = tfunc
        self.tline: int = tline


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


# The structure stores information about trace report.
class StructTraceReport:
    def __init__(self, startguard: int, endguard: int,
                 constraint: 'list[str]', stvalue: 'list[list[str, str]]', programcontent: 'list[str]'):
        self.startguard = startguard
        self.endguard = endguard
        self.constraint = constraint
        self.stvalue = stvalue
        self.progcontent = programcontent

class StructCmpIns:
    def __init__(self, stcmpid, startguard, endguard, stvalue:list, stargs):
        self.stcmpid = stcmpid
        self.startguard = startguard
        self.endguard = endguard
        self.stvalue = stvalue  # type, func_pc, caller_pc ...
        self.stargs = stargs  # arg1, arg2, arg3 ...


class StructCmpInfo:
    def __init__(self, cmptype, inputmap: list, ansvalue, startguard, endguardtrue, endguardfalse):
        self.cmptype = cmptype
        self.inputmap = inputmap  # Compare the input bytes involved in the instruction.
        self.ansvalue = ansvalue
        self.startguard = startguard
        self.endguardtrue = endguardtrue
        self.endguardfalse = endguardfalse


# Identification of the type of comparison instruction.
class StructCmpInfer:
    def __init__(self, var0_type: int, var0_cont: list, var1_type: int, var1_cont: list):
        self.var0_type = var0_type
        self.var0_cont = var0_cont
        self.var1_type = var1_type
        self.var1_cont = var1_cont