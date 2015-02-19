"""
Merge function for 2048 game, creating only one new list.
"""

def first_not_zero(line):
    """
    Returns the first non-zero value in a list.
    """
    for dummy_i in line:
        if dummy_i != 0:
            return dummy_i
        
    return False  # no non-zero values found

def merge(line):
    """
    Function that merges a single row or column in 2048.
    """
    return_list = []
    nextval = 0
    index = 0
    jump = False
    zeros = 0
    
    for dummy_i in line:
        if dummy_i == 0:
            index += 1
            zeros += 1
        else:
            if jump == False:
                nextval = first_not_zero(line[index+1:])
                if dummy_i == nextval:
                    return_list.append(dummy_i * 2)
                    zeros += 1
                    jump = True
                else:
                    return_list.append(dummy_i)
                index += 1
            else:
                index += 1
                jump = False
                
    for dummy_i in range(zeros):
        return_list.append(0)
            
    return return_list
