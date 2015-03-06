def merge(line):
    """
    Helper function that merges a single row or column in 2048
    """
    merged_line = [0] * len(line)
    merge_idx = 0
    for value in line:
        if value:
            if not(merged_line[merge_idx]):
                merged_line[merge_idx] = value
            elif value == merged_line[merge_idx]:
                merged_line[merge_idx] *= 2
                merge_idx+=1
            else:
                merge_idx+=1
                merged_line[merge_idx] = value            
    return merged_line   