#include "llvm/Pass.h"
#include "llvm/IR/Function.h"
#include "llvm/Support/raw_ostream.h"
#include "llvm/IR/Instructions.h"
#include "llvm/Support/CommandLine.h"
#include <vector>

using std::vector;
using namespace llvm;

// Specify block tracking granularity.
static cl::opt<int> splitNum("size_num", cl::init(1), cl::desc("<-size_num>: Specify block tracking granularity. The range of values is 0-1."));

namespace{
    class TrackingEachBlock : public FunctionPass{
        public:
            static char ID;
            TrackingEachBlock() : FunctionPass(ID) {}

            bool runOnFunction(Function &F);
    };
}

bool TrackingEachBlock::runOnFunction(Function &F){
    // todo
    vector<BasicBlock*> origBB;
    for(BasicBlock &BB : F){
        origBB.push_back(&BB);
    }

    return true;
}

char TrackingEachBlock::ID = 0;
static RegisterPass<TrackingEachBlock> X("teb", "Split one basic block inro multiple block;");