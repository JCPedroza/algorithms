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
    helper = lambda xs: filter(lambda x: x, xs)
    result = helper(reduce(lambda a, b: a + [b]
               if a[-1] != b else a[:-1] + [a[-1] * 2, 0], helper(line), [0]))
    return result + [0] * (len(line) - len(result))


class TwentyFortyEight:
    """
    Class to run the game logic.
    """

    def __init__(self, grid_height, grid_width):
        self._grid_height = grid_height
        self._grid_width = grid_width
        self.reset()

    def reset(self):
        """
        Reset the game so the grid is empty except for two
        initial tiles.
        """
        self._grid = [[0 for _ in range(self.get_grid_width())]
                        for _ in range(self.get_grid_height())]
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
        return self._grid_height

    def get_grid_width(self):
        """
        Get the width of the board.
        """
        return self._grid_width

    def _break_condition(self, cur_col, cur_row):
        """
        Helper function to check if we are outside our board
        borders.
        """
        if cur_col >= self.get_grid_width() or cur_row >= self.get_grid_height():
            return True
        if cur_col < 0 or cur_row < 0:
            return True
    
    def _iterate(self, row_idx, col_idx, direction):
        """
        Iterates over board according to the given conditions.
        """
        idx = 0
        while True:
            cur_row = row_idx + direction[0] * idx
            cur_col = col_idx + direction[1] * idx
            if self._break_condition(cur_col, cur_row):
                break
            idx += 1
            yield cur_row, cur_col, self.get_tile(cur_row, cur_col)

    def _copy(self, row_idx, col_idx, direction):
        """
        Copy row or column of the board.
        """
        return [tile for _, _, tile in
                self._iterate(row_idx, col_idx, direction)]

    def _insert(self, new_tiles, row_idx, col_idx, direction):
        """
        Insert vector into the board.
        """
        gen = self._iterate(row_idx, col_idx, direction)
        for tile in new_tiles:
            row, col, _ = gen.next()
            self.set_tile(row, col, tile)

    def _move(self, initial, direction):
        """
        Move given row or column according to the given condtition.
        """
        moved = False

        for row_idx, col_idx in initial:

            tmp_line = self._copy(row_idx, col_idx, direction)
            
            merged = merge(tmp_line)
            if merged != tmp_line:
                moved = True
                self._insert(merged, row_idx, col_idx, direction)

        return moved

    def move(self, direction):
        """
        Move all tiles in the given direction and add
        a new tile if any tiles moved.
        """
        if direction == UP:
            initial = [(0, col) for col in range(self.get_grid_width())]
        elif direction == DOWN:
            initial = [(self.get_grid_height() - 1, col)
                       for col in range(self.get_grid_width())]
        elif direction == LEFT:
            initial = [(row, 0) for row in range(self.get_grid_height())]
        elif direction == RIGHT:
            initial = [(row, self.get_grid_width() - 1)
                       for row in range(self.get_grid_height())]

        if self._move(initial, OFFSETS[direction]):
            self.new_tile()

    def new_tile(self):
        """
        Create a new tile in a randomly selected empty
        square.  The tile should be 2 90% of the time and
        4 10% of the time.
        """
        # retrieve the list of empty tiles
        free = []
        for row in range(self.get_grid_height()):
            for col in range(self.get_grid_width()):
                if self.get_tile(row, col) == 0:
                    free.append((row, col))

        if not free:
            return

        val = 4
        if random.random() <= 0.9:
            val = 2

        # randomly choose a free tile
        tmp = free[random.randrange(0, len(free))]
        self.set_tile(tmp[0], tmp[1], val)

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
