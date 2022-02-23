#include "llvm/Pass.h"
#include "llvm/IR/Function.h"
#include "llvm/Support/raw_ostream.h"
#include "llvm/IR/Instructions.h"
#include "llvm/Support/CommandLine.h"
#include "SplitBasicBlock.h"
#include <vector>

using std::vector;
using namespace llvm;

// 可选的参数 指定基本块分割数
static cl::opt<int> splitNum("split_num", cl::init(2), cl::desc("Split <split_num> time(s) each BB"));

namespace{
    class SplitBasicBlock : public FunctionPass{
        public:
            static char ID;
            SplitBasicBlock() : FunctionPass(ID) {}

            bool runOnFunction(Function &F);

            bool containsPHI(BasicBlock *BB);

            void split(BasicBlock *BB);
    };
}

bool SplitBasicBlock::runOnFunction(Function &F){
    // todo
    vector<BasicBlock*> origBB;
    for(BasicBlock &BB : F){
        origBB.push_back(&BB);
    }
    for(BasicBlock *BB : origBB){
        if(!containsPHI(BB)){
            split(BB);
        }
    }
    return true;
}

bool SplitBasicBlock::containsPHI(BasicBlock *BB){
    for(Instruction &I : *BB){
        if(isa<PHINode>(&I)){
            return true;
        }
    }
    return false;
}

void SplitBasicBlock::split(BasicBlock *BB){
    //计算分裂后每个基本块的大小   原基本块大小 / 分裂数目   (向上取整)
    int splitSize = (BB->size() + splitNum - 1) / splitNum;
    BasicBlock *curBB = BB;
    for(int i = 1;i < splitNum;i ++){
        int cnt = 0;
        for(Instruction &I : *curBB){
            if(cnt++ == splitSize){
                // 在I指令处对基本块进行分割
                curBB = curBB->splitBasicBlock(&I);
                break;
            }
        }
    }
}

FunctionPass* llvm::createSplitBasicBlockPass(){
    return new SplitBasicBlock();
}

char SplitBasicBlock::ID = 0;
static RegisterPass<SplitBasicBlock> X("split", "Split one basic block inro multiple block;");