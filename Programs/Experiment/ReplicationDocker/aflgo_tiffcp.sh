echo core > /proc/sys/kernel/core_pattern
echo performance | tee /sys/devices/system/cpu/cpu*/cpufreq/scaling_governor
export AFLGO=$HOME/aflgo  # /root/aflgo
# tar -zxvf libtiff-Release-v4-0-7.tar.gz

mkdir obj-aflgo; 
mkdir obj-aflgo/temp

export SUBJECT=$PWD; 
export TMP_DIR=$PWD/obj-aflgo/temp  
export CC=$AFLGO/afl-clang-fast; 
export CXX=$AFLGO/afl-clang-fast++  
export LDFLAGS=-lpthread 
export ADDITIONAL="-targets=$TMP_DIR/BBtargets.txt -outdir=$TMP_DIR -flto -fuse-ld=gold -Wl,-plugin-opt=save-temps" 
echo $'tiffcp.c:784\ntiffcp.c:304\nlibc-start.c:308' > $TMP_DIR/BBtargets.txt
cd obj-aflgo; 
CFLAGS="$ADDITIONAL" CXXFLAGS="$ADDITIONAL" ../configure --disable-shared --prefix=`pwd`
make clean; 
make

cat $TMP_DIR/BBnames.txt | rev | cut -d: -f2- | rev | sort | uniq > $TMP_DIR/BBnames2.txt && mv $TMP_DIR/BBnames2.txt $TMP_DIR/BBnames.txt
cat $TMP_DIR/BBcalls.txt | sort | uniq > $TMP_DIR/BBcalls2.txt && mv $TMP_DIR/BBcalls2.txt $TMP_DIR/BBcalls.txt

cd tools; 
$AFLGO/scripts/genDistance.sh $SUBJECT $TMP_DIR tiffcp
cd ../../; 
mkdir obj-dist; 
cd obj-dist; # work around because cannot run make distclean

CFLAGS="-distance=$TMP_DIR/distance.cfg.txt" CXXFLAGS="-distance=$TMP_DIR/distance.cfg.txt" ../configure --disable-shared --prefix=`pwd`
make

mkdir in; 
echo "" > in/in

$AFLGO/afl-fuzz -m none -z exp -c 45m -i in -o out tools/tiffcp -i @@ /tmp/foo

# mkdir out; for i in {1..10}; do timeout -sHUP 60m $AFLGO/afl-fuzz -m none -z exp -c 45m -i in -o "out/out_$i" binutils/cxxfilt > /dev/null 2>&1 & done
