# This python file uses the following encoding: utf-8

"""
Computes a distance field using a breath-first 
search algorithm.

Using this algorithm a distance field can be easily built
even when impassible cells (obstacles) are present.
"""

import sys, random
sys.path.append("../../Tools")
from tools import Queue, Grid, FULL, OBSTACLE, EMPTY

WIDTH = 11
HEIGHT = 11
MAX_OBSTACLES = 30
STRMAP = {0: "0", 1: "1", 2: "2", 3: "3", 4: "4", 5: "5", 6: "6", 7: "7", 8: "8", 
          9: "9", -1: " ", OBSTACLE: "X", 10: "10", 11: "11", 12: "12", 13: "13"}

def distance_field(grid, position, obstacles):
    """
    Compute a distance field on a grid in a given position, 
    with the given obstacles.
    """
    boundary = Queue()                            # bsf uses queue dynamics
    boundary.enqueue((position[0], position[1]))  # put the starting grid in the queue
    visited = [[EMPTY for _ in xrange(WIDTH)] for _ in xrange(HEIGHT)]
    visited[position[0]][position[1]] = FULL      # set the starting cell to visited
    field = Grid(HEIGHT, WIDTH, STRMAP)           # we'll store the distance field as a grid
    field.set_all_to(-1)                          # -1 will symbolize unreachable cells

    # Set obstacles
    for obstacle in obstacles:
        grid.set_obstacle(obstacle[0], obstacle[1])
        field.set_obstacle(obstacle[0], obstacle[1])
    field.set_empty(position[0], position[1])                   # set the root position

    while boundary:                                             # while the queue is not empty
        current = boundary.dequeue()                            # get a grid cell from the queue
        neighbors = grid.four_neighbors(current[0], current[1]) # get the four neighbor cells:
                                                                # up, down, left, and right

        for neighbor in neighbors:                            # for every neighbor cell
            # If the cell hasn't been visited and has no obstacles:
            if not visited[neighbor[0]][neighbor[1]] and grid.is_empty(neighbor[0], neighbor[1]):
                visited[neighbor[0]][neighbor[1]] = FULL      # set it as visited
                boundary.enqueue(neighbor)                    # add it to the queue
                field.set_to(neighbor[0], neighbor[1],        # set the distance from the root
                    field.get_cell(current[0], current[1]) + 1)

    return field

obstacles = [[random.randrange(HEIGHT), random.randrange(WIDTH)] for _ in range(MAX_OBSTACLES)]
field = distance_field(Grid(HEIGHT, WIDTH), [HEIGHT/2, WIDTH/2], obstacles)

print "\nobstacles: ", obstacles
print
print field
