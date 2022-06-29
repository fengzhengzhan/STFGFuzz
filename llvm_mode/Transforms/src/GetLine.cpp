#include "llvm/Pass.h"
#include "llvm/IR/Function.h"
#include "llvm/Support/raw_ostream.h"
#include "llvm/IR/DebugInfo.h"
#include "llvm/IR/Instruction.h"

#include <iostream>
#include <string>
#include <fstream>

#define MAXLEN  128*1024*1024

using namespace llvm;

namespace{
    class GetLine : public FunctionPass{
        public:
            static char ID;

            GetLine() : FunctionPass(ID) {}

            bool runOnFunction(Function &F);
    };
}

bool GetLine::runOnFunction(Function &F){
    outs() << "\'" << F.getName() << "\':{";
    for(BasicBlock &BB : F){
        for(Instruction &In : BB){
            const DebugLoc &location = In.getDebugLoc();
            if (location){
                // Get the function filename.
                std::string temp_name = std::string(location->getFilename());
                std::string filename = "";
                for (int i=size(temp_name)-1; i >= 0; --i) {
                    if (temp_name[i] != '/') {
                        filename = temp_name[i] + filename;
                    }
                    else {
                        break;
                    }
                }

                // Get the Asm remove space.
                std::string ins;
                llvm::raw_string_ostream(ins) << In;
                ins.erase(std::remove_if(ins.begin(), ins.end(), isspace), ins.end());
                // std::string blanks("\f\v\r\t\n ");
                // ins.erase(0,ins.find_first_not_of(blanks));
                // ins.erase(ins.find_last_not_of(blanks) + 1);

                // Get the json file.
                outs() << location.getLine() << ":{"
                        // << "\'D\':\'" << location->getDirectory() << "\',"
                        << "\'N\':\'" << filename << "\',"
                        << "\'F\':\'" << F.getName() << "\',"
                        << "\'C\':\'" << location.getCol() << "\',"
                        // << "\'I\':\'" << In << "\',"
                        << "\'I\':\'" << ins << "\',"
                        << "},";
                        // << "\'P\':\'" << location->isImplicitCode() << "\',"

                // std::string str;
                // llvm::raw_string_ostream rso(str);
                // In.print(rso);

                // std::string filename = std::string(location->getFilename());
                // std::string ins = std::string(In);

                // for (int i=size(filename)-1; i >= 0; --i) {
                //     outs() << fs::path(filename).filename();
                // }
                // llvm::StringRef ins = In;

                // outs() << "{"
                //         // << "\'D\':\'" << location->getDirectory() << "\',"
                //         << "\'N\':\'" << location->getFilename() << "\',"
                //         << "\'F\':\'" << F.getName() << "\',"
                //         << "\'L\':\'" << location.getLine() << "\',"
                //         << "\'C\':\'" << location.getCol() << "\',"
                //         << "\'I\':\'" << In << "\',"
                //         << "},";

                        // << "\"" << In.getModule() << "\","
                        // << "},";
                        // << "\'P\':\'" << location->isImplicitCode() << "\',"
                
            }
                
        }
    }
    outs() << "},";
    return true;
}

char GetLine::ID = 0;
static RegisterPass<GetLine> X("line", "Binary to source code line mapping.");