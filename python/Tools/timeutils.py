"""
Utilities for running time measurement.
"""

import time, resource, random

def runtime(f, num, repeats):
    """
    Measures running time of a function using time.clock().
    """
    start = time.clock()
    for i in xrange(repeats): 
        f(num)
    end = time.clock()
    return end - start

def runtime_range(f, init, end, repeats):
    """
    Measures running time of a function using time.clock().
    The input of the function is incremented on each iteration.
    """
    start = time.clock()
    for i in xrange(repeats): 
        for j in xrange(init, end):
            f(j)
    end = time.clock()
    return end - start

def resource_runtime(f, num, repeats):
    """
    Measures running time of a function using the resource module.
    Index 0 is user time, index 1 is system time.
    """
    start = resource.getrusage(resource.RUSAGE_SELF)
    for i in xrange(repeats): 
        f(num)
    end   = resource.getrusage(resource.RUSAGE_SELF)
    return (end.ru_utime - start.ru_utime, 
            end.ru_stime - start.ru_stime)

def resource_runtime_range(f, init, end, repeats):
    """
    Measures running time of a function using the resource module.
    Index 0 is user time, index 1 is system time.
    The input of the function is incremented on each iteration.
    """
    start = resource.getrusage(resource.RUSAGE_SELF)
    for i in xrange(repeats):
        for j in xrange(init, end):
            f(j)
    end   = resource.getrusage(resource.RUSAGE_SELF)
    return (end.ru_utime - start.ru_utime,
            end.ru_stime - start.ru_stime)

def resource_runtime_plot(f, start, end, stride, repeats, verbose=False):
    """
    Measures running time of a function using the resource module.
    The function is run with all the integer values in the given range
    (start and end), this is repeated n (repeats)times.
    Returns the tuple (arguments, results, average), a result is the average
    runtime for that argument, and average is the total average time for all
    arguments.
    """
    arguments = range(start, end, stride)
    results = [0 for i in arguments]
    mult = 1.0 / repeats
    average = 0  
    
    if verbose:
        print "\nmasuring function ", f.__name__
    for j in xrange(repeats):
        if verbose:
            print "\nstarting repeat {0} of {1}".format(j, repeats)
        for i in xrange(len(arguments)):
            if verbose:
                print "measuring function for argument", arguments[i]
            start = resource.getrusage(resource.RUSAGE_SELF)
            f(arguments[i])
            end = resource.getrusage(resource.RUSAGE_SELF)
            time = (end.ru_utime - start.ru_utime) * mult
            results[i] += time
            average += time

    return arguments, results, average



# Working with iterables

def create_lists(count, size):
    """
    Returns a list of lists, count is the number of lists, and size is the length
    of the lists.
    """
    return_list = []
    for i in range(count):
        return_list.append([random.randrange(2) for j in range(size)])
    return return_list

def runtime_lists(f, iterables):
    """
    Measures running time of a function using time.clock().
    Returns the tuple (total, average).
    The iterable parameter is a list of iterables.
    The function will be called with every iterable in iterables as argument.
    """
    start = time.clock()
    for i in iterables:
        f(i)
    end = time.clock()
    total = end - start
    return (total, total / len(iterables))

