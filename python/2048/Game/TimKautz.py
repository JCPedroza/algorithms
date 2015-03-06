# http://www.codeskulptor.org/#user39_JfENODiAiDEEHXy.py

"""
Clone of 2048 game.
"""

#import poc_2048_gui
from random import choice, randint


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


def merge(line, direction=1):
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


class TwentyFortyEight:
    """
    Class to run the game logic.
    """

    def __init__(self, grid_height, grid_width):

        self._grid = []
        self._rows = grid_height
        self._cols = grid_width

        self.reset()


    def reset(self):
        """
        Reset the game so the grid is empty except for two
        initial tiles.
        """

        self._grid = [[0] * self._cols for dummy_row in range(self._rows)]
        self.new_tile()
        self.new_tile()


    def __str__(self):
        """
        Return a string representation of the grid for debugging.
        """

        return str(self._grid)


    def get_grid_height(self):
        """
        Get the height of the board.
        """

        return self._rows


    def get_grid_width(self):
        """
        Get the width of the board.
        """

        return self._cols


    def move(self, direction):
        """
        Move all tiles in the given direction and add
        a new tile if any tiles moved.
        """

        # Set up helper vars
        self._dir = OFFSETS[direction][0] or OFFSETS[direction][1]
        self._check = self._grid[:]

        # If direction is UP or DOWN convert columns into lists
        if direction in [UP, DOWN]:
            self._grid = [col for col in zip(*self._grid)]
        
        # For each list in the grid
        for idx, row in enumerate(self._grid):
            # Replace it with the merged list
            self._grid[idx] = merge(row, self._dir)[::self._dir]

        # If direction is UP or DOWN convert merged lists back to columns
        if direction in [UP, DOWN]:
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

        # Set up helper vars
        self._rand_r = randint(0, self._rows-1)
        self._rand_c = randint(0, self._cols-1)

        # Check if a tile has value 0 and set a new one
        if self.get_tile(self._rand_r, self._rand_c):
            self.new_tile()
        else:
            self.set_tile(self._rand_r, self._rand_c, choice([2] * 9 + [4]))


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
