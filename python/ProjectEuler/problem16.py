"""
projecteuler.net problem 16.

Power digit sum.

2^15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.
What is the sum of the digits of the number 2^1000?
"""


def solution():
    the_num = 2 ** 1000
    the_sum = 0

    while the_num > 0:
        result = divmod(the_num, 10)
        the_sum += result[1]
        the_num = result[0]

    return the_sum

print solution()
