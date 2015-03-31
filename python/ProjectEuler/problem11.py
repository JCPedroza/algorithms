# This Python file uses the following encoding: utf-8

"""
projecteuler.net problem 11.

Largest product in a grid.

08 02 22 97 38 15 00 40 00 75 04 05 07 78 52 12 50 77 91 08
49 49 99 40 17 81 18 57 60 87 17 40 98 43 69 48 04 56 62 00
81 49 31 73 55 79 14 29 93 71 40 67 53 88 30 03 49 13 36 65
52 70 95 23 04 60 11 42 69 24 68 56 01 32 56 71 37 02 36 91
22 31 16 71 51 67 63 89 41 92 36 54 22 40 40 28 66 33 13 80
24 47 32 60 99 03 45 02 44 75 33 53 78 36 84 20 35 17 12 50
32 98 81 28 64 23 67 10 26 38 40 67 59 54 70 66 18 38 64 70
67 26 20 68 02 62 12 20 95 63 94 39 63 08 40 91 66 49 94 21
24 55 58 05 66 73 99 26 97 17 78 78 96 83 14 88 34 89 63 72
21 36 23 09 75 00 76 44 20 45 35 14 00 61 33 97 34 31 33 95
78 17 53 28 22 75 31 67 15 94 03 80 04 62 16 14 09 53 56 92
16 39 05 42 96 35 31 47 55 58 88 24 00 17 54 24 36 29 85 57
86 56 00 48 35 71 89 07 05 44 44 37 44 60 21 58 51 54 17 58
19 80 81 68 05 94 47 69 28 73 92 13 86 52 17 77 04 89 55 40
04 52 08 83 97 35 99 16 07 97 57 32 16 26 26 79 33 27 98 66
88 36 68 87 57 62 20 72 03 46 33 67 46 55 12 32 63 93 53 69
04 42 16 73 38 25 39 11 24 94 72 18 08 46 29 32 40 62 76 36
20 69 36 41 72 30 23 88 34 62 99 69 82 67 59 85 74 04 36 16
20 73 35 29 78 31 90 01 74 31 49 71 48 86 81 16 23 57 05 54
01 70 54 71 83 51 54 69 16 92 33 48 61 43 52 01 89 19 67 48

What is the greatest product of four adjacent numbers in the same 
direction (up, down, left, right, or diagonally) in the 20×20 grid?
"""

from operator import mul

UP = 1
DOWN = 2
LEFT = 3
RIGHT = 4
DOWNRIGHT = 5
UPLEFT = 6
DOWNLEFT = 7
UPRIGHT = 8
COLUMNS = 20
ROWS = 20
LAST_INDEX = COLUMNS * ROWS - 1

grid = ("08 02 22 97 38 15 00 40 00 75 04 05 07 78 52 12 50 77 91 08 "
        "49 49 99 40 17 81 18 57 60 87 17 40 98 43 69 48 04 56 62 00 "
        "81 49 31 73 55 79 14 29 93 71 40 67 53 88 30 03 49 13 36 65 "
        "52 70 95 23 04 60 11 42 69 24 68 56 01 32 56 71 37 02 36 91 "
        "22 31 16 71 51 67 63 89 41 92 36 54 22 40 40 28 66 33 13 80 "
        "24 47 32 60 99 03 45 02 44 75 33 53 78 36 84 20 35 17 12 50 "
        "32 98 81 28 64 23 67 10 26 38 40 67 59 54 70 66 18 38 64 70 "
        "67 26 20 68 02 62 12 20 95 63 94 39 63 08 40 91 66 49 94 21 "
        "24 55 58 05 66 73 99 26 97 17 78 78 96 83 14 88 34 89 63 72 "
        "21 36 23 09 75 00 76 44 20 45 35 14 00 61 33 97 34 31 33 95 "
        "78 17 53 28 22 75 31 67 15 94 03 80 04 62 16 14 09 53 56 92 "
        "16 39 05 42 96 35 31 47 55 58 88 24 00 17 54 24 36 29 85 57 "
        "86 56 00 48 35 71 89 07 05 44 44 37 44 60 21 58 51 54 17 58 "
        "19 80 81 68 05 94 47 69 28 73 92 13 86 52 17 77 04 89 55 40 "
        "04 52 08 83 97 35 99 16 07 97 57 32 16 26 26 79 33 27 98 66 "
        "88 36 68 87 57 62 20 72 03 46 33 67 46 55 12 32 63 93 53 69 "
        "04 42 16 73 38 25 39 11 24 94 72 18 08 46 29 32 40 62 76 36 "
        "20 69 36 41 72 30 23 88 34 62 99 69 82 67 59 85 74 04 36 16 "
        "20 73 35 29 78 31 90 01 74 31 49 71 48 86 81 16 23 57 05 54 "
        "01 70 54 71 83 51 54 69 16 92 33 48 61 43 52 01 89 19 67 48 ")

