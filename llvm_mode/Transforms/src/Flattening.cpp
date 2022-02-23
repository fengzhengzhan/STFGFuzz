#include "llvm/IR/Function.h"
#include "llvm/Pass.h"
#include "llvm/IR/LegacyPassManager.h"
#include "llvm/Transforms/IPO/PassManagerBuilder.h"
#include "llvm/Support/raw_ostream.h"
#include "llvm/IR/Instructions.h"
#include "llvm/Transforms/Utils.h"
#include "llvm/Support/CommandLine.h"
#include "llvm/Transforms/Utils/Local.h"
#include "SplitBasicBlock.h"
#include "Utils.h"
#include <vector>
#include <cstdlib>
#include <ctime>
using namespace llvm;
using std::vector;

namespace{
    class Flattening : public FunctionPass{
        public:
            static char ID;
            Flattening() : FunctionPass(ID){
                srand(time(0));
            }

            // Using flatten for function F.
            void flatten(Function &F);
            
            bool runOnFunction(Function &F);
    };
}

bool Flattening::runOnFunction(Function &F){
    INIT_CONTEXT(F);
    // Split Basic Block
    FunctionPass *pass = createSplitBasicBlockPass();
    pass->runOnFunction(F);
    flatten(F);
    return true;
}

void Flattening::flatten(Function &F){
    // Step 1: Save all basic blocks except entry block.
    vector<BasicBlock*> origBB;
    for(BasicBlock &BB : F){
        origBB.push_back(&BB);
    }
    origBB.erase(origBB.begin());
    BasicBlock &entryBB = F.getEntryBlock();

    // The entry block will be determined whether it is a conditional jump or not. 
    if(BranchInst *br = dyn_cast<BranchInst>(entryBB.getTerminator())){
        if(br->isConditional()){
            origBB.insert(origBB.begin(), entryBB.splitBasicBlock(br));
        }
    }

    // Step 2: Create dispatch blocks and return blocks.
    BasicBlock *dispatchBB = BasicBlock::Create(*CONTEXT, "dispatchBB", &F, &entryBB);
    BasicBlock *returnBB = BasicBlock::Create(*CONTEXT, "returnBB", &F, &entryBB);
    entryBB.moveBefore(dispatchBB);
    entryBB.getTerminator()->eraseFromParent();
    BranchInst::Create(dispatchBB, &entryBB);
    BranchInst::Create(dispatchBB, returnBB);

    // Step 3: Implementing the scheduling function for distribution blocks.
    int randNumCase = rand();
    AllocaInst *swVarPtr = new AllocaInst(TYPE_I32, 0, "swVar.ptr", entryBB.getTerminator());
    new StoreInst(CONST_I32(randNumCase), swVarPtr, entryBB.getTerminator());
    LoadInst *swVar = new LoadInst(TYPE_I32, swVarPtr, "swVar", dispatchBB);
    BasicBlock *defaultBB = BasicBlock::Create(*CONTEXT, "defaultBB", &F, returnBB);
    BranchInst::Create(returnBB, defaultBB);
    SwitchInst *swInst = SwitchInst::Create(swVar, defaultBB, 0, dispatchBB);
    for(BasicBlock *BB : origBB){
        BB->moveBefore(returnBB);
        swInst->addCase(CONST_I32(randNumCase), BB);
        randNumCase = rand();
    }
    // Step 4: Implement automatic adjustment of distribution blocks.
    for(BasicBlock *BB : origBB){
        if(BB->getTerminator()->getNumSuccessors() == 0){
            continue;
        }else if(BB->getTerminator()->getNumSuccessors() == 1){
            ConstantInt *numCase = swInst->findCaseDest(BB->getTerminator()->getSuccessor(0));
            new StoreInst(numCase, swVarPtr, BB->getTerminator());
            BB->getTerminator()->eraseFromParent();
            BranchInst::Create(returnBB, BB);
        }else if(BB->getTerminator()->getNumSuccessors() == 2){
            ConstantInt *numCase1 = swInst->findCaseDest(BB->getTerminator()->getSuccessor(0));
            ConstantInt *numCase2 = swInst->findCaseDest(BB->getTerminator()->getSuccessor(1));
            BranchInst *br = cast<BranchInst>(BB->getTerminator());
            SelectInst *sel = SelectInst::Create(br->getCondition(), numCase1, numCase2, "", BB->getTerminator());
            new StoreInst(sel, swVarPtr, BB->getTerminator());
            BB->getTerminator()->eraseFromParent();
            BranchInst::Create(returnBB, BB);
        }
    }
    // Step 5: Fix PHI commands and escape variables.
    fixStack(F);

}

char Flattening::ID = 0;
static RegisterPass<Flattening> X("fla", "My control flow flattening obfuscation."); 
