# Extra resources:
# Video explanation: https://www.youtube.com/watch?v=kgBjXUE_Nwc
# (including bubble sort)

# Merge sort scales: input size x log input size : n * log n
# 1) Recursively sort first half of input array
# 2) Recursively sort second half of input array
# 3) Merge two sorted sublists into one
# remember base cases

# Pseudocode for Merge
# C = output [length = n]
# A = 1st sorted array (n/2)
# B = 2nd sorted array (n/2)
# i = 1 (counter for left)
# j = 1 (counter for right)
# for k = 1 to n
#     if A(i) < B(j)
#         C(k) = A(i)
#         i++
#     else
#         C(k) = B(j)
#         j++
# end
# (ignores end cases)

# Merge principle:
# Given two separate lists A and B ordered from least to greatest, construct a list
# C by repeatedly comparing the least value of A to the least value of B, removing the lesser value,
# and appending it onto C. When one list is exhausted, append the remaining items in the other list onto
# C in order. The list C is then also a sorted list:

# A = 1, 3
# B = 2, 4
# C =
# min(min(A), min(B)) = 1

# A = 3
# B = 2, 4
# C = 1
# min(min(A), min(B)) = 2

# A = 3
# B = 4
# C = 1, 2
# min(min(A), min(B)) = 3

# A =
# B = 4
# C = 1, 2, 3
# Now A is exhausted, so extend C with the remaining values from B:

# C = 1, 2, 3, 4

# The merge_sort function is simply a function that divides a list in half, sorts those two lists,
# and then merges those two lists together in the manner described above. The only catch is that because
# it is recursive, when it sorts the two sub-lists, it does so by passing them to itself! If you're having
# difficulty understanding the recursion here, I would suggest studying simpler problems first. But if
# you get the basics of recursion already, then all you have to realize is that a one-item list is already
# sorted. Merging two one-item lists generates a sorted two-item list; merging two two-item lists
# generates a sorted four-item list; and so on.

# Merge sort algorithm works like this:
# 1: divide a larg list in half
# 2: divide each smaller list in half until each small list consists only of one value
# 3: sort this single value with a neighboring single value list
# 4: merge these smaller, sorted lists into larger lists
# 5: sort each merged list
# 6: repeat steps 4 and 5 until the entire list is sorted

# Recursive function calls are just like regular functions there is nothing special about them. So when
# you return aList it goes back up one function call to whatever called merge_sort and continues executing.
# If aList has a length greater than one it goes and recurses. In your case that means it will call merge_sort
# on the left:
# left = merge_sort(left)
# And than on the right:
# right = merge_sort(right)
# And than executes:
# return list(merge(left, right))

# The downward descent of recursion ends when you get to lists of length 1. However, all of mergesort's actual sorting
# is done on the way up. For a simple example, here's an 8-element unsorted list:
# (8, 4, 7, 2, 1, 5, 3, 6)
# Step 1: separate: (8) (4) (7) (2) (1) (5) (3) (6). This is the deepest part of your recursion.
# Step 2: Go up 1 level in the recursion. Begin merging, first to lists of length 2. (4, 8) (2, 7) (1, 5) (3, 6).
# Step 3: Go up another level in recursion. Merge to lists of length 4. (2, 4, 7, 8) (1, 3, 5, 6).
# Step 4: Go up to the final level of recursion. The final list is (1, 2, 3, 4, 5, 6, 7, 8).
# def merge_sort
#      <split lists> # this is done on the way down
#      <merge_sort on left list>
#      <merge_sort on right list>
#      <merge lists together> # this is done on the way up
# Once the recursive calls end, you still have to do the <merge lists together> step. The function isn't returning
# when it finishes the recursive calls, rather it has to do another step (merging) first.

# -------------------------------------------------
# --------------- THE CODE ------------------------
# -------------------------------------------------


def merge_sort(alist):
    # Base case, returns the input list if it is of length 1 or 0
    if len(alist) <= 1:
        return alist
    # Divides the input list in two lists, left and right
    middle = len(alist) / 2
    left = alist[:middle]
    right = alist[middle:]
    # Divide each of the two sublists recursively until we have list sizes of length 1,
    # in which case the list itself is returned
    left = merge_sort(left)
    right = merge_sort(right)
    return list(merge(left, right))


def merge(left, right):
    result = []
    left_idx, right_idx = 0, 0
    while left_idx < len(left) and right_idx < len(right):
        if left[left_idx] <= right[right_idx]:
            result.append(left[left_idx])
            left_idx += 1
        else:
            result.append(right[right_idx])
            right_idx += 1
    if left:
        result.extend(left[left_idx:])
    if right:
        result.extend(right[right_idx:])
    return result

# -------------------------------------------------
# --------THE CODE WITH PRINT COMMENTS ------------
# -------------------------------------------------


def merge_sort_commented(alist):
    """ merge_sort with print statements """
    print ""
    print "+++++++++++++ MERGE SORT CALL ++++++++++++++++++"
    print "calling merge_sort with: ", alist
    if len(alist) <= 1:
        print "reached base case with: ", alist
        return alist
    middle = len(alist) / 2
    left = alist[:middle]
    right = alist[middle:]
    left = merge_sort_commented(left)
    right = merge_sort_commented(right)
    print "right is: ", right
    print "left is: ", left
    toreturn = list(merge_commented(left, right))
    print "merge_sort is returning: ", toreturn
    print "++++++++++++ END MERGE SORT CALL ++++++++++++++"
    print ""
    return toreturn


def merge_commented(left, right):
    """ merge with print statements """
    print ""
    print "    -------- MERGE CALL ----------"
    print "    calling merge with: ", left, right
    result = []
    left_idx, right_idx = 0, 0
    while left_idx < len(left) and right_idx < len(right):
        if left[left_idx] <= right[right_idx]:
            result.append(left[left_idx])
            left_idx += 1
        else:
            result.append(right[right_idx])
            right_idx += 1
    if left:
        result.extend(left[left_idx:])
    if right:
        result.extend(right[right_idx:])
    print "    returning: ", result
    print "    ------ END MERGE CALL --------"
    print ""
    return result

alist = [1, 2, 3, 4]

merge_sort_commented(alist)
