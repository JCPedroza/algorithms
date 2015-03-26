"""
projecteuler.net problem 1.

Multiples of 3 and 5.

If we list all the natural numbers below 10 that are multiples of 3 or 5, 
we get 3, 5, 6 and 9. The sum of these multiples is 23. Find the sum of
all the multiples of 3 or 5 below 1000.
"""

LIMIT = 1000

def is_multiple(n):
    """
    Helper function, returns True if n is multiple 
    of 3 or 5.
    """
    return n % 3 == 0 or n % 5 == 0

def solution1():
    """
    Solution that uses for loop and helper 
    function is_multiple.
    """
    total = 0
    for value in range(LIMIT):
        if is_multiple(value):
            total += value
    return total

def solution2():
    """
    One-liner solution that uses list comprehension, sum
    built-in function, and a lambda helper function.
    """
    return sum([v if (lambda x: x % 3 == 0 or x % 5 == 0)(v) else 0 for v in range(1000)])

print solution1()
print solution2()