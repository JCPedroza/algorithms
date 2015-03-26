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


# Measurement and plotting:

START = 1000
END = 1500
STRIDE = 1
REPEATS = 2

td_results = T.resource_runtime_plot(trial_division, START, END, STRIDE, REPEATS)
aks_results = T.resource_runtime_plot(aks, START, END, STRIDE, REPEATS)

print "average for trial division: ", td_results[2]
print "average for aks:            ", aks_results[2]

fig = plt.figure()
ax1 = fig.add_subplot(211)
ax1.plot(td_results[0], td_results[1], label="td")
ax2 = fig.add_subplot(212)
ax2.plot(aks_results[0], aks_results[1], label="aks")
plt.show()

