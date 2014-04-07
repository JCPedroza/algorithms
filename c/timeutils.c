#include <stdio.h>
#include <time.h>
#include "timeutils.h"


// =========================================================================
//                               Timing
// =========================================================================

double time_it(long n, long times, long(*f)(long)) {
    clock_t start = clock();
    for (long i = 0; i < times; i++) {
        f(n);
    }
    return (clock() - start) / 1000000.0;
}

double time_it_char(char* s, long times, int(*f)(char*)) {
    clock_t start = clock();
    for (long i = 0; i < times; i++) {
        f(s);
    }
    return (clock() - start) / 1000000.0;
}

