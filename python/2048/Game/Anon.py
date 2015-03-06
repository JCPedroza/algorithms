"""
Clone of 2048 game.
"""

import random

# Directions, DO NOT MODIFY
UP = 1
DOWN = 2
LEFT = 3
RIGHT = 4

def merge(line):
    """
    Helper function that merges a single row or column in 2048
    """
    ans = [0] * len(line)
    allow_merge = False
    idx = 0
    for num in line:
        if num:
            if allow_merge and num == ans[idx-1]:
                allow_merge = False
                ans[idx-1] *= 2
            else:
                allow_merge = True
                ans[idx] = num
                idx += 1
    return ans

class TwentyFortyEight:
    """
    Class to run the game logic.
    """

    def __init__(self, grid_height, grid_width):
        self._grid_height = grid_height
        self._grid_width = grid_width
        self._iter_order = {
            UP   :[[(row, col) for row in range(grid_height)] 
                               for col in range(grid_width)], 
            DOWN :[[(row, col) for row in range(grid_height-1, -1, -1)] 
                               for col in range(grid_width)], 
            LEFT :[[(row, col) for col in range(grid_width)] 
                               for row in range(grid_height)], 
            RIGHT:[[(row, col) for col in range(grid_width-1, -1, -1)] 
                               for row in range(grid_height)], 
        }
        self.reset()

    def reset(self):
        """
        Reset the game so the grid is empty except for two
        initial tiles.
        """
        self._grid = [[0 for dummy_col in range(self._grid_width)]
                         for dummy_row in range(self._grid_height)]
        self.new_tile()
        self.new_tile()

    def __str__(self):
        """
        Return a string representation of the grid for debugging.
        """
        return ('%5d' * self._grid_width + '\n') * self._grid_height \
                % tuple(num for row in self._grid for num in row)

    def get_grid_height(self):
        """
        Get the height of the board.
        """
        return self._grid_height

    def get_grid_width(self):
        """
        Get the width of the board.
        """
        return self._grid_width

    def move(self, direction):
        """
        Move all tiles in the given direction and add
        a new tile if any tiles moved.
        """
        moved = False
        for order in self._iter_order[direction]:
            line = self.get_tiles(order)
            merged_line = merge(line)
            self.set_tiles(order, merged_line)
            if not moved and merged_line != line:
                moved = True
        if moved:
            self.new_tile()

    def new_tile(self):
        """
        Create a new tile in a randomly selected empty
        square.  The tile should be 2 90% of the time and
        4 10% of the time.
        """
        empty_cells = [(row, col) for row in range(self._grid_height) 
                                  for col in range(self._grid_width) 
                                  if self.get_tile(row, col) == 0]
        if empty_cells:
            row, col = random.choice(empty_cells)
            value = 2 if random.random() < .9 else 4
            self.set_tile(row, col, value)
        

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
    
    def get_tiles(self, order):
        """
        Get tiles by given order
        """
        return [self.get_tile(row, col) for row, col in order]

    def set_tiles(self, order, tiles):
        """
        Set given tiles by given order
        """
        for (row, col), value in zip(order, tiles):
            self.set_tile(row, col, value)
