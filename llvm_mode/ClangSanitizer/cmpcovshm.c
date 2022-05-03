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

#define SHMGET_SIZE 2147483648  // 2*1024*1024*1024  2GB
#define SEND_SIZE 64
char* data = NULL;
char* senddata = NULL;
int savelen = 15;
int interlen = 16;
char buf[1024*1024];
char sendcmpid[64];
char eachcmpid[64];
char* defaultcmpid = "None";
char* guard = "Guard";
int blocknum = -1;
int blockcmpcount = 0;

int retSame(char* each){
    int same = -1;
    int sendlen = strlen(sendcmpid);
    int eachlen = strlen(each);
    int idx = 0;
    // printf("%s %s\n", sendcmpid, each);
    // printf("%d %d\n", strlen(sendcmpid), strlen(each));
    // int scmp1 = strcmp(sendcmpid, each);
    if(senddata == NULL) {
        same = 0;
    } else if (sendlen == strlen(defaultcmpid)) {
        int judge = 1;
        for (idx = 0; idx < sendlen; idx ++){
            if(sendcmpid[idx] != defaultcmpid[idx]){
                judge = 0;
                break;
            }
        }
        if (judge == 1){
            same = 0;
        }  
    } else if (sendlen == strlen(guard)) {
        int judge = 1;
        for (idx = 0; idx < sendlen; idx ++){
            if(sendcmpid[idx] != guard[idx]){
                judge = 0;
                break;
            }
        }
        if (judge == 1){
            same = 1;
        }  
    } else if (sendlen == eachlen) {
        int judge = 1;
        for (idx = 0; idx < sendlen; idx ++){
            if(sendcmpid[idx] != each[idx]){
                judge = 0;
                break;
            }
        }
        if (judge == 1){
            same = 0;
        } 
    }
    // printf("%d", same);

    return same;
}

// The end of analysis.
void saveCovOnEnd() {
    sprintf(eachcmpid, "Eend");
    // printf("%s %s\n", sendcmpid, eachcmpid);
    if(retSame(eachcmpid) >= 0) {
        // printf("\nE %p Z\n", GET_FUNC_PC);
        // Add dataflow analysis information.

        sprintf(buf, "['E','%d_%d','Eend'],",blocknum, blockcmpcount);
        blockcmpcount++;
        strcpy(data + interlen, buf);
        interlen += strlen(buf);
        // Update interlen
        sprintf(buf, "L%dZ", interlen);
        strcpy(data, buf);

    
        // Separating shared memory from the current process.
        // if (shmdt(data) == -1)
        // {
        //     printf("Error Shmdt failed.\n");
        //     exit(1);
        // }
        // shmctl(id, IPC_RMID, 0);
    }
}

void handleTraceCmp(uint64_t arg1, uint64_t arg2, int arg_len, char funcinfo) {
    sprintf(eachcmpid, "%c%p%p", funcinfo, GET_FUNC_PC, GET_CALLER_PC);
    // printf("%s %s\n", sendcmpid, eachcmpid);
    if(retSame(eachcmpid) >= 0) {
        // uintptr_t PC = reinterpret_cast<uintptr_t>(GET_FUNC_PC);

        // printf("\n%c %p %lu %lu %d Z\n", funcinfo, GET_FUNC_PC, arg1, arg2, arg_len);
        // Add dataflow analysis information.

        sprintf(buf, "['%c','%d_%d','%c%p%p',%lu,%lu,%d],", funcinfo, blocknum, blockcmpcount, funcinfo, GET_FUNC_PC, GET_CALLER_PC,arg1, arg2, arg_len);
        blockcmpcount++;
        strcpy(data + interlen, buf);
        interlen += strlen(buf);
        // Update interlen
        sprintf(buf, "L%dZ", interlen);
        strcpy(data, buf);
    }
} 

