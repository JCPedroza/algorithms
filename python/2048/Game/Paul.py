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
    #creates a list with non-zero numbers
    new_line = []
    for item in line:
        if item > 0:
            new_line.append(item)
    
    #sets length of new list to match orignal list
    while len(new_line) != len(line):
        new_line.append(0)
    #if original list is single number, returns original list    
    if len(new_line) < 2:
        return new_line

    #checks created list for adjacent matching numbers and doubles first occurance
    #creates new list with double number and zero
    double_line = []
    for num in range(1, len(new_line)):
        if new_line[num] == new_line[num - 1]:
            double_line.append(new_line[num-1]*2)
            new_line[num] = 0
        else:
            double_line.append(new_line[num-1])
    
    #add non matching number to new list
    if new_line[-1] != new_line[-2]:
        double_line.append(new_line[-1])

    #new list of of non-zero numbers
    final_line = []
    for double in double_line:
        if double > 0:
            final_line.append(double)
   
    #match length of new list to original list
    while len(final_line) != len(line):
        final_line.append(0)    
    return final_line


def traverse_grid(start_cell, direction, num_steps):
    """
    Function that iterates through the cells in a grid
    in a linear direction
    
    Both start_cell is a tuple(row, col) denoting the
    starting cell
    
    direction is a tuple that contains difference between
    consecutive cells in the traversal
    """
    dum_list = []
    for step in range(num_steps):
        row = start_cell[0] + step * direction[0]
        col = start_cell[1] + step * direction[1]
        ind = (row, col)
        dum_list.append(ind)
    return dum_list



        
class TwentyFortyEight:
    """
    Class to run the game logic.
    """

    def __init__(self, grid_height, grid_width):
        # replace with your code
        self._grid_height = grid_height
        self._grid_width = grid_width
        self.reset()
        self._up_dir = traverse_grid((0, 0), (0, 1), grid_width)
        self._down_dir = traverse_grid((grid_height-1, 0), (0, 1), grid_width)
        self._left_dir = traverse_grid((0, 0), (1, 0), grid_height)
        self._right_dir = traverse_grid((0, grid_width-1), (1, 0), grid_height)
        self._movements = {UP: self._up_dir, DOWN: self._down_dir, LEFT: self._left_dir, RIGHT: self._right_dir}

    def reset(self):
        """
        Reset the game so the grid is empty except for two
        initial tiles.
        """
        self._grid = []
        self._grid = [ [0 for dummy_col in range(self._grid_width)] for dummy_row in range(self._grid_height)]
        
        self.new_tile()
        self.new_tile()
        
    def __str__(self):
        """
        Return a string representation of the grid for debugging.
        """
        return "The game board is " + str(self._grid_width) + "by" + str(self._grid_height)

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

    
    def traverse_grid2(self, start_cell, direction, num_steps):
        """
    Function that iterates through the cells in a grid
    in a linear direction creating list of values

    Both start_cell is a tuple(row, col) denoting the
    starting cell

    direction is a tuple that contains difference between
    consecutive cells in the traversal
    """
        n2_list = []
        for step in range(num_steps):
            row_b = start_cell[0] + step * direction[0]
            col_b = start_cell[1] + step * direction[1]             
            n2_list.append(self._grid[row_b][col_b])
        return n2_list


    def traverse_grid3(self, start_cell, direction, num_steps):
        """
    Function that iterates through the cells in a grid
    in a linear direction and sets new value into grid

    Both start_cell is a tuple(row, col) denoting the
    starting cell

    direction is a tuple that contains difference between
    consecutive cells in the traversal
    """
        n3_list = []
        for step in range(num_steps):
            row_c = start_cell[0] + step * direction[0]
            col_c = start_cell[1] + step * direction[1]
            self.set_tile(row_c, col_c, self._merged[step])
            
        return n3_list
      
    def move(self, direction):
        """
        Move all tiles in the given direction and add
        a new tile if any tiles moved.
        """
        self._direction = direction
        grid2 = []
        for item in self._grid:
            grid2.append(list(item))
        
        
        if direction == UP:
            for direction in self._movements[direction]:
                #print 'direction = ', direction
                new_list = []
                new_list.append(direction)
                #print 'new_list = ',  new_list

                val_list = self.traverse_grid2(direction, OFFSETS[UP], self._grid_height)
                self._merged = merge(val_list)
                #print 'merged =', merged
                self.traverse_grid3(direction, OFFSETS[UP], self._grid_height)
        
        elif direction == DOWN:
            for direction in self._movements[direction]:
                #print 'direction = ', direction
                new_list = []
                new_list.append(direction)
                #print 'new_list = ',  new_list

                val_list = self.traverse_grid2(direction, OFFSETS[DOWN], self._grid_height)
                self._merged = merge(val_list)
                #print 'merged =', merged
                self.traverse_grid3(direction, OFFSETS[DOWN], self._grid_height)
        
        elif direction == LEFT:
            for direction in self._movements[direction]:
                #print 'direction = ', direction
                new_list = []
                new_list.append(direction)
                #print 'new_list = ',  new_list

                val_list = self.traverse_grid2(direction, OFFSETS[LEFT], self._grid_width)
                self._merged = merge(val_list)
                #print 'merged =', merged
                self.traverse_grid3(direction, OFFSETS[LEFT], self._grid_width)
        
        elif direction == RIGHT:
            for direction in self._movements[direction]:
                #print 'direction = ', direction
                new_list = []
                new_list.append(direction)
                #print 'new_list = ',  new_list

                val_list = self.traverse_grid2(direction, OFFSETS[RIGHT], self._grid_width)
                self._merged = merge(val_list)
                #print 'merged =', merged
                self.traverse_grid3(direction, OFFSETS[RIGHT], self._grid_width)

        
        if self._grid != grid2:
            self.new_tile()
        
            
            
                            
    def new_tile(self):
        """
        Create a new tile in a randomly selected empty
        square.  The tile should be 2 90% of the time and
        4 10% of the time.
        """
        rand_row = random.randrange(0, self._grid_height)
        rand_col = random.randrange(0, self._grid_width)
        if self._grid[rand_row][rand_col] == 0:
            self._grid[rand_row][rand_col] = random.choice([2, 2, 2, 2, 2, 2, 2, 2, 2, 4])
       
        else:
            self.new_tile()
        #print self.grid

    def set_tile(self, row, col, value):
        """
        Set the tile at position row, col to have the given value.
        """
        self._row = row
        self._col = col
        self._value = value
        self._grid[row][col] = value
        #print self.value
        

    def get_tile(self, row, col):
        """
        Return the value of the tile at position row, col.
        """
        self._row = row
        self._col = col
        return self._grid[row][col]
    
