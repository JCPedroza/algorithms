import timeit
"""
Different implementations of a simple factorial algorithm.
To run this code: python factorial.py
"""
# ===============================
#        The Algorithms
# ===============================

def factorialRecursive(n):
    """ Computes factorial of n using recursion. """
    if n < 1: return 1
    else:     return n * factorialRecursive(n - 1)

def factorialTailRecursive(n):
    """ # Computes factorial of n using tail recursion. """
    def recursion(n, acc):
        if n < 1: return acc
        else:     return recursion(n - 1, acc * n)
    return recursion(n, 1)

def factorialIterW(n):
    """ Computes factorial of n using iteration and while loop. """
    acc = 1
    while n > 1:
        acc *= n
        n   -= 1
    return acc

def factorialIterF(n):
    """ Computes factorial of n using iteration and for loop. """
    acc = 1
    for i in range(1, n + 1): 
        acc *= i
    return acc

# ===============================
#    Timing the Algorithms
# ===============================

repeats = 5000

print ""
print "==========================================================================="
print ""
print "Running time of different factorial algorithm implementations,"
print "in wall clock seconds, not CPU time."
print ""
print "Compute 150 factorial {0} times:".format(repeats)

timer1 = timeit.Timer("factorialRecursive(150)", "from __main__ import factorialRecursive")
print ""
print "factorialRecursive()"
print timer1.timeit(repeats)

timer2 = timeit.Timer("factorialTailRecursive(150)", "from __main__ import factorialTailRecursive")
print ""
print "factorialTailRecursive()"
print timer2.timeit(repeats)

timer3 = timeit.Timer("factorialIterW(150)", "from __main__ import factorialIterW")
print ""
print "factorialIterW()"
print timer3.timeit(repeats)

timer4 = timeit.Timer("factorialIterF(150)", "from __main__ import factorialIterF")
print ""
print "factorialIterF()"
print timer4.timeit(repeats)

print ""
print "==========================================================================="
print ""



