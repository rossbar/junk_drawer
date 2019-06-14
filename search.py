"""
Generic search algorithms implemented in python.
"""
from data_structures import Stack

class Node(object):
    """
    Record of state during search.
    """
    def __init__(self, state, parent_node, cost=0.0, heuristic=0.0):
        """
        Node object for keeping track of state during a generic search.

        Parameters
        ----------
        state : Generic
            Current state of search. For example, during maze-solving search,
            the state would be the current location in the maze.
        parent_node : Node
            Previous node from which current Node is derived.
            Can be None.
        cost : float
            Evaluated result of cost function (optional)
        heuristic : float
            Evaluated heuristic (optional)
        """
        self.state = state
        self.parent = parent_node
        self.cost = cost
        self.heuristic = heuristic

    def __lt__(self, other):
        return (self.cost + self.heuristic) < (other.cost + other.heuristic)

def dfs(initial, goal_test, successors):
    """
    Depth-first search.

    Parameters
    ----------
    initial : Generic
        Starting point of the search.
    goal_test : Callable
        Callable returing boolean value indicating search success.
    successors : Callable
        Callable returning list of next possible locations in search space.

    Returns
    -------
    found : Generic
        Node corresponding to successful goal_test.
        Returns None if search fails.
    """
    # References to candidate and previously-explored nodes in search space
    frontier = Stack()
    explored = Stack()

    # Initialize candidate search locations with initial condition
    frontier.push(Node(initial, None))

    # Continue search as long as their are candidates in the search space
    while not frontier.empty:
        current_node = frontier.pop()
        current_state = current_node.state
        # If current node meets goal, then search completes successfully
        if goal_test(current_state):
            return current_node
        # Populate next step in search
        for child in successors(current_state):
            # Skip previously-explored states
            if child in explored: 
                continue
            explored.push(child)
            frontier.push(Node(child, current_node))
    # Search terminates without finding goal
    return None

def node_to_path(goal_node):
    """
    Back-track through nodes to determine path through search space for a 
    successful search using the node.parent.

    Parameters
    ----------
    goal_node : Node
        Node returned by successful search

    Returns
    -------
    path : List
        List of nodes comprising the successful search path, from start to end
    """
    # Initialize path with end state
    path = [goal_node.state]
    # Work backwards through nodes
    node = goal_node
    while node.parent is not None:
        node = node.parent
        path.append(node.state)
    # Flip order of path so that it is from start->end
    path.reverse()
    return path
