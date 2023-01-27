git clone git://repo.or.cz/nasm.git nasm
cd nasm;
git checkout 7a81ead
cd ..


DATASET=nasm
PROGRAM=nasm
SEED=paste.asm
TAINTPATH=/root/datav5/Angora-1.2.2/experiment/${DATASET}
ANGORA=/root/datav5/Angora-1.2.2

# compile dataset
echo core | sudo tee /proc/sys/kernel/core_pattern
cp -r ${DATASET} track
cd track

./autogen.sh
CC=${ANGORA}/bin/angora-clang CXX=${ANGORA}/bin/angora-clang++ CFLAGS="-Wno-error" ./configure --prefix=`pwd`/install
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
cd seeds
cp /root/dataset/${SEED} .
cp ${SEED} seed
rm ${SEED}
cd ..

${ANGORA}/angora_fuzzer -i seeds -o output -t ./track/install/bin/${PROGRAM} -- ./fast/install/bin/${PROGRAM} -f bin @@ -o /dev/null
