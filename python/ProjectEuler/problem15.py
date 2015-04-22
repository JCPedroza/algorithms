# This python file uses the following encoding: UTF-8

"""
projecteuler.net problem 15.

Lattice paths.

Starting in the top left corner of a 2×2 grid, and only being able to move to the
right and down, there are exactly 6 routes to the bottom right corner.

(see image at https://projecteuler.net/problem=15)

How many such routes are there through a 20×20 grid?
"""

from math import factorial

# number of paths = the central binomial coefficients
# (2n)! / (n!^2)
print factorial(2*20) / (factorial(20) ** 2)
