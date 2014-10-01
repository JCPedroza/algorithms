from math import *
import numpy as np

"""
Different ways to find the n fibonacci number.
"""

def fibR(n):
    """ Computes the n fibonacci number using recursion.
    f(0) = 0
    """
    if n < 2: 
        return n
    else:
        return fibR(n-1) + fibR(n-2) 

def fibTR(n):
    """ 
    Computes the n fibonacci number using tail recursion.
    f(0) = 0
    """
    def loop(n, acc, buff):
        if n < 1:
            return acc
        else:
            return loop(n-1, acc+buff, acc)
    return loop(n, 0, 1)

def fibFR(n):
    """ 
    Computes the n fibonacci number using for loop and range().
    f(0) = 0
    """
    acc  = 0
    last = 1
    for i in range(n):
        acc, last = last+acc, acc
    return acc

def fibFX(n):
    """ 
    Computes the n fibonacci number using for loop and xrange().
    f(0) = 0
    """
    acc  = 0
    last = 1
    for i in xrange(n):
        acc, last = last+acc, acc
    return acc

def fibFN(n):
    """ 
    Computes the n fibonacci number using for loop and numpy.arange().
    f(0) = 0
    """
    acc  = 0
    last = 1
    for i in np.arange(n):
        acc, last = last+acc, acc
    return acc

def fibAnalytic(n):
    """ 
    Computes the n fibonacci number using analytic approach.
    f(0) = 1, f(1) = 1, f(2) = 1, f(3) = 2
    """
    sqrt5 = sqrt(5)
    p = (1 + sqrt5) / 2
    q = 1/p
    return int( (p**n + q**n) / sqrt5 + 0.5 )

def fibMatrix(n):
    """
    Matrix-based computation of the n fibonacci number.
    f(0) = 1, f(1) = 1, f(2) = 2
    """
    def prevPowTwo(n):
        if ((n & -n) == n):
            return n
        else:
            n -= 1
            n |= n >> 1
            n |= n >> 2
            n |= n >> 4
            n |= n >> 8
            n |= n >> 16
            n += 1
            return (n/2)

    powTwo = prevPowTwo(n)
 
    q = r = i = 1
    s = 0
 
    while(i < powTwo):
        i *= 2
        q, r, s = q*q + r*r, r * (q + s), (r*r + s*s)
 
    while(i < n):
        i += 1
        q, r, s = q+r, q, r
 
    return q

def fibLSR(n, c={0:1, 1:1}):
    """
    Calculates the n fibonacci number using large step recurrence.
    f(0) = 1, f(1) = 1, f(2) = 2
    """
    if n not in c:
        x = n // 2
        c[n] = fibLSR(x-1) * fibLSR(n-x-1) + fibLSR(x) * fibLSR(n - x)
    return c[n]
