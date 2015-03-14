"""
Functions to enumerate sequences of outcomes.
Repetition of outcomes is allowed.
"""

def gen_all_sequences(outcomes, length):
    """
    Iterative function that enumerates the set of all sequences of
    outcomes of given length.
    """
    ans = set([()])
    for dummy_idx in range(length):
        temp = set()
        for seq in ans:
            for item in outcomes:
                new_seq = list(seq)        # create a new list from current item in ans
                new_seq.append(item)       # add the new item
                temp.add(tuple(new_seq))   # add the new list to temp
        ans = temp
    return ans


def gen_sorted_sequences(outcomes, length):
    """
    Function that creates all sorted sequences via gen_all_sequences.
    """    
    all_sequences = gen_all_sequences(outcomes, length)
    sorted_sequences = [tuple(sorted(sequence)) for sequence in all_sequences]
    return set(sorted_sequences)

