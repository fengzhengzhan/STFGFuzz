#!/bin/bash

if [ $1 == "-n" ]
then
	PROGRAMNAME=$2
	PROGRAMNAME_TRACE="${PROGRAMNAME}_trace"
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
	clang++ -g -emit-llvm -c ${SOURCES}/${PROGRAMNAME}.cc -o ${IR}/${PROGRAMNAME}.${SUFFIX} # IR
	clang++ -fsanitize-recover=address -fsanitize-coverage=trace-pc-guard,trace-cmp -emit-llvm -c ${IR}/${PROGRAMNAME}.${SUFFIX} -o ${IR}/${PROGRAMNAME_TRACE}.${SUFFIX} 
	rm -f ${LINE_SAVE}
	echo "{" >> ${LINE_SAVE}
	opt -load ../../${LLVMPASSPATH} -line -S ${IR}/${PROGRAMNAME_TRACE}.${SUFFIX} -o ${IR}/${PROGRAMNAME_PASS}.${SUFFIX} >> ${LINE_SAVE}
	echo "}" >> ${LINE_SAVE}
	llc -filetype=obj ${IR}/${PROGRAMNAME_PASS}.${SUFFIX} -o ${IR}/${PROGRAMNAME}.o  # Object file
	clang++ -fsanitize=address -Wl,--whole-archive -L../../${SANPATH} -lcmpcov -Wl,--no-whole-archive ${IR}/${PROGRAMNAME}.o -o ${BIN}/${PROGRAMNAME}  # Link
	cd ../..


	echo -e "\n------- ${PROGRAMNAME} -------"
	# Run
	./${PROGRAMS}/${PROGRAMNAME}/${BIN}/${PROGRAMNAME} -f "${PROGRAMS}/${PROGRAMNAME}/seeds_crash/final.seed"


	# Clear files.
	if [ $3 == "-rm" ]
	then
		echo "-rm"
		echo "rm -f ./${PROGRAMS}/${PROGRAMNAME}/${IR}/${PROGRAMNAME_TRACE}.${SUFFIX}"
		echo "rm -f ./${PROGRAMS}/${PROGRAMNAME}/${IR}/${PROGRAMNAME_PASS}.${SUFFIX}"
		echo "rm -f ./${PROGRAMS}/${PROGRAMNAME}/${IR}/${PROGRAMNAME}.o"
		echo "rm -f ./${PROGRAMS}/${PROGRAMNAME}/${BIN}/${PROGRAMNAME}"
		rm -f ./${PROGRAMS}/${PROGRAMNAME}/${IR}/${PROGRAMNAME_TRACE}.${SUFFIX}
		rm -f ./${PROGRAMS}/${PROGRAMNAME}/${IR}/${PROGRAMNAME_PASS}.${SUFFIX}
		rm -f ./${PROGRAMS}/${PROGRAMNAME}/${IR}/${PROGRAMNAME}.o
		rm -f ./${PROGRAMS}/${PROGRAMNAME}/${BIN}/${PROGRAMNAME}

	elif [ $3 == "-rma" ]
	then
		echo "-rma"
		echo "${SANPATH}  make clean"
		echo "rm -rf llvm_mode/Build/*"
		echo "rm -f ./${PROGRAMS}/${PROGRAMNAME}/${IR}/${PROGRAMNAME_TRACE}.${SUFFIX}"
		echo "rm -f ./${PROGRAMS}/${PROGRAMNAME}/${IR}/${PROGRAMNAME_PASS}.${SUFFIX}"
		echo "rm -f ./${PROGRAMS}/${PROGRAMNAME}/${IR}/${PROGRAMNAME}.o"
		echo "rm -f ./${PROGRAMS}/${PROGRAMNAME}/${BIN}/${PROGRAMNAME}"
		cd ${SANPATH}
		make clean
		cd ../..
		rm -rf llvm_mode/Build/*
		rm -f ./${PROGRAMS}/${PROGRAMNAME}/${IR}/${PROGRAMNAME_TRACE}.${SUFFIX}
		rm -f ./${PROGRAMS}/${PROGRAMNAME}/${IR}/${PROGRAMNAME_PASS}.${SUFFIX}
		rm -f ./${PROGRAMS}/${PROGRAMNAME}/${IR}/${PROGRAMNAME}.o
		rm -f ./${PROGRAMS}/${PROGRAMNAME}/${BIN}/${PROGRAMNAME}
	fi
else
	echo "Usage: ./build.sh [-n <program_name>] [-rm] [-rma]"
fi


