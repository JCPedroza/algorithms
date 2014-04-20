// Needs timing, implement a timing dynamic similar to what you did in python

#include <stdio.h>

// ======================================================
// Algorithms for primarlity test using trial division.
// ======================================================

// The simplest primality test is trial division: Given an input number n, check 
// whether any integer m from 2 to n − 1 evenly divides n (the division leaves no 
// remainder). If n is divisible by any m then n is composite, otherwise it is prime.
short is_prime_1(long n) {
    for (long divisor = 2; divisor < n; divisor++)
        if (n % divisor == 0) return 0;
    return 1;
}

// However, we don't actually have to check all numbers up to n. Let's look at another
// example: all the divisors of 100: 2, 4, 5, 10, 20, 25, 50. Here we see that the largest 
// factor is 100/2 = 50. This is true for all n: all divisors are less than or equal to n/2. 
short is_prime_2(long n) {
    long limit = n / 2;
    for (long divisor = 2; divisor <= limit; divisor++) 
        if (n % divisor == 0) return 0;
    return 1;
}

// We can do better though. If we take a closer look at the divisors, we will see that some 
// of them are redundant. If we write the list differently:
// 100 = 2 × 50 = 4 × 25 = 5 × 20 = 10 × 10 = 20 × 5 = 25 × 4 = 50 × 2
// it becomes obvious. Once we reach 10, which is sqrt(100), the divisors just flip around and 
// repeat. Therefore we can further eliminate testing divisors greater than sqrt(n). 
short is_prime_3(long n) {
    long limit = n * 0.5;
    for (long divisor = 2; divisor <= limit; divisor++) 
        if (n % divisor == 0) return 0;
    return 1;
}

// We can also eliminate all the even numbers greater than 2, since if an even number can 
// divide n, so can 2.
short is_prime_4(long n) {
    if (n != 2 && n % 2 == 0) return 0;
    long limit = n * 0.5;
    for (long divisor = 3; divisor <= limit; divisor += 2) 
        if (n % divisor == 0) return 0;
    return 1;
}

// The algorithm can be improved further by observing that all primes are of the form 6k ± 1, 
// with the exception of 2 and 3. This is because all integers can be expressed as (6k + i) for 
// some integer k and for i = −1, 0, 1, 2, 3, or 4 2 divides (6k + 0), (6k + 2), (6k + 4); and 
// 3 divides (6k + 3). So a more efficient method is to test if n is divisible by 2 or 3, then to 
// check through all the numbers of form 6k ± 1 <= sqrt(n). This is 3 times as fast 
// as testing all m.
short is_prime_5(long n) {
    if (n == 2 || n == 3)         return 1;
    if (n % 2 == 0 || n % 3 == 0) return 0;
    long limit = n * 0.5;
    for (long divisor = 5; divisor <= limit; divisor += 2) 
        if (n % divisor == 0) return 0;
    return 1;
}

// Generalising further, it can be seen that all primes are of the form c#k + i for i < c# where i 
// represents the numbers that are coprime to c# and where c and k are integers. For example, let c = 6. 
// Then c# = 2 \cdot 3 \cdot 5  = 30. All integers are of the form 30k + i for i = 0, 1, 2,...,29 and k 
// an integer. However, 2 divides 0, 2, 4,...,28 and 3 divides 0, 3, 6,...,27 and 5 divides 0, 5, 10,...,25. 
// So all prime numbers are of the form 30k + i for i = 1, 7, 11, 13, 17, 19, 23, 29 (i.e. for i < 30 such 
// that gcd(i,30) = 1). Note that if i and 30 are not coprime, then 30k + i is divisible by a prime 
// divisor of 30, namely 2, 3 or 5, and is therefore not prime.
// As c → ∞, the number of values that c#k + i can take over a certain range decreases, and so the time to 
// test n decreases. For this method, it is also necessary to check for divisibility by all primes that are 
// less than c. Observations analogous to the preceding can be applied recursively, giving the Sieve of 
// Eratosthenes.
short is_prime_6(long n) {
    if (n < 2)                    return 0;
    if (n == 2 || n == 3)         return 1;
    if (n % 2 == 0 || n % 3 == 0) return 0;
    long limit = n * 0.5;
    for (long divisor = 5; divisor <= limit; divisor += 6) 
        if (n % divisor == 0 || n % (divisor + 2) == 0) return 0;
    return 1;
}

int main(int charc, char* charv[]) {
    printf("\n%d\n\n", is_prime_6(2341));
}