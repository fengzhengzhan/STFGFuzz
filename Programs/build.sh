#!/bin/bash

time=$(date "+%Y-%m-%d %H:%M:%S")
echo "${time}"

if [ $1 == "-n" ]
then
	PROGRAMNAME=$2
	COMPILER=$3
	PROGRAMNAME_TRACE="${PROGRAMNAME}_trace"
	PROGRAMNAME_PASS="${PROGRAMNAME}_pass"
	
	# Compile the program
	PROGRAMS="Programs"
	SOURCES="code_sources"
	IR="code_IR"
	BIN="code_Bin"

	LLVMPASSPATH="llvm_mode/Build/LLVMObfuscator.so"
	LINE_SAVE="data_graph/binaryline.info"
	SANPATH="llvm_mode/ClangSanitizer"
	SUFFIX="bc"
	
	echo "ProgramName: <${PROGRAMNAME}>"
	
	# Create Files
	cd ${PROGRAMNAME}
	if [ ! -d code_Bin ];then
		mkdir -m 775 code_Bin
	fi
	if [ ! -d code_IR ];then
		mkdir -m 775 code_IR
	fi
	if [ ! -d code_sources ];then
		mkdir -m 775 code_sources
	fi
	if [ ! -d data_graph ];then
		mkdir -m 775 data_graph
	fi
	if [ ! -d data_patchloc ];then
		mkdir -m 775 data_patchloc
	fi
	if [ ! -d seeds_crash ];then
		mkdir -m 775 seeds_crash
	fi
	if [ ! -d seeds_init ];then
		mkdir -m 775 seeds_init
	fi
	if [ ! -d seeds_mutate ];then
		mkdir -m 775 seeds_mutate
	fi
	cd ..
	
	# Using clang sanitizer to hook functions.
	cd ..  # Return to the root path.
	
	# Clear files.
	if [ $4 ] && [ $4 == "-rm" ]
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

	elif [ $4 ] && [ $4 == "-rma" ]
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
	
	elif [ $3 == "clang" ] || [ $3 == "clang++" ]
	then
		cd llvm_mode/ClangSanitizer
		make
		cd ../..

		# Building the LLVM Pass project.
		cd llvm_mode/Build
		cmake ../Transforms
		make
		cd ../..


		# Compile the program
		cd ${PROGRAMS}/${PROGRAMNAME}
		# clang -g -emit-llvm -c ${SOURCES}/${PROGRAMNAME}.cc -o ${IR}/${PROGRAMNAME}.${SUFFIX} # IR
		# -fsanitize-recover=address,memory -fsanitize-coverage=bb,no-prune,trace-pc-guard  -fsanitize-coverage=edge,trace-pc-guard (default)
		${COMPILER} -fsanitize-recover=address -fsanitize-coverage=bb,no-prune,trace-pc-guard,trace-cmp -emit-llvm -c ${SOURCES}/${PROGRAMNAME}.${SUFFIX} -o ${IR}/${PROGRAMNAME_TRACE}.${SUFFIX} 
		rm -f ${LINE_SAVE}
		echo "{" >> ${LINE_SAVE}
		opt -load ../../${LLVMPASSPATH} -line -S ${IR}/${PROGRAMNAME_TRACE}.${SUFFIX} -o ${IR}/${PROGRAMNAME_PASS}.${SUFFIX} >> ${LINE_SAVE}
		echo "}" >> ${LINE_SAVE}
		llc -filetype=obj ${IR}/${PROGRAMNAME_PASS}.${SUFFIX} -o ${IR}/${PROGRAMNAME}.o  # Object file
		${COMPILER} -lz -fsanitize=address -Wl,--whole-archive -L../../${SANPATH} -lcmpcov -Wl,--no-whole-archive ${IR}/${PROGRAMNAME}.o -o ${BIN}/${PROGRAMNAME}  # Link
		# ${COMPILER} -fsanitize=address -Wl,--whole-archive -L../../${SANPATH} -lcmpcov -Wl,--no-whole-archive ${IR}/${PROGRAMNAME}.o -o ${BIN}/${PROGRAMNAME}  # Link
		# clang -fsanitize=address -Wl,--whole-archive -L../../${SANPATH} -lcmpcov -Wl,--no-whole-archive -L/usr/local/lib/ -lhiredis ${IR}/${PROGRAMNAME}.o -o ${BIN}/${PROGRAMNAME}  # Link
		cd ../..
		
		# Run
		if [ $5 ]
		then
			echo -e "\n------- ${PROGRAMNAME} -------"
			if [ $5 == "rand.seed" ]
			then
				./${PROGRAMS}/${PROGRAMNAME}/${BIN}/${PROGRAMNAME} $4 "${PROGRAMS}/${PROGRAMNAME}/seeds_init/rand.seed"
			elif [ $5 == "crash.seed" ]
			then
				./${PROGRAMS}/${PROGRAMNAME}/${BIN}/${PROGRAMNAME} $4 "${PROGRAMS}/${PROGRAMNAME}/seeds_crash/crash.seed"
			else
				echo "Usage: ./build.sh -n demo clang++ -f rand.seed"
				echo "Usage: ./build.sh -n base64 clang -d crash.seed"
			fi
		fi
		
		echo -e "\n"
	else
		echo "Usage: ./build.sh -n demo clang++ -rma"
		echo "Usage: ./build.sh -n base64 clang -rma"
	fi

else
	echo "Usage: ./build.sh [-n <program_name> <clang|clang++> <runseeds>] [-rm] [-rma]"
fi

echo "${time}"


