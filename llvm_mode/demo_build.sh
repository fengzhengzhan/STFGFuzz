#!/bin/bash
# Using clang sanitizer to hook functions.
cd ./ClangSanitizer
make
cd ..

# Building the LLVM Pass project.
cd ./Build
cmake ../Transforms
make
cd ..

# Compile the program
IR="IR"
BIN="Bin"
DEMO="demo"
DEMO_PASS="demo_pass"
PROGRAMS="Programs"

cd ./${PROGRAMS}
clang++ -S -emit-llvm ${DEMO}/${DEMO}.cc -o ${IR}/${DEMO}.ll -fsanitize=address -fsanitize-coverage=trace-pc-guard,trace-cmp  # IR
opt -load ../Build/LLVMObfuscator.so -split -S ${IR}/${DEMO}.ll -o ${IR}/${DEMO_PASS}.ll
llc -filetype=obj ${IR}/${DEMO_PASS}.ll -o ${IR}/${DEMO_PASS}.o  # Object file 
clang++ ${IR}/${DEMO_PASS}.o -o ${BIN}/${DEMO} -fsanitize=address -Wl,--whole-archive -L../ClangSanitizer -lcmpcov -Wl,--no-whole-archive  # Link
cd ..

./${PROGRAMS}/${BIN}/${DEMO} aaabaaacaaadaaaeaaafaaagaaahaaaiaaajaaakaaalaaamaaanaaaoaaapaaaqaaar  # Run


# Clear files.
echo -e "\n"
if [ $1 == "rm" ]
then
	echo "rm"
	rm -f ./${PROGRAMS}/${IR}/${DEMO}.ll
	rm -f ./${PROGRAMS}/${IR}/${DEMO_PASS}.ll
	rm -f ./${PROGRAMS}/${IR}/${DEMO_PASS}.o
	rm -f ./${PROGRAMS}/${BIN}/${DEMO}
fi
if [ $1 == "rmall" ]
then
	echo "rmall"
	cd ./ClangSanitizer
	make clean
	cd ..
	rm -rf ./Build/*
	rm -f ./${PROGRAMS}/${IR}/${DEMO}.ll
	rm -f ./${PROGRAMS}/${IR}/${DEMO_PASS}.ll
	rm -f ./${PROGRAMS}/${IR}/${DEMO_PASS}.o
	rm -f ./${PROGRAMS}/${BIN}/${DEMO}
fi


