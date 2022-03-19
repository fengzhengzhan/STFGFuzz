# Run BTFuzz on LAVA dataset

- Download LAVA-M Dataset: [Download](http://panda.moyix.net/~moyix/lava_corpus.tar.xz)

## base64

```bash
# docker:ubuntu18.04
docker pull ubuntu18.04
docker images
sudo docker run --restart=always --name=base64 -v /home/dataset:/root/dataset -itd ubuntu:18.04 /bin/bash
docker ps -a
sudo docker exec -it ContainerID /bin/bash

# root 
apt-get install python3 python3-pip
pip3 install wllvm

chmod 777 dataset
cd lava_corpus/LAVA-M/base64/coreutils-8.24-lava-safe
# wllvm-sanity-checker
export FORCE_UNSAFE_CONFIGURE=1
export LLVM_COMPILER=clang
CC=wllvm CFLAGS="-g -O0" LIBS="-lacl" ./configure --prefix=`pwd`/lava-install
make -j6  # -j Depends on the number of computer processes.
make install
cd lava-install/bin/
extract-bc base64

clang -fsanitize=address -fsanitize-coverage=trace-pc-guard,trace-cmp -emit-llvm -c base64.bc -o base64trace.bc
opt -load ../Build/LLVMObfuscator.so -line -S base64trace.bc -o base64_pass.bc
llc -filetype=obj base64_pass.bc -o base64.o
clang++ -fsanitize=address -Wl,--whole-archive -L./ClangSanitizer -lcmpcov -Wl,--no-whole-archive base64.o -o base64
```

## Problems

```bash
apt install build-essential
# install libacl
apt-get install libacl1-dev
# xlocale.h file not found
ln -s /usr/include/locale.h /usr/include/xlocale.h
# selinux/context.h file not found
apt-get install libselinux-dev 
apt install selinux selinux-utils selinux-basics auditd audispd-plugins
apt-get install libcap-dev
apt-get install libgmp3-dev
# configure: error: C compiler cannot create executables
apt-get install gcc libc6-dev
# fatal error: zlib.h: No such file or directory
apt-get install zlib1g-dev
# install check
./configure
make
make check
make install then
make installcheck 
## /usr/bin/ld: ../boot/a6le/kernel.o: relocation R_X86_64_32S against `.rodata' can not be used when making a PIE object; recompile with -fPIE
LDFLAGS=-no-pie ./configure
# -fsanitize-recover=address
```

 
