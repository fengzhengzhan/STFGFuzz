git clone https://git.code.sf.net/p/giflib/code giflib-bugs-74
cd giflib-bugs-74; git checkout 72e31ff
cd ..


DATASET=giflib-bugs-74
PROGRAM=gifsponge
TAINTPATH=/root/datav5/Angora-1.2.2/experiment/${PROGRAM}
ANGORA=/root/datav5/Angora-1.2.2

# compile dataset
echo core | sudo tee /proc/sys/kernel/core_pattern
cp -r ${DATASET} track
cd track

./autogen.sh
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

./autogen.sh
CC=${ANGORA}/bin/angora-clang CXX=${ANGORA}/bin/angora-clang++ CFLAGS="-Wno-error" ./configure --prefix=`pwd`/install --disable-shared
make
make install
cd ..

# Seeds
mkdir seeds
echo "GIF Hello World" > seeds/seed.txt

${ANGORA}/angora_fuzzer -i seeds -o output -t ./track/util/${PROGRAM} -- ./fast/util/${PROGRAM}
