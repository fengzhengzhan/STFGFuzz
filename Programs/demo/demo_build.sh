#!/bin/bash
# Using clang sanitizer to hook functions.
cd ../..  # Return to the root path.

cd llvm_mode/ClangSanitizer
make
cd ../..

# Building the LLVM Pass project.
cd llvm_mode/Build
cmake ../Transforms
make
cd ../..

# Compile the program
PROGRAMS="Programs"
PROGRAMNAME="demo"
PROGRAMNAME_PASS="demo_pass"

SOURCES="code_sources"
IR="code_IR"
BIN="code_Bin"

LLVMPASSPATH="llvm_mode/Build/LLVMObfuscator.so"
SANPATH="llvm_mode/ClangSanitizer"
SUFFIX="bc"

cd ${PROGRAMS}/${PROGRAMNAME}
clang++ -g -c -emit-llvm ${SOURCES}/${PROGRAMNAME}.cc -o ${IR}/${PROGRAMNAME}.${SUFFIX} -fsanitize=address -fsanitize-coverage=trace-pc-guard,trace-cmp  # IR
opt -load ../../${LLVMPASSPATH} -line -S ${IR}/${PROGRAMNAME}.${SUFFIX} -o ${IR}/${PROGRAMNAME_PASS}.${SUFFIX}
llc -filetype=obj ${IR}/${PROGRAMNAME_PASS}.${SUFFIX} -o ${IR}/${PROGRAMNAME_PASS}.o  # Object file 
clang++ ${IR}/${PROGRAMNAME_PASS}.o -o ${BIN}/${PROGRAMNAME} -fsanitize=address -Wl,--whole-archive -L../../${SANPATH} -lcmpcov -Wl,--no-whole-archive  # Link
cd ../..

echo -e "\n------- demo -------"
# Run
./${PROGRAMS}/${PROGRAMNAME}/${BIN}/${PROGRAMNAME} -f "${PROGRAMS}/${PROGRAMNAME}/seeds_init/init3.seed"


# Clear files.
echo -e "\n"
if [ $1 == "-rm" ]
then
	echo "-rm"
	rm -f ./${PROGRAMS}/${PROGRAMNAME}/${IR}/${PROGRAMNAME}.${SUFFIX}
	rm -f ./${PROGRAMS}/${PROGRAMNAME}/${IR}/${PROGRAMNAME_PASS}.${SUFFIX}
	rm -f ./${PROGRAMS}/${PROGRAMNAME}/${IR}/${PROGRAMNAME_PASS}.o
	rm -f ./${PROGRAMS}/${PROGRAMNAME}/${BIN}/${PROGRAMNAME}
fi
if [ $1 == "-rma" ]
then
	echo "-rma"
	cd ${SANPATH}
	make clean
	cd ../..
	rm -rf llvm_mode/Build/*
	rm -f ./${PROGRAMS}/${PROGRAMNAME}/${IR}/${PROGRAMNAME}.${SUFFIX}
	rm -f ./${PROGRAMS}/${PROGRAMNAME}/${IR}/${PROGRAMNAME_PASS}.${SUFFIX}
	rm -f ./${PROGRAMS}/${PROGRAMNAME}/${IR}/${PROGRAMNAME_PASS}.o
	rm -f ./${PROGRAMS}/${PROGRAMNAME}/${BIN}/${PROGRAMNAME}
fi

# clang++ -S -emit-llvm ${DEMO}/${DEMO}.cc -o ${IR}/${DEMO}.ll -fsanitize=address -fsanitize-coverage=trace-pc-guard,trace-cmp  # IR
# opt -load ../${LLVMPASSPATH} -line -S ${IR}/${DEMO}.ll -o ${IR}/${DEMO_PASS}.ll
# llc -filetype=obj ${IR}/${DEMO_PASS}.ll -o ${IR}/${DEMO_PASS}.o  # Object file 
# clang++ ${IR}/${DEMO_PASS}.o -o ${BIN}/${DEMO} -fsanitize=address -Wl,--whole-archive -L../${SANPATH} -lcmpcov -Wl,--no-whole-archive  # Link