void handleStrMemCmp(void *called_pc, const char *s1, const char *s2, int n, int result, char funcinfo) {
    // printf("%p", called_pc);  called_pc stored PC (program counter) address of the original call.
    sprintf(eachcmpid, "%c%p", funcinfo, called_pc);
    if (retSame(eachcmpid) >= 0) {
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
        sprintf(buf, "['%c','%d_%d','%c%p'", funcinfo, blocknum, blockcmpcount, funcinfo, called_pc);
        blockcmpcount++;
        // uint64_t traceflag =  reinterpret_cast<uint64_t>(called_pc) |
        //     (reinterpret_cast<uint64_t>(s1) << 48) |
        //     (reinterpret_cast<uint64_t>(s2) << 60);
        // printf("%lx ", traceflag);
        
        // printf("<s1\"%s\"1s> <s2\"%s\"2s> ", s1, s2);

        int i = 0;
        // printf("<s1\"");
        sprintf(buf+strlen(buf), ",'");

        for (i = 0; i < n1; i ++) {
            // printf("%c", s1[i]);
            if (s1[i] == '"' || s1[i] == '\\' || s1[i] == '\'') {
                sprintf(buf+strlen(buf), "\\%c", s1[i]);
            } else {
                sprintf(buf+strlen(buf), "%c", s1[i]);
            }
        }
        // printf("\"1s> <s2\"");
        sprintf(buf+strlen(buf), "','");

        for (i = 0; i < n2; i ++) {
            // printf("%c", s2[i]);
            if (s2[i] == '"' || s2[i] == '\\' || s2[i] == '\'') {
                sprintf(buf+strlen(buf), "\\%c", s2[i]);
            } else {
                sprintf(buf+strlen(buf), "%c", s2[i]);
            }               
        }
        // printf("\"2s> ");
        sprintf(buf+strlen(buf), "'");
        
        // printf("%d %d Z\n", n, result);
        sprintf(buf+strlen(buf), ",%d,%d],", n, result);
        // printf("%s\n", buf);
        strcpy(data + interlen, buf);
        interlen += strlen(buf);
        // Update interlen
        sprintf(buf, "L%dZ", interlen);
        strcpy(data, buf);
    }
}


