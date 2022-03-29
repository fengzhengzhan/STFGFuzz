#ifdef _WIN32
#include <windows.h>
#include <psapi.h>
#elif __linux__
#include <unistd.h>
#endif

#include <stdio.h>
#include <stdlib.h>
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

int id = 0;
char* data = NULL;
int savelen = 15;
int interlen = 16;
char buf[1024*1024];

// The end of analysis.
static void saveCovOnEnd() {
    // printf("\nE %p Z\n", GET_FUNC_PC);
    // Add dataflow analysis information.
    sprintf(buf, "[\"E\",\"%p\"],", GET_FUNC_PC);
    strcpy(data + interlen, buf);
    interlen += strlen(buf);
    // Update interlen
    sprintf(buf, "L%dZ", interlen);
    strcpy(data, buf);
    
    // Separating shared memory from the current process.
    if (shmdt(data) == -1)
    {
        printf("Error Shmdt failed.\n");
        exit(1);
    }
    // shmctl(id, IPC_RMID, 0);
}

static void handleTraceCmp(uint64_t arg1, uint64_t arg2, int arg_len, char funcinfo) {
    // uintptr_t PC = reinterpret_cast<uintptr_t>(GET_FUNC_PC);

    // printf("\n%c %p %lu %lu %d Z\n", funcinfo, GET_FUNC_PC, arg1, arg2, arg_len);
    // Add dataflow analysis information.
    sprintf(buf, "[\"%c\",\"%p\",\"%p\",\"%lu\",\"%lu\",\"%d\"],", funcinfo, GET_FUNC_PC, GET_CALLER_PC, arg1, arg2, arg_len);
    strcpy(data + interlen, buf);
    interlen += strlen(buf);
    // Update interlen
    sprintf(buf, "L%dZ", interlen);
    strcpy(data, buf);
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
    
    // printf("\n%c %x ", funcinfo, *(int *)called_pc);
    sprintf(buf, "[\"%c\",\"%p\",\"%p\"", funcinfo, GET_FUNC_PC, GET_CALLER_PC);
    strcpy(data + interlen, buf);
    interlen += strlen(buf);

    // uint64_t traceflag =  reinterpret_cast<uint64_t>(called_pc) |
    //     (reinterpret_cast<uint64_t>(s1) << 48) |
    //     (reinterpret_cast<uint64_t>(s2) << 60);
    // printf("%lx ", traceflag);
    
    // printf("<s1\"%s\"1s> <s2\"%s\"2s> ", s1, s2);

    int i = 0;
    // printf("<s1\"");
    sprintf(buf, ",\"");
    strcpy(data + interlen, buf);
    interlen += strlen(buf);

    for (i = 0; i < n1; i ++) {
        // printf("%c", s1[i]);
        if (s1[i] == '"' || s1[i] == '\\') {
            sprintf(buf, "\\%c", s1[i]);
            strcpy(data + interlen, buf);
            interlen += strlen(buf);
        } else {
            sprintf(buf, "%c", s1[i]);
            strcpy(data + interlen, buf);
            interlen += strlen(buf);
        }
    }
    // printf("\"1s> <s2\"");
    sprintf(buf, "\",\"");
    strcpy(data + interlen, buf);
    interlen += strlen(buf);

    for (i = 0; i < n2; i ++) {
        // printf("%c", s2[i]);
        if (s2[i] == '"' || s2[i] == '\\') {
            sprintf(buf, "\\%c", s2[i]);
            strcpy(data + interlen, buf);
            interlen += strlen(buf);
        } else {
            sprintf(buf, "%c", s2[i]);
            strcpy(data + interlen, buf);
            interlen += strlen(buf);
        }               
    }
    // printf("\"2s> ");
    sprintf(buf, "\"");
    strcpy(data + interlen, buf);
    interlen += strlen(buf);
    
    // printf("%d %d Z\n", n, result);
    sprintf(buf, ",\"%d\",\"%d\"],", n, result);
    strcpy(data + interlen, buf);
    interlen += strlen(buf);
    // Update interlen
    sprintf(buf, "L%dZ", interlen);
    strcpy(data, buf);
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
    sprintf(buf, "[\"%c\",\"%p\",\"%p\",\"%lu\",\"%lu\"", COV_TRACE_SWITCH, GET_FUNC_PC, GET_CALLER_PC, Cases[0], Cases[1]);
    strcpy(data + interlen, buf);
    interlen += strlen(buf);

    for (int i = 0; i < Cases[0]; i ++) {
        // printf(" %lu", Cases[2 + i]);
        sprintf(buf, ",\"%lu\"", Cases[2 + i]);
        strcpy(data + interlen, buf);
        interlen += strlen(buf);
    }
    // printf(" Z\n");
    // Add dataflow analysis information.
    sprintf(buf, "],");
    strcpy(data + interlen, buf);
    interlen += strlen(buf);
    // Update interlen
    sprintf(buf, "L%dZ", interlen);
    strcpy(data, buf);
}


