def merge(line):
    """
    Helper function that merges a single row or column in 2048
    """
    # new line is a list that contains the same number of 0's as the length of the line argument
    new_line = [0] * len(line)
    
    # index is the index of new line
    index = 0
    
    # Iterate over the line
    for tile in line:
        # if tile is non-zero
        if tile:
            if not (new_line[index]):
                new_line[index] = tile
            elif new_line[index] - tile:
                index += 1
                new_line[index] = tile
            else:
                new_line[index] += tile
                index += 1
                
    return new_line