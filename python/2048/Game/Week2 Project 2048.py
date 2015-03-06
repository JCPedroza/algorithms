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
    Function that merges a single row or column in 2048.
    """
    merged_line = [0] * len(line)
    merge_idx = 0
    for value in line:
        if value:
            if not(merged_line[merge_idx]):
                merged_line[merge_idx] = value
            elif value == merged_line[merge_idx]:
                merged_line[merge_idx] *= 2
                merge_idx+=1
            else:
                merge_idx+=1
                merged_line[merge_idx] = value            
    return merged_line

class TwentyFortyEight:
    """
    Class to run the game logic.
    """

    def __init__(self, grid_height, grid_width):
        self._grid_height = grid_height
        self._grid_width = grid_width

        self._init_tiles = {UP: [[0, col] for col in range(grid_width)],
                           DOWN: [[grid_height - 1, col] for col in range(grid_width)],
                           LEFT: [[row, 0] for row in range(grid_height)],
                           RIGHT: [[row, grid_width -1] for row in range(grid_height)] }
        self.reset()
        
    def _get_empty(self):
        """
        Returns a list of the indexes of empty cells.
        """
        empty_cells = []
        row_i = 0
        column_i = 0

        for row in self._grid:
            column_i = 0
            for column in row:
                if column == 0:
                    empty_cells.append([row_i, column_i])
                column_i += 1
            row_i += 1

        return empty_cells
        
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

    def _get_line_values(self, init_tile, direction):
        """
        Returns the values of a line from an initial
        tile through a given direction.
        """
        values = []
        row_i = init_tile[0]
        column_i = init_tile[1]
        offset = OFFSETS[direction]
        iterations = self._grid_height + self._grid_width - len(self._init_tiles[direction])
        for dummy_i in range(iterations):
            values.append(self.get_tile(row_i, column_i))
            row_i += offset[0]
            column_i += offset[1]
        return values

    def _update_line(self, init_tile, new_line, direction):
        """
        Updates a given line with new values.
        Returns number of moves.
        """
        row_i = init_tile[0]
        column_i = init_tile[1]
        offset = OFFSETS[direction]
        moves = 0

        for value in new_line:
            old_value = self.get_tile(row_i, column_i)
            if old_value != value:
                moves += 1
            self.set_tile(row_i, column_i, value)
            row_i += offset[0]
            column_i += offset[1]

        return moves

    def move(self, direction):
        """
        Move all tiles in the given direction and add
        a new tile if any tiles moved.
        """
        init_tiles = self._init_tiles[direction]
        moves = 0
        for tile in init_tiles:
            merged_line = merge(self._get_line_values(tile, direction))
            moves += self._update_line(tile, merged_line, direction)
        if moves > 0:
            self.new_tile()
        
    def new_tile(self):
        """
        Create a new tile in a randomly selected empty
        square.  The tile should be 2 90% of the time and
        4 10% of the time.
        """
        empty_cells = self._get_empty()
        choice = random.choice(empty_cells)
        rng = random.randrange(10)
        if rng == 0:
            self._grid[choice[0]][choice[1]] = 4
        else:
            self._grid[choice[0]][choice[1]] = 2
        
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

