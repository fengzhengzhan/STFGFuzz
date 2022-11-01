clang++ -g -emit-llvm -c example.cc -o example.bc

cd ../..
sudo ./build.sh -n example clang++
sudo chmod -R 777 example

cd example/data_graph
opt -dot-cfg ../code_IR/example_trace.bc
dot -Tpng -o main.png .main.dot
