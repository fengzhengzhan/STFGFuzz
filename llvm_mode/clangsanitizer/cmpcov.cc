#include <iostream>

using namespace std;

extern "C"{

// Using clang tracing data flow. 
// https://clang.llvm.org/docs/SanitizerCoverage.html#tracing-data-flow
// Called before a comparison instruction.
// Arg1 and Arg2 are arguments of the comparison.
void __sanitizer_cov_trace_cmp1(uint8_t Arg1, uint8_t Arg2){
    cout << "__sanitizer_cov_trace_cmp1 " << Arg1 << " " << Arg2 << endl;
};
void __sanitizer_cov_trace_cmp2(uint16_t Arg1, uint16_t Arg2){
    cout << "__sanitizer_cov_trace_cmp2 " << Arg1 << " " << Arg2 << endl;
};
void __sanitizer_cov_trace_cmp4(uint32_t Arg1, uint32_t Arg2){
    cout << "__sanitizer_cov_trace_cmp4 " << Arg1 << " " << Arg2 << endl;
};
void __sanitizer_cov_trace_cmp8(uint64_t Arg1, uint64_t Arg2){
    cout << "__sanitizer_cov_trace_cmp8 " << Arg1 << " " << Arg2 << endl;
};

// Called before a comparison instruction if exactly one of the arguments is constant.
// Arg1 and Arg2 are arguments of the comparison, Arg1 is a compile-time constant.
// These callbacks are emitted by -fsanitize-coverage=trace-cmp since 2017-08-11
void __sanitizer_cov_trace_const_cmp1(uint8_t Arg1, uint8_t Arg2){
    cout << "__sanitizer_cov_trace_const_cmp1 " << Arg1 << " " << Arg2 << endl;
};
void __sanitizer_cov_trace_const_cmp2(uint16_t Arg1, uint16_t Arg2){
    cout << "__sanitizer_cov_trace_const_cmp2 " << Arg1 << " " << Arg2 << endl;
};
void __sanitizer_cov_trace_const_cmp4(uint32_t Arg1, uint32_t Arg2){
    cout << "__sanitizer_cov_trace_const_cmp4 " << Arg1 << " " << Arg2 << endl;
};
void __sanitizer_cov_trace_const_cmp8(uint64_t Arg1, uint64_t Arg2){
    cout << "__sanitizer_cov_trace_const_cmp8 " << Arg1 << " " << Arg2 << endl;
};

// Called before a switch statement.
// Val is the switch operand.
// Cases[0] is the number of case constants.
// Cases[1] is the size of Val in bits.
// Cases[2:] are the case constants.
void __sanitizer_cov_trace_switch(uint64_t Val, uint64_t *Cases);


}