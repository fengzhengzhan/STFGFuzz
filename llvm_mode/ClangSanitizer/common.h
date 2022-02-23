#ifndef CMPCOV_COMMON_H_
#define CMPCOV_COMMON_H_

#include <stddef.h>
#include <stdint.h>


// The first 8 bytes magic numbers of *.sancov files.
// From: https://clang.llvm.org/docs/SanitizerCoverage.html#id13
const uint64_t fMagic64 = 0xC0BFFFFFFFFFFF64;
const uint64_t fMagic32 = 0xC0BFFFFFFFFFFF32;

// Maximum length memory/string buffer for strcmp(), strncmp() and memcmp() functions.
const uint8_t maxCmpLen = 32;

int GetPid();

#endif  // CMPCOV_COMMON_H_