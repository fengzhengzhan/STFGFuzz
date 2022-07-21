#!/bin/bash
# Compile and install LLVM

# install environment
apt update
apt -y install wget vim
apt -y install xz-utils 
apt -y install zlib1g-dev zlib*
apt -y install graphviz
apt -y install autopoint
apt -y install gcc g++ automake autoconf libtool make
apt -y install build-essential
apt -y install libacl1-dev
apt -y install python3 python3-pip  # ubuntu20.04 python3.8
pip3 install wllvm


cd ..

if [ ! -d "LLVM" ]; then
  mkdir LLVM
fi
cd LLVM

# link install cmake 3.21.1
if [ ! -f "cmake-3.21.1-linux-x86_64.tar.gz" ]; then
  wget https://github.com/Kitware/CMake/releases/download/v3.21.1/cmake-3.21.1-linux-x86_64.tar.gz
fi
tar -zxvf cmake-3.21.1-linux-x86_64.tar.gz
rm -f cmake-3.21.1-linux-x86_64.tar.gz
mv cmake-3.21.1-linux-x86_64 /opt/cmake-3.21.1
ln -sf /opt/cmake-3.21.1/bin/* /usr/bin/
cmake --version

# wget clang, llvm, compiler-rt.
if [ ! -f "clang-12.0.1.src.tar.xz" ]; then
  wget https://github.com/llvm/llvm-project/releases/download/llvmorg-12.0.1/clang-12.0.1.src.tar.xz
fi
tar -xf clang-12.0.1.src.tar.xz
rm -f clang-12.0.1.src.tar.xz
mv clang-12.0.1.src clang

if [ ! -f "llvm-12.0.1.src.tar.xz" ]; then
  wget https://github.com/llvm/llvm-project/releases/download/llvmorg-12.0.1/llvm-12.0.1.src.tar.xz
fi
tar -xf llvm-12.0.1.src.tar.xz
rm -f llvm-12.0.1.src.tar.xz
mv llvm-12.0.1.src llvm

if [ ! -f "compiler-rt-12.0.1.src.tar.xz" ]; then
  wget https://github.com/llvm/llvm-project/releases/download/llvmorg-12.0.1/compiler-rt-12.0.1.src.tar.xz
fi
tar -xf compiler-rt-12.0.1.src.tar.xz
rm -f compiler-rt-12.0.1.src.tar.xz
mv compiler-rt-12.0.1.src compiler-rt

# Create build.sh file. The contents of this file.
mkdir build
echo "cd build
cmake -G \"Unix Makefiles\" -DLLVM_ENABLE_PROJECTS=\"clang\" -DCMAKE_BUILD_TYPE=Release -DLLVM_TARGETS_TO_BUILD=\"X86\" -DBUILD_SHARED_LIBS=On ../llvm
make -j6
make install" > build.sh
chmod +x build.sh
# vim build.sh
# Build it.
./build.sh
clang -v

# Build compiler-rt.
mv compiler-rt llvm/projects/
cd llvm/projects/compiler-rt
cmake ../compiler-rt -DLLVM_CONFIG_PATH=../../../build/bin/llvm-config
# vim CMakeCache.txt  # COMPILER_RT_INSTALL_PATH:PATH=/usr/local/lib/clang/12.0.1  # Replace path string.
find -name 'CMakeCache.txt' | xargs perl -pi -e 's|COMPILER_RT_INSTALL_PATH:PATH=/usr/local|COMPILER_RT_INSTALL_PATH:PATH=/usr/local/lib/clang/12.0.1|g'
make -j6
make install
