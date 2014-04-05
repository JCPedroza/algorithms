#include <stdio.h>
#include <stdlib.h>
#include <tgmath.h>
#include "timeutils.h"

// =========================================================================
//                               Functions
// =========================================================================

// Using for loop
long for_fibonacci(long n) {
    long acc  = 0;
    long last = 1;
    long temp;
    for (long i = 0; i < n; i++) {
        temp = acc;
        acc += last;
        last = temp;
    }
    return acc;
}

// Using while loop
long while_fibonacci(long n) {
    long acc  = 0;
    long last = 1;
    long temp;
    while (n > 0) {
        temp = acc;
        acc += last;
        last = temp;
        n--;
    }
    return acc;
}

// Using recursion
long recursive_fibonacci(long n) {
    if (n < 2) return n;
    return recursive_fibonacci(n - 1) + recursive_fibonacci(n - 2);
}

// Using recursion and ternary operator
long recursive_ternary_fibonacci(long n) {
    return n < 2 ? n : recursive_ternary_fibonacci(n - 1) + recursive_ternary_fibonacci(n - 2);
}

// Using analytic approach
long analytic_fibonacci(long n) {
    return floor( (pow(((1 + sqrt(5))/2), n) - pow(1 - ((1 + sqrt(5))/2), n)) / sqrt(5) );
}

// =========================================================================
//                               Main()
// =========================================================================

int main(int argc, char *argv[]) {

    long numbera = 10;
    long numberb = 11;
    long numberc = 12;
    long numberd = 13;

    long a = analytic_fibonacci(numbera);
    long b = analytic_fibonacci(numberb);
    long c = analytic_fibonacci(numberc);
    long d = analytic_fibonacci(numberd);

    printf("\n %ld fibonacci is: %ld\n\n", numbera, a);
    printf("\n %ld fibonacci is: %ld\n\n", numberb, b);
    printf("\n %ld fibonacci is: %ld\n\n", numberc, c);
    printf("\n %ld fibonacci is: %ld\n\n", numberd, d);
}