void sanCovTraceSwitch(uint64_t Val, uint64_t *Cases) {
    // Called before a switch statement.
    // Val is the switch value.
    // Cases[0] is the number of case constants.
    // Cases[1] is the size of Val in bits.
    // Cases[2:] are the case constants.
    if (Cases[0] == 0) {
        return ;
    }

    sprintf(eachcmpid, "%c%p%p", COV_TRACE_SWITCH, GET_FUNC_PC, GET_CALLER_PC);
    if(retSame(eachcmpid) >= 0) {

        // printf("\n%c %p %lu %lu", COV_TRACE_SWITCH, GET_FUNC_PC, Cases[0], Cases[1]);
        sprintf(buf, "['%c','%d_%d','%c%p%p',%lu,%lu,%lu", COV_TRACE_SWITCH, blocknum, blockcmpcount, COV_TRACE_SWITCH, GET_FUNC_PC, GET_CALLER_PC, Cases[0], Cases[1], Val);
        blockcmpcount++;

        for (int i = 0; i < Cases[0]; i ++) {
            // printf(" %lu", Cases[2 + i]);
            sprintf(buf+strlen(buf), ",%lu", Cases[2 + i]);
        }
        // printf(" Z\n");
        // Add dataflow analysis information.
        sprintf(buf+strlen(buf), "],");
        strcpy(data + interlen, buf);
        interlen += strlen(buf);
        // Update interlen
        sprintf(buf, "L%dZ", interlen);
        strcpy(data, buf);
    }
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
    int id;
    id = shmget(id_shm, SHMGET_SIZE, IPC_CREAT | 0666);
    // srand((unsigned)time(NULL));
    // id_shm = rand();
    while (id < 0 ) {
        // srand(id_shm);
        id_shm = rand();
        id = shmget(id_shm, SHMGET_SIZE, IPC_CREAT | 0666);
    }

    data = (char *)shmat(id, NULL, 0);
    // if ((int)(data)==-1)
    if (data == NULL)
    {  
        printf("Error Data Shmat failed.\n");
        exit(1); 
    }  

    // if (data == NULL)
    // {
    //     data = shmat(id, data, 0666);
    // }

    // if (data == NULL)
    // {
    //     printf("Error Shmat failed.\n");
    //     exit(1);
    // }

    // Printf memory share id towards to terminal.
    printf("D%dZ\n", id_shm);  

    // memory get
    key_t send_shm = 168421;
    int sendid;
    sendid = shmget(send_shm, SEND_SIZE, IPC_CREAT | 0666);
    if (sendid < 0 ) {
        FILE *fp = NULL;
        char buff[64];

        fp = fopen("/tmp/shmsendkey", "r");
        fscanf(fp, "%s", buff);
        int file_shm = atoi(buff);
        // printf("%d %d\n", buff, sendid);
        sendid = shmget(file_shm, SEND_SIZE, IPC_CREAT | 0666);
        if (sendid < 0) {
            printf("Error Send Shmget failed.\n");
            exit(1); 
        }
    }

    senddata = (char *)shmat(sendid, NULL, 0);
    strcpy(sendcmpid, senddata);  // Get the sendcmpid
    // if (strcmp(sendcmpid, defaultcmpid) == 0) {
    //     printf("ok");
    // }
    // printf("%s\n", sendcmpid);

    // sprintf(eachcmpid, "I%p", GET_FUNC_PC);
    // // printf("%s\n", eachcmpid);
    // if(strcmp(sendcmpid, eachcmpid) == 0) {
    //     printf("ok");
    // }


    // if (senddata == NULL)
    // {  
    //     printf("Error Senddata Shmat failed.\n");
    //     exit(1); 
    // }

    // strcpy(data, "CMPCOVSHM");

    
    if (start == stop || *start) return;  // Initialize only once.
    
    sprintf(eachcmpid, "I%p", GET_FUNC_PC);
    if(retSame(eachcmpid) >= 0) {
        // void *PC = __builtin_return_address(0);
        // char PcDescr[10240];
        // __sanitizer_symbolize_pc(PC, "%p %F %L", PcDescr, sizeof(PcDescr));
        static uint64_t N;  // Counter for the guards.
        // printf("\nI %p %p %p Z\n", GET_FUNC_PC, start, stop);
        // Add dataflow analysis information.
        for (uint32_t *x = start; x < stop; x++)
        {
            *x = ++N;
        }

        sprintf(buf, "['I','%d_%d','I%p',%lu,'%p','%p'],", blocknum, blockcmpcount, GET_FUNC_PC, N, start, stop);
        blockcmpcount++;
        strcpy(data + interlen, buf);
        interlen += strlen(buf);
        // Update interlen
        sprintf(buf, "L%dZ", interlen);
        strcpy(data, buf);
        // printf("\nS %p %lu Z\n", GET_FUNC_PC, N);  // Guards should start from 1.
        // Add dataflow analysis information.
    } else {
        sprintf(buf, " ");
        strcpy(data + interlen, buf);
        interlen += strlen(buf);
        // Update interlen
        sprintf(buf, "L%dZ", interlen);
        strcpy(data, buf);
    }
    
    atexit(saveCovOnEnd);
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
    sprintf(eachcmpid, "G%p", GET_FUNC_PC);
    if (retSame(eachcmpid) == 1) {
        sprintf(buf, "['G',%d],", *guard);
        strcpy(data + interlen, buf);
        interlen += strlen(buf);
        // Update interlen
        sprintf(buf, "L%dZ", interlen);
        strcpy(data, buf);
    }
    blocknum = *guard;
    blockcmpcount = 0;
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