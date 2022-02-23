cd ./Build
cmake ../Transforms
make
cd ../Test
# clang -S -emit-llvm demo.cpp -o demo.ll
# opt -load ../Build/LLVMObfuscator.so -hlw -S IR/demo.ll -o IR/demo_hlw.ll
opt -load ../Build/LLVMObfuscator.so -split -S IR/demo.ll -o IR/demo_split.ll
# clang IR/demo_hlw.ll -o Bin/demo_hlw
# ./demo_hlw
