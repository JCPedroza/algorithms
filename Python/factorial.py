import timeit
"""
Different implementations of a simple factorial algorithm.
To run this code: python factorial.py
"""
# ===============================
#        The Algorithms
# ===============================

def factorial_recursive(n):
    """ Computes factorial of n using recursion. """
    if n < 1: return 1
    else:     return n * factorial_recursive(n - 1)

def factorial_tail_resursive(n):
    """ Computes factorial of n using tail recursion. """
    def recursion(n, acc):
        if n < 1: return acc
        else:     return recursion(n - 1, acc * n)
    return recursion(n, 1)

def factorial_iter_w(n):
    """ Computes factorial of n using iteration and while loop. """
    acc = 1
    while n > 1:
        acc *= n
        n   -= 1
    return acc

def factorial_iter_f(n):
    """ Computes factorial of n using iteration and for loop. """
    acc = 1
    for i in range(1, n + 1): 
        acc *= i
    return acc

# ===============================
#    Timing the Algorithms
# ===============================

repeats = 5000

def time_timeit():
    print ""
    print "==========================================================================="
    print ""
    print "Running time of different factorial algorithm implementations,"
    print "in wall clock seconds, not CPU time."
    print ""
    print "Compute 150 factorial {0} times:".format(repeats)

    timer1 = timeit.Timer("factorial_recursive(150)", "from __main__ import factorial_recursive")
    print ""
    print "factorial_recursive()"
    print timer1.timeit(repeats)

    timer2 = timeit.Timer("factorial_tail_resursive(150)", "from __main__ import factorial_tail_resursive")
    print ""
    print "factorial_tail_resursive()"
    print timer2.timeit(repeats)

    timer3 = timeit.Timer("factorial_iter_w(150)", "from __main__ import factorial_iter_w")
    print ""
    print "factorial_iter_w()"
    print timer3.timeit(repeats)

    timer4 = timeit.Timer("factorial_iter_f(150)", "from __main__ import factorial_iter_f")
    print ""
    print "factorial_iter_f()"
    print timer4.timeit(repeats)

    print ""
    print "==========================================================================="
    print ""

time_timeit()


