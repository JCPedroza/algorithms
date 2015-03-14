import itertools

def permutations(sample_space, length):
    """
    Creates generatior object of permutations of sample_space of given length.
    """
    return itertools.permutations(sample_space, length)

