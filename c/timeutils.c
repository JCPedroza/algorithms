#include <time.h>
#include "timeutils.h"


// =========================================================================
//                               Timing
// =========================================================================

// Measures the CPU time of a function executed x times
double time_it(long n, long times, long(*f)(long)) {
    clock_t start = clock();
    for (long i = 0; i < times; i++) {
        f(n);
    }
    return (clock() - start) / 1000000.0;
}
