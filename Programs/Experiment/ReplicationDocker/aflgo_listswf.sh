# dataset

# git clone https://github.com/libming/libming.git libming-CVE-2018-8807
# cd libming-CVE-2018-8807/;
# git checkout b72cc2f # version 0.4.8

# cp /root/LAVA-1.tar /root/aflgo/scripts/fuzz
# tar -xf LAVA-1.tar
# cd LAVA-1
# export LINE=292_R_0x12345678-0x12545678  # change it
# cp -r file-5.22/ file-5.22.$LINE ;
# cd file-5.22.$LINE
# git reset --hard
# git checkout $LINE ;

# tar -zxvf libming-ming-0_4_8.tar.gz
cd libming-ming-0_4_8

# compile
echo core >/proc/sys/kernel/core_pattern
echo performance | tee /sys/devices/system/cpu/cpu*/cpufreq/scaling_governor
export AFLGO=$HOME/aflgo

mkdir obj-aflgo; 
mkdir obj-aflgo/temp

export SUBJECT=$PWD; 
export TMP_DIR=$PWD/obj-aflgo/temp
export CC=$AFLGO/afl-clang-fast; 
export CXX=$AFLGO/afl-clang-fast++
export LDFLAGS=-lpthread
# -fcommon
export ADDITIONAL="-targets=$TMP_DIR/BBtargets.txt -outdir=$TMP_DIR -flto -fuse-ld=gold -Wl,-plugin-opt=save-temps -fcommon"
echo $'parser.c:1948' > $TMP_DIR/BBtargets.txt  # change it 
# ./autogen.sh;
autoreconf -f -i
cd obj-aflgo; 
# CFLAGS="-DFORTIFY_SOURCE=2 -fstack-protector-all -fno-omit-frame-pointer -g -Wno-error $ADDITIONAL" LDFLAGS="-ldl -lutil" ../configure --disable-shared --disable-gdb --disable-libdecnumber --disable-readline --disable-sim --disable-ld --with-php-config=/usr/bin/php-config7.2
CFLAGS="$ADDITIONAL" CXXFLAGS="$ADDITIONAL" ../configure --disable-shared --prefix=`pwd`
make clean; 
make

cat $TMP_DIR/BBnames.txt | rev | cut -d: -f2- | rev | sort | uniq > $TMP_DIR/BBnames2.txt && mv $TMP_DIR/BBnames2.txt $TMP_DIR/BBnames.txt
cat $TMP_DIR/BBcalls.txt | sort | uniq > $TMP_DIR/BBcalls2.txt && mv $TMP_DIR/BBcalls2.txt $TMP_DIR/BBcalls.txt

cd util; 
$AFLGO/scripts/genDistance.sh $SUBJECT $TMP_DIR swftophp
cd ../../; 
mkdir obj-dist; 
cd obj-dist; # work around because cannot run make distclean

# CC="/root/aflgo/scripts/../afl-clang-fast"
# CXX="/root/aflgo/scripts/../afl-clang-fast++"
# CFLAGS="$CFLAGS -distance=/root/aflgo/experiment/libming048/libming-ming-0_4_8/obj-aflgo/temp/distance.cfg.txt"
# CXXFLAGS="$CXXFLAGS -distance=/root/aflgo/experiment/libming048/libming-ming-0_4_8/obj-aflgo/temp/distance.cfg.txt"


# CFLAGS="-DFORTIFY_SOURCE=2 -fstack-protector-all -fno-omit-frame-pointer -g -Wno-error -distance=$TMP_DIR/distance.cfg.txt" LDFLAGS="-ldl -lutil" ../configure --disable-shared --disable-gdb --disable-libdecnumber --disable-readline --disable-sim --disable-ld
CFLAGS="-distance=$TMP_DIR/distance.cfg.txt -fcommon" CXXFLAGS="-distance=$TMP_DIR/distance.cfg.txt -fcommon" ../configure --disable-shared --prefix=`pwd`
make
mkdir in; 
# echo "" > in/in
# $AFLGO/afl-fuzz -m none -z exp -c 45m -i in -o out binutils/cxxfilt
wget -P in http://condor.depaul.edu/sjost/hci430/flash-examples/swf/bumble-bee1.swf
cp in/bumble-bee1.swf in/bumble-bee.swf
rm -rf in/bumble-bee1.swf
$AFLGO/afl-fuzz -m none -z exp -c 45m -i in -o out util/listswf @@
# mkdir out; for i in {1..10}; do timeout -sHUP 60m $AFLGO/afl-fuzz -m none -z exp -c 45m -i in -o "out/out_$i" binutils/cxxfilt > /dev/null 2>&1 & done

