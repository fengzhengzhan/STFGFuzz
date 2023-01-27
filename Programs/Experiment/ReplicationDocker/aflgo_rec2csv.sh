echo core > /proc/sys/kernel/core_pattern
echo performance | tee /sys/devices/system/cpu/cpu*/cpufreq/scaling_governor
export AFLGO=$HOME/aflgo  # /root/aflgo

wget ftp://ftp.gnu.org/gnu/recutils/recutils-1.8.tar.gz;
tar xvzf recutils-1.8.tar.gz; mv recutils-1.8 rec2csv; 
cd rec2csv;

# git clone https://github.com/libcheck/check.git && cd check && git checkout 0.12.0
# autoreconf --install
# ./configure
# make
# make check
# sudo make install

# apt-get install mdbtools mdbtools-gmdb mdbtools-dev
# sudo apt-get install kexi

mkdir obj-aflgo; mkdir obj-aflgo/temp
export SUBJECT=$PWD; export TMP_DIR=$PWD/obj-aflgo/temp
export CC=$AFLGO/afl-clang-fast; export CXX=$AFLGO/afl-clang-fast++
export LDFLAGS=-lpthread
export ADDITIONAL="-targets=$TMP_DIR/BBtargets.txt -outdir=$TMP_DIR -flto -fuse-ld=gold -Wl,-plugin-opt=save-temps"
echo $'rec2csv.c:342\nrecutl.c:332\nrecutl.c:246\nrec-parser.c:549\nrec-parser.c:1131\nrec-comment.c:43\nrec-parser.c:612\nrec-rset.c:263\nrec-mset.c:152\ngl_list.h:760\ngl_array_list.c:436\nrec-mset.c:814\nrec-mset.c:905\nrec-rset.c:1031\nrec-comment.c:49' > $TMP_DIR/BBtargets.txt

cd obj-aflgo; 
CFLAGS="$ADDITIONAL" CXXFLAGS="$ADDITIONAL" ../configure --disable-shared --prefix=`pwd`
make clean; 
make

cat $TMP_DIR/BBnames.txt | rev | cut -d: -f2- | rev | sort | uniq > $TMP_DIR/BBnames2.txt && mv $TMP_DIR/BBnames2.txt $TMP_DIR/BBnames.txt
cat $TMP_DIR/BBcalls.txt | sort | uniq > $TMP_DIR/BBcalls2.txt && mv $TMP_DIR/BBcalls2.txt $TMP_DIR/BBcalls.txt


cd utils; 
$AFLGO/scripts/genDistance.sh $SUBJECT $TMP_DIR rec2csv
cd ../../; 
mkdir obj-dist; 
cd obj-dist; # work around because cannot run make distclean

# CFLAGS="-DFORTIFY_SOURCE=2 -fstack-protector-all -fno-omit-frame-pointer -g -Wno-error -distance=$TMP_DIR/distance.cfg.txt" LDFLAGS="-ldl -lutil" ../configure --disable-shared --disable-gdb --disable-libdecnumber --disable-readline --disable-sim --disable-ld
CFLAGS="-distance=$TMP_DIR/distance.cfg.txt" CXXFLAGS="-distance=$TMP_DIR/distance.cfg.txt" ../configure --disable-shared --prefix=`pwd`
make
mkdir in; 
echo "00010002" > in/in
$AFLGO/afl-fuzz -m none -z exp -c 45m -i in -o out ./utils/rec2csv @@
