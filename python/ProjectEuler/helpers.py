"""
Helper functions.
"""

import math

def is_prime(n):
    """
    Primality test.
    If n is between 30,000,000 and 341,550,071,728,321 use Miller-Rabin
    algorithm, else use trial division.
    """

    def mr(n, _known_primes = [2, 3], _precision_for_huge_n=16, ):

        def _try_composite(a, d, n, s):
            if pow(a, d, n) == 1:
                return False
            for i in range(s):
                if pow(a, 2**i * d, n) == n-1:
                    return False
            return True # n  is definitely composite

        if n in _known_primes:
            return True
        if n in (0, 1):
            return False
        if any((n % p) == 0 for p in _known_primes):
            return False
        d, s = n - 1, 0
        while not d % 2:
            d, s = d >> 1, s + 1

        # Returns exact according to http://primes.utm.edu/prove/prove2_3.html
        if n < 1373653: 
            return not any(_try_composite(a, d, n, s) for a in (2, 3))
        if n < 25326001: 
            return not any(_try_composite(a, d, n, s) for a in (2, 3, 5))
        if n < 118670087467: 
            if n == 3215031751: 
                return False
            return not any(_try_composite(a, d, n, s) for a in (2, 3, 5, 7))
        if n < 2152302898747: 
            return not any(_try_composite(a, d, n, s) for a in (2, 3, 5, 7, 11))
        if n < 3474749660383: 
            return not any(_try_composite(a, d, n, s) for a in (2, 3, 5, 7, 11, 13))
        if n < 341550071728321: 
            return not any(_try_composite(a, d, n, s) for a in (2, 3, 5, 7, 11, 13, 17))
        # otherwise
        return not any(_try_composite(a, d, n, s) 
                       for a in _known_primes[:_precision_for_huge_n])

    def trial_division(n):
        if n < 2:
            return False
        if n in (2, 3):
            return True
        if n % 2 == 0 or n % 3 == 0:
            return False

        limit   = int(math.sqrt(n))
        divisor = 5

        while divisor <= limit:
            if n % divisor == 0 or n % (divisor + 2) == 0:
                return False
            divisor += 6

        return True

    if 30000000  < n < 341550071728321:
        return mr(n)
    else:
        return trial_division(n)