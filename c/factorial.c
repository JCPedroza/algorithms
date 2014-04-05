#include <stdio.h>
#include <stdlib.h>
#include <time.h>

// =========================================================================
//                               Functions
// =========================================================================

// Using for loop
double iterative_for_factorial(double n) {
    double acc = 1;
    for (n = n; n > 0; n--) acc *= n;
    return acc;
}

// Using while loop
double iterative_while_factorial(double n) {
    double acc = 1;
    while (n > 0) {
        acc *= n;
        n--;
    }
    return acc;
}

// Using recursion
double recursive_factorial(double n) {
    if (n < 1) return 1;
    return n * recursive_factorial(n-1);
}

// Using recursion and ternary operator
double recursive_ternary_factorial(double n) {
    return n < 1 ? 1 : n * recursive_ternary_factorial(n - 1);
}

// =========================================================================
//                               Timing
// =========================================================================

// Measures the CPU time of a function executed x times
double timeIt(double n, double times, double(*f)(double)) {
    clock_t start = clock();
    for (double i = 0; i < times; i++) {
        f(n);
    }
    return (clock() - start);
}

// =========================================================================
//                               Main()
// =========================================================================

int main(int argc, char *argv[]) {

    if (argc != 3) {
        printf("\nusage: factorial <factorial to calculate> <repetitions>\n\n");
        return 1;
    }

    double number = atof(argv[1]);
    double times  = atof(argv[2]);

    double iterative_for_time     = timeIt(number, times, iterative_for_factorial) / 1000000.0;
    double iterative_while_time   = timeIt(number, times, iterative_while_factorial) / 1000000.0;
    double recursive_time         = timeIt(number, times, recursive_factorial) / 1000000.0;
    double recursive_ternary_time = timeIt(number, times, recursive_ternary_factorial) / 1000000.0;

    double iterative_for_average     = iterative_for_time     / times;
    double iterative_while_average   = iterative_while_time   / times;
    double recursive_average         = recursive_time         / times;
    double recursive_ternary_average = recursive_ternary_time / times;
    
    printf("\n");
    printf("==============================================\n");
    printf("==============================================\n\n");
    printf("Factorial Algorithm\n");
    printf("Factorial calculated: %f\n", number);
    printf("Number of times: %f\n", times);
    printf("(all results are in seconds) \n");
    printf("----------------------------------------------\n");
    printf("\n");

    printf("Total time:\n");
    printf("iterative_for_factorial:     %f\n", iterative_for_time);
    printf("iterative_while_factorial:   %f\n", iterative_while_time);
    printf("recursive_factorial:         %f\n", recursive_time);
    printf("recursive_ternary_factorial: %f\n", recursive_ternary_time);

    printf("\n");

    printf("Average time:\n");
    printf("iterative_for_factorial:     %f\n", iterative_for_average);
    printf("iterative_while_factorial:   %f\n", iterative_while_average);
    printf("recursive_factorial:         %f\n", recursive_average);
    printf("recursive_ternary_factorial: %f\n", recursive_ternary_average);

    printf("\n");
    printf("==============================================\n");
    printf("==============================================\n\n");

    return 0;

}

