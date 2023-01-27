git clone https://github.com/mdadams/jasper.git jasper-CVE-2015-5221
cd jasper-CVE-2015-5221; git checkout 142245b
cd ..

DATASET=jasper-CVE-2015-5221
PROGRAM=jasper
SEED=dog.1324.mif
TAINTPATH=/root/datav5/Angora-1.2.2/experiment/${PROGRAM}
ANGORA=/root/datav5/Angora-1.2.2

# compile dataset
echo core | sudo tee /proc/sys/kernel/core_pattern
cp -r ${DATASET} track
cd track

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
cd seeds
cp /root/dataset/${SEED} .
cp ${SEED} seed
rm ${SEED}
cd ..
# echo "00010002" > seeds/seed.txt

${ANGORA}/angora_fuzzer -i seeds -o output -t ./track/install/bin/${PROGRAM} -- ./fast/install/bin/${PROGRAM} -f @@ -t mif -F /tmp/out -T jpg
