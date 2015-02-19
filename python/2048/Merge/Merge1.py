"""
Merge function for 2048 game.
"""

def slide(line):
    """
    Slides all numbers to the left.
    """
    return_list = [0 for dummy_i in range(len(line))]
    available = 0
    for dummy_i in line:
        if dummy_i != 0:
            return_list[available] = dummy_i
            available += 1
    return return_list

def merge(line):
    """
    Function that merges a single row or column in 2048.
    """
    slide_list = slide(line)
    
    for dummy_i in range(len(slide_list) - 1):
        if slide_list[dummy_i] == slide_list[dummy_i + 1]:
            slide_list[dummy_i] *= 2
            slide_list[dummy_i + 1] = 0
            
    return slide(slide_list)