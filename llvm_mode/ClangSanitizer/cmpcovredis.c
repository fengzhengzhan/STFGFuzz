#ifdef _WIN32
#include <windows.h>
#include <psapi.h>
#elif __linux__
#include <unistd.h>
#endif

#include <stdio.h>
#include <stdlib.h>
#include <hiredis/hiredis.h>
#include <sanitizer/dfsan_interface.h>
#include <assert.h>
#include <string.h>
#include <stddef.h>
#include <stdint.h>
#include <sys/shm.h>
#include <time.h>

#if defined(__SANITIZE_ADDRESS__) || (defined(__has_feature) && __has_feature(address_sanitizer))
#error The cmpcov module should be compiled separately to the fuzzing target,\
       without AddressSanitizer enabled, to avoid infinite recursions and other\
       problems. Compile cmpcov to object files first, and then include them in\
       your project.
#endif

#if !defined(_WIN32) && !defined(__linux__)
#error Unsupported operating system.
#endif


// Define the type of all hook functions for the compare instruction.
#define COV_TRACE_CMP1 'a'
#define COV_TRACE_CMP2 'b'
#define COV_TRACE_CMP4 'c'
#define COV_TRACE_CMP8 'd'

#define COV_TRACE_CONST_CMP1 'e'
#define COV_TRACE_CONST_CMP2 'f'
#define COV_TRACE_CONST_CMP4 'g'
#define COV_TRACE_CONST_CMP8 'h'

#define COV_TRACE_SWITCH 'i'
#define COV_TRACE_DIV4 'j'
#define COV_TRACE_DIV8 'k'
#define COV_TRACE_GEP 'l'

#define WEAK_HOOK_MEMCMP 'm'
#define WEAK_HOOK_STRNCMP 'n'
#define WEAK_HOOK_STRCMP 'o'
#define WEAK_HOOK_STRNCASECMP 'p'
#define WEAK_HOOK_STRCASECMP 'q'

// return the stack of the function
// __builtin_return_address(LEVEL)
// This function is used to return the return address of the current function or caller. 
// The function's parameter LEVEl indicates the different levels of functions in the function call chain, and each value represents the following meaning.

// 0: return the return address of the current function.
// 1: returns the return address of the current function caller.
// 2: returns the return address of the caller of the current function caller.
// ......
#define GET_FUNC_PC __builtin_return_address(0)
#define GET_CALLER_PC __builtin_return_address(1)

//// The first 8 bytes magic numbers of *.sancov files.
//// From: https://clang.llvm.org/docs/SanitizerCoverage.html#id13
//const uint64_t fMagic64 = 0xC0BFFFFFFFFFFF64;
//const uint64_t fMagic32 = 0xC0BFFFFFFFFFFF32;
//
//// Maximum length memory/string buffer for strcmp(), strncmp() and memcmp() functions.
//const uint8_t maxCmpLen = 32;

#define SHMGET_SIZE 2147483648  // 2*1024*1024*1024  2GB
int id = 0;
char* data = NULL;
int savelen = 15;
int interlen = 16;
char buf[1024*1024];
redisContext *conn;
redisReply *reply;
// freeReplyObject(reply);


// The end of analysis.
static void saveCovOnEnd() {

    sprintf(buf, "rpush %p E",GET_FUNC_PC);
    reply = (redisReply*)redisCommand(conn, buf);
    freeReplyObject(reply);

    redisFree(conn);
}

static void handleTraceCmp(uint64_t arg1, uint64_t arg2, int arg_len, char funcinfo) {
    // uintptr_t PC = reinterpret_cast<uintptr_t>(GET_FUNC_PC);
    sprintf(buf, "rpush %p%p %c %lu %lu %d",GET_FUNC_PC, GET_CALLER_PC, funcinfo, arg1, arg2, arg_len);
    reply = (redisReply*)redisCommand(conn, buf);
    freeReplyObject(reply);
} 

static void handleStrMemCmp(void *called_pc, const char *s1, const char *s2, int n, int result, char funcinfo) {
    // The length of each string.
    int n1;
    int n2;
    if (n == 0) {
        n1 = strlen(s1);
        n2 = strlen(s2);
    } else if (n != 0)
    {
        n1 = n;
        n2 = n;
    }
    
    sprintf(buf, "rpush %p%p %c \"",GET_FUNC_PC, GET_CALLER_PC, funcinfo);
    int i = 0;

    for (i = 0; i < n1; i ++) {
        // printf("%c", s1[i]);
        if (s1[i] == '"' || s1[i] == '\\') {
            sprintf(buf, "\\%c", s1[i]);
        } else {
            sprintf(buf, "%c", s1[i]);
        }
    }
    // printf("\"1s> <s2\"");
    sprintf(buf, "\" \"");

    for (i = 0; i < n2; i ++) {
        // printf("%c", s2[i]);
        if (s2[i] == '"' || s2[i] == '\\') {
            sprintf(buf, "\\%c", s2[i]);
        } else {
            sprintf(buf, "%c", s2[i]);
        }               
    }
    sprintf(buf, "\"");
    
    sprintf(buf, " %d %d", n, result); 
    reply = (redisReply*)redisCommand(conn, buf);
    freeReplyObject(reply);
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

    // printf("\n%c %p %lu %lu", COV_TRACE_SWITCH, GET_FUNC_PC, Cases[0], Cases[1]);
    sprintf(buf, "rpush %p%p %c %lu %lu %lu",GET_FUNC_PC, GET_CALLER_PC, COV_TRACE_SWITCH, Cases[0], Cases[1], Val);

    for (int i = 0; i < Cases[0]; i ++) {
        // printf(" %lu", Cases[2 + i]);
        sprintf(buf, " %lu", Cases[2 + i]);
    }
    reply = (redisReply*)redisCommand(conn, buf);
    freeReplyObject(reply);
}


