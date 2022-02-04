#include "pin.H"
#include <iostream>
#include <fstream>
#include <string>

#define IMGBASEADDR "M"  // "->MainExecutable"
#define INSIP "I"  // "->FuncIP"
#define OPERANDVALUE "O"  // "->Regs"
#define CMPINS "C"  // cmp instruments
#define OTHERCMPINS "OC" //other cmp instruments

using namespace std;

ofstream out_file;
KNOB<string> KnobOutputFile(KNOB_MODE_WRITEONCE, "pintool", "o", "dynamic_info.out", "dynamic information file");
// KNOB<string> KnobOutputFile(KNOB_MODE_WRITEONCE, "pintool", "o", "info_data/dynamic_info.out", "dynamic information file");
KNOB<ADDRINT> KnobIDAImageBase(KNOB_MODE_WRITEONCE, "pintool", "b", "0x00400000", "IDA base address");

ADDRINT image_base; 
ADDRINT image_end;

void image(IMG img, void * v) {
    if (IMG_IsMainExecutable(img)) {
        image_base = IMG_LowAddress(img);
        image_end = IMG_HighAddress(img);

        char temp[1024];
        sprintf(temp, "%s %s %p ", IMGBASEADDR, IMG_Name(img).c_str(), (void *)image_base);
        out_file << temp << endl;
    }
}

// transition IP forward IDApython static address
ADDRINT translateIP(ADDRINT ip){
    // address translate
    return ip - image_base + KnobIDAImageBase.Value();
}

// cmp INS insert functions
//Reg
void regAndReg(ADDRINT ip, ADDRINT reg0, ADDRINT reg1) {
    out_file << CMPINS << " " << hex << "0x" << translateIP(ip) << " " << reg0 << " " << reg1 << endl;
}
void regAndMem(ADDRINT ip, ADDRINT reg0, ADDRINT* mem1) {
    ADDRINT val1;
    PIN_SafeCopy(&val1, mem1, sizeof(ADDRINT));
    out_file << CMPINS << " " << hex << "0x" << translateIP(ip) << " " << reg0 << " " << val1 << endl;
}
void regAndImm(ADDRINT ip, ADDRINT reg0, UINT32 imm1) {
    out_file << CMPINS << " " << hex << "0x" << translateIP(ip) << " " << reg0 << " " << imm1 << endl;
}
//Mem
void memAndReg(ADDRINT ip, ADDRINT* mem0, ADDRINT reg1) {
    ADDRINT val0;
    PIN_SafeCopy(&val0, mem0, sizeof(ADDRINT));
    out_file << CMPINS << " " << hex << "0x" << translateIP(ip) << " " << val0 << " " << reg1 << endl;
}
void memAndMem(ADDRINT ip, ADDRINT* mem0, ADDRINT* mem1) {
    ADDRINT val0;
    PIN_SafeCopy(&val0, mem0, sizeof(ADDRINT));
    ADDRINT val1;
    PIN_SafeCopy(&val1, mem1, sizeof(ADDRINT));
    out_file << CMPINS << " " << hex << "0x" << translateIP(ip) << " " << val0 << " " << val1 << endl;
}
void memAndImm(ADDRINT ip, ADDRINT* mem0, UINT32 imm1) {
    ADDRINT val0;
    PIN_SafeCopy(&val0, mem0, sizeof(ADDRINT));
    out_file << CMPINS << " " << hex << "0x" << translateIP(ip) << " " << val0 << " " << imm1 << endl;
}
//Imm
void immAndReg(ADDRINT ip, UINT32 imm0, ADDRINT reg1) {
    out_file << CMPINS << " " << hex << "0x" << translateIP(ip) << " " << imm0 << " " << reg1 << endl;
}
void immAndMem(ADDRINT ip, UINT32 imm0, ADDRINT* mem1) {
    ADDRINT val1;
    PIN_SafeCopy(&val1, mem1, sizeof(ADDRINT));
    out_file << CMPINS << " " << hex << "0x" << translateIP(ip) << " " << imm0 << " " << val1 << endl;
}
void immAndImm(ADDRINT ip, UINT32 imm0, UINT32 imm1) {
    out_file << CMPINS << " " << hex << "0x" << translateIP(ip) << " " << imm0 << " " << imm1 << endl;
}


void otherCmp(ADDRINT ip, const string *s) {
    out_file << OTHERCMPINS << " " << hex << "0x" << translateIP(ip) << endl;
}

void otherIns(ADDRINT ip, const string *s) {
    out_file << INSIP << " " << hex << "0x" << translateIP(ip) << endl;
}


