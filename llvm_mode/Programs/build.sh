cd clangsanitizer/
make
cd ..
# clang++ -c demo.cc -o demo.o -fsanitize=address -fsanitize-coverage=trace-pc-guard,trace-cmp
# clang++ demo.o -o demo -fsanitize=address -Wl,--whole-archive -L./clangsanitizer -lcmpcov -Wl,--no-whole-archive


# clang++ -c -emit-llvm demo.cc -o demo.bc
clang++ -S -emit-llvm demo.cc -o demo.ll -fsanitize=address -fsanitize-coverage=trace-pc-guard,trace-cmp
llc -filetype=obj demo_split.ll -o demo_split.o
clang++ demo_split.o -o demo -fsanitize=address -Wl,--whole-archive -L./clangsanitizer -lcmpcov -Wl,--no-whole-archive
# clang++ demo.o -o demo -fsanitize=address -Wl,--whole-archive -L./clangsanitizer -lcmpcov -Wl,--no-whole-archive
# rm -f demo.o
# ./demo aaabaaacaaadaaaeaaafaaagaaahaaaiaaajaaakaaalaaamaaanaaaoaaapaaaqaaar




# cd cmptype
# clang++ -c Cycle.cpp -o Cycle.o -fsanitize=address -fsanitize-coverage=trace-pc-guard,trace-cmp
# clang++ Cycle.o -o Cycle -fsanitize=address -Wl,--whole-archive -L../clangsanitizer -lcmpcov -Wl,--no-whole-archive
