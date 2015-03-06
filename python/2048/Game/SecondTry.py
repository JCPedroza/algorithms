"""
2048 game.
"""

import random

class TwentyFortyEight:
    """
    Class to run the game logic.
    """

    def __init__(self, grid_height, grid_width):
        self._grid_height = grid_height
        self._grid_width = grid_width
        # Directions
        self._UP = 1
        self._DOWN = 2
        self._LEFT = 3
        self._RIGHT = 4
        # Offsets for computing tile indices in each direction.
        self._offsets = {self._UP: (1, 0), self._DOWN: (-1, 0), self._LEFT: (0, 1), self._RIGHT: (0, -1)}

        self.reset()

    def merge(self, line, direction=1):
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
        
    def reset(self):
        """
        Reset the game so the grid is empty except for two
        initial tiles.
        """
        self._grid = [[0 for dummy_c in range(self._grid_width)] 
                       for dummy_r in range(self._grid_height)]
        # Create X new tiles. Using a loop for flexibility
        for dummy_i in range(2):
            self.new_tile()
        
    def __str__(self):
        """
        Return a string representation of the grid for debugging.
        """
        return_str = "\n"
        for row in self._grid:
            return_str += str(row) + "\n"
        return return_str

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

        # Set up helper vars
        self._dir = self._offsets[direction][0] or self._offsets[direction][1]
        self._check = self._grid[:]

        # If direction is UP or DOWN convert columns into lists
        if direction in [self._UP, self._DOWN]:
            self._grid = [col for col in zip(*self._grid)]
        
        # For each list in the grid
        for idx, row in enumerate(self._grid):
            # Replace it with the merged list
            self._grid[idx] = self.merge(row, self._dir)[::self._dir]

        # If direction is UP or DOWN convert merged lists back to columns
        if direction in [self._UP, self._DOWN]:
            self._grid = [list(row) for row in zip(*self._grid)]

        # Check if the grid has changed and place a new tile
        if self._check != self._grid:
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

