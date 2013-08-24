import random

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


# Counting only the numbers of comparisons made.
def bubble_sort_counter(alist):
    return_list = alist
    length = len(return_list) - 1
    is_sorted = False
    counter = 0
    # Will continue iterating until no swap is made, in that case
    # is_sorted = True and the sorted list is returned.
    while not is_sorted:
        is_sorted = True
        for e in range(length):
            # Counts iteration
            counter += 1
            if return_list[e] > return_list[e + 1]:
                # flag that there was a swap in the scan
                is_sorted = False
                # swap items
                return_list[e], return_list[e + 1] = return_list[e + 1], return_list[e]
                # Counts swap (should I be adding 2 instead of 1?)
    return counter

# Timing tests
list5000 = [random.randrange(0, 10) for e in range(5000)]
list10000 = [random.randrange(0, 10) for e in range(10000)]
# list30000 = [random.randrange(0, 10) for e in range(30000)]
# list50000 = [random.randrange(0, 10) for e in range(50000)]

print "5000: ", bubble_sort_counter(list5000)
print "10000: ", bubble_sort_counter(list10000)
# print "30000: ", bubble_sort_counter(list30000)
# print "50000: ", bubble_sort_counter(list50000)
