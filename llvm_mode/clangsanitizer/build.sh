rm -rf libcmpcov.a
clang++ -c -o cmpcov.o cmpcov.cc -O2 -fPIC
ar cr libcmpcov.a cmpcov.o
