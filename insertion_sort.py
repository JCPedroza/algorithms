def insertion_sort(alist):
    return_list = alist
    for index in range(1, len(return_list)):
        value = return_list[index]
        i = index - 1
        while i >= 0:
            if value < return_list[i]:
                # Swap:
                return_list[i + 1] = return_list[i]
                return_list[i] = value
                i -= 1
            else:
                break
    return return_list


# Another implementation:
def InsertionSort(array):
    """Insertion sorting algorithm"""
    i = 0
    j = 0
    n = len(array)
    for j in range(n):
        key = array[j]
        i = j - 1
        while (i >= 0 and array[i] > key):
            array[i + 1] = array[i]
            i = i - 1
        array[i + 1] = key


# Another implementation:
def insertion_sort_bin(seq):
    for i in range(1, len(seq)):
        key = seq[i]
        # invariant: ``seq[:i]`` is sorted
        # find the least `low' such that ``seq[low]`` is not less then `key'.
        #   Binary search in sorted sequence ``seq[low:up]``:
        low, up = 0, i
        while up > low:
            middle = (low + up) // 2
            if seq[middle] < key:
                low = middle + 1
            else:
                up = middle
        # insert key at position ``low``
        seq[:] = seq[:low] + [key] + seq[low:i] + seq[i + 1:]


# TESTS:

list1 = [5, 4, 2, 3, 1]

insertion_sort_bin(list1)

print list1
