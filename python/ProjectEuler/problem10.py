# This Python file uses the following encoding: utf-8

"""
projecteuler.net problem 10.

Summation of primes.

The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.
"""

from helpers import is_prime

LIMIT = 2000000


def solution():
    total = 0
    for num in range(LIMIT):
        if is_prime(num):
            total += num
    return total

print solution()