// compiler-rt functions.

// This callback is inserted by the compiler as a module constructor
// into every DSO. 'start' and 'stop' correspond to the
// beginning and end of the section with the guards for the entire
// binary (executable or DSO). The callback will be called at least
// once per DSO and may be called multiple times with the same parameters.
void __sanitizer_cov_trace_pc_guard_init(uint32_t *start, uint32_t *stop) {
    
    //memory share
    key_t id_shm = 124816;
    id = shmget(id_shm, 512 * 1024 * 1024, IPC_CREAT | 0777);
    // srand((unsigned)time(NULL));
    // id_shm = rand();
    while (id < 0 ) {
        // srand(id_shm);
        id_shm = rand();
        id = shmget(id_shm, 512 * 1024 * 1024, IPC_CREAT | 0777);
    }

    data = (char *)shmat(id, NULL, 0);
    if (data == NULL)
    {
        printf("Error Shmat failed.\n");
        exit(1);
    }
    printf("D%dZ\n", id_shm);  // Printf memory share id towards to terminal.

    // strcpy(data, "CMPCOVSHM");

    static uint64_t N;  // Counter for the guards.
    if (start == stop || *start) return;  // Initialize only once.
    // void *PC = __builtin_return_address(0);
    
    // char PcDescr[10240];
    // __sanitizer_symbolize_pc(PC, "%p %F %L", PcDescr, sizeof(PcDescr));

    // printf("\nI %p %p %p Z\n", GET_FUNC_PC, start, stop);
    // Add dataflow analysis information.
    sprintf(buf, "[\"I\",\"%p\",\"%p\",\"%p\"],", GET_FUNC_PC, start, stop);
    strcpy(data + interlen, buf);
    interlen += strlen(buf);
    // Update interlen
    sprintf(buf, "L%dZ", interlen);
    strcpy(data, buf);

    for (uint32_t *x = start; x < stop; x++)
    {
        *x = ++N;
    }

    // printf("\nS %p %lu Z\n", GET_FUNC_PC, N);  // Guards should start from 1.
    // Add dataflow analysis information.
    sprintf(buf, "[\"S\",\"%p\",\"%lu\"],", GET_FUNC_PC, N);
    strcpy(data + interlen, buf);
    interlen += strlen(buf);
    // Update interlen
    sprintf(buf, "L%dZ", interlen);
    strcpy(data, buf);

    int value;
    value = atexit(saveCovOnEnd);
    // if(value != 0) {
    //     cout << "atexit() function registration failed!";
    //     exit(1);
    // }
}

// This callback is inserted by the compiler on every edge in the
// control flow (some optimizations apply).
// Typically, the compiler will emit the code like this:
//    if(*guard)
//      __sanitizer_cov_trace_pc_guard(guard);
// But for large functions it will emit a simple call:
//    __sanitizer_cov_trace_pc_guard(guard);
void __sanitizer_cov_trace_pc_guard(uint32_t *guard) {
    if (!*guard) return;  // Duplicate the guard check.
    // If you set *guard to 0 this code will not be called again for this edge.
    // Now you can get the PC and do whatever you want:
    //   store it somewhere or symbolize it and print right away.
    // The values of `*guard` are as you set them in
    // __sanitizer_cov_trace_pc_guard_init and so you can make them consecutive
    // and use them to dereference an array or a bit vector.

    // This function is a part of the sanitizer run-time.
    // To use it, link with AddressSanitizer or other sanitizer.
    // char PcDescr[10240];
    // __sanitizer_symbolize_pc(PC, "%p_%F_%L", PcDescr, sizeof(PcDescr));
    // printf("\nG %p %x %s\n", guard, *guard, PcDescr);
    // printf("\nG %p %p %p %x Z\n", GET_FUNC_PC, GET_CALLER_PC, guard, *guard);
    // Add dataflow analysis information.
    // sprintf(buf, "[\"G\",\"%p\",\"%p\",\"%p\",\"%x\"],", GET_FUNC_PC, GET_CALLER_PC, guard, *guard);
    sprintf(buf, "[\"G\",\"%x\"],", *guard);
    strcpy(data + interlen, buf);
    interlen += strlen(buf);
    // Update interlen
    sprintf(buf, "L%dZ", interlen);
    strcpy(data, buf);
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