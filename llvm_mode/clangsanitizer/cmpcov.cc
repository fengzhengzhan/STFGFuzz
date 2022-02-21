#include <iostream>

# define GET_CALLER_PC() __builtin_return_address(0)  // return the stack of the function

using namespace std;


static void handleTraceCmp(uint64_t arg1, uint64_t arg2, int arg_len) {
    uintptr_t PC = reinterpret_cast<uintptr_t>(GET_CALLER_PC());
    cout << "tracecmp:" << PC << " " << arg1 << " " << arg2 << " " << arg_len << endl;
} 

void sanCovTraceCmp1(uint8_t Arg1, uint8_t Arg2) {
    handleTraceCmp(Arg1, Arg2, 1);
}
void sanCovTraceCmp2(uint16_t Arg1, uint16_t Arg2) {
    handleTraceCmp(Arg1, Arg2, 2);
}
void sanCovTraceCmp4(uint32_t Arg1, uint32_t Arg2) {
    handleTraceCmp(Arg1, Arg2, 4);
}
void sanCovTraceCmp8(uint64_t Arg1, uint64_t Arg2) {
    handleTraceCmp(Arg1, Arg2, 8);
}

void sanCovTraceConstCmp1(uint8_t Arg1, uint8_t Arg2) {
    handleTraceCmp(Arg1, Arg2, 1);
}
void sanCovTraceConstCmp2(uint16_t Arg1, uint16_t Arg2) {
    handleTraceCmp(Arg1, Arg2, 2);
}
void sanCovTraceConstCmp4(uint32_t Arg1, uint32_t Arg2) {
    handleTraceCmp(Arg1, Arg2, 4);
}
void sanCovTraceConstCmp8(uint64_t Arg1, uint64_t Arg2) {
    handleTraceCmp(Arg1, Arg2, 8);
}

void sanCovTraceSwitch(uint64_t Val, uint64_t *Cases) {

}

void sanCovTraceDiv4(uint32_t Val) {

}
void sanCovTraceDiv8(uint64_t Val) {

}

void sanCovTraceGep(uintptr_t Idx) {
    
}

void sanWeakHookMemcmp(void *caller_pc, const void *s1, const void *s2, size_t n, int result) {
    
}

void sanWeakHookStrncmp(void *caller_pc, const char *s1, const char *s2, size_t n, int result) {
    
}
void sanWeakHookStrcmp(void *caller_pc, const char *s1, const char *s2, int result) {
    
}
void sanWeakHookStrncasecmp(void *called_pc, const char *s1, const char *s2, size_t n, int result) {
    
}
void sanWeakHookStrcasecmp(void *called_pc, const char *s1, const char *s2, int result) {
    
}



extern "C"{
void __sanitizer_cov_trace_cmp1(uint8_t Arg1, uint8_t Arg2) { sanCovTraceCmp1(Arg1, Arg2); }
void __sanitizer_cov_trace_cmp2(uint16_t Arg1, uint16_t Arg2) { sanCovTraceCmp2(Arg1, Arg2); }
void __sanitizer_cov_trace_cmp4(uint32_t Arg1, uint32_t Arg2) { sanCovTraceCmp4(Arg1, Arg2); }
void __sanitizer_cov_trace_cmp8(uint64_t Arg1, uint64_t Arg2) { sanCovTraceCmp8(Arg1, Arg2); }

void __sanitizer_cov_trace_const_cmp1(uint8_t Arg1, uint8_t Arg2) { sanCovTraceConstCmp1(Arg1, Arg2); }
void __sanitizer_cov_trace_const_cmp2(uint16_t Arg1, uint16_t Arg2) { sanCovTraceConstCmp2(Arg1, Arg2); }
void __sanitizer_cov_trace_const_cmp4(uint32_t Arg1, uint32_t Arg2) { sanCovTraceConstCmp4(Arg1, Arg2); }
void __sanitizer_cov_trace_const_cmp8(uint64_t Arg1, uint64_t Arg2) { sanCovTraceConstCmp8(Arg1, Arg2); }

void __sanitizer_cov_trace_switch(uint64_t Val, uint64_t *Cases) { sanCovTraceSwitch(Val, Cases); }

void __sanitizer_cov_trace_div4(uint32_t Val) { sanCovTraceDiv4(Val); }
void __sanitizer_cov_trace_div8(uint64_t Val) { sanCovTraceDiv8(Val); }

void __sanitizer_cov_trace_gep(uintptr_t Idx) { sanCovTraceGep(Idx); }

void __sanitizer_weak_hook_memcmp(void *caller_pc, const void *s1, const void *s2, size_t n, int result) { sanWeakHookMemcmp(caller_pc, s1, s2, n, result); }

void __sanitizer_weak_hook_strncmp(void *caller_pc, const char *s1, const char *s2, size_t n, int result) { sanWeakHookStrncmp(caller_pc, s1, s2, n, result); }
void __sanitizer_weak_hook_strcmp(void *caller_pc, const char *s1, const char *s2, int result) { sanWeakHookStrcmp(caller_pc, s1, s2, result); }
void __sanitizer_weak_hook_strncasecmp(void *called_pc, const char *s1, const char *s2, size_t n, int result) { sanWeakHookStrncasecmp(called_pc, s1, s2, n, result); }
void __sanitizer_weak_hook_strcasecmp(void *called_pc, const char *s1, const char *s2, int result) { sanWeakHookStrcasecmp(called_pc, s1, s2, result); }
}