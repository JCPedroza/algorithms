import time

# ======================================================
#                 Timing Algorithms
# ======================================================

def clock(f, n, repetitions):
    """
    Measures running time of a function using time.clock().
    Returns a tuple with the total and the average time.
    """
    start = time.clock()
    for i in range(repetitions):
        f(n)
    total = time.clock() - start
    return (total, total / repetitions)

def clock_range(f, range_start, range_end):
    """
    Measures running time of a function using time.clock().
    Returns a tuple with the total and the average time.
    """
    start = time.clock()
    for i in range(range_start, range_end):
        f(i)
    total = time.clock() - start
    return (total, total / (range_end - range_start))