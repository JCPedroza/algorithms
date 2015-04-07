"""
Recursive implementations of a binary search algorithm.

Input list must be sorted.
"""

def binary_search1(lst, n):
    """" 
    Is n in lst? Creates a new list with each recursive case. 
    Assumes the input list is not empty.
    """
    if len(lst) == 1:
        return lst[0] == n;

    mid_index = len(lst) / 2
    mid_value = lst[mid_index]

    if mid_value == n:
        return True
    if mid_value > n:
        return binary_search1(lst[:mid_index], n)
    else:
        return binary_search1(lst[mid_index:], n)

def binary_search2(lst, left, right, n):
    """
    Is n in lst? Doesn't create list copies, instead keeps track
    of the left and right limit indexes.
    """
    if left > right:
        return False
    
    mid_index = (left + right) / 2
    
    if n == lst[mid_index]:
        return True
    if n < lst[mid_index]:
        return binary_search2(lst, left, mid_index - 1, n)
    else:
        return binary_search2(lst, mid_index + 1, right, n)


# Some testing

test_list = [1, 3, 5, 7, 9, 12, 15, 18, 22, 34, 55]

assert binary_search1(test_list, 11) == False
assert binary_search1(test_list, 5) == True

assert binary_search2(test_list, 0, len(test_list) - 1, 11) == False
assert binary_search2(test_list, 0, len(test_list) - 1, 5) == True