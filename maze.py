"""
Solving mazes with generic search (without numpy)

See 'Classic Computer Science Problems in Python', Ch. 2
"""
from enum import Enum
from collections import namedtuple
import random

class Cell(str, Enum):
    empty =   " "
    blocked = "X"
    start =   "S"
    goal =    "G"
    path =    "*"

MazeLocation = namedtuple("MazeLocation", ("row", "col"))

class Maze(object):
    """
    2D grid maze
    """
    def __init__(self, nrows=10, ncols=10, blocked_fraction=0.2,
                 start=MazeLocation(0, 0), end=MazeLocation(9, 9)):
        self._nrows = nrows
        self._ncols = ncols
        self._blocked_cells = 0
        self.start = start,
        self.goal = end
        # Initialize grid
        self._grid = [[Cell.empty for c in range(self._ncols)] for r in range(self._nrows)]
        # Randomly block
        self._randomly_fill(blocked_fraction)
        # Set start and end points
        self._grid[start.row][start.col] = Cell.start
        self._grid[end.row][end.col] = Cell.goal

    def __str__(self):
        out = ''
        for row in self._grid:
            out += "".join([c.value for c in row]) + "\n"
        return out

    def _randomly_fill(self, blocked_fraction):
        """
        Randomly fill maze with blocked locations.
        """
        for row in range(self._nrows):
            for col in range(self._ncols):
                if random.uniform(0, 1.0) < blocked_fraction:
                    self._grid[row][col] = Cell.blocked
                    self._blocked_cells += 1

    def goal_test(loc):
        """
        Test whether the end of the maze has been reached.
        """
        return loc == self.goal
