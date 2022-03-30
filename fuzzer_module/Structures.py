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
    def __init__(self, startguard: int, endguard: int, constraint: 'list[str]', stvalue: 'list[list[str, str]]', programcontent: 'list[str]'):
        self.startguard = startguard
        self.endguard = endguard
        self.constraint = constraint
        self.stvalue = stvalue
        self.progcontent = programcontent

class StructCmpIns:
    def __init__(self, constraint, startguard, endguard, stvalue:list, stargs):
        self.constraint = constraint
        self.startguard = startguard
        self.endguard = endguard
        self.stvalue = stvalue
        self.stargs = stargs


class StructCmpReport:
    def __init__(self, mutseed: StructSeed, sttype: str, init_sttrace: list, mut_sttrace: list, startguard: int, endguard: int, stpcguard: str):
        self.mutseed = mutseed
        self.sttype = sttype
        self.init_sttrace = init_sttrace
        self.mut_sttrace = mut_sttrace
        self.startguard = startguard
        self.endguard = endguard
        self.stpcguard = stpcguard


# This is the global compare command mapping.
class StructCmpMap:
    def __init__(self):
        self.cmpmap: 'dict[StructCmpInfo]' = {}


class StructCmpInfo:
    def __init__(self, cmptype, inputmap: list, ansvalue, startguard, endguardtrue, endguardfalse):
        self.cmptype = cmptype
        self.inputmap = inputmap  # Compare the input bytes involved in the instruction.
        self.ansvalue = ansvalue
        self.startguard = startguard
        self.endguardtrue = endguardtrue
        self.endguardfalse = endguardfalse


# class StructFreezeMap:
#     def __init__(self):
#         self.freezemap = []

class StructMutLoc:
    def __init__(self):
        self.freezemap = []
        self.mutonelist = []
        self.rawdatalist = []


# This is the global constraint graph.
class StructSTGraph:
    def __init__(self):
        self.constraintgraph = []

# Identification of the type of comparison instruction.
class StructCmpInfer:
    def __init__(self, var1_type: int, var1_cont: list, var2_type: int, var2_cont: list):
        self.var1_type = var1_type
        self.var1_cont = var1_cont
        self.var2_type = var2_type
        self.var2_cont = var2_cont