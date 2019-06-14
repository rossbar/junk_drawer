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
        self.start = start
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

    def goal_test(self, loc):
        """
        Test whether the end of the maze has been reached.
        """
        return loc == self.goal

    def possible_next_locations(self, loc):
        """
        Given the current location, determine valid locations for the next
        move in the maze.

        Parameters
        ----------
        loc : MazeLocation
            Current location in the grid

        Returns
        -------
        possible_locations : List[MazeLocation]
            List of allowed locations for the next move on the grid
        """
        possible_locations = []
        # Check left
        if loc.col > 0 and self._grid[loc.row][loc.col - 1] != Cell.blocked:
            possible_locations.append(MazeLocation(loc.row, loc.col - 1))
        # Check right
        if loc.col + 1 < self._ncols and self._grid[loc.row][loc.col + 1] != Cell.blocked:
            possible_locations.append(MazeLocation(loc.row, loc.col + 1))
        # Check top
        if loc.row > 0 and self._grid[loc.row - 1][loc.col] != Cell.blocked:
            possible_locations.append(MazeLocation(loc.row - 1, loc.col))
        # Check bottom
        if loc.row + 1 < self._nrows and self._grid[loc.row + 1][loc.col] != Cell.blocked:
            possible_locations.append(MazeLocation(loc.row + 1, loc.col))
        return possible_locations

    def mark_path(self, path):
        """
        Mark path through the maze.

        Parameters
        ----------
        path : list
            List of MazeLocation objects representing path.
        """
        for ml in path:
            self._grid[ml.row][ml.col] = Cell.path
        # Re-label start and end
        self._grid[self.start.row][self.start.col] = Cell.start
        self._grid[self.goal.row][self.goal.col] = Cell.goal

    def clear_path(self):
        """
        Remove path visualization from maze, if any.
        """
        for i, row in enumerate(self._grid):
            for j, cell in enumerate(row):
                if cell == Cell.path:
                    self._grid[i][j] = Cell.empty
