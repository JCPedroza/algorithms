import timeit
import time
import resource

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

def factorial_tail_recursive(n):
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
num     = 150

def performance(f, num):
    """
    Measures running time of a function using time.clock().
    """
    start = time.clock()
    for i in range(0, repeats): f(num)
    return time.clock() - start

def resource_performance(f, num):
    """
    Measures running time of a function using the resource module.
    Index 0 is user time, index 1 is system time.
    """
    start = resource.getrusage(resource.RUSAGE_SELF)
    for i in range(0, repeats): f(num)
    end   = resource.getrusage(resource.RUSAGE_SELF)
    return (end.ru_utime - start.ru_utime, 
            end.ru_stime - start.ru_stime)

print ""
print "==========================================================================="
print ""
print "Running time of different factorial algorithm implementations."
print "Uses timeit module, resource module, and a custom performance function."
print ""
print "Compute {0} factorial {1} times:".format(num, repeats)

timer1 = timeit.Timer("factorial_recursive(150)", "from __main__ import factorial_recursive")
print ""
print "factorial_recursive()"
print "timeit:          " + str(timer1.timeit(repeats))
print "custom:          " + str(performance(factorial_recursive, num))
factorial_recursive_resource = resource_performance(factorial_recursive, num)
print "resource user:   " + str(factorial_recursive_resource[0])
print "resource system: " + str(factorial_recursive_resource[1])

timer2 = timeit.Timer("factorial_tail_recursive(150)", "from __main__ import factorial_tail_recursive")
print ""
print "factorial_tail_recursive()"
print "timeit:          " + str(timer2.timeit(repeats))
print "custom:          " + str(performance(factorial_tail_recursive, num))
factorial_tail_recursive_resource = resource_performance(factorial_tail_recursive, num)
print "resource user:   " + str(factorial_tail_recursive_resource[0])
print "resource system: " + str(factorial_tail_recursive_resource[1])

timer3 = timeit.Timer("factorial_iter_w(150)", "from __main__ import factorial_iter_w")
print ""
print "factorial_iter_w()"
print "timeit:          " + str(timer3.timeit(repeats))
print "custom:          " + str(performance(factorial_iter_w, num))
factorial_iter_w_resource = resource_performance(factorial_iter_w, num)
print "resource user:   " + str(factorial_iter_w_resource[0])
print "resource system: " + str(factorial_iter_w_resource[1])

timer4 = timeit.Timer("factorial_iter_f(150)", "from __main__ import factorial_iter_f")
print ""
print "factorial_iter_f()"
print "timeit:          " + str(timer4.timeit(repeats))
print "custom:          " + str(performance(factorial_iter_f, num))
factorial_iter_f_resource = resource_performance(factorial_iter_f, num)
print "resource user:   " + str(factorial_iter_f_resource[0])
print "resource system: " + str(factorial_iter_f_resource[1])

print ""
print "==========================================================================="
print ""




