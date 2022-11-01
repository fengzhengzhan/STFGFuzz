#!/bin/bash

time=$(date "+%Y-%m-%d %H:%M:%S")
echo "[+] Start time: ${time}"

if [ $1 ]
then
	echo $1
	# change git branch
	cp -r file-5.22/ file-5.22.$1
	cd file-5.22.$1
	git checkout $1
	
	# compile program for tracking
	
	
	# compile
	autoreconf -f -i
	CC=gclang CFLAGS="-g -O0 -fvisibility=default -ggdb" ./configure --enable-static --disable-shared --prefix=`pwd`/obj-bc
	make 
	make install
	cd obj-bc/bin/
	get-bc file
	
	# angora compile
	
	
	
	
else
	echo "[!] Usage: ./script.sh lava1_id"
fi


time=$(date "+%Y-%m-%d %H:%M:%S")
echo "[+] End time: ${time}"

