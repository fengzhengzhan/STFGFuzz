#include <iostream>
#include <cstring>
#include <stdio.h>
#include <sanitizer/dfsan_interface.h>
#include <assert.h>

#include "common.h"
#include "tracking.h"


using namespace std;


extern "C"{

// The end of analysis.
static void saveCovOnEnd() {
    printf("\nE %x Z\n", *(int *)GET_CALLER_PC);
}

int value = atexit(saveCovOnEnd);
// if(value != 0) {
//     cout << "atexit() function registration failed!";
//     exit(1);
// }

static void handleTraceCmp(uint64_t arg1, uint64_t arg2, int arg_len, char funcinfo) {
    // uintptr_t PC = reinterpret_cast<uintptr_t>(GET_CALLER_PC);
    printf("\n%c %x %lu %lu %d Z\n", funcinfo, *(int *)GET_CALLER_PC, arg1, arg2, arg_len);
} 

static void handleStrMemCmp(void *called_pc, const char *s1, const char *s2, int n, int result, char funcinfo) {

    printf("\n%c %x ", funcinfo, *(int *)called_pc);

    // uint64_t traceflag =  reinterpret_cast<uint64_t>(called_pc) |
    //     (reinterpret_cast<uint64_t>(s1) << 48) |
    //     (reinterpret_cast<uint64_t>(s2) << 60);
    // printf("%lx ", traceflag);
    int i = 0;
    if(n == 0){
        // printf("<s1\"");
        // i = 0;
        // while (1)
        // {
        //     if(s1[i] == '\0'){
        //         break;
        //     }
        //     printf("%c", s1[i]);
        //     i ++;
        // }
        // printf("\"1s> <s2\"");
        // i = 0;
        // while (1)
        // {
        //     if(s2[i] == '\0'){
        //         break;
        //     }
        //     printf("%c", s2[i]);
        //     i ++;
        // }
        // printf("\"2s> ");

        printf("<s1\"%s\"1s> <s2\"%s\"2s> ", s1, s2);
    }
    else if(n != 0){
        printf("<s1\"");
        for (i = 0; i < n; i ++) {
            printf("%c", s1[i]);
        }
        printf("\"1s> <s2\"");
        for (i = 0; i < n; i ++) {
            printf("%c", s2[i]);
        }
        printf("\"2s> ");
    }
    
    printf("%d %d Z\n", n, result);
}

void sanCovTraceCmp1(uint8_t Arg1, uint8_t Arg2) {
    handleTraceCmp(Arg1, Arg2, 1, COV_TRACE_CMP1);
}
void sanCovTraceCmp2(uint16_t Arg1, uint16_t Arg2) {
    handleTraceCmp(Arg1, Arg2, 2, COV_TRACE_CMP2);
}
void sanCovTraceCmp4(uint32_t Arg1, uint32_t Arg2) {
    handleTraceCmp(Arg1, Arg2, 4, COV_TRACE_CMP4);
}
void sanCovTraceCmp8(uint64_t Arg1, uint64_t Arg2) {
    handleTraceCmp(Arg1, Arg2, 8, COV_TRACE_CMP8);
}

void sanCovTraceConstCmp1(uint8_t Arg1, uint8_t Arg2) {
    handleTraceCmp(Arg1, Arg2, 1, COV_TRACE_CONST_CMP1);
}
void sanCovTraceConstCmp2(uint16_t Arg1, uint16_t Arg2) {
    handleTraceCmp(Arg1, Arg2, 2, COV_TRACE_CONST_CMP2);
}
void sanCovTraceConstCmp4(uint32_t Arg1, uint32_t Arg2) {
    handleTraceCmp(Arg1, Arg2, 4, COV_TRACE_CONST_CMP4);
}
void sanCovTraceConstCmp8(uint64_t Arg1, uint64_t Arg2) {
    handleTraceCmp(Arg1, Arg2, 8, COV_TRACE_CONST_CMP8);
}

void sanCovTraceSwitch(uint64_t Val, uint64_t *Cases) {
    // Called before a switch statement.
    // Val is the switch operand.
    // Cases[0] is the number of case constants.
    // Cases[1] is the size of Val in bits.
    // Cases[2:] are the case constants.
    if (Cases[0] == 0) {
        return ;
    }

    printf("\n%c %x %lu %lu", COV_TRACE_SWITCH, *(int *)GET_CALLER_PC, Cases[0], Cases[1]);

    for (int i = 0; i < Cases[0]; i ++) {
        printf(" %lu", Cases[2 + i]);
    }
    printf(" Z\n");

}

void sanCovTraceDiv4(uint32_t Val) {

}
void sanCovTraceDiv8(uint64_t Val) {

}

void sanCovTraceGep(uintptr_t Idx) {
    
}

void sanWeakHookMemcmp(void *called_pc, const void *s1, const void *s2, size_t n, int result) {
    // Skip comparison of long strings. 
    // if (n > maxCmpLen) {
    //     return ;
    // }

    handleStrMemCmp(called_pc, static_cast<const char *>(s1), static_cast<const char *>(s2), n, result, WEAK_HOOK_MEMCMP);
}

void sanWeakHookStrncmp(void *called_pc, const char *s1, const char *s2, size_t n, int result) {
    // Skip comparison of long strings. 
    // if (n > maxCmpLen) {
    //     return ;
    // }

    handleStrMemCmp(called_pc, s1, s2, n, result, WEAK_HOOK_STRNCMP);
    
}
void sanWeakHookStrcmp(void *called_pc, const char *s1, const char *s2, int result) {
    // Skip comparison of long strings. 
    // if (n > maxCmpLen) {
    //     return ;
    // }
    // printf("test  ");
    handleStrMemCmp(called_pc, s1, s2, 0, result, WEAK_HOOK_STRCMP);
}
void sanWeakHookStrncasecmp(void *called_pc, const char *s1, const char *s2, size_t n, int result) {
    // Skip comparison of long strings. 
    // if (n > maxCmpLen) {
    //     return ;
    // }

    handleStrMemCmp(called_pc, s1, s2, n, result, WEAK_HOOK_STRNCASECMP);
}
void sanWeakHookStrcasecmp(void *called_pc, const char *s1, const char *s2, int result) {
    // Skip comparison of long strings. 
    // if (n > maxCmpLen) {
    //     return ;
    // }

    handleStrMemCmp(called_pc, s1, s2, 0, result, WEAK_HOOK_STRCASECMP);
}




void __sanitizer_cov_trace_cmp1(uint8_t Arg1, uint8_t Arg2) { 
    sanCovTraceCmp1(Arg1, Arg2); }
void __sanitizer_cov_trace_cmp2(uint16_t Arg1, uint16_t Arg2) { 
    sanCovTraceCmp2(Arg1, Arg2); }
void __sanitizer_cov_trace_cmp4(uint32_t Arg1, uint32_t Arg2) { 
    sanCovTraceCmp4(Arg1, Arg2); }
void __sanitizer_cov_trace_cmp8(uint64_t Arg1, uint64_t Arg2) { 
    sanCovTraceCmp8(Arg1, Arg2); }

void __sanitizer_cov_trace_const_cmp1(uint8_t Arg1, uint8_t Arg2) { 
    sanCovTraceConstCmp1(Arg1, Arg2); }
void __sanitizer_cov_trace_const_cmp2(uint16_t Arg1, uint16_t Arg2) { 
    sanCovTraceConstCmp2(Arg1, Arg2); }
void __sanitizer_cov_trace_const_cmp4(uint32_t Arg1, uint32_t Arg2) { 
    sanCovTraceConstCmp4(Arg1, Arg2); }
void __sanitizer_cov_trace_const_cmp8(uint64_t Arg1, uint64_t Arg2) { 
    sanCovTraceConstCmp8(Arg1, Arg2); }

void __sanitizer_cov_trace_switch(uint64_t Val, uint64_t *Cases) { 
    sanCovTraceSwitch(Val, Cases); }

void __sanitizer_cov_trace_div4(uint32_t Val) { 
    sanCovTraceDiv4(Val); }
void __sanitizer_cov_trace_div8(uint64_t Val) { 
    sanCovTraceDiv8(Val); }

void __sanitizer_cov_trace_gep(uintptr_t Idx) { 
    sanCovTraceGep(Idx); }

void __sanitizer_weak_hook_memcmp(void *called_pc, const void *s1, const void *s2, size_t n, int result) { 
    sanWeakHookMemcmp(called_pc, s1, s2, n, result); }

void __sanitizer_weak_hook_strncmp(void *called_pc, const char *s1, const char *s2, size_t n, int result) { 
    sanWeakHookStrncmp(called_pc, s1, s2, n, result); }
void __sanitizer_weak_hook_strcmp(void *called_pc, const char *s1, const char *s2, int result) { 
    sanWeakHookStrcmp(called_pc, s1, s2, result); }
void __sanitizer_weak_hook_strncasecmp(void *called_pc, const char *s1, const char *s2, size_t n, int result) { 
    sanWeakHookStrncasecmp(called_pc, s1, s2, n, result); }
void __sanitizer_weak_hook_strcasecmp(void *called_pc, const char *s1, const char *s2, int result) { 
    sanWeakHookStrcasecmp(called_pc, s1, s2, result); }

void __dfsan_load_callback(dfsan_label Label, void* Addr);
void __dfsan_store_callback(dfsan_label Label, void* Addr);
void __dfsan_mem_transfer_callback(dfsan_label *Start, size_t Len);
void __dfsan_cmp_callback(dfsan_label CombinedLabel);
}