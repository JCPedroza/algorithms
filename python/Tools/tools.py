EMPTY = 0
FULL = 1
MARKED = 2

STRMAP = {EMPTY: " ",
          FULL: "O",
          MARKED: "X"}

class Collection(object):
    """
    Superclass for collections, like queues and stacks.
    """

    def __init__(self, items = []):
        """ 
        Initialize the queue.
        """
        self._items = list(items)

    def __len__(self):
        """
        Return the number of items in the queue.
        """
        return len(self._items)
    
    def __iter__(self):
        """
        Create an iterator for the queue.
        """
        for item in self._items:
            yield item

    def __str__(self):
        """
        Return a string representation of the queue.
        """
        return str(self._items)

    def clear(self):
        """
        Remove all items from the queue.
        """
        self._items = []

class Queue(Collection):
    """
    A simple implementation of a FIFO queue.
    """

    def enqueue(self, item):
        """
        Add item to the queue.
        """        
        self._items.append(item)

    def dequeue(self):
        """
        Remove and return the least recently inserted item.
        """
        return self._items.pop(0)

class Stack(Collection):
    """
    A simple implementation of a LIFO stack.
    """

    def push(self, item):
        """
        Add item to the queue.
        """        
        self._items.append(item)

    def pop(self):
        """
        Remove and return the least recently inserted item.
        """
        return self._items.pop()

class Grid:
    """
    Implementation of 2D grid of cells
    Includes boundary handling
    """
    
    def __init__(self, grid_height, grid_width):
        """
        Initializes grid to be empty, take height and width of grid as parameters
        Indexed by rows (left to right), then by columns (top to bottom)
        """
        self._grid_height = grid_height
        self._grid_width = grid_width
        self._cells = [[EMPTY for dummy_col in range(self._grid_width)] 
                       for dummy_row in range(self._grid_height)]
                
    def __str__(self):
        """
        Return multi-line string represenation for grid
        """
        rep = ""
        for row in range(self._grid_height):
            for col in range(self._grid_width):
                rep += STRMAP[self._cells[row][col]]
                if col == self._grid_width - 1:
                    rep += "\n"
                else:
                    rep += " | "
            if row != self._grid_height - 1:
                rep += "-" * (4 * self._grid_width - 3)
                rep += "\n"
        rep += "\n"
        return rep
    
    def get_height(self):
        """
        Return the height of the grid for use in the GUI
        """
        return self._grid_height

    def get_width(self):
        """
        Return the width of the grid for use in the GUI
        """
        return self._grid_width

    def clear(self):
        """
        Clears grid to be empty
        """
        self._cells = [[EMPTY for dummy_col in range(self._grid_width)]
                       for dummy_row in range(self._grid_height)]
                
    def set_empty(self, row, col):
        """
        Set cell with index (row, col) to be empty
        """
        self._cells[row][col] = EMPTY
    
    def set_full(self, row, col):
        """
        Set cell with index (row, col) to be full
        """
        self._cells[row][col] = FULL

    def set_marked(self, row, col):
        """
        Set cell with index (row, col) to be full
        """
        self._cells[row][col] = MARKED
    
    def is_empty(self, row, col):
        """
        Checks whether cell with index (row, col) is empty
        """
        return self._cells[row][col] == EMPTY
 
    def four_neighbors(self, row, col):
        """
        Returns horiz/vert neighbors of cell (row, col)
        """
        ans = []
        if row > 0:
            ans.append((row - 1, col))
        if row < self._grid_height - 1:
            ans.append((row + 1, col))
        if col > 0:
            ans.append((row, col - 1))
        if col < self._grid_width - 1:
            ans.append((row, col + 1))
        return ans

    def eight_neighbors(self, row, col):
        """
        Returns horiz/vert neighbors of cell (row, col) as well as
        diagonal neighbors
        """
        ans = []
        if row > 0:
            ans.append((row - 1, col))
        if row < self._grid_height - 1:
            ans.append((row + 1, col))
        if col > 0:
            ans.append((row, col - 1))
        if col < self._grid_width - 1:
            ans.append((row, col + 1))
        if (row > 0) and (col > 0):
            ans.append((row - 1, col - 1))
        if (row > 0) and (col < self._grid_width - 1):
            ans.append((row - 1, col + 1))
        if (row < self._grid_height - 1) and (col > 0):
            ans.append((row + 1, col - 1))
        if (row < self._grid_height - 1) and (col < self._grid_width - 1):
            ans.append((row + 1, col + 1))
        return ans
