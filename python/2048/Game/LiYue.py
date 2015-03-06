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
    # new line is a list that contains the same number of 0's as the length of the line argument
    new_line = [0] * len(line)
    
    # index is the index of new line
    index = 0
    
    # Iterate over the line
    for tile in line:
        # if tile is non-zero
        if tile:
            if not (new_line[index]):
                new_line[index] = tile
            elif new_line[index] - tile:
                index += 1
                new_line[index] = tile
            else:
                new_line[index] += tile
                index += 1
                
    return new_line

class TwentyFortyEight:
    """
    Class to run the game logic.
    """
    def __init__(self, grid_height, grid_width):
        self._height = grid_height
        self._width = grid_width
        self._board = [[0 for col in range(self._width)]
                          for row in range(self._height)]
        self._start_cells = {UP: [(0, col) for col in range(self._width)],
                           DOWN: [(self._height - 1, col) for col in range(self._width)],
                           LEFT: [(row, 0) for row in range(self._height)],
                          RIGHT: [(row, self._width - 1) for row in range(self._height)]}
        self.reset()


    def reset(self):
        """
        Reset the game so the grid is empty except for two
        initial tiles.
        """
        # reset the grid board
        for row in range(self._height):
            for col in range(self._width):
                self._board[row][col] = 0
        # add two initial tiles      
        self.new_tile()
        self.new_tile()

    def __str__(self):
        """
        Return a string representation of the grid for debugging.
        """
        # a string representation of the grid
        string = ''
        for row in self._board:
            string += "[%s]\n" %', '.join(map(str, row))
        
        return string

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
        # initial the max steps
        num_steps = (direction <= DOWN) and self._height or self._width
                
        for start_cell in self._start_cells[direction]:
            position = []
            tiles= []
            # initial a line
            for step in range(num_steps):                
                row = start_cell[0] + step * OFFSETS[direction][0]
                col = start_cell[1] + step * OFFSETS[direction][1]
                position.append((row, col))
                tiles.append(self.get_tile(row, col))

            # merge a line
            tiles = merge(tiles)
         
            # updata a line
            for pos, tile in zip(position, tiles):
                self.set_tile(pos[0], pos[1], tile)
                
        # add new tile  
        if not self.is_full():
            self.new_tile()                
    
    def is_full(self):
        """
        return Ture if board is full, else False
        """
        return all(tile for row in self._board for tile in row)

    def new_tile(self):
        """
        Create a new tile in a randomly selected empty
        square.  The tile should be 2 90% of the time and
        4 10% of the time.
        """
        
        while True:
            row = random.choice(range(self._height))
            col = random.choice(range(self._width))
            # if tile is empty, set new tile
            if not (self.get_tile(row, col)):
                self.set_tile(row, col, random.choice([2]*9 + [4]))
                break


    def set_tile(self, row, col, value):
        """
        Set the tile at position row, col to have the given value.
        """
        self._board[row][col] = value

    def get_tile(self, row, col):
        """
        Return the value of the tile at position row, col.
        """
        return self._board[row][col]
