# From codewa.rs/r/c0Rejw

# Write a function that returns all of the sublists of a list or Array.
# Your function should be pure; it cannot modify its input.

# Example:

# power([1,2,3]);
# => [[], [1], [2], [1, 2], [3], [1, 3], [2, 3], [1, 2, 3]]

# For more details see https://en.wikipedia.org/wiki/Power_set

def power_1(s):
    """ Computes all of the sublists of s """
    from itertools import combinations
    return [list(c) for i in range(len(s) + 1) for c in combinations(s, i)]

def power_2(s):
    """ Computes all of the sublists of s """
    r = set([(), tuple(s)])
    r.update(*(power_2(s[:i] + s[i+1:]) for i in xrange(len(s))))
    return r

def power_3(s):
    """ Computes all of the sublists of s """
    the_set = [[]]
    for num in s:
        the_set += [x+[num] for x in the_set]
    return the_set 

def power_4(s):
    """ Computes all of the sublists of s """
    result = [[]]
    for i in s:
        result.extend(list([subset + [i] for subset in result]))
    return result
