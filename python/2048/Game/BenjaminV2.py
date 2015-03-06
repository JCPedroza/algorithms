"""
Clone of 2048 game.
I went back and also pre-computed the grid entries for the merge 
lists in the __init__ in an attempt to make the move() method more 
run time efficient. So more overhead work done at __init__ to enable 
less work during actual game play. 
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
        self._height = grid_height
        self._width = grid_width
        self.reset()
        
        # Calculate initial tiles for lines for each move direction
        initial_tiles = {UP: [(0,col) for col in range(grid_width)],
                         DOWN: [(grid_height-1,col) for col in range(grid_width)],
                         LEFT: [(row,0) for row in range(grid_height)],
                         RIGHT: [(row, grid_width-1) for row in range(grid_height)]}

        # Set line lengths for each direction
        line_lengths = {UP: grid_height,
                        DOWN: grid_height,
                        LEFT: grid_width,
                        RIGHT: grid_width}
        
        # Initialize dictionary to store grid coordinates of lines for each move direction
        self._lines = {UP:[],
                       DOWN: [],
                       LEFT: [],
                       RIGHT: []}
        
        # Calculate grid coordinates for each move line and put into dictionary
        for direction in [UP, DOWN, LEFT, RIGHT]:
            for initial_tile in initial_tiles[direction]:
                line = [(initial_tile[0]+idx*OFFSETS[direction][0],
                          initial_tile[1]+idx*OFFSETS[direction][1])
                        for idx in range(line_lengths[direction])]
                self._lines[direction].append(line)
        
    def reset(self):
        """
        Reset the game so the grid is empty except for two
        initial tiles.
        """
        # Reset all tiles to 0
        self._grid = [[0 for dummy_col in range(self._width)]
                      for dummy_row in range(self._height)]
        
        # Create two new tiles
        self.new_tile()
        self.new_tile()

    def __str__(self):
        """
        Return a string representation of the grid for debugging.
        """
        string = ""
        for row in self._grid:
            string += str(row)+"\n"
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
        # Note: move() method references dictionary self._lines defined in self.__init__
        
        tiles_same = True
        for line in self._lines[direction]:
            # Create line from grid row or column depending on direction
            line_values = [self.get_tile(line[idx][0],line[idx][1]) for idx in range(len(line))]
            
            # Run merge function on line
            new_line_values = merge(line_values)
            
            # Check if any tiles changed
            tiles_same = tiles_same and (new_line_values == line_values)
            
            # Update row or column with values after tile merge
            for idx in range(len(line)):
                self.set_tile(line[idx][0], line[idx][1], new_line_values[idx])
 
        # If tiles changed, add a new tile
        if not tiles_same:
            self.new_tile()

    def new_tile(self):
        """
        Create a new tile in a randomly selected empty
        square.  The tile should be 2 90% of the time and
        4 10% of the time.
        """
        # Choose randomly from list representing probability distribution for new tile value
        random_tile_value = random.choice([2]*9 + [4])
        
        # Create list of empty tiles to choose from
        empty_tiles = [[row,col]
                       for col in range(self.get_grid_width()) 
                       for row in range(self.get_grid_height())
                       if not(self.get_tile(row,col))]
                    
        # If empty tile(s) exist, randomly assign one to the random tile value
        if empty_tiles:
            random_tile = random.choice(empty_tiles)
            self.set_tile(random_tile[0], random_tile[1], random_tile_value)

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

