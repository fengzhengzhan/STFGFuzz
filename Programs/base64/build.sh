#!/bin/bash

if [ $1 == "-n" ]
then
	PROGRAMNAME=$2
	PROGRAMNAME_PASS="${PROGRAMNAME}_pass"
	echo "ProgramName: <${PROGRAMNAME}>"
	
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

	SOURCES="code_sources"
	IR="code_IR"
	BIN="code_Bin"

	LLVMPASSPATH="llvm_mode/Build/LLVMObfuscator.so"
	LINE_SAVE="data_graph/binaryline.info"
	SANPATH="llvm_mode/ClangSanitizer"
	SUFFIX="bc"


	cd ${PROGRAMS}/${PROGRAMNAME}
	# clang++ -g -c -emit-llvm ${SOURCES}/${PROGRAMNAME}.cc -o ${IR}/${PROGRAMNAME}.${SUFFIX} -fsanitize=address -fsanitize-coverage=trace-pc-guard,trace-cmp  # IR
	rm -f ${LINE_SAVE}
	echo "{" >> ${LINE_SAVE}
	opt -load ../../${LLVMPASSPATH} -line -S ${IR}/${PROGRAMNAME}.${SUFFIX} -o ${IR}/${PROGRAMNAME_PASS}.${SUFFIX} >> ${LINE_SAVE}
	echo "}" >> ${LINE_SAVE}
	echo opt -load ../../${LLVMPASSPATH} -line -S ${IR}/${PROGRAMNAME}.${SUFFIX} -o ${IR}/${PROGRAMNAME_PASS}.${SUFFIX} >> ${LINE_SAVE}
	llc -filetype=obj ${IR}/${PROGRAMNAME_PASS}.${SUFFIX} -o ${IR}/${PROGRAMNAME_PASS}.o  # Object file 
	clang++ ${IR}/${PROGRAMNAME_PASS}.o -o ${BIN}/${PROGRAMNAME} -fsanitize=address -Wl,--whole-archive -L../../${SANPATH} -lcmpcov -Wl,--no-whole-archive  # Link
	cd ../..


	echo -e "\n------- ${PROGRAMNAME} -------"
	# Run
	./${PROGRAMS}/${PROGRAMNAME}/${BIN}/${PROGRAMNAME} -d "${PROGRAMS}/${PROGRAMNAME}/seeds_init/rand.b64"


	# Clear files.
	if [ $3 == "-rm" ]
	then
		echo "-rm"
		echo "rm -f ./${PROGRAMS}/${PROGRAMNAME}/${IR}/${PROGRAMNAME}.${SUFFIX}"
		echo "rm -f ./${PROGRAMS}/${PROGRAMNAME}/${IR}/${PROGRAMNAME_PASS}.${SUFFIX}"
		echo "rm -f ./${PROGRAMS}/${PROGRAMNAME}/${IR}/${PROGRAMNAME_PASS}.o"
		echo "rm -f ./${PROGRAMS}/${PROGRAMNAME}/${BIN}/${PROGRAMNAME}"
		rm -f ./${PROGRAMS}/${PROGRAMNAME}/${IR}/${PROGRAMNAME}.${SUFFIX}
		rm -f ./${PROGRAMS}/${PROGRAMNAME}/${IR}/${PROGRAMNAME_PASS}.${SUFFIX}
		rm -f ./${PROGRAMS}/${PROGRAMNAME}/${IR}/${PROGRAMNAME_PASS}.o
		rm -f ./${PROGRAMS}/${PROGRAMNAME}/${BIN}/${PROGRAMNAME}

	elif [ $3 == "-rma" ]
	then
		echo "-rma"
		echo "${SANPATH}  make clean"
		echo "rm -rf llvm_mode/Build/*"
		echo "rm -f ./${PROGRAMS}/${PROGRAMNAME}/${IR}/${PROGRAMNAME}.${SUFFIX}"
		echo "rm -f ./${PROGRAMS}/${PROGRAMNAME}/${IR}/${PROGRAMNAME_PASS}.${SUFFIX}"
		echo "rm -f ./${PROGRAMS}/${PROGRAMNAME}/${IR}/${PROGRAMNAME_PASS}.o"
		echo "rm -f ./${PROGRAMS}/${PROGRAMNAME}/${BIN}/${PROGRAMNAME}"
		cd ${SANPATH}
		make clean
		cd ../..
		rm -rf llvm_mode/Build/*
		rm -f ./${PROGRAMS}/${PROGRAMNAME}/${IR}/${PROGRAMNAME}.${SUFFIX}
		rm -f ./${PROGRAMS}/${PROGRAMNAME}/${IR}/${PROGRAMNAME_PASS}.${SUFFIX}
		rm -f ./${PROGRAMS}/${PROGRAMNAME}/${IR}/${PROGRAMNAME_PASS}.o
		rm -f ./${PROGRAMS}/${PROGRAMNAME}/${BIN}/${PROGRAMNAME}
	fi
else
	echo "Usage: ./build.sh [-n <program_name>] [-rm] [-rma]"
fi



# clang++ -S -emit-llvm ${DEMO}/${DEMO}.cc -o ${IR}/${DEMO}.ll -fsanitize=address -fsanitize-coverage=trace-pc-guard,trace-cmp  # IR
# opt -load ../${LLVMPASSPATH} -line -S ${IR}/${DEMO}.ll -o ${IR}/${DEMO_PASS}.ll
# llc -filetype=obj ${IR}/${DEMO_PASS}.ll -o ${IR}/${DEMO_PASS}.o  # Object file 
# clang++ ${IR}/${DEMO_PASS}.o -o ${BIN}/${DEMO} -fsanitize=address -Wl,--whole-archive -L../${SANPATH} -lcmpcov -Wl,--no-whole-archive  # Link

