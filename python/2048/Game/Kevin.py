"""
Clone of 2048 game.
"""

import random

# Directions, DO NOT MODIFY
UP = 1
DOWN = 2
LEFT = 3
RIGHT = 4

def slide(line):
    """
    Function that slides the non-zero values to the left
    """
    
    # Iterate over the input and create an output list that
    # has all the non-zero titles slide over to the
    # beginning of the list with the appropriate number of
    # zeros at the end of the list.
    new_line = []
        
    for tile in line:
        if tile != 0:
            new_line.append(tile)
    
    if len(new_line) != len(line):
        zeroes = len(line) - len(new_line)
        for dummy_num in range(zeroes):
            new_line.append(0)
        
    return new_line

def merge(line):
    """
    Helper function that merges a single row or column in 2048
    """
    # Iterate the list created in the previous step and
    # create another new list in which pairs of tiles in the
    # first list are replaced with a tile of twice the
    # value and a zero tile
    
    new_line = slide(line)
    merged_line = []
    
    for idx, tile in enumerate(new_line):

        if idx != 0:
            if tile != 0:

                if tile == new_line[idx - 1]:
                    merged_line.append(tile*2) # double match
                    new_line[idx] = 0 # place zero in tile
                
                else:
                    merged_line.append(new_line[idx-1])

    if len(merged_line) != len(new_line):
        merged_idx = len(merged_line)
        for idx, tile in enumerate(new_line):
            if idx >= merged_idx:
                merged_line.append(tile)        
    
    merged_line = slide(merged_line)
    
    return merged_line

def transpose(grid):
    '''Helper function that transposes a matrix'''  
    return [[grid[j][i] for j in range(len(grid))] for i in range(len(grid[0]))]

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
        # initialize grid
        self._grid =  [ [0 for dummy_col in range(self.get_grid_width())] 
                          for dummy_row in range(self.get_grid_height())]
        self.new_tile()
        self.new_tile()
        
    def __str__(self):
        """
        Return a string representation of the grid for debugging.
        """        
        return '\n'.join(str(value) for value in self._grid)
    
    def get_grid(self):
        """
        Get the values of the board.
        """
        return self._grid
    
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
        merge_temp = []
        
        if direction == UP or direction == DOWN:
            # transpose the value matrix
            temp_grid_value = transpose(self.get_grid())
        else:
            temp_grid_value = self.get_grid()

        for line in temp_grid_value:
            if direction == DOWN or direction == RIGHT:
                # reverse the list so all sliding/merging goes toward index 0
                line = line[::-1]
                merged_line_temp = merge(line)
                # reverse the list back to the original direction
                merged_line_temp = merged_line_temp[::-1]
            else:
                # no need to reverse for UP and LEFT
                merged_line_temp = merge(line)
            
            merge_temp.append(merged_line_temp)

            
        if direction == UP or direction == DOWN:
            merge_temp = transpose(merge_temp)

        self._grid = merge_temp
        board_check = 0 #self.get_height() * self.get_width()
            
        for line in self.get_grid():
            for tile in line:
                if tile == 0:
                    board_check -= 1
                else:
                    board_check += 1
        
        if board_check < self.get_grid_height() * self.get_grid_width():
            self.new_tile()

    def new_tile(self):
        """
        Create a new tile in a randomly selected empty
        square.  The tile should be 2 90% of the time and
        4 10% of the time.
        """       
        
        row = random.randrange(0, self.get_grid_height() )
        col = random.randrange(0, self.get_grid_width() )
        
        while self.get_tile(row, col) != 0:
            row = random.randrange(0, self.get_grid_height() )
            col = random.randrange(0, self.get_grid_width() )
            
            # the below loop and break condition checks to see if
            # all the tiles on the board are occupied. If they are
            # the game will reset

        value = random.choice([2, 2, 2, 2, 2, 2, 2, 2, 2, 4])
        
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
