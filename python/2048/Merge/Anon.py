def merge(line):
    """
    Helper function that merges a single row or column in 2048
    """
    ans = [0] * len(line)
    allow_merge = False
    idx = 0
    for num in line:
        if num:
            if allow_merge and num == ans[idx-1]:
                allow_merge = False
                ans[idx-1] *= 2
            else:
                allow_merge = True
                ans[idx] = num
                idx += 1
    return ans