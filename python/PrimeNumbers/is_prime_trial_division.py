# -*- coding: utf-8 -*-

import math
import time_utils

# ======================================================
# Algorithms for primarlity test using trial division.
# ======================================================

# The simplest primality test is trial division: Given an input number n, check 
# whether any integer m from 2 to n − 1 evenly divides n (the division leaves no 
# remainder). If n is divisible by any m then n is composite, otherwise it is prime.
def is_prime_trial_division_1(n):
    for divisor in range(2, n):
        if n % divisor == 0:
            return False
    return True

# However, we don't actually have to check all numbers up to n. Let's look at another
# example: all the divisors of 100: 2, 4, 5, 10, 20, 25, 50. Here we see that the largest 
# factor is 100/2 = 50. This is true for all n: all divisors are less than or equal to n/2. 
def is_prime_trial_division_2(n):
    for divisor in range(2, (n / 2) + 1):
        if n % divisor == 0:
            return False
    return True

# We can do better though. If we take a closer look at the divisors, we will see that some 
# of them are redundant. If we write the list differently:
# 100 = 2 × 50 = 4 × 25 = 5 × 20 = 10 × 10 = 20 × 5 = 25 × 4 = 50 × 2
# it becomes obvious. Once we reach 10, which is sqrt(100), the divisors just flip around and 
# repeat. Therefore we can further eliminate testing divisors greater than sqrt(n). 
def is_prime_trial_division_3(n):
    for divisor in range(2, int(math.sqrt(n)) + 1):
        if n % divisor == 0:
            return False
    return True

# We can also eliminate all the even numbers greater than 2, since if an even number can 
# divide n, so can 2.
def is_prime_trial_division_4(n):

    if ( n != 2 and n % 2 == 0):
        return False

    divisor = 3
    limit   = int(math.sqrt(n))
    while divisor <= limit:
        if n % divisor == 0:
            return False
        divisor += 2

    return True

# The algorithm can be improved further by observing that all primes are of the form 6k ± 1, 
# with the exception of 2 and 3. This is because all integers can be expressed as (6k + i) for 
# some integer k and for i = −1, 0, 1, 2, 3, or 4 2 divides (6k + 0), (6k + 2), (6k + 4); and 
# 3 divides (6k + 3). So a more efficient method is to test if n is divisible by 2 or 3, then to 
# check through all the numbers of form 6k ± 1 <= sqrt(n). This is 3 times as fast 
# as testing all m.
def is_prime_trial_division_5(n): 

    if n in (2, 3):
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False

    divisor = 5
    limit   = int(math.sqrt(n))
    while divisor <= limit:
        if n % divisor == 0:
            return False
        divisor += 2

    return True

# Generalising further, it can be seen that all primes are of the form c#k + i for i < c# where i 
# represents the numbers that are coprime to c# and where c and k are integers. For example, let c = 6. 
# Then c# = 2 \cdot 3 \cdot 5  = 30. All integers are of the form 30k + i for i = 0, 1, 2,...,29 and k 
# an integer. However, 2 divides 0, 2, 4,...,28 and 3 divides 0, 3, 6,...,27 and 5 divides 0, 5, 10,...,25. 
# So all prime numbers are of the form 30k + i for i = 1, 7, 11, 13, 17, 19, 23, 29 (i.e. for i < 30 such 
# that gcd(i,30) = 1). Note that if i and 30 are not coprime, then 30k + i is divisible by a prime 
# divisor of 30, namely 2, 3 or 5, and is therefore not prime.
# As c → ∞, the number of values that c#k + i can take over a certain range decreases, and so the time to 
# test n decreases. For this method, it is also necessary to check for divisibility by all primes that are 
# less than c. Observations analogous to the preceding can be applied recursively, giving the Sieve of 
# Eratosthenes.
def is_prime_trial_division_6(n):

    if n < 2:
        return False
    if n in (2, 3):
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False

    limit   = int(math.sqrt(n))
    divisor = 5

    while divisor <= limit:
        if n % divisor == 0 or n % (divisor + 2) == 0:
            return False
        divisor += 6

    return True


# ======================================================
#                Measuring Execution Time
# ======================================================

from_number = 2
the_number  = 2000000

# is_prime_trial_division_1_time = time_utils.clock_range(is_prime_trial_division_1, from_number, the_number)
# is_prime_trial_division_2_time = time_utils.clock_range(is_prime_trial_division_2, from_number, the_number)
is_prime_trial_division_3_time = time_utils.clock_range(is_prime_trial_division_3, from_number, the_number)
is_prime_trial_division_4_time = time_utils.clock_range(is_prime_trial_division_4, from_number, the_number)
is_prime_trial_division_5_time = time_utils.clock_range(is_prime_trial_division_5, from_number, the_number)
is_prime_trial_division_6_time = time_utils.clock_range(is_prime_trial_division_6, from_number, the_number)

# ======================================================
#                     Print Results
# ======================================================

print ""
print "======================================================="
print ""

print "Total:"
# print "is_prime_trial_division_1: " + str(is_prime_trial_division_1_time[0])
# print "is_prime_trial_division_2: " + str(is_prime_trial_division_2_time[0])
print "is_prime_trial_division_3: " + str(is_prime_trial_division_3_time[0])
print "is_prime_trial_division_4: " + str(is_prime_trial_division_4_time[0])
print "is_prime_trial_division_5: " + str(is_prime_trial_division_5_time[0])
print "is_prime_trial_division_6: " + str(is_prime_trial_division_6_time[0])

print ""

print "Average:"
# print "is_prime_trial_division_1: " + "{:.12f}".format(is_prime_trial_division_1_time[1])
# print "is_prime_trial_division_2: " + "{:.12f}".format(is_prime_trial_division_2_time[1])
print "is_prime_trial_division_3: " + "{:.12f}".format(is_prime_trial_division_3_time[1])
print "is_prime_trial_division_4: " + "{:.12f}".format(is_prime_trial_division_4_time[1])
print "is_prime_trial_division_5: " + "{:.12f}".format(is_prime_trial_division_5_time[1])
print "is_prime_trial_division_6: " + "{:.12f}".format(is_prime_trial_division_6_time[1])

print ""
print "======================================================="
print ""






