def bubble_sort(alist):
    return_list = alist
    length = len(return_list) - 1
    is_sorted = False
    # Will continue iterating until no swap is made, in that case
    # is_sorted = True and the sorted list is returned.
    while not is_sorted:
        is_sorted = True
        for e in range(length):
            if return_list[e] > return_list[e + 1]:
                # flag that there was a swap in the scan
                is_sorted = False
                # swap items
                return_list[e], return_list[e + 1] = return_list[e + 1], return_list[e]
    return return_list

print bubble_sort([7, 3, 4, 8, 2, 1, 9, 6, 5, 10])