void instruction(INS ins, VOID* v) {
    ADDRINT addr = INS_Address(ins);
    if (addr < image_base || addr > image_end) return ;

    // gain two of operand numbers in nine kinds of circumstances
    // cmp instruments
    if (INS_Opcode(ins) == XED_ICLASS_CMP)
    {
        // Reg
        if (INS_OperandIsReg(ins, 0) && INS_OperandIsReg(ins, 1))
        {
            REG reg0 = INS_OperandReg(ins, 0);
            REG reg1 = INS_OperandReg(ins, 1);
            // ins insert call
            INS_InsertCall(ins, IPOINT_BEFORE, (AFUNPTR)regAndReg, 
                        IARG_INST_PTR, 
                        IARG_REG_VALUE, reg0,
                        IARG_REG_VALUE, reg1,
                        IARG_END);
        }
        else if (INS_OperandIsReg(ins, 0) && INS_OperandIsMemory(ins, 1))
        {
            REG reg0 = INS_OperandReg(ins, 0);
            // ins insert call
            INS_InsertCall(ins, IPOINT_BEFORE, (AFUNPTR)regAndMem, 
                        IARG_INST_PTR, 
                        IARG_REG_VALUE, reg0,
                        IARG_MEMORYREAD_EA,
                        IARG_END);
        }
        else if (INS_OperandIsReg(ins, 0) && INS_OperandIsImmediate(ins, 1))
        {
            REG reg0 = INS_OperandReg(ins, 0);
            // ins insert call
            INS_InsertCall(ins, IPOINT_BEFORE, (AFUNPTR)regAndImm, 
                        IARG_INST_PTR, 
                        IARG_REG_VALUE, reg0,
                        IARG_ADDRINT, INS_OperandImmediate(ins, 1),
                        IARG_END);
        }
        // Mem
        else if (INS_OperandIsMemory(ins, 0) && INS_OperandIsReg(ins, 1))
        {
            REG reg1 = INS_OperandReg(ins, 1);
            // ins insert call
            INS_InsertCall(ins, IPOINT_BEFORE, (AFUNPTR)memAndReg, 
                        IARG_INST_PTR, 
                        IARG_MEMORYREAD_EA,
                        IARG_REG_VALUE, reg1,
                        IARG_END);
        }
        else if (INS_OperandIsMemory(ins, 0) && INS_OperandIsMemory(ins, 1))
        {
            INS_InsertCall(ins, IPOINT_BEFORE, (AFUNPTR)memAndMem, 
                        IARG_INST_PTR, 
                        IARG_MEMORYREAD_EA,
                        IARG_MEMORYREAD_EA,
                        IARG_END);
        }
        else if (INS_OperandIsMemory(ins, 0) && INS_OperandIsImmediate(ins, 1))
        {
            INS_InsertCall(ins, IPOINT_BEFORE, (AFUNPTR)memAndImm, 
                        IARG_INST_PTR, 
                        IARG_MEMORYREAD_EA,
                        IARG_ADDRINT, INS_OperandImmediate(ins, 1),
                        IARG_END);
        }
        // Imm
        else if (INS_OperandIsImmediate(ins, 0) && INS_OperandIsReg(ins, 1))
        {
            REG reg1 = INS_OperandReg(ins, 1);
            // ins insert call
            INS_InsertCall(ins, IPOINT_BEFORE, (AFUNPTR)immAndReg, 
                        IARG_INST_PTR, 
                        IARG_ADDRINT, INS_OperandImmediate(ins, 0),
                        IARG_REG_VALUE, reg1,
                        IARG_END);
        }
        else if (INS_OperandIsImmediate(ins, 0) && INS_OperandIsMemory(ins, 1))
        {
            // ins insert call
            INS_InsertCall(ins, IPOINT_BEFORE, (AFUNPTR)immAndMem, 
                        IARG_INST_PTR, 
                        IARG_ADDRINT, INS_OperandImmediate(ins, 0),
                        IARG_MEMORYREAD_EA,
                        IARG_END);
        }
        else if (INS_OperandIsImmediate(ins, 0) && INS_OperandIsImmediate(ins, 1))
        {
            // ins insert call
            INS_InsertCall(ins, IPOINT_BEFORE, (AFUNPTR)immAndImm, 
                        IARG_INST_PTR, 
                        IARG_ADDRINT, INS_OperandImmediate(ins, 0),
                        IARG_ADDRINT, INS_OperandImmediate(ins, 1),
                        IARG_END);
        }
        // Other
        else
        {
            // ins insert call
            INS_InsertCall(ins, IPOINT_BEFORE, (AFUNPTR)otherCmp, 
                        IARG_INST_PTR, 
                        IARG_END);
        }
    }
    // other instruments 
    else
    {
        INS_InsertCall(ins, IPOINT_BEFORE, (AFUNPTR)otherIns, 
                    IARG_INST_PTR, 
                    IARG_END);
    }
    
}


INT32 Usage()
{
    cerr << "This tool gain the dynamic information of program." << endl;
    return -1;
}


VOID Fini(INT32 code, VOID* v)
{
    if (out_file.is_open()) out_file.close();
}


int main(int argc, char* argv[])
{
    PIN_InitSymbols();
    if (PIN_Init(argc, argv)) return Usage();

    out_file.open(KnobOutputFile.Value().c_str());
    IMG_AddInstrumentFunction(image, 0);
    INS_AddInstrumentFunction(instruction, 0);
    PIN_AddFiniFunction(Fini, 0);
    PIN_StartProgram();
    return 0;
}