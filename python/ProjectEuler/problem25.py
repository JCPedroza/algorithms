"""
projecteuler.net problem 25.

1000-digit Fibonacci number.

What is the first term in the Fibonacci sequence to contain 1000 digits?
1 = 1, 2 = 1, 3 = 2, 4 = 3, 5 = 5, 6 = 8, 7 = 13
"""

import math

LIMIT = 1000


def digits(n):
    """ Returns the number of digits of a positive integer. """
    return int(math.log10(n)) + 1


def fibo():
    """
    Infinite generator for the Fibonacci sequence.
    Returns the tuple (value, sequence position)
    """
    a = 0
    b = 1
    count = 0
    while True:
        a, b = a + b, a
        count += 1
        yield a, count


def solution(limit):
    """
    Finds the first term in the Fibonacci sequence that contains
    <limit> digits.
    """
    for n in fibo():
        if digits(n[0]) >= limit:
            return n[1]


print solution(LIMIT)
