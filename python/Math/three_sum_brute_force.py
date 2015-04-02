# ==================================================
#    The 3-Sum algorithm, brute force approach
# ==================================================

def three_sum_count(numberList):

    array_length = len(numberList)
    count = 0

    for i in range(0, array_length):
        for j in range(i + 1, array_length):
            for k in range(j + 1, array_length):
                if numberList[i] + numberList[j] + numberList[k] == 0:
                    count += 1;

    return count


# ==================================================
#                     Test Area
# ==================================================

list0 = [1, 2, 3, -3, -5]

print three_sum_count(list0)