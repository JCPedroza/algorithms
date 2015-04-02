# This python file uses the following encoding: utf-8

"""
Breath-first search algorithm implemented in a grid.
Like a depth-first search, but uses a queue instead
of a stack.

The algorithm:

while boundary is not empty:
    current_cell  ←  dequeue boundary
    for all neighbor_cell of current_cell:
        if neighbor_cell is not in visited:
            add neighbor_cell to visited
            enqueue neighbor_cell onto boundary

In this example, neighbors cells are the cells located
up, down, left, and right from a given cell. Diagonals are
not considered adjacent.
"""

import sys
sys.path.append('../../Tools')
from tools import Queue
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
    boundary = Queue()            # bsf uses queue dynamics
    boundary.enqueue((row, col))  # put the starting grid in the queue
    visited = [[EMPTY for _ in xrange(WIDTH)] for _ in xrange(HEIGHT)]

    while boundary:    # while the queue is not empty
        current = boundary.dequeue()  # get a grid cell from the queue
        grid.set_full(current[0], current[1])  # mark it as searched
        neighbors = grid.four_neighbors(current[0], current[1]) # get the four neighbor cells:
        print grid                                              # up, down, left, and right

        for neighbor in neighbors: # for every neighbor cell
            if not visited[neighbor[0]][neighbor[1]]:  # if it hasn't been visited
                visited[neighbor[0]][neighbor[1]] = FULL  # mark it as visited
                boundary.enqueue(neighbor)  # add it to the queue

bfs(Grid(HEIGHT, WIDTH), HEIGHT/2, WIDTH/2)
