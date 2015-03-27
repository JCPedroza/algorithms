# This Python file uses the following encoding: utf-8

"""
projecteuler.net problem 6.

Sum square difference.

The sum of the squares of the first ten natural numbers is:
1^2 + 2^2 + ... + 10^2 = 385.

The square of the sum of the first ten natural numbers is:
(1 + 2 + ... + 10)^2 = 55^2 = 3025

Hence the difference between the sum of the squares of the first ten 
natural numbers and the square of the sum is 3025 − 385 = 2640.

Find the difference between the sum of the squares of the first one 
hundred natural numbers and the square of the sum.
"""

THE_LIMIT = 100

def solution1(limit):
    """
    Brue force solution. Loop, multiply, difference.
    """
    sum_of_squares = 0;
    square_of_sum = 0;

    for n in range(1, limit+1):
        sum_of_squares += n * n
        square_of_sum += n
    square_of_sum *= square_of_sum

    return square_of_sum - sum_of_squares

def solution2(limit):
    """
    Better solution using aritmetic sum formulas.
    0 + 1 + 2 + ... + n = 1/2(n + 1)n
    0^2 + 1^2 + ... + n^2 = ((2n + 1)(n + 1)n) / 6
    """
    the_sum = ((limit + 1) * limit) / 2
    square_of_sum = the_sum * the_sum
    sum_of_squares = ((2 * limit + 1) * (limit + 1) * limit) / 6
    return square_of_sum - sum_of_squares

print solution1(THE_LIMIT)
print solution2(THE_LIMIT)


