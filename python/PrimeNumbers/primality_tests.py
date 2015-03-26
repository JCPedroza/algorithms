"""
Prime test algorithms.
"""

import math, sys
import matplotlib.pyplot as plt
sys.path.append('../')
import Timeutils as T

def trial_division(n):
    """
    Prime test using trial division:
    http://en.wikipedia.org/wiki/Trial_division
    """

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

def aks(n):
    """
    Prime test using aks:
    http://en.wikipedia.org/wiki/AKS_primality_test
    """
    def expand_x_1(n):
        ex = [1]
        for i in range(n):
            ex.append(ex[-1] * -(n-i) / (i+1))
        return ex[::-1]

    if n < 2:
        return False
    ex = expand_x_1(n)
    ex[0] += 1
    return not any(mult % n for mult in ex[0:-1])

def mr(n, _known_primes = [2, 3], _precision_for_huge_n=16, ):
    """
    Miller-Rabin primality test:
    http://en.wikipedia.org/wiki/Miller%E2%80%93Rabin_primality_test
    Deterministic bellow 341550071728321.
    """

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
 

# Measurement and plotting:

START = 30000000
END = 30002000
STRIDE = 1
REPEATS = 1

td_results = T.resource_runtime_plot(trial_division, START, END, STRIDE, REPEATS)
# aks_results = T.resource_runtime_plot(aks, START, END, STRIDE, REPEATS)
mr_results = T.resource_runtime_plot(mr, START, END, STRIDE, REPEATS)

print "average for trial division: ", td_results[2]
# print "average for aks:            ", aks_results[2]
print "average for mr:             ", mr_results[2]

# fig = plt.figure()
# ax1 = fig.add_subplot(211)
# ax1.plot(td_results[0], td_results[1], label="td")
# ax2 = fig.add_subplot(212)
# ax2.plot(aks_results[0], aks_results[1], label="aks")
# ax3 = fig.add_subplot(212)
# ax3.plot(mr_results[0], mr_results[1], label="mr")
# plt.show()

plt.plot(td_results[0], td_results[1], "b-", label="td")
plt.plot(mr_results[0], mr_results[1], "r-", label="mr")
plt.legend()
plt.show()


