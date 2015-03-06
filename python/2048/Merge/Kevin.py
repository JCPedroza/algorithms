def slide(line):
    """
    Function that slides the non-zero values to the left
    """
    
    # Iterate over the input and create an output list that
    # has all the non-zero titles slide over to the
    # beginning of the list with the appropriate number of
    # zeros at the end of the list.
    new_line = []
        
    for tile in line:
        if tile != 0:
            new_line.append(tile)
    
    if len(new_line) != len(line):
        zeroes = len(line) - len(new_line)
        for dummy_num in range(zeroes):
            new_line.append(0)
        
    return new_line

def merge(line):
    """
    Helper function that merges a single row or column in 2048
    """
    # Iterate the list created in the previous step and
    # create another new list in which pairs of tiles in the
    # first list are replaced with a tile of twice the
    # value and a zero tile
    
    new_line = slide(line)
    merged_line = []
    
    for idx, tile in enumerate(new_line):

        if idx != 0:
            if tile != 0:

                if tile == new_line[idx - 1]:
                    merged_line.append(tile*2) # double match
                    new_line[idx] = 0 # place zero in tile
                
                else:
                    merged_line.append(new_line[idx-1])

    if len(merged_line) != len(new_line):
        merged_idx = len(merged_line)
        for idx, tile in enumerate(new_line):
            if idx >= merged_idx:
                merged_line.append(tile)        
    
    merged_line = slide(merged_line)
    
    return merged_line