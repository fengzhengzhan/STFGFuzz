#!/bin/bash

time=$(date "+%Y-%m-%d %H:%M:%S")
echo "[+] Start time: ${time}"

if [ $1 ]
then

	if [ $2 ] && [ $2 == "-rm" ]
	then
		rm -rf file-5.22.$1
		rm -rf track
		rm -rf fast
		rm -rf seeds
		rm -rf output
	else
		echo $1
		echo core | sudo tee /proc/sys/kernel/core_pattern
		ANGORA=/root/datav5/Angora-1.2.2
		
		# change git branch
		cp -r file-5.22/ file-5.22.$1
		cd file-5.22.$1
		git checkout $1
		cd ..
		
		# compile program for tracking
		cp -r file-5.22.$1 track
		cd track
		autoreconf -f -i
		CC=${ANGORA}/bin/angora-clang CFLAGS="-fvisibility=default -ggdb" ./configure --prefix=`pwd`/install --enable-static --disable-shared
		USE_TRACK=1 make
		
		
		${ANGORA}/tools/gen_library_abilist.sh /usr/lib/x86_64-linux-gnu/libz.so  discard > zlib_abilist.txt
		export ANGORA_TAINT_RULE_LIST=/root/datav5/Angora-1.2.2/lava1/lava_corpus/LAVA-1/track/zlib_abilist.txt
		make clean
		USE_TRACK=1 make
		make install
		cd ..
		
		# Compile program for branch counting
		cp -r file-5.22.$1 fast
		cd fast
		autoreconf -f -i
		CC=${ANGORA}/bin/angora-clang CFLAGS="-fvisibility=default -ggdb" ./configure --prefix=`pwd`/install -enable-static --disable-shared
		make
		make install
		cd ..
		
		# Seeds
		mkdir seeds
		echo "Hello World" > seeds/seed.txt
		
		# run
		# ${ANGORA}/angora_fuzzer -i seeds -o output -j 1 -t ./track/install/bin/file -- cat @@ | xargs /fast/install/bin/file
		${ANGORA}/angora_fuzzer -i seeds -o output -j 1 -t ./track/install/bin/file -- ./fast/install/bin/file @@
		
		
		# # compile
		# autoreconf -f -i
		# CC=gclang CFLAGS="-g -O0 -fvisibility=default -ggdb" ./configure --enable-static --disable-shared --prefix=`pwd`/obj-bc
		# make 
		# make install
		# cd obj-bc/bin/
		# get-bc file
		# # angora compile
		# ${ANGORA}/bin/angora-clang file.bc -o file.fast
	
	fi
	
	
	
else
	echo "[!] Usage: ./script.sh lava1_id"
fi


time=$(date "+%Y-%m-%d %H:%M:%S")
echo "[+] End time: ${time}"

