#include "llvm/Pass.h"
#include "llvm/IR/Function.h"
#include "llvm/Support/raw_ostream.h"
#include "llvm/IR/DebugInfo.h"
#include "llvm/IR/Instruction.h"

#include <iostream>
#include <string>
#include <fstream>

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
                

                outs() << location.getLine() << ":{"
                        << "\'I\':\'" << In << "\',"
                        << "\'F\':\'" << F.getName() << "\',"
                        << "\'C\':\'" << location.getCol() << "\',"
                        << "\'N\':\'" << location->getFilename() << "\',"
                        << "\'D\':\'" << location->getDirectory() << "\',"
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