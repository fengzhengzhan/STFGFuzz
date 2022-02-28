# Run BTFuzz on LAVA dataset

- Download LAVA-M Dataset: [Download](http://panda.moyix.net/~moyix/lava_corpus.tar.xz)

## base64

```bash
apt-get install python3-pip
pip install wllvm

cd lava_corpus/LAVA-M/base64/coreutils-8.24-lava-safe
export FORCE_UNSAFE_CONFIGURE=1
export LLVM_COMPILER=clang
CC=wllvm CFLAGS="-fsanitize=address -fsanitize-coverage=trace-pc-guard,trace-cmp" ./configure --disable-shared --prefix=`pwd`/lava-install LIBS="-lacl"
make -j6  # -j Depends on the number of computer processes.
make install
cd lava-install/bin/

extract-bc base64
opt -load ../Build/LLVMObfuscator.so -split -S xx.bc -o xx_pass.bc
llc -filetype=obj base64.bc -o base64.o
clang++ base64.o -o base64 -fsanitize=address -Wl,--whole-archive -L./ClangSanitizer -lcmpcov -Wl,--no-whole-archive 
```
