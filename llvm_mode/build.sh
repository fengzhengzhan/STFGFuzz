cd clangsanitizer/
./build.sh
cd ..
clang++ -c demo.cc -o demo.o -fsanitize=address -fsanitize-coverage=trace-pc-guard,trace-cmp
clang++ demo.o -o demo -fsanitize=address -Wl,--whole-archive -L./clangsanitizer -lcmpcov -Wl,--no-whole-archive
./demo aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa


# cd cmptype
# clang++ -c Cycle.cpp -o Cycle.o -fsanitize=address -fsanitize-coverage=trace-pc-guard,trace-cmp
# clang++ Cycle.o -o Cycle -fsanitize=address -Wl,--whole-archive -L../clangsanitizer -lcmpcov -Wl,--no-whole-archive
