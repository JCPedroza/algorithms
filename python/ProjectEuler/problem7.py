"""
projecteuler.net problem 7.

10001st prime.

By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we 
can see that the 6th prime is 13.

What is the 10,001st prime number?
"""

from helpers import is_prime

def nth_prime1(n):
    """
    Loop through numbers and use trial division for primarly test, 
    keep count of which ones are prime, return the nth prime.
    """
    count = 0
    current = 1
    while count < n:
        current += 1
        if is_prime(current):
            count += 1
    return current

print nth_prime1(10001)