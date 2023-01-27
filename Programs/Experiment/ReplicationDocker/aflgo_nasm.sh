echo core > /proc/sys/kernel/core_pattern
echo performance | tee /sys/devices/system/cpu/cpu*/cpufreq/scaling_governor
export AFLGO=$HOME/aflgo  # /root/aflgo

git clone git://repo.or.cz/nasm.git nasm
cd nasm;
git checkout 7a81ead


mkdir obj-aflgo; mkdir obj-aflgo/temp
export SUBJECT=$PWD; export TMP_DIR=$PWD/obj-aflgo/temp
export CC=$AFLGO/afl-clang-fast; export CXX=$AFLGO/afl-clang-fast++
export LDFLAGS=-lpthread
export ADDITIONAL="-targets=$TMP_DIR/BBtargets.txt -outdir=$TMP_DIR -flto -fuse-ld=gold -Wl,-plugin-opt=save-temps"
echo $'nasm.c:453\nnasm.c:1233\npreproc.c:5211\npreproc.c:4867\npreproc.c:1226\nmalloc.c:47\npreproc.c:5116\npreproc.c:1284\nmalloc.c:77\npreproc.c:1305' > $TMP_DIR/BBtargets.txt

./autogen.sh; make distclean
cd obj-aflgo; 
CFLAGS="$ADDITIONAL" CXXFLAGS="$ADDITIONAL" ../configure --prefix=`pwd`
make clean; 
make

cat $TMP_DIR/BBnames.txt | rev | cut -d: -f2- | rev | sort | uniq > $TMP_DIR/BBnames2.txt && mv $TMP_DIR/BBnames2.txt $TMP_DIR/BBnames.txt
cat $TMP_DIR/BBcalls.txt | sort | uniq > $TMP_DIR/BBcalls2.txt && mv $TMP_DIR/BBcalls2.txt $TMP_DIR/BBcalls.txt


cd util; 
$AFLGO/scripts/genDistance.sh $SUBJECT $TMP_DIR nasm
cd ../../; 
mkdir obj-dist; 
cd obj-dist; # work around because cannot run make distclean

# CFLAGS="-DFORTIFY_SOURCE=2 -fstack-protector-all -fno-omit-frame-pointer -g -Wno-error -distance=$TMP_DIR/distance.cfg.txt" LDFLAGS="-ldl -lutil" ../configure --disable-shared --disable-gdb --disable-libdecnumber --disable-readline --disable-sim --disable-ld
CFLAGS="-distance=$TMP_DIR/distance.cfg.txt" CXXFLAGS="-distance=$TMP_DIR/distance.cfg.txt" ../configure --prefix=`pwd`
make
mkdir in; 
echo "" > in/in
$AFLGO/afl-fuzz -m none -z exp -c 45m -i in -o out $FUZZ_DIR/nasm -f bin @@ -o /dev/null
