# Install LLVM.

## Environment

- Ubuntu 18.04.5 LTS or Ubuntu 20.04.3 LTS
- LLVM 12.0.1
- Clang 12.0.1
- CMake 3.21.1

## Download the files to be compiled.

```bash
sudo apt update
sudo apt upgrade
sudo apt-get install xz-utils 
sudo apt-get install gcc automake autoconf libtool make
sudo apt-get install build-essential
sudo apt-get install python3.7
mkdir LLVM
# install cmake 3.21.1
wget https://github.com/Kitware/CMake/releases/download/v3.21.1/cmake-3.21.1-linux-x86_64.tar.gz
tar -zxvf cmake-3.21.1-linux-x86_64.tar.gz
mv cmake-3.21.1-linux-x86_64 /opt/cmake-3.21.1
ln -sf /opt/cmake-3.21.1/bin/* /usr/bin/
cmake --version

# install clang, llvm, compiler-rt.
wget https://github.com/llvm/llvm-project/releases/download/llvmorg-12.0.1/clang-12.0.1.src.tar.xz
tar -xf clang-12.0.1.src.tar.xz
mv clang-12.0.1.src clang

wget https://github.com/llvm/llvm-project/releases/download/llvmorg-12.0.1/llvm-12.0.1.src.tar.xz
tar -xf llvm-12.0.1.src.tar.xz
mv llvm-12.0.1.src llvm
mkdir build

wget https://github.com/llvm/llvm-project/releases/download/llvmorg-12.0.1/compiler-rt-12.0.1.src.tar.xz
tar -xf compiler-rt-12.0.1.src.tar.xz
mv compiler-rt-12.0.1.src compiler-rt

vim build.sh
```

Create build.sh file. The contents of this file.

```bash
cd build
cmake -G "Unix Makefiles" -DLLVM_ENABLE_PROJECTS="clang" \
    -DCMAKE_BUILD_TYPE=Release -DLLVM_TARGETS_TO_BUILD="X86" \
    -DBUILD_SHARED_LIBS=On ../llvm
make -j6
make install
```

Build it.

```bash
sudo ./build.sh
clang -v
```

Build compiler-rt.

```bash
mv compiler-rt llvm/projects/
cd llvm/projects/compiler-rt
cmake ../compiler-rt -DLLVM_CONFIG_PATH=PATH/LLVM/build/bin/llvm-config
vim CMakeCache.txt
# COMPILER_RT_INSTALL_PATH:PATH=/usr/local/lib/clang/12.0.1  # Replace path string.
make -j6
make install
```

