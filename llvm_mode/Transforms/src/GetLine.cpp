#include "llvm/Pass.h"
#include "llvm/IR/Function.h"
#include "llvm/Support/raw_ostream.h"
#include "llvm/IR/DebugInfo.h"
#include "llvm/IR/Instruction.h"

#include <string>

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
    for(BasicBlock &BB : F){
        for(Instruction &In : BB){
            const DebugLoc &location = In.getDebugLoc();
            if (location)
                outs() << In <<" see line:  " << location.getLine() << ", col " << location.getCol() << F.getName() << "   " << location->getFilename() << " " << location->getDirectory() << " \n \n \n";
            else
                outs() << "no debugloc information detected\n";
        }
    }
}

char GetLine::ID = 0;
static RegisterPass<GetLine> X("line", "My first line of llvm pass");