// compiler-rt functions.

// This callback is inserted by the compiler as a module constructor
// into every DSO. 'start' and 'stop' correspond to the
// beginning and end of the section with the guards for the entire
// binary (executable or DSO). The callback will be called at least
// once per DSO and may be called multiple times with the same parameters.
void __sanitizer_cov_trace_pc_guard_init(uint32_t *start, uint32_t *stop) {
    // Redis
    conn = redisConnect("127.0.0.1", 6379);
    if(conn != NULL && conn->err)
    {
        printf("Error Redis connection: %s\n", conn->errstr);
        exit(1);
    }

    static uint64_t N;  // Counter for the guards.
    if (start == stop || *start) return;  // Initialize only once.
    // void *PC = __builtin_return_address(0);
    
    // char PcDescr[10240];
    // __sanitizer_symbolize_pc(PC, "%p %F %L", PcDescr, sizeof(PcDescr));

    sprintf(buf, "rpush %p I %p %p",GET_FUNC_PC, start, stop);
    reply = (redisReply*)redisCommand(conn, buf);
    freeReplyObject(reply);

    for (uint32_t *x = start; x < stop; x++)
    {
        *x = ++N;
    }
    sprintf(buf, "rpush %p S %lu", GET_FUNC_PC, N);
    reply = (redisReply*)redisCommand(conn, buf);
    freeReplyObject(reply);

    atexit(saveCovOnEnd);
    // if(value != 0) {
    //     cout << "atexit() function registration failed!";
    //     exit(1);
    // }
}


void __sanitizer_cov_trace_pc_guard(uint32_t *guard) {

}

void __sanitizer_cov_trace_cmp1(uint8_t Arg1, uint8_t Arg2) { 
    handleTraceCmp(Arg1, Arg2, 1, COV_TRACE_CMP1); }
void __sanitizer_cov_trace_cmp2(uint16_t Arg1, uint16_t Arg2) { 
    handleTraceCmp(Arg1, Arg2, 2, COV_TRACE_CMP2); }
void __sanitizer_cov_trace_cmp4(uint32_t Arg1, uint32_t Arg2) { 
    handleTraceCmp(Arg1, Arg2, 4, COV_TRACE_CMP4); }
void __sanitizer_cov_trace_cmp8(uint64_t Arg1, uint64_t Arg2) { 
    handleTraceCmp(Arg1, Arg2, 8, COV_TRACE_CMP8); }

void __sanitizer_cov_trace_const_cmp1(uint8_t Arg1, uint8_t Arg2) { 
    handleTraceCmp(Arg1, Arg2, 1, COV_TRACE_CONST_CMP1); }
void __sanitizer_cov_trace_const_cmp2(uint16_t Arg1, uint16_t Arg2) { 
    handleTraceCmp(Arg1, Arg2, 2, COV_TRACE_CONST_CMP2); }
void __sanitizer_cov_trace_const_cmp4(uint32_t Arg1, uint32_t Arg2) { 
    handleTraceCmp(Arg1, Arg2, 4, COV_TRACE_CONST_CMP4); }
void __sanitizer_cov_trace_const_cmp8(uint64_t Arg1, uint64_t Arg2) { 
    handleTraceCmp(Arg1, Arg2, 8, COV_TRACE_CONST_CMP8);}

void __sanitizer_cov_trace_switch(uint64_t Val, uint64_t *Cases) { 
    sanCovTraceSwitch(Val, Cases); }

void __sanitizer_cov_trace_div4(uint32_t Val) { 
    }
void __sanitizer_cov_trace_div8(uint64_t Val) { 
    }

void __sanitizer_cov_trace_gep(uintptr_t Idx) { 
    }

void __sanitizer_weak_hook_memcmp(void *called_pc, const void *s1, const void *s2, size_t n, int result) { 
    handleStrMemCmp(called_pc, (char *)s1, (char *)s2, n, result, WEAK_HOOK_MEMCMP); }

void __sanitizer_weak_hook_strncmp(void *called_pc, const char *s1, const char *s2, size_t n, int result) { 
    handleStrMemCmp(called_pc, s1, s2, n, result, WEAK_HOOK_STRNCMP); }
void __sanitizer_weak_hook_strcmp(void *called_pc, const char *s1, const char *s2, int result) { 
    handleStrMemCmp(called_pc, s1, s2, 0, result, WEAK_HOOK_STRCMP); }
void __sanitizer_weak_hook_strncasecmp(void *called_pc, const char *s1, const char *s2, size_t n, int result) { 
    handleStrMemCmp(called_pc, s1, s2, n, result, WEAK_HOOK_STRNCASECMP); }
void __sanitizer_weak_hook_strcasecmp(void *called_pc, const char *s1, const char *s2, int result) { 
    handleStrMemCmp(called_pc, s1, s2, 0, result, WEAK_HOOK_STRCASECMP); }

void __dfsan_load_callback(dfsan_label Label, void* Addr);
void __dfsan_store_callback(dfsan_label Label, void* Addr);
void __dfsan_mem_transfer_callback(dfsan_label *Start, size_t Len);
void __dfsan_cmp_callback(dfsan_label CombinedLabel);