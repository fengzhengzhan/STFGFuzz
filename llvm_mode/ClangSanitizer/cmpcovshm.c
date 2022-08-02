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
#define WEAK_HOOK_STRSTR 'r'
#define WEAK_HOOK_STRCASESTR 's'
#define WEAK_HOOK_MEMMEM 't'

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
#define GET_BLOCK_PC __builtin_return_address(2)

//// The first 8 bytes magic numbers of *.sancov files.
//// From: https://clang.llvm.org/docs/SanitizerCoverage.html#id13
//const uint64_t fMagic64 = 0xC0BFFFFFFFFFFF64;
//const uint64_t fMagic32 = 0xC0BFFFFFFFFFFF32;
//
//// Maximum length memory/string buffer for strcmp(), strncmp() and memcmp() functions.
//const uint8_t maxCmpLen = 32;

// Define trace levels  O P Q R S T U
#define LEVEL_NULL 0 
#define LEVEL_GUARDFAST 1
#define LEVEL_GUARD 2
#define LEVEL_GUARDSYMBOL 3
#define LEVEL_CMPFILTER 4
#define LEVEL_CMP 5
#define LEVEL_CMPGUARD 6
#define LEVEL_CMPGUARDSYMBOL 7

#define TRACE_LEN 1
#define TRACE_NULL 'O'
#define TRACE_GUARDFAST 'P'
#define TRACE_GUARD 'Q'
#define TRACE_GUARDSYMBOL 'R'
#define TRACE_CMPFILTER 'S'
#define TRACE_CMP 'T'
#define TRACE_CMPGUARD 'U'
#define TRACE_CMPGUARDSYMBOL 'V'

// Define the size of memory size.
#define SHMGET_SIZE 2147483648  // 2*1024*1024*1024  2GB

// Set variable.
char* data = NULL;
int filterlen = 128;
int savelen = 144;
int interlen = 160;  // 128+16+16
char buf[1024*1024];
char sendcmpid[128];
char eachcmpid[128];
int blocknum = -1;
int blockcmpcount = 0;
char *cover;
int covernum = 0;
int cmpfilterguard = 0;
char PcDescr[1024];


int retSame(char* each){
    int same = -1;
    int sendlen = strlen(sendcmpid);
    int eachlen = strlen(each);
    int idx = 0;
    
    // printf("%d %d\n", strlen(sendcmpid), strlen(each));
    // int scmp1 = strcmp(sendcmpid, each);
    if(sendlen == 0) {
        same = 0;
    } else if (sendlen == TRACE_LEN) {
        // printf("%d", sendcmpid[0] == TRACE_NULL);
        if (sendcmpid[0] == TRACE_NULL) { same = LEVEL_NULL; } 
        else if (sendcmpid[0] == TRACE_GUARDFAST) { same = LEVEL_GUARDFAST; } 
        else if (sendcmpid[0] == TRACE_GUARD) { same = LEVEL_GUARD; } 
        else if (sendcmpid[0] == TRACE_GUARDSYMBOL) { same = LEVEL_GUARDSYMBOL; } 
        // else if (sendcmpid[0] == TRACE_CMPFILTER) { same = LEVEL_CMPFILTER; } 
        else if (sendcmpid[0] == TRACE_CMP) { same = LEVEL_CMP; } 
        else if (sendcmpid[0] == TRACE_CMPGUARD) { same = LEVEL_CMPGUARD; } 
        else if (sendcmpid[0] == TRACE_CMPGUARDSYMBOL) { same = LEVEL_CMPGUARDSYMBOL; } 
    } else if (sendlen == eachlen) {
        int judge = 1;
        for (idx = 0; idx < sendlen; idx ++){
            if(sendcmpid[idx] != each[idx]){
                judge = 0;
                break;
            }
        }
        if (judge == 1){
            same = LEVEL_CMPFILTER;
        } 
    }

    // printf("%s %s %d %d %d\n", sendcmpid, each, same, sendlen, eachlen);
    return same;
}

