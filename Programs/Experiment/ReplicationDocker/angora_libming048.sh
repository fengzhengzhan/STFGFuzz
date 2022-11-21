# compile dataset
echo core | sudo tee /proc/sys/kernel/core_pattern
ANGORA=/root/datav5/Angora-1.2.2
TIME=$(date "+%Y%m%d_%H%M%S")
PROGRAM=libming-ming-0_4_8

mkdir libming048
cd libming048
mv ${PROGRAM} ${PROGRAM}_${TIME}
tar -zxvf ../libming-ming-0_4_8.tar.gz

# compile track
cp -r ${PROGRAM} track
cd track
./autogen.sh
# CC=/root/datav5/Angora-1.2.2/bin/angora-clang CXX=/root/datav5/Angora-1.2.2/bin/angora-clang++ CFLAGS="-g -O0 -fcommon -ferror-limit=0 -Wno-error" ./configure --prefix=`pwd`/install --with-php-config=/usr/bin/php-config7.2  --enable-static --disable-shared --enable-php 
CC=${ANGORA}/bin/angora-clang CXX=${ANGORA}/bin/angora-clang++ CFLAGS="-g -O0 -fcommon -ferror-limit=0 -Wno-error" ./configure --prefix=`pwd`/install --with-php-config=/usr/bin/php-config7.2  --enable-static --disable-shared --enable-php 
USE_TRACK=1 make

# /root/datav5/Angora-1.2.2/tools/gen_library_abilist.sh /usr/lib/x86_64-linux-gnu/libz.so  discard > zlib_abilist.txt
${ANGORA}/tools/gen_library_abilist.sh /usr/lib/x86_64-linux-gnu/libz.so  discard > zlib_abilist.txt
export ANGORA_TAINT_RULE_LIST=/root/datav5/Angora-1.2.2/experiment/libming048/track/zlib_abilist.txt
make clean
USE_TRACK=1 make
make install
cd ..

# Compile program for branch counting
cp -r cxxfilt-CVE-2016-4487 fast
cd fast

CC=${ANGORA}/bin/angora-clang CXX=${ANGORA}/bin/angora-clang++ LD=${ANGORA}/bin/angora-clang CFLAGS="-Wno-error" ./configure --prefix=`pwd`/install --disable-shared
make
make install
cd ..

# Seeds
mkdir seeds
echo "Hello World" > seeds/seed.txt
#${ANGORA}/angora_fuzzer -i seeds -o output -j 1 -t ./track/install/bin/c++filt -- cat @@ | xargs fast/install/bin/c++filt
${ANGORA}/angora_fuzzer -i seeds -o output -j 1 -t ./track/install/bin/c++filt -- ./fast/install/bin/c++filt
if [ -d @@ ];then cat @@ | xargs fast/install/bin/c++filt; else ./fast/install/bin/c++filt -n ; fi






# get .bc file
#export FORCE_UNSAFE_CONFIGURE=1
#export LLVM_COMPILER=clang
#CC=wllvm CXX=wllvm++ CFLAGS="-DFORTIFY_SOURCE=2 -fno-omit-frame-pointer -g -O0 -Wno-error" LDFLAGS="-ldl -lutil" ./configure --prefix=`pwd`/obj-bc --enable-static --disable-shared --disable-gdb --disable-libdecnumber --disable-readline --disable-sim --disable-ld
#make clean
#make -j # -j$(nproc)  Depends on the number of computer processes.
#make install
#cd obj-bc/bin/
#extract-bc c++filt
#
#$ANGORA/bin/angora-clang c++filt.bc -o c++filt.fast
#USE_TRACK=1 $ANGORA/bin/angora-clang c++filt.bc -o c++filt.tt
#
#cd ..
#mkdir seeds
#echo "Hello World" > seeds/seed.txt
#rm -rf output
#$ANGORA/angora_fuzzer -i seeds -o output -t bin/c++filt.tt -- ./bin/c++filt.fast @@
