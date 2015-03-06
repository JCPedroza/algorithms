def merge(line):
    """
    Function that merges a single row or column in 2048.
    """
    #creates a list with non-zero numbers
    new_line = []
    for item in line:
        if item > 0:
            new_line.append(item)
    
    #sets length of new list to match orignal list
    while len(new_line) != len(line):
        new_line.append(0)
    #if original list is single number, returns original list    
    if len(new_line) < 2:
        return new_line

    #checks created list for adjacent matching numbers and doubles first occurance
    #creates new list with double number and zero
    double_line = []
    for num in range(1, len(new_line)):
        if new_line[num] == new_line[num - 1]:
            double_line.append(new_line[num-1]*2)
            new_line[num] = 0
        else:
            double_line.append(new_line[num-1])
    
    #add non matching number to new list
    if new_line[-1] != new_line[-2]:
        double_line.append(new_line[-1])

    #new list of of non-zero numbers
    final_line = []
    for double in double_line:
        if double > 0:
            final_line.append(double)
   
    #match length of new list to original list
    while len(final_line) != len(line):
        final_line.append(0)    
    return final_line