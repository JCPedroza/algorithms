"""
Clone of 2048 game.
"""

import random

# Directions, DO NOT MODIFY
UP = 1
DOWN = 2
LEFT = 3
RIGHT = 4

# Offsets for computing tile indices in each direction.
# DO NOT MODIFY this dictionary.
OFFSETS = {UP: (1, 0),
           DOWN: (-1, 0),
           LEFT: (0, 1),
           RIGHT: (0, -1)}

def merge(line):
    """
    Helper function that merges a single row or column in 2048
    """
    num1 = 0
    num2 = 0    
    index = 0
    result_list = [0] * len(line)
    for num in line:
        if num != 0:
            if num1 == 0:
                num1 = num
            elif num2 == 0:
                num2 = num
        if num1 != 0 and num2 != 0:            
            if num1 == num2:
                result_list[index] = num1 + num2                
                num1 = 0                
            else:
                result_list[index] = num1                
                num1 = num2
            num2 = 0
            index += 1
    if num1 != 0:
        result_list[index] = num1    
    return result_list

class TwentyFortyEight:
    """
    Class to run the game logic.
    """

    def __init__(self, grid_height, grid_width):
        # replace with your code
        self._height = grid_height
        self._width = grid_width
        self._grid = []
        self.reset()        

    def reset(self):
        """
        Reset the game so the grid is empty except for two
        initial tiles.
        """
        self._grid = [[0 for dummy_col in range(self._width)] for dummy_row in range(self._height)]
        self.new_tile()
        self.new_tile()

    def __str__(self):
        """
        Return a string representation of the grid for debugging.
        """
        temp = ""
        for row in self._grid:
            temp += str(row) + "\n"
        return temp

    def get_grid_height(self):
        """
        Get the height of the board.
        """        
        return self._height

    def get_grid_width(self):
        """
        Get the width of the board.
        """        
        return self._width

    def move(self, direction):
        """
        Move all tiles in the given direction and add
        a new tile if any tiles moved.
        """   
        temp_grid = [row[:] for row in self._grid]
        if direction == UP or direction == DOWN:            
            for col in range(self._width):
                temp_pos = []
                temp_value = []
                for row in range(self._height)[::OFFSETS[direction][0]]:
                    temp_pos.append((row, col))
                    temp_value.append(self._grid[row][col])
                temp_value = merge(temp_value)
                for value in range(self._height):
                    self._grid[temp_pos[value][0]][temp_pos[value][1]] = temp_value[value]                
            
        elif direction == LEFT or direction == RIGHT:            
            for row in range(self._height):
                temp_pos = []
                temp_value = []
                for col in range(self._width)[::OFFSETS[direction][1]]:
                    temp_pos.append((row, col))
                    temp_value.append(self._grid[row][col])
                temp_value = merge(temp_value)
                for value in range(self._width):
                    self._grid[temp_pos[value][0]][temp_pos[value][1]] = temp_value[value]
        
        if temp_grid != self._grid:
            self.new_tile()
            
    def new_tile(self):
        """
        Create a new tile in a randomly selected empty
        square.  The tile should be 2 90% of the time and
        4 10% of the time.
        """        
        if random.random() > 0.1:
            value = 2
        else:
            value = 4            
        zeros = [(row, col)
                 for row in range(len(self._grid))
                 for col in range(len(self._grid[row]))
                 if self._grid[row][col] == 0]
        random_tile = random.choice(zeros)
        self.set_tile(random_tile[0], random_tile[1], value)        

    def set_tile(self, row, col, value):
        """
        Set the tile at position row, col to have the given value.
        """
        self._grid[row][col] = value

    def get_tile(self, row, col):
        """
        Return the value of the tile at position row, col.
        """        
        return self._grid[row][col]
