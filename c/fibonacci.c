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

// Using tail recursion
long tail_helper(long term, long val, long prev) {
    if (term == 0) return prev;
    if (term == 1) return val;
    return tail_helper(term - 1, val + prev, val);
}
long tail_fibonacci(long n) {
    return tail_helper(n, 1, 0);

}

// Using analytic approach (Binet's formula)
long analytic_fibonacci(long n) {
    return floor( (pow(((1 + sqrt(5))/2), n) - pow(1 - ((1 + sqrt(5))/2), n)) / sqrt(5) );
}

// =========================================================================
//                               Main()
// =========================================================================

int main(int argc, char *argv[]) {

    if (argc != 3) {
        printf("\nusage: factorial <factorial to calculate> <repetitions>\n\n");
        return 1;
    }

    long number = atol(argv[1]);
    long times  = atol(argv[2]);

    double for_time               = time_it(number, times, for_fibonacci);
    double while_time             = time_it(number, times, while_fibonacci);
    double recursive_time         = time_it(number, times, recursive_fibonacci);
    double recursive_ternary_time = time_it(number, times, recursive_ternary_fibonacci);
    double tail_time              = time_it(number, times, tail_fibonacci);
    double analytic_time          = time_it(number, times, analytic_fibonacci);

    double for_average               = for_time               / times;
    double while_average             = while_time             / times;
    double recursive_average         = recursive_time         / times;
    double recursive_ternary_average = recursive_ternary_time / times;
    double tail_average              = tail_time              / times;
    double analytic_average          = analytic_time          / times;

    printf("\n");
    printf("==============================================\n");
    printf("==============================================\n\n");
    printf("Fibonacci Algorithm\n");
    printf("Fibonacci calculated: %ld\n", number);
    printf("Number of times: %ld\n", times);
    printf("(time in seconds) \n");
    printf("----------------------------------------------\n");
    printf("\n");

    printf("Total time:\n");
    printf("for loop:          %f\n", for_time);
    printf("while loop:        %f\n", while_time);
    printf("recursion:         %f\n", recursive_time);
    printf("recursion ternary: %f\n", recursive_ternary_time);
    printf("tail recursion:    %f\n", tail_time);
    printf("analytic:          %f\n", analytic_time);

    printf("\n");

    printf("Average time:\n");
    printf("for loop:          %f\n", for_average);
    printf("while loop:        %f\n", while_average);
    printf("recursion:         %f\n", recursive_average);
    printf("recursion ternary: %f\n", recursive_ternary_average);
    printf("tail recursion:    %f\n", tail_average);
    printf("analytic:          %f\n", analytic_average);


    printf("\n");
    printf("==============================================\n");
    printf("==============================================\n\n");

    return 0;
}
