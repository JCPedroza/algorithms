"""
projecteuler.net problem 3.

Largest prime factor.

The prime factors of 13195 are 5, 7, 13 and 29.
What is the largest prime factor of the number 600851475143 ?
"""

from helpers import is_prime
from math import sqrt

THE_NUMBER = 600851475143;

def solution1(n):
    """
    Slow solution. Performs primarly test in a range and checks
    if it is a factor of n, divides n by it, and repeats until
    factor of n is 1.
    """
    current = n
    max_factor = 1

    while not is_prime(current) and current > 1:
        for number in range(int(sqrt(current))):
            if is_prime(number) and current % number == 0:
                current = current / number
                if number > max_factor:
                    max_factor = number

    return max_factor

def solution2(n):
    """
    Much faster solution. The primarly test is not necessary because
    for each k, if it is a factor of n then we divide n by k and completely 
    divide out each k before moving to the next k. It can be seen that
    when k is a factor it will necessarily be prime, as all smaller factors have 
    been removed, and the final result of this process will be n = 1.
    """
    if n % 2 == 0:
        last_factor = 2
        n = n / 2
        while n % 2 == 0:
            n = n / 2
    else:
        last_factor = 1

    factor = 3
    max_factor = sqrt(n)   # every number n can at most have one prime factor greater than sqrt(n)

    while n > 1 and factor <= max_factor:
        if n % factor == 0:
            n = n / factor
            last_factor = factor
            while n % factor == 0:
                n = n / factor
            max_factor = sqrt(n)

        factor = factor + 2   # 2 is the only even prime, so if we treat 2 separately 
                              # we can increase factor with 2 every step.

    if n == 1:
        return last_factor
    else:
        return n

    

print solution1(THE_NUMBER)
print solution2(THE_NUMBER)

