/*
Largest prime factor

Problem 3

The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?
*/

#include <stdio.h>
#include <math.h>
#include "timeutils.h"

// ==============================================================
//                     Helpers: Is prime?
// ==============================================================

long is_prime_iterative(long n) {
    for (int i = 2; i < n; i++)
        if (n % i == 0) return 0;
    return 1;
}

long is_prime_faster(long n) {

    if (n == 2)     return 1;
    if (n == 3)     return 1;
    if (n % 2 == 0) return 0;
    if (n % 3 == 0) return 0;

    int i = 5;
    int w = 2;

    while (i * i <= n) {
        if (n % i == 0) return 0;
        i += w;
        w  = 6 - w;
    }

    return 1; 

}

// ==============================================================
//                Finding the greatest prime factor
// ==============================================================

long find_greatest_prime_factor_1(long n) {

    long limit      = sqrt(n);
    long highest    = 0;
    long current    = 0;
    long previous   = 0;

    for (long i = 2; i < limit; i++) {
        if (n % i == 0) {
            current  = n / i;
            if (is_prime_faster(current) && current > highest ) {
                previous = highest;
                highest  = current;
            }
            if (is_prime_faster(i) && i > highest) {
                previous = highest;
                highest  = i;
            }
        }
    }

    return highest;

}

// Doesn't use helpers
long find_greatest_prime_factor_2(long n) {

    long factor;
    long last_factor;
    long max_factor;

    if (n % 2 == 0) {
        last_factor = 2;
        n = n / 2;
        while (n % 2 == 0) {
            n = n / 2;
        }
    } else {
        last_factor = 1;
    }

    factor = 3;
    max_factor = sqrt(n);

    while (n > 1 && factor <= max_factor) {
        if (n % factor == 0) {
            n = n / factor;
            last_factor = factor;
            while (n % factor == 0) {
                n = n / factor;
            }
            max_factor = sqrt(n);
        }
        factor = factor + 2;
    }

    if (n == 1) return last_factor;
    else        return n;
}

// ==============================================================
//                       main & timing
// ==============================================================

int main() {

    long value       = 600851475143;
    long repetitions = 70;

    double prime_iterative_time = time_it(value, repetitions, is_prime_iterative);
    double prime_faster_time    = time_it(value, repetitions, is_prime_faster);
    double gpf1_time            = time_it(value, repetitions, find_greatest_prime_factor_1);
    double gpf2_time            = time_it(value, repetitions, find_greatest_prime_factor_2);

    double prime_iterative_average = prime_iterative_time / repetitions;
    double prime_faster_average    = prime_faster_time    / repetitions;
    double gpf1_average            = gpf1_time            / repetitions;
    double gpf2_average            = gpf2_time            / repetitions;

    printf("\n===========================================================\n\n");
    printf("-------------------------------------------\n");
    printf("Execution time for is prime algorithms\n");
    printf("n = %ld\n", value);
    printf("repetitions = %ld\n", repetitions);
    printf("-------------------------------------------\n\n");


    printf("Total:\n");
    printf("is_prime_iterative: %f\n", prime_iterative_time);
    printf("is_prime_faster:    %f\n", prime_faster_time);

    printf("Average:\n");
    printf("is_prime_iterative: %f\n", prime_iterative_average);
    printf("is_prime_faster:    %f\n", prime_faster_average);

    printf("\n\n");

    printf("-------------------------------------------\n");
    printf("Execution time find greatest prime factor algorithms\n");
    printf("n = %ld\n", value);
    printf("repetitions = %ld\n", repetitions);
    printf("-------------------------------------------\n\n");

    printf("Total:\n");
    printf("gpf1: %f\n", gpf1_time);
    printf("gpf2: %f\n", gpf2_time);

    printf("Average:\n");
    printf("gpf1: %f\n", gpf1_average);
    printf("gpf2: %f\n", gpf2_average);

    printf("\n\n");
    printf("===========================================================\n\n");










}