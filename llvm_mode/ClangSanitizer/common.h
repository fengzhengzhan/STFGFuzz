#ifndef CMPCOV_COMMON_H_
#define CMPCOV_COMMON_H_

#include <stddef.h>
#include <stdint.h>

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


// The first 8 bytes magic numbers of *.sancov files.
// From: https://clang.llvm.org/docs/SanitizerCoverage.html#id13
const uint64_t fMagic64 = 0xC0BFFFFFFFFFFF64;
const uint64_t fMagic32 = 0xC0BFFFFFFFFFFF32;

// Maximum length memory/string buffer for strcmp(), strncmp() and memcmp() functions.
const uint8_t maxCmpLen = 32;

int GetPid();

#endif  // CMPCOV_COMMON_H_