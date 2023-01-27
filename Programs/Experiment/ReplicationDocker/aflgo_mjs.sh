echo core > /proc/sys/kernel/core_pattern
echo performance | tee /sys/devices/system/cpu/cpu*/cpufreq/scaling_governor
export AFLGO=$HOME/aflgo  # /root/aflgo

git clone https://github.com/cesanta/mjs.git mjs
cd mjs; 
# 1. mjs73
# git checkout e4ea33a
# 2. mjs.c:9320
# git checkout d6c06a6
# 3. mjs.c:13671
git checkout 9eae0e6
mkdir obj-aflgo; mkdir obj-aflgo/temp
export SUBJECT=$PWD; export TMP_DIR=$PWD/obj-aflgo/temp
export CC=$AFLGO/afl-clang-fast; export CXX=$AFLGO/afl-clang-fast++
export LDFLAGS=-lpthread
export ADDITIONAL="-targets=$TMP_DIR/BBtargets.txt -outdir=$TMP_DIR -flto -fuse-ld=gold -Wl,-plugin-opt=save-temps"
# 1. mjs73
# echo $'mjs.c:12068\nmjs.c:9781\nmjs.c:9758\nmjs.c:9418\nmjs.c:13706\nmjs.c:4924\nmjs.c:9541\nmjs.c:12012\nmjs.c:11963\nmjs.c:6434\nmjs.c:6058\nmjs.c:5976\nmjs.c:5936\nmjs.c:5970\nmjs.c:5884\nmjs.c:11870\nmjs.c:5938\nmjs.c:5794\nmjs.c:5790' > $TMP_DIR/BBtargets.txt
# 2. mjs.c:9320
# echo $'mjs.c:12068\nmjs.c:9781\nmjs.c:9758\nmjs.c:9418\nmjs.c:13706\nmjs.c:4924\nmjs.c:9541\nmjs.c:12012\nmjs.c:11963\nmjs.c:6434\nmjs.c:6058\nmjs.c:5976\nmjs.c:5936\nmjs.c:5970\nmjs.c:5884\nmjs.c:11870\nmjs.c:5938\nmjs.c:5794\nmjs.c:5790' > $TMP_DIR/BBtargets.txt
# 3. mjs.c:13671
echo $'mjs.c:13671\nmjs.c:11870\nmjs.c:5884' > $TMP_DIR/BBtargets.txt
$CC -DMJS_MAIN mjs.c $ADDITIONAL -ldl -g -o mjs-bin
cat $TMP_DIR/BBnames.txt | rev | cut -d: -f2- | rev | sort | uniq > $TMP_DIR/BBnames2.txt && mv $TMP_DIR/BBnames2.txt $TMP_DIR/BBnames.txt
cat $TMP_DIR/BBcalls.txt | sort | uniq > $TMP_DIR/BBcalls2.txt && mv $TMP_DIR/BBcalls2.txt $TMP_DIR/BBcalls.txt
$AFLGO/scripts/genDistance.sh $SUBJECT $TMP_DIR mjs-bin
$CC -DMJS_MAIN mjs.c -distance=$TMP_DIR/distance.cfg.txt -ldl -g -o mjs-bin
cd obj-aflgo; mkdir in; echo "" > in/in
$AFLGO/afl-fuzz -m none -z exp -c 45m -i in -o out ../mjs-bin -f @@
# mkdir out; for i in {1..10}; do timeout -sHUP 180m $AFLGO/afl-fuzz -m none -z exp -c 45m -i in -o "out/out_$i" ../mjs-bin -f @@ > /dev/null 2>&1 & done
