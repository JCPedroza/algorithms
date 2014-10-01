import time
import resource

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
