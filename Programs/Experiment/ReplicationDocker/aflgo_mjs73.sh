echo core > /proc/sys/kernel/core_pattern
echo performance | tee /sys/devices/system/cpu/cpu*/cpufreq/scaling_governor
export AFLGO=$HOME/aflgo  # /root/aflgo

git clone https://github.com/cesanta/mjs.git mjs-issues-73
cd mjs-issues-73; git checkout e4ea33a
mkdir obj-aflgo; mkdir obj-aflgo/temp
export SUBJECT=$PWD; export TMP_DIR=$PWD/obj-aflgo/temp
export CC=$AFLGO/afl-clang-fast; export CXX=$AFLGO/afl-clang-fast++
export LDFLAGS=-lpthread
export ADDITIONAL="-targets=$TMP_DIR/BBtargets.txt -outdir=$TMP_DIR -flto -fuse-ld=gold -Wl,-plugin-opt=save-temps"
echo $'mjs.c:9320\nmjs.c:9503\nmjs.c:9526' > $TMP_DIR/BBtargets.txt
$CC -DMJS_MAIN mjs.c $ADDITIONAL -ldl -g -o mjs-bin
cat $TMP_DIR/BBnames.txt | rev | cut -d: -f2- | rev | sort | uniq > $TMP_DIR/BBnames2.txt && mv $TMP_DIR/BBnames2.txt $TMP_DIR/BBnames.txt
cat $TMP_DIR/BBcalls.txt | sort | uniq > $TMP_DIR/BBcalls2.txt && mv $TMP_DIR/BBcalls2.txt $TMP_DIR/BBcalls.txt
$AFLGO/scripts/genDistance.sh $SUBJECT $TMP_DIR mjs-bin
$CC -DMJS_MAIN mjs.c -distance=$TMP_DIR/distance.cfg.txt -ldl -g -o mjs-bin
cd obj-aflgo; mkdir in; echo "" > in/in
$AFLGO/afl-fuzz -m none -z exp -c 45m -i in -o out ../mjs-bin -f @@
# mkdir out; for i in {1..10}; do timeout -sHUP 180m $AFLGO/afl-fuzz -m none -z exp -c 45m -i in -o "out/out_$i" ../mjs-bin -f @@ > /dev/null 2>&1 & done
