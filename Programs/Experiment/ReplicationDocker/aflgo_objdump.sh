echo core > /proc/sys/kernel/core_pattern
echo performance | tee /sys/devices/system/cpu/cpu*/cpufreq/scaling_governor
export AFLGO=$HOME/aflgo  # /root/aflgo

git clone git://sourceware.org/git/binutils-gdb.git objdump
cd objdump; 
git checkout 2c49145
mkdir obj-aflgo; 
mkdir obj-aflgo/temp

export SUBJECT=$PWD;  # /root/aflgo/scripts/fuzz/objdump
export TMP_DIR=$PWD/obj-aflgo/temp  # /root/aflgo/scripts/fuzz/objdump/obj-aflgo/temp
export CC=$AFLGO/afl-clang-fast;   # /root/aflgo/afl-clang-fast
export CXX=$AFLGO/afl-clang-fast++  # /root/aflgo/afl-clang-fast++
export LDFLAGS=-lpthread  # 优化参数  引入多线程库，-pthread多引用，-lpthread线程安全
export ADDITIONAL="-targets=$TMP_DIR/BBtargets.txt -outdir=$TMP_DIR -flto -fuse-ld=gold -Wl,-plugin-opt=save-temps"  # -flto 会生成 GIMPLE（GCC 的内部表示之一）并将其写入目标文件中的特殊 ELF 部分。 -fuse-ld=gold GIMPLE 字节码的目标文件。 
echo $'libbfd.c:184\ncompress.c:248\nsection.c:1637\nelf.c:1036\nelf.c:1783\nelfcode.h:803\nformat.c:305\nobjdump.c:3418\nobjdump.c:3509\nobjdump.c:3530\nobjdump.c:3813' > $TMP_DIR/BBtargets.txt
cd obj-aflgo; 
CFLAGS="-DFORTIFY_SOURCE=2 -fstack-protector-all -fno-omit-frame-pointer -g -Wno-error $ADDITIONAL" LDFLAGS="-ldl -lutil" ../configure --disable-shared --disable-gdb --disable-libdecnumber --disable-readline --disable-sim --disable-ld
make clean; 
make

cat $TMP_DIR/BBnames.txt | rev | cut -d: -f2- | rev | sort | uniq > $TMP_DIR/BBnames2.txt && mv $TMP_DIR/BBnames2.txt $TMP_DIR/BBnames.txt
cat $TMP_DIR/BBcalls.txt | sort | uniq > $TMP_DIR/BBcalls2.txt && mv $TMP_DIR/BBcalls2.txt $TMP_DIR/BBcalls.txt

cd binutils; 
$AFLGO/scripts/genDistance.sh $SUBJECT $TMP_DIR cxxfilt
cd ../../; 
mkdir obj-dist; 
cd obj-dist; # work around because cannot run make distclean

CFLAGS="-DFORTIFY_SOURCE=2 -fstack-protector-all -fno-omit-frame-pointer -g -Wno-error -distance=$TMP_DIR/distance.cfg.txt" LDFLAGS="-ldl -lutil" ../configure --disable-shared --disable-gdb --disable-libdecnumber --disable-readline --disable-sim --disable-ld
make
mkdir in; 
echo "" > in/in
$AFLGO/afl-fuzz -m none -z exp -c 45m -i in -o out binutils/objdump -x @@

# mkdir out; for i in {1..10}; do timeout -sHUP 60m $AFLGO/afl-fuzz -m none -z exp -c 45m -i in -o "out/out_$i" binutils/cxxfilt > /dev/null 2>&1 & done
