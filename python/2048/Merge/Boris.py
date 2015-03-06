def merge(line):
    """
    Helper function that merges a single row or column in 2048
    """
    helper = lambda xs: filter(lambda x: x, xs)
    result = helper(reduce(lambda a, b: a + [b]
               if a[-1] != b else a[:-1] + [a[-1] * 2, 0], helper(line), [0]))
    return result + [0] * (len(line) - len(result))