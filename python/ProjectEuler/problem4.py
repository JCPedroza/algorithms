# This Python file uses the following encoding: utf-8

"""
projecteuler.net problem 4.

Largest palindrome product.

A palindromic number reads the same both ways. The largest palindrome made 
from the product of two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.
"""

HIGH_LIMIT = 999
LOW_LIMIT = 100

def is_palindrome(n):
    """
    Checks if a number is a palindrome.
    """
    reverse = 0
    number = n

    while number > 0:
        reverse = 10 * reverse + (number % 10)
        number = number / 10

    return reverse == n

def largest_palindrome_product():
    """
    Finds the largest palindrome made from the product of two 3-digit numbers.
    """
    product = 0
    largest_palindrome = 0

    for a in range(HIGH_LIMIT, LOW_LIMIT-1, -1):
        for b in range(HIGH_LIMIT, a-1, -1):
            product = a * b
            if product <= largest_palindrome:
                break
            if is_palindrome(product):
                largest_palindrome = product

    return largest_palindrome

print largest_palindrome_product()