def get_num(index):
    """
    Get the number at the given string grid index.
    """
    return int(grid[3*index:3*index+2])

def get_horizontal(index, direction, quantity):
    """
    Get <quantity> number of items from index in the given horizontal
    direction.
    """
    items = [get_num(index)]
    count = 1

    if direction == RIGHT:
        index += 1
        while count < quantity and index % COLUMNS != 0:
            items.append(get_num(index))
            index += 1
            count += 1
    elif direction == LEFT:
        index -= 1
        while count < quantity and index % COLUMNS != COLUMNS - 1:
            items.append(get_num(index))
            index -= 1
            count += 1
     
    return items

def get_vertical(index, direction, quantity):
    """
    Get <quantity> number of items from index in the given vertical
    direction.
    """
    items = [get_num(index)]
    count = 1

    if direction == DOWN:
        index += COLUMNS
        while count < quantity and index <= LAST_INDEX:
            items.append(get_num(index))
            count += 1
            index += COLUMNS

    if direction == UP:
        index -= COLUMNS
        while count < quantity and index >= 0:
            items.append(get_num(index))
            count += 1
            index -= COLUMNS

    return items

def get_diagonal(index, direction, quantity):
    """
    Get <quantity> number of items from index in the given horizontal
    direction.
    """
    items = [get_num(index)]
    count = 1

    if direction == DOWNRIGHT:
        index += COLUMNS + 1
        while count < quantity and index % COLUMNS != 0 and index <= LAST_INDEX:
            items.append(get_num(index))
            count += 1
            index += COLUMNS + 1

    if direction == UPLEFT:
        index -= COLUMNS + 1
        while count < quantity and index >= 0 and (index + 1) % COLUMNS != 0:
            items.append(get_num(index))
            count += 1
            index -= COLUMNS + 1

    if direction == DOWNLEFT:
        index += COLUMNS - 1
        while count < quantity and index < LAST_INDEX and (index + 1) % COLUMNS != 0:
            items.append(get_num(index))
            count += 1
            index += COLUMNS - 1

    if direction == UPRIGHT:
        index -= COLUMNS - 1
        while count < quantity and index % COLUMNS != 0 and index >= 0:
            items.append(get_num(index))
            count += 1
            index -= COLUMNS - 1

    return items

def get_values(index, direction, quantity):
    if direction == LEFT or direction == RIGHT:
        return get_horizontal(index, direction, quantity)
    elif direction == UP or direction == DOWN:
        return get_horizontal(index, direction, quantity)
    else:
        return get_diagonal(index, direction, quantity)

def solution():
    max_product = 0

    for i in range(LAST_INDEX):
        for d in range(1, 9):
            values = get_values(i, d, 4)
            product = reduce(mul, values, 1)
            if product > max_product:
                max_product = product

    return max_product

print solution()

# assert get_product([1, 2, 3, 4]) == 24

# assert get_horizontal(12, RIGHT, 10) == [7, 78, 52, 12, 50, 77, 91, 8]
# assert get_horizontal(22, LEFT, 2) == [99, 49]
# assert get_horizontal(42, LEFT, 4) == [31, 49, 81]

# assert get_vertical(0, DOWN, 2) == [8, 49]
# assert get_vertical(300, DOWN, 6) == [88, 4, 20, 20, 1]
# assert get_vertical(20, UP, 3) == [49, 8]

# assert get_diagonal(0, DOWNRIGHT, 30) == [8, 49, 31, 23, 51, 3, 67, 20, 97, 45, 3, 
#         24, 44, 52, 26, 32, 40, 4, 5, 48]
# assert get_diagonal(18, DOWNRIGHT, 3) == [91, 0]
# assert get_diagonal(360, DOWNRIGHT, 3) == [20, 70]

# assert get_diagonal(399, UPLEFT, 30) == [48, 5, 4, 40, 32, 26, 52, 44, 24, 3, 45, 97, 
#         20, 67, 3, 51, 23, 31, 49, 8]
# assert get_diagonal(381, UPLEFT, 3) == [70, 20]
# assert get_diagonal(39, UPLEFT, 3) == [0, 91]

# assert get_diagonal(19, DOWNLEFT, 30) == [8, 62, 13, 37, 28, 84, 54, 63, 78, 35, 94, 55, 
#         7, 47, 35, 57, 73, 36, 73, 1]
# assert get_diagonal(1, DOWNLEFT, 3) == [2, 49]
# assert get_diagonal(379, DOWNLEFT, 3) == [54, 67]

# assert get_diagonal(397, UPRIGHT, 5) == [19, 5, 16]
# assert get_diagonal(397, UPRIGHT, 2) == [19, 5]
# assert get_diagonal(19, UPRIGHT, 2) == [8]
# assert get_diagonal(20, UPRIGHT, 4) == [49, 2]





