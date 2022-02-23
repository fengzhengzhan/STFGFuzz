#include "llvm/Pass.h"
#include "llvm/IR/Function.h"
#include "llvm/Support/raw_ostream.h"

using namespace llvm;

namespace{
    class HelloWorld : public FunctionPass{
        public:
            static char ID;
            HelloWorld() : FunctionPass(ID) {}

            bool runOnFunction(Function &F);
    };
}

bool HelloWorld::runOnFunction(Function &F){
    // todo
    outs() << "Func: " << F.getName() << "\n";  //获取llvm的输出流
}

char HelloWorld::ID = 0;
static RegisterPass<HelloWorld> X("hlw", "My first line of llvm pass");