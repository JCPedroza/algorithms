"""
Merge function for 2048 game.
"""

def slide(line):
    """
    Slides all numbers to the left.
    """
    return_list = [0 for i in range(len(line))]
    available = 0
    for i in line:
        if i != 0:
            return_list[available] = i
            available += 1
    return return_list

def merge(line):
    """
    Function that merges a single row or column in 2048.
    """
    slide_list = slide(line)
    
    for i in range(len(slide_list) - 1):
        if slide_list[i] == slide_list[i + 1]:
            slide_list[i] *= 2
            slide_list[i + 1] = 0
            
    return slide(slide_list)