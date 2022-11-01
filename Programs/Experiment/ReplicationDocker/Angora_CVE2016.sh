export ANGORA=$HOME/datav5/Angora-1.2.2
git clone git://sourceware.org/git/binutils-gdb.git cxxfilt-CVE-2016-4487
cd cxxfilt-CVE-2016-4487
git checkout 2c49145

# get .bc file
export FORCE_UNSAFE_CONFIGURE=1
export LLVM_COMPILER=clang
CC=wllvm CXX=wllvm++ CFLAGS="-DFORTIFY_SOURCE=2 -fno-omit-frame-pointer -g -O0 -Wno-error" LDFLAGS="-ldl -lutil" ./configure --prefix=`pwd`/obj-bc --enable-static --disable-shared --disable-gdb --disable-libdecnumber --disable-readline --disable-sim --disable-ld
make clean
make -j # -j$(nproc)  Depends on the number of computer processes.
make install
cd obj-bc/bin/
extract-bc c++filt

$ANGORA/bin/angora-clang c++filt.bc -o c++filt.fast
USE_TRACK=1 $ANGORA/bin/angora-clang c++filt.bc -o c++filt.tt

cd ..
mkdir seeds
echo "Hello World" > seeds/seed.txt
rm -rf output
$ANGORA/angora_fuzzer -i seeds -o output -t bin/c++filt.tt -- ./bin/c++filt.fast @@
