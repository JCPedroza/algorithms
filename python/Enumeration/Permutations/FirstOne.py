def permutations(sample_space, length):
    """
    Generates set of permutations of sample_space of given length.
    """
    ans = set([()])
    for _ in range(length):
        temp = set()
        for seq in ans:
            for item in sample_space:
                if not item in seq:
                    new_seq = list(seq)
                    new_seq.append(item)
                    temp.add(tuple(new_seq))
        ans = temp
    return ans