// The end of analysis.
void saveCovOnEnd() {
    sprintf(eachcmpid, "Eend");
    // printf("%s %s\n", sendcmpid, eachcmpid);
    if(retSame(eachcmpid) > LEVEL_GUARDSYMBOL) {
        // printf("\nE %p Z\n", GET_FUNC_PC);
        // Add dataflow analysis information.

        sprintf(buf, "['Eend','E','%s+%d+%d'],", PcDescr, blocknum, blockcmpcount);
        blockcmpcount++;
        strcpy(data + interlen, buf);
        interlen += strlen(buf);
        // Update interlen
        sprintf(buf, "L%dZ", interlen);
        strcpy(data + filterlen, buf);

    
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
    int flag;
    flag = retSame(eachcmpid);
    if(flag > LEVEL_GUARDSYMBOL) {
        if (flag == LEVEL_CMPFILTER && cmpfilterguard == 0) {
            cmpfilterguard += 1;
        }
        // uintptr_t PC = reinterpret_cast<uintptr_t>(GET_FUNC_PC);

        // printf("\n%c %p %lu %lu %d Z\n", funcinfo, GET_FUNC_PC, arg1, arg2, arg_len);
        // Add dataflow analysis information.

        sprintf(buf, "['%c%p%p','%c','%s+%d+%d',%lu,%lu,%d],", funcinfo, GET_FUNC_PC, GET_CALLER_PC, funcinfo, PcDescr, blocknum, blockcmpcount, arg1, arg2, arg_len);
        blockcmpcount++;
        strcpy(data + interlen, buf);
        interlen += strlen(buf);
        // Update interlen
        sprintf(buf, "L%dZ", interlen);
        strcpy(data + filterlen, buf);
    }
} 

void handleStrMemCmp(void *called_pc, const char *s1, const char *s2, int len1, int len2, char *result, char funcinfo) {
    // printf("%p", called_pc);  called_pc stored PC (program counter) address of the original call.
    sprintf(eachcmpid, "%c%p", funcinfo, called_pc);
    int flag;
    flag = retSame(eachcmpid);
    if (flag > LEVEL_GUARDSYMBOL) {
        if (flag == LEVEL_CMPFILTER && cmpfilterguard == 0) {
            cmpfilterguard += 1;
        }
        // The length of each string.
        int n1;
        int n2;
        if (len1 != 0) {
            n1 = len1;
        } else {
            n1 = strlen(s1);
        }

        if (len2 != 0) {
            n2 = len2;
        } else {
            n2 = strlen(s2);
        }
        
        // printf("\n%c %x ", funcinfo, *(int *)called_pc);
        sprintf(buf, "['%c%p','%c','%s+%d+%d'", funcinfo, called_pc, funcinfo, PcDescr, blocknum, blockcmpcount);
        blockcmpcount++;
        // uint64_t traceflag =  reinterpret_cast<uint64_t>(called_pc) |
        //     (reinterpret_cast<uint64_t>(s1) << 48) |
        //     (reinterpret_cast<uint64_t>(s2) << 60);
        // printf("%lx ", traceflag);
        
        // printf("<s1\"%s\"1s> <s2\"%s\"2s> ", s1, s2);

        int i = 0;
        // printf("<s1\"");
        sprintf(buf+strlen(buf), ",b'");

        for (i = 0; i < n1; i ++) {
            // printf("%c", s1[i]);
            sprintf(buf+strlen(buf), "\\x%02x", (unsigned char)s1[i]);
            // if (s1[i] == '"' || s1[i] == '\\' || s1[i] == '\'') {
            //     sprintf(buf+strlen(buf), "\\%c", s1[i]);
            // } else {
            //     sprintf(buf+strlen(buf), "%c", s1[i]);
            // }
            // printf("\\x%02x,%c ", (unsigned char)s1[i],(unsigned char)s1[i]);
        }
        // printf("\"1s> <s2\"");
        sprintf(buf+strlen(buf), "',b'");

        for (i = 0; i < n2; i ++) {
            // printf("%c", s2[i]);
            sprintf(buf+strlen(buf), "\\x%02x", (unsigned char)s2[i]);
            // if (s2[i] == '"' || s2[i] == '\\' || s2[i] == '\'') {
            //     sprintf(buf+strlen(buf), "\\%c", s2[i]);
            // } else {
            //     sprintf(buf+strlen(buf), "%c", s2[i]);
            // }     
            // printf("\\x%02x,%c ", (unsigned char)s2[i],(unsigned char)s2[i]);          
        }
        // printf("\"2s> ");
        sprintf(buf+strlen(buf), "'");
        
        // printf("%d %d Z\n", n, result);
        sprintf(buf+strlen(buf), ",%d,%d,'%s'],", len1, len2, result);
        // printf("%s\n", buf);
        strcpy(data + interlen, buf);
        interlen += strlen(buf);
        // Update interlen
        sprintf(buf, "L%dZ", interlen);
        strcpy(data + filterlen, buf);
    }
}


void sanCovTraceSwitch(uint64_t Val, uint64_t *Cases) {
    // Called before a switch statement.
    // Val is the switch value. Operation Num.
    // Cases[0] is the number of case constants.
    // Cases[1] is the size of Val in bits.
    // Cases[2:] are the case constants.
    if (Cases[0] == 0) {
        return ;
    }

    sprintf(eachcmpid, "%c%p%p", COV_TRACE_SWITCH, GET_FUNC_PC, GET_CALLER_PC);
    int flag;
    flag = retSame(eachcmpid);
    if(flag > LEVEL_GUARDSYMBOL) {
        if (flag == LEVEL_CMPFILTER && cmpfilterguard == 0) {
            cmpfilterguard += 1;
        }
        // printf("\n%c %p %lu %lu", COV_TRACE_SWITCH, GET_FUNC_PC, Cases[0], Cases[1]);
        sprintf(buf, "['%c%p%p','%c','%s+%d+%d',%lu,%lu,%lu", COV_TRACE_SWITCH, GET_FUNC_PC, GET_CALLER_PC, COV_TRACE_SWITCH, PcDescr, blocknum, blockcmpcount, Cases[0], Cases[1], Val);
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
        strcpy(data + filterlen, buf);
    }
}


// compiler-rt functions.

// This callback is inserted by the compiler as a module constructor
// into every DSO. 'start' and 'stop' correspond to the
// beginning and end of the section with the guards for the entire
// binary (executable or DSO). The callback will be called at least
// once per DSO and may be called multiple times with the same parameters.
void __sanitizer_cov_trace_pc_guard_init(uint32_t *start, uint32_t *stop) {

    static uint64_t N;
    
    if (start == stop || *start) return;  // Initialize only once.
    
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
    if (data == NULL)
    {  
        printf("Error Data Shmat failed.\n");
        exit(1); 
    }  
    // printf("'%s' ", data);
    // Printf memory share id towards to terminal.
    printf("D%dZ\n", id_shm);  

    // memory get
    strcpy(sendcmpid, data);  // Get the sendcmpid
    printf("F%sZ\n", sendcmpid);


    // void *PC = __builtin_return_address(0);
    // char PcDescr[1024];
    // __sanitizer_symbolize_pc(PC, "%p %F %L", PcDescr, sizeof(PcDescr));
    // int n = 0;  // Counter for the guards.
    // printf("\nI %p %p %p Z\n", GET_FUNC_PC, start, stop);
    // Add dataflow analysis information.
    for (uint32_t *x = start; x < stop; x++)
    {
        *x = ++N;
    }
    // printf("%d", N);

    cover = (char *)malloc(N*sizeof(char));

    sprintf(eachcmpid, "I%p", GET_FUNC_PC);
    if(retSame(eachcmpid) > LEVEL_GUARDSYMBOL) {

        sprintf(buf, "['I%p','I','%s+%d+%d',%lu,'%p','%p'],", GET_FUNC_PC, PcDescr, blocknum, blockcmpcount, N, start, stop);
        blockcmpcount++;
        strcpy(data + interlen, buf);
        interlen += strlen(buf);
        // Update interlen
        sprintf(buf, "L%dZ", interlen);
        strcpy(data + filterlen, buf);
        // printf("\nS %p %lu Z\n", GET_FUNC_PC, N);  // Guards should start from 1.
        // Add dataflow analysis information.
    } else {
        sprintf(buf, " ");
        strcpy(data + interlen, buf);
        interlen += strlen(buf);
        // Update interlen
        sprintf(buf, "L%dZ", interlen);
        strcpy(data + filterlen, buf);
    }

    // covernum
    sprintf(buf, "C%dZ", covernum);
    strcpy(data + savelen, buf);
    
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
    // if (!*guard) return;  // Duplicate the guard check.
    // If you set *guard to 0 this code will not be called again for this edge.
    // Now you can get the PC and do whatever you want:
    //   store it somewhere or symbolize it and print right away.
    // The values of `*guard` are as you set them in
    // __sanitizer_cov_trace_pc_guard_init and so you can make them consecutive
    // and use them to dereference an array or a bit vector.

    // This function is a part of the sanitizer run-time.
    // To use it, link with AddressSanitizer or other sanitizer.
    // sprintf(eachcmpid, "G%p", GET_FUNC_PC);
    sprintf(eachcmpid, "Guard");
    int flag;
    flag = retSame(eachcmpid);
    // printf("%d", flag);
    if (cmpfilterguard > 0) {
        sprintf(buf, "['G%p','G',%d,'%s'],", GET_FUNC_PC, *guard, PcDescr);
        // printf("['G%p','G','%s',%d],", GET_FUNC_PC, PcDescr, *guard);
        strcpy(data + interlen, buf);
        interlen += strlen(buf);
        // Update interlen
        sprintf(buf, "L%dZ", interlen);
        strcpy(data + filterlen, buf);
        cmpfilterguard -= 1;
    }
    else if (flag == LEVEL_GUARDFAST) {
        sprintf(buf, "%d,", *guard);
        strcpy(data + interlen, buf);
        interlen += strlen(buf);
        // Update interlen
        sprintf(buf, "L%dZ", interlen);
        strcpy(data + filterlen, buf);
    }
    else if (flag == LEVEL_GUARD || flag == LEVEL_CMPGUARD) {
        // This function is a part of the sanitizer run-time.
        // To use it, link with AddressSanitizer or other sanitizer.
        // __sanitizer_symbolize_pc(PC, "%p %F %L", PcDescr, sizeof(PcDescr));

        // printf("guard:%s\n", PcDescr);
        sprintf(buf, "['G%p','G',%d,'%s'],", GET_FUNC_PC, *guard, PcDescr);
        // printf("['G%p','G','%s',%d],", GET_FUNC_PC, PcDescr, *guard);
        strcpy(data + interlen, buf);
        interlen += strlen(buf);
        // Update interlen
        sprintf(buf, "L%dZ", interlen);
        strcpy(data + filterlen, buf);
    }
    else if (flag == LEVEL_GUARDSYMBOL || flag == LEVEL_CMPGUARDSYMBOL) {
        // This function is a part of the sanitizer run-time.
        // To use it, link with AddressSanitizer or other sanitizer.
        // __sanitizer_symbolize_pc(PC, "%p %F %L", PcDescr, sizeof(PcDescr));

        // Spend Many time.
        __sanitizer_symbolize_pc(GET_FUNC_PC, "%F", PcDescr, sizeof(PcDescr));
        int i;
        for (i = 3; i <= strlen(PcDescr); i++)
        {
            PcDescr[i-3] = PcDescr[i];
        }

        // printf("guard:%s\n", PcDescr);
        sprintf(buf, "['G%p','G',%d,'%s'],", GET_FUNC_PC, *guard, PcDescr);
        // printf("['G%p','G','%s',%d],", GET_FUNC_PC, PcDescr, *guard);
        strcpy(data + interlen, buf);
        interlen += strlen(buf);
        // Update interlen
        sprintf(buf, "L%dZ", interlen);
        strcpy(data + filterlen, buf);
    }

    blocknum = *guard;
    blockcmpcount = 0;
    if (cover[blocknum] != 'C') {
        cover[blocknum] = 'C';
        covernum += 1;
        sprintf(buf, "C%dZ", covernum);
        strcpy(data + savelen, buf);
    }
}

void __sanitizer_cov_trace_cmp1(uint8_t Arg1, uint8_t Arg2) { 
    handleTraceCmp(Arg1, Arg2, 1, COV_TRACE_CMP1); 
}
void __sanitizer_cov_trace_cmp2(uint16_t Arg1, uint16_t Arg2) { 
    handleTraceCmp(Arg1, Arg2, 2, COV_TRACE_CMP2); 
}
void __sanitizer_cov_trace_cmp4(uint32_t Arg1, uint32_t Arg2) { 
    handleTraceCmp(Arg1, Arg2, 4, COV_TRACE_CMP4); 
}
void __sanitizer_cov_trace_cmp8(uint64_t Arg1, uint64_t Arg2) { 
    handleTraceCmp(Arg1, Arg2, 8, COV_TRACE_CMP8); 
}

void __sanitizer_cov_trace_const_cmp1(uint8_t Arg1, uint8_t Arg2) { 
    handleTraceCmp(Arg1, Arg2, 1, COV_TRACE_CONST_CMP1); 
}
void __sanitizer_cov_trace_const_cmp2(uint16_t Arg1, uint16_t Arg2) { 
    handleTraceCmp(Arg1, Arg2, 2, COV_TRACE_CONST_CMP2); 
}
void __sanitizer_cov_trace_const_cmp4(uint32_t Arg1, uint32_t Arg2) { 
    handleTraceCmp(Arg1, Arg2, 4, COV_TRACE_CONST_CMP4); 
}
void __sanitizer_cov_trace_const_cmp8(uint64_t Arg1, uint64_t Arg2) { 
    handleTraceCmp(Arg1, Arg2, 8, COV_TRACE_CONST_CMP8);
}

void __sanitizer_cov_trace_switch(uint64_t Val, uint64_t *Cases) { 
    sanCovTraceSwitch(Val, Cases); 
}


void __sanitizer_weak_hook_memcmp(void *called_pc, const void *s1, const void *s2, size_t n, int result) { 
    char covres = result + '\0';
    handleStrMemCmp(called_pc, (char *)s1, (char *)s2, n, n, &covres, WEAK_HOOK_MEMCMP); 
}
void __sanitizer_weak_hook_strncmp(void *called_pc, const char *s1, const char *s2, size_t n, int result) { 
    char covres = result + '\0';
    handleStrMemCmp(called_pc, s1, s2, n, n, &covres, WEAK_HOOK_STRNCMP); 
}
void __sanitizer_weak_hook_strcmp(void *called_pc, const char *s1, const char *s2, int result) { 
    char covres = result + '\0';
    handleStrMemCmp(called_pc, s1, s2, 0, 0, &covres, WEAK_HOOK_STRCMP); 
}
void __sanitizer_weak_hook_strncasecmp(void *called_pc, const char *s1, const char *s2, size_t n, int result) { 
    char covres = result + '\0';
    handleStrMemCmp(called_pc, s1, s2, n, n, &covres, WEAK_HOOK_STRNCASECMP); 
}
void __sanitizer_weak_hook_strcasecmp(void *called_pc, const char *s1, const char *s2, int result) { 
    char covres = result + '\0';
    handleStrMemCmp(called_pc, s1, s2, 0, 0, &covres, WEAK_HOOK_STRCASECMP); 
}

void __sanitizer_weak_hook_strstr(void *called_pc, const char *s1, const char *s2, char *result) {
    handleStrMemCmp(called_pc, s1, s2, 0, 0, result, WEAK_HOOK_STRSTR); 
}
void __sanitizer_weak_hook_strcasestr(void *called_pc, const char *s1, const char *s2, char *result){
    handleStrMemCmp(called_pc, s1, s2, 0, 0, result, WEAK_HOOK_STRCASESTR); 
}
void __sanitizer_weak_hook_memmem(void *called_pc, const void *s1, size_t len1, const void *s2, size_t len2, void *result){
    handleStrMemCmp(called_pc, (char *)s1, (char *)s2, len1, len2, (char *)result, WEAK_HOOK_MEMMEM); 
}

// void __sanitizer_ptr_cmp(void *a, void *b) {
//     printf("test");
// }

// void __sanitizer_malloc_hook(const volatile void *ptr, size_t size){
//     printf("test");
// }

// void __sanitizer_free_hook(const volatile void *ptr){
//     printf("test");
// }

// void __sanitizer_cov_trace_div4(uint32_t Val) {
// }
// void __sanitizer_cov_trace_div8(uint64_t Val) {
// }
// void __sanitizer_cov_trace_gep(uintptr_t Idx) {
// }

// void __dfsan_load_callback(dfsan_label Label, void* Addr);
// void __dfsan_store_callback(dfsan_label Label, void* Addr);
// void __dfsan_mem_transfer_callback(dfsan_label *Start, size_t Len);
// void __dfsan_cmp_callback(dfsan_label CombinedLabel);
