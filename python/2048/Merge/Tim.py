def merge(line, direction=1):
    """
    Helper function that merges a single row or column in 2048
    """

    # Create a new list from line with non-zero values.
    merged_line = [val for val in line if val][::direction]

    # Add up adjacent cells of same value.
    for idx in range(len(merged_line) - 1):
        if merged_line[idx] == merged_line[idx+1]:
            merged_line[idx], merged_line[idx+1] = merged_line[idx] * 2, 0

    # Create a merged list of non-zero values.
    merged_line = [val for val in merged_line if val]

    # Return merged list with 0s added if necessary.
    return merged_line + [0] * (len(line) - len(merged_line))