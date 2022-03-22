# STFGFuzz
Constraint Flow Graph Fuzzer

# Building STFGFuzz

### Build Requirements

- Linux-amd64 (Tested on Ubuntu 18.04/20.04)
- LLVM (llvm_mode/llvm_install.md)
- target programs (Programs/compile_programs.md)

### Build Target Program

```bash
pip install wllvm

# wllvm-sanity-checker
export FORCE_UNSAFE_CONFIGURE=1
export LLVM_COMPILER=clang
CC=wllvm CFLAGS="-g -O0" LIBS="-lacl" ./configure --prefix=`pwd`
make -j6  # -j Depends on the number of computer processes.
make install
extract-bc xxx  # Get the file in .bc format.

clang -fsanitize=address -fsanitize-coverage=trace-pc-guard,trace-cmp -emit-llvm -c xxx.bc -o xxxtrace.bc
opt -load ../Build/LLVMObfuscator.so -line -S xxxtrace.bc -o xxx_pass.bc
llc -filetype=obj xxx_pass.bc -o xxx.o
clang++ -fsanitize=address -Wl,--whole-archive -L./ClangSanitizer -lcmpcov -Wl,--no-whole-archive xxx.o -o xxx
```

# Program Structure

### Directory structure

- STFGFuzzer.py

