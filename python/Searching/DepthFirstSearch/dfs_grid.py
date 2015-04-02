# This python file uses the following encoding: utf-8

"""
Depth-first search algorithm implemented in a grid.
Like a breath-first search, but uses a stack instead
of a queue.

The algorithm:

while boundary is not empty:
    current_cell  ←  pop boundary
    for all neighbor_cell of current_cell:
        if neighbor_cell is not in visited:
            add neighbor_cell to visited
            push neighbor_cell onto boundary

In this example, neighbors cells are the cells located
up, down, left, and right from a given cell. Diagonals are
not considered adjacent.

In the print, cells with an X are visited, and cells with an 
O are in the stack.
"""

import sys
sys.path.append('../../Tools')
from tools import Stack
from tools import Grid

HEIGHT = 5
WIDTH = 5
EMPTY = 0
FULL = 1

def bfs(grid, row, col):
    """
    Perform a breath-first search in the given grid, starting
    in the given cell.
    """
    boundary = Stack()            # dfs uses stack dynamics
    boundary.push((row, col))     # put the starting grid in the stack
    visited = [[EMPTY for _ in xrange(WIDTH)] for _ in xrange(HEIGHT)]
    visited[row][col] = FULL      # set the starting cell to visited

    while boundary:                                             # while the stack is not empty
        current = boundary.pop()                                # get a grid cell from the stack
        grid.set_marked(current[0], current[1])                 # (this is for the print)
        neighbors = grid.four_neighbors(current[0], current[1]) # get the four neighbor cells:
        print grid                                              # up, down, left, and right

        for neighbor in neighbors:                        # for every neighbor cell
            if not visited[neighbor[0]][neighbor[1]]:     # if it hasn't been visited
                visited[neighbor[0]][neighbor[1]] = FULL  # set it as visited
                boundary.push(neighbor)                   # add it to the stack
                grid.set_full(neighbor[0], neighbor[1])   # (this is for the print)
        print grid

bfs(Grid(HEIGHT, WIDTH), HEIGHT/2, WIDTH/2)
