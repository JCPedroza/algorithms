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

