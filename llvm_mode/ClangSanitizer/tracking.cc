#include <iostream>
#include <stdint.h>
#include <stdio.h>
// #include <sanitizer/coverage_interface.h>

#include "tracking.h"

using namespace std;

extern "C"{
    // This callback is inserted by the compiler as a module constructor
    // into every DSO. 'start' and 'stop' correspond to the
    // beginning and end of the section with the guards for the entire
    // binary (executable or DSO). The callback will be called at least
    // once per DSO and may be called multiple times with the same parameters.
    void __sanitizer_cov_trace_pc_guard_init(uint32_t *start, uint32_t *stop) {
        static uint64_t N;  // Counter for the guards.
        if (start == stop || *start) return;  // Initialize only once.
        // void *PC = __builtin_return_address(0);
        
        // char PcDescr[10240];
        // __sanitizer_symbolize_pc(PC, "%p %F %L", PcDescr, sizeof(PcDescr));
        // printf("\nI %p %p %s\n", start, stop, PcDescr);
        printf("\nI %x %p %p Z\n", *(int *)GET_CALLER_PC, start, stop);
        for (uint32_t *x = start; x < stop; x++)
        {
            *x = ++N;
        }

        printf("\nS %x %lu Z\n", *(int *)GET_CALLER_PC, N);  // Guards should start from 1.
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
        printf("\nG %x %p %x Z\n", *(int *)GET_CALLER_PC, guard, *guard);
    }

}

Tracking::Tracking(/* args */)
{
}

Tracking::~Tracking()
{
}