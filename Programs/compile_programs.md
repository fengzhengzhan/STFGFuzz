# Run BTFuzz on LAVA dataset

- Download LAVA-M Dataset: [Download](http://panda.moyix.net/~moyix/lava_corpus.tar.xz)

## LAVA-1

### lava-13796
```bash
sudo apt-get install autoconf automake libtool
# Do not change folder permissions, as CRASH_INPUT may not be generated.
su root
cd lava_corpus/LAVA-1/
# ./validate.sh
cp -r file-5.22/ file13796
cd file13796
git checkout 13796_R_0x12345678-0x22345678

# wllvm-sanity-checker
export FORCE_UNSAFE_CONFIGURE=1
export LLVM_COMPILER=clang
autoreconf -f -i
# WLLVM_CONFIGURE_ONLY=1
CC=wllvm CFLAGS="-g -O0 -fvisibility=default" LIBS="-lacl" ./configure --enable-static --disable-shared --prefix=`pwd`/lava-install
make -j$(nproc)  # -j Depends on the number of computer processes.
make install
cd lava-install/bin/
extract-bc file

sudo clang -lz -fsanitize=address -Wl,--whole-archive -L../../llvm_mode/ClangSanitizer -lcmpcov -Wl,--no-whole-archive code_IR/lava13796.o -o code_Bin/lava13796
```

## CVE-2016-4487

```
git clone git://sourceware.org/git/binutils-gdb.git cxxfilt-CVE-2016-4487
cd cxxfilt-CVE-2016-4487
git checkout 2c49145

# wllvm-sanity-checker
export FORCE_UNSAFE_CONFIGURE=1
export LLVM_COMPILER=clang
# --disable-multilib 64-bit-only  CC=wllvm CXX=wllvm++ CFLAGS="-g -O0 -fvisibility=default" LIBS="-lacl" ./configure --enable-static --disable-shared --prefix=`pwd`/lava-install
# AFLGo: CFLAGS="-DFORTIFY_SOURCE=2 -fstack-protector-all -fno-omit-frame-pointer -g -Wno-error -flto -fuse-ld=gold" LDFLAGS="-ldl -lutil" ../configure --disable-shared --disable-gdb --disable-libdecnumber --disable-readline --disable-sim --disable-ld
CC=wllvm CXX=wllvm++ CFLAGS="-g -O0 -Wno-error" LDFLAGS="-lutil" ./configure --enable-static --disable-shared --disable-gdb --disable-libdecnumber --disable-readline --disable-sim --disable-ld --prefix=`pwd`/obj-bc
make -j$(nproc)  # -j Depends on the number of computer processes.
make install
cd lava-install/bin/
extract-bc file


sudo clang -lz -fsanitize=address -Wl,--whole-archive -L../../llvm_mode/ClangSanitizer -lcmpcov -Wl,--no-whole-archive code_IR/lava13796.o -o code_Bin/lava13796
```

## LAVA-M

### base64

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
CC=wllvm CFLAGS="-g -O0" LIBS="-lacl" ./configure --disable-shared --prefix=`pwd`/lava-install
make -j$(nproc)  # -j Depends on the number of computer processes.
make install
cd lava-install/bin/
extract-bc base64

# clang -g -emit-llvm -c code.cc -o code.bc
# -fsanitize-coverage=bb,no-prune,trace-pc-guard  -fsanitize-coverage=edge,trace-pc-guard (default)
clang -fsanitize=address -fsanitize-coverage=edge,trace-pc-guard,trace-cmp -emit-llvm -c base64.bc -o base64_trace.bc
echo "{" >> file
opt -load ../Build/LLVMObfuscator.so -line -S base64_trace.bc -o base64_pass.bc >> file
echo "}" >> file
llc -filetype=obj base64_pass.bc -o base64.o
clang -fsanitize=address -Wl,--whole-archive -L./ClangSanitizer -lcmpcov -Wl,--no-whole-archive base64.o -o base64
```

### Problems

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

# fatal error: 'zlib.h' file not found
apt-get install zlib1g-dev

# ImportError: No module named 'typing'
wget https://bootstrap.pypa.io/pip/3.7/get-pip.py
python3 get-pip.py

# makeinfo: not found
sudo apt-get install texinfo

# bison: not found
sudo apt-get install flex bison

# Building GCC requires GMP 4.2+, MPFR 2.4.0+ and MPC 0.8.0+.
Install requires package.

# configure: error: I suspect your system does not have 32-bit developement libraries (libc and headers). If you have them, rerun configure with --enable-multilib. If you do not have them, and want to build a 64-bit-only compiler, rerun configure with --disable-multilib.
sudo apt-get install gcc-multilib
```

 
