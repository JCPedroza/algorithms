# This Python file uses the following encoding: utf-8

"""
projecteuler.net problem 9.

Special Pythagorean triplet.

A Pythagorean triplet is a set of three natural numbers, a < b < c, for which a^2 + b^2 = c^2.

For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.
"""

TOTAL = 1000


def solution():
    for a in range(3, (TOTAL - 3) / 3):
        for b in range(a + 1, (TOTAL - 1 - a) / 2):
            c = TOTAL - a - b
            if c * c == a * a + b * b:
                return a * b * c
    return -1

print solution()
