#ifndef CMPCOV_COMMON_H_
#define CMPCOV_COMMON_H_

// Maximum length memory/string buffer for strcmp(), strncmp() and memcmp() functions.
const size_t maxCmpLen = 32;

int GetPid();

#endif  // CMPCOV_COMMON_H_