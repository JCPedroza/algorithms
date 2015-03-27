"""
projecteuler.net problem 5.

Smallest multiple.

2520 is the smallest number that can be divided by each of the numbers 
from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of 
the numbers from 1 to 20?
"""

def solution1():
    """
    Simple while loop. Numbers in strides of 20 are tested until
    one divisible by all the numbers in the range is found.
    This algorithm can take a while to reach the solution.
    """
    stride = 20
    current = 20
    result = 0

    while True:
        result = 0
        for n in xrange(2, 21):
            result += current % n
        if result == 0:
            return current
        current += stride


print solution1()

