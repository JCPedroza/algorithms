"""
Recursive implementations of linear search algorithm.
"""

def linear_search1(lst, n):
    """
    Is n in lst? Creates a new list with each recursive case.
    """
    if lst:
        if lst[0] == n:
            return True
        return linear_search1(lst[1:], n)
    return False

def linear_search2(lst, n, idx=0):
    """
    Is n in lst? Doesn't create list copies, keeps track of 
    the index instead.
    """
    if idx >= len(lst):
        return False
    if lst[idx] == n:
        return True
    else:
        return linear_search2(lst, n, idx + 1)


# Some testing

test_list = [0, 4, 5, 9, 13, 18, 24, 55, 97]

assert linear_search1(test_list, 10) == False
assert linear_search1(test_list, 55) == True

assert linear_search2(test_list, 10) == False
assert linear_search2(test_list, 55) == True
