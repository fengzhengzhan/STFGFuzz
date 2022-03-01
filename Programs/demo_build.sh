#!/bin/bash
# Using clang sanitizer to hook functions.
cd ..  # Return to the root path.

cd llvm_mode/ClangSanitizer
make
cd ../..

# Building the LLVM Pass project.
cd llvm_mode/Build
cmake ../Transforms
make
cd ../..

# Compile the program
IR="IR"
BIN="Bin"
DEMO="demo"
DEMO_PASS="demo_pass"
PROGRAMS="Programs"
LLVMPASSPATH="llvm_mode/Build/LLVMObfuscator.so"
SANPATH="llvm_mode/ClangSanitizer"

cd ${PROGRAMS}
clang++ -S -emit-llvm ${DEMO}/${DEMO}.cc -o ${IR}/${DEMO}.ll -fsanitize=address -fsanitize-coverage=trace-pc-guard,trace-cmp  # IR
opt -load ../${LLVMPASSPATH} -split -S ${IR}/${DEMO}.ll -o ${IR}/${DEMO_PASS}.ll
llc -filetype=obj ${IR}/${DEMO_PASS}.ll -o ${IR}/${DEMO_PASS}.o  # Object file 
clang++ ${IR}/${DEMO_PASS}.o -o ${BIN}/${DEMO} -fsanitize=address -Wl,--whole-archive -L../${SANPATH} -lcmpcov -Wl,--no-whole-archive  # Link
cd ..

echo -e "\n------- demo -------"
# Run
./${PROGRAMS}/${BIN}/${DEMO} -f "SeedPool/init_seeds/${DEMO}/final.seed"


# Clear files.
echo -e "\n"
if [ $1 == "-rm" ]
then
	echo "-rm"
	rm -f ./${PROGRAMS}/${IR}/${DEMO}.ll
	rm -f ./${PROGRAMS}/${IR}/${DEMO_PASS}.ll
	rm -f ./${PROGRAMS}/${IR}/${DEMO_PASS}.o
	rm -f ./${PROGRAMS}/${BIN}/${DEMO}
fi
if [ $1 == "-rma" ]
then
	echo "-rma"
	cd ${SANPATH}
	make clean
	cd ../..
	rm -rf llvm_mode/Build/*
	rm -f ./${PROGRAMS}/${IR}/${DEMO}.ll
	rm -f ./${PROGRAMS}/${IR}/${DEMO_PASS}.ll
	rm -f ./${PROGRAMS}/${IR}/${DEMO_PASS}.o
	rm -f ./${PROGRAMS}/${BIN}/${DEMO}
fi


