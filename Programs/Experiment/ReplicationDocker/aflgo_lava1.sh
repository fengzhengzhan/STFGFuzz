export AFLGO=$HOME/aflgo
export LINE=357_R_0x12345678-0x12345678    # change it

echo core >/proc/sys/kernel/core_pattern
echo performance | tee /sys/devices/system/cpu/cpu*/cpufreq/scaling_governor
tar -xf /root/LAVA-1.tar -C ./
cd LAVA-1


cp -r file-5.22/ file-5.22.$LINE ;
cd file-5.22.$LINE
git reset --hard
git checkout $LINE ;

mkdir obj-aflgo; 
mkdir obj-aflgo/temp

export SUBJECT=$PWD; 
export TMP_DIR=$PWD/obj-aflgo/temp
export CC=$AFLGO/afl-clang-fast; 
export CXX=$AFLGO/afl-clang-fast++
export LDFLAGS=-lpthread
export ADDITIONAL="-targets=$TMP_DIR/BBtargets.txt -outdir=$TMP_DIR -flto -fuse-ld=gold -Wl,-plugin-opt=save-temps"
echo $'cdf.c:298' > $TMP_DIR/BBtargets.txt  # change it 
autoreconf -f -i
cd obj-aflgo; 

# CFLAGS="-DFORTIFY_SOURCE=2 -fstack-protector-all -fno-omit-frame-pointer -g -Wno-error $ADDITIONAL" LDFLAGS="-ldl -lutil" ../configure --disable-shared --disable-gdb --disable-libdecnumber --disable-readline --disable-sim --disable-ld
CFLAGS="-fvisibility=default -Wno-error $ADDITIONAL" ../configure --disable-shared
make clean; 
make

cat $TMP_DIR/BBnames.txt | rev | cut -d: -f2- | rev | sort | uniq > $TMP_DIR/BBnames2.txt && mv $TMP_DIR/BBnames2.txt $TMP_DIR/BBnames.txt
cat $TMP_DIR/BBcalls.txt | sort | uniq > $TMP_DIR/BBcalls2.txt && mv $TMP_DIR/BBcalls2.txt $TMP_DIR/BBcalls.txt
cd src; 
$AFLGO/scripts/genDistance.sh $SUBJECT $TMP_DIR file
cd ../../; 
mkdir obj-dist; 
cd obj-dist; # work around because cannot run make distclean

# CFLAGS="-DFORTIFY_SOURCE=2 -fstack-protector-all -fno-omit-frame-pointer -g -Wno-error -distance=$TMP_DIR/distance.cfg.txt" LDFLAGS="-ldl -lutil" ../configure --disable-shared --disable-gdb --disable-libdecnumber --disable-readline --disable-sim --disable-ld
# CFLAGS="-Wno-error -distance=$TMP_DIR/distance.cfg.txt" LDFLAGS="-ldl -lutil" ../configure --disable-shared
CFLAGS="-fvisibility=default -Wno-error -distance=$TMP_DIR/distance.cfg.txt" ../configure --disable-shared
make

mkdir in; 
# cp /root/aflgov6/helloworld_elf in/in
# echo "" > in/in
cp /root/dataset/rand.seed in/in
$AFLGO/afl-fuzz -m none -z exp -c 45m -i in -o out src/file
# mkdir out; for i in {1..10}; do timeout -sHUP 60m $AFLGO/afl-fuzz -m none -z exp -c 45m -i in -o "out/out_$i" binutils/cxxfilt > /dev/null 2>&1 & done

