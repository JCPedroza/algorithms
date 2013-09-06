# ----------------------------------------------------------------
# Measurement of running time difference between recursion
# and iteration in Python.
#
# To use this code from the command line:
# python recursion_vs_iteration.py number_of_tests test_depth
# For example, to make 100 tests with 200 recursion and 
# iteration depth:
# python recursion_vs_iteration.py 100 200
# That will print the total and average time of the test.
#
# To use this code from interpreter:
# Change the values of number_of_tests and test_depth variables,
# then run.
# ----------------------------------------------------------------

import time
import sys

# Increments the stack depth allowed. Need this to make deep recursion tests.
sys.setrecursionlimit(50000)

# ========================
# Defining the functions:
# ========================

def iteration(depth):
    for i in range(depth):
        pass
    return True


def recursion(depth):
    if depth == 0:
        return True
    else:
        depth -= 1
        return recursion(depth)

# ========================
# Testing:
# ========================

number_of_tests = int(sys.argv[1])
test_depth = int(sys.argv[2])

iteration_start = time.time()
for e in range(number_of_tests):
    iteration(test_depth)
iteration_total = time.time() - iteration_start
iteration_average = iteration_total / number_of_tests

recursion_start = time.time()
for e in range(number_of_tests):
    recursion(test_depth)
recursion_total = time.time() - recursion_start
recursion_average = recursion_total / number_of_tests

# ========================
# Prints:
# ========================

print ""
print "Results for {0} tests with {1} depth, in seconds: ".format(number_of_tests, test_depth)
print ""

print "Iteration: total = {0} average = {1}".format(iteration_total, iteration_average)
print "Recursion: total = {0} average = {1}".format(recursion_total, recursion_average)
print ""