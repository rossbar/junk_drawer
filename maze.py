"""
Solving mazes with generic search (without numpy)

See 'Classic Computer Science Problems in Python', Ch. 2
"""
from enum import Enum
from collections import namedtuple
import random
from math import sqrt

class Cell(str, Enum):
    empty =   " "
    blocked = "X"
    start =   "S"
    goal =    "G"
    path =    "*"

MazeLocation = namedtuple("MazeLocation", ("row", "col"))

def euclidean_distance(goal):
    """
    Return a callable that computes the euclidean distance between an input
    MazeLocation and the goal.
    """
    def distance(ml):
        dx = (ml.col - goal.col)
        dy = (ml.row - goal.row)
        return sqrt(dx**2 + dy**2)
    return distance

def manhattan_distance(goal):
    """
    Return a callable that computes the manhattan distance between an input
    MazeLocation and the goal
    """
    def distance(ml):
        dx = (ml.col - goal.col)
        dy = (ml.row - goal.row)
        return abs(dx) + abs(dy)
    return distance

def grid_cost(current_node):
    """
    Cost function for cardinal motion on a grid.
    """
    return current_node.cost + 1

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

if __name__ == "__main__":
    import time
    from search import dfs, bfs, a_star, node_to_path
    m = Maze()
    print(m)
    tic = time.time()
    df_solution = dfs(m.start, m.goal_test, m.possible_next_locations)
    toc = time.time()
    if df_solution is None:
        print("Depth-first search did not find solution")
    else:
        df_path = node_to_path(df_solution)
        m.mark_path(df_path)
        print("Depth-first search results:")
        print("  Path length: {}".format(len(df_path)))
        print("  Eval time: %.5f" %(toc - tic))
        print(m)
    m.clear_path()
    tic = time.time()
    bf_solution = bfs(m.start, m.goal_test, m.possible_next_locations)
    toc = time.time()
    if bf_solution is None:
        print("Breadth-first search failed to find solution")
    else:
        bf_path = node_to_path(bf_solution)
        m.mark_path(bf_path)
        print("Path from BFS:")
        print("  Path length: {}".format(len(bf_path)))
        print("  Eval time: %.5f"%(toc - tic))
        print(m)
    m.clear_path()
    heur = euclidean_distance(m.goal)
    tic = time.time()
    astar_solution = a_star(m.start, m.goal_test, m.possible_next_locations,
                            grid_cost, heur)
    toc = time.time()
    if astar_solution is None:
        print("A* search failed to find a solution")
    else:
        astar_path = node_to_path(astar_solution)
        m.mark_path(astar_path)
        print("Path from A*:")
        print("  Path length: {}".format(len(astar_path)))
        print("  Eval time: %.5f" %(toc-tic))
        print(m)
    m.clear_path()
