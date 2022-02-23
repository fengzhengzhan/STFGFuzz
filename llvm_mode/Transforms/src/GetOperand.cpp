#include "llvm/Pass.h"
#include "llvm/IR/Function.h"
#include "llvm/Support/raw_ostream.h"

using namespace llvm;

namespace{
    class GetOperand : public FunctionPass{
        public:
            static char ID;
            GetOperand() : FunctionPass(ID) {}

            bool runOnFunction(Function &F);
    };
}

bool GetOperand::runOnFunction(Function &F){
    for(BasicBlock &BB : F){
        for(Instruction &In : BB){
            for(int i = 0; i < In.getNumOperands(); i ++){
                Value *v = In.getOperand(i);
                outs() << "Op" << i << ": " << *v << "\n";  //获取llvm的输出流
            }
        }
    }
}

char GetOperand::ID = 0;
static RegisterPass<GetOperand> X("op", "My first line of llvm pass");