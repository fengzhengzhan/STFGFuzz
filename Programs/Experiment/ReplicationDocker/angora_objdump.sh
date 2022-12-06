# git clone git://sourceware.org/git/binutils-gdb.git binutils_gdb_cve2016_nocheckout
# cd binutils_gdb_cve2016_nocheckout
# git checkout 2c49145
# cd ..

# objdump
DATASET=binutils-2.29
TAINTPATH=/root/datav5/Angora-1.2.2/experiment/objdump229
ANGORA=/root/datav5/Angora-1.2.2

# compile dataset
echo core | sudo tee /proc/sys/kernel/core_pattern
cp -r ${DATASET} track
cd track
# CC=${ANGORA}/bin/angora-clang CFLAGS="-Wno-error" ./configure --prefix=`pwd`/install --disable-shared
# CC=${ANGORA}/bin/angora-clang CFLAGS="-DFORTIFY_SOURCE=2 -fno-omit-frame-pointer -g -O0 -Wno-error" LDFLAGS="-ldl -lutil" ./configure --prefix=`pwd`/install --enable-static --disable-shared --disable-gdb --disable-libdecnumber --disable-readline --disable-sim --disable-ld
# CC=${ANGORA}/bin/angora-clang CXX=${ANGORA}/bin/angora-clang++ LD=${ANGORA}/bin/angora-clang CFLAGS="-Wno-error" ./configure --prefix=`pwd`/install --disable-shared
CC=${ANGORA}/bin/angora-clang CXX=${ANGORA}/bin/angora-clang++ CFLAGS="-Wno-error" ./configure --prefix=`pwd`/install --disable-shared
USE_TRACK=1 make

${ANGORA}/tools/gen_library_abilist.sh /usr/lib/x86_64-linux-gnu/libz.so  discard > zlib_abilist.txt
export ANGORA_TAINT_RULE_LIST=${TAINTPATH}/track/zlib_abilist.txt
make clean
USE_TRACK=1 make
make install
cd ..

# Compile program for branch counting
cp -r ${DATASET} fast
cd fast

CC=${ANGORA}/bin/angora-clang CXX=${ANGORA}/bin/angora-clang++ CFLAGS="-Wno-error" ./configure --prefix=`pwd`/install --disable-shared
make
make install
cd ..

# Seeds
mkdir seeds
echo "Hello World" > seeds/seed.txt
#${ANGORA}/angora_fuzzer -i seeds -o output -j 1 -t ./track/install/bin/c++filt -- cat @@ | xargs fast/install/bin/c++filt
# /root/datav5/Angora-1.2.2/angora_fuzzer -i seeds -o output -j 1 -t ./track/install/bin/size -- ./fast/install/bin/size @@
${ANGORA}/angora_fuzzer -i seeds -o output -t ./track/install/bin/objdump -- ./fast/install/bin/objdump -x @@
