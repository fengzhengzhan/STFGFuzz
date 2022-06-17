#!/bin/bash

echo "Creating directories for each bug..."
cat branches.txt | while read line ; 
do
    cp -r file-5.22/ file-5.22.${line} ;
    cd file-5.22.${line} ;
    git reset --hard
    git checkout ${line} ;
    cd .. ;
    dir="file-5.22.${line}"
    cd "$dir"
    export FORCE_UNSAFE_CONFIGURE=1
    export LLVM_COMPILER=clang
    autoreconf -f -i
    CC=wllvm WLLVM_CONFIGURE_ONLY=1 CFLAGS="-g -O0 -fvisibility=default" LIBS="-lacl" ./configure --enable-static --disable-shared --prefix=`pwd`/lava-install
    make   # -j Depends on the number of computer processes.
    make install
    cd lava-install/bin/
    extract-bc file
    cd ../..
    cd ..
#    echo ${line} ;
done
#done &> /dev/null

#echo "Building buggy versions..."
#cat branches.txt | xargs -P $(nproc) -n 1 ./conf.sh &> /dev/null
#
#echo "Validating bugs..."
#for d in file-5.22.* ; do
#    { ${d}/lava-install/bin/file ${d}/CRASH_INPUT ; } &> /dev/null
#    echo ${d} $?
#done > validated.txt

#awk 'BEGIN {valid = 0} $2 > 128 { valid += 1 } END { print "Validated", valid, "/", NR, "bugs" }' validated.txt
#
#echo "You can see validated.txt for the exit code of each buggy version."
