"""
Dijkstra's algorithm for solving the single-source, shortest-path problem.

See Classic Computer Science Problems in Python, Ch. 4.5.
"""
import sys
sys.path.append('..')
sys.path.append('../..')

from graph import WeightedGraph
from data_structures import PriorityQueue

class DijkstraNode(object):
    """
    Data class for comparing costs between explored nodes in Dijkstra's 
    algorithm.
    """
    def __init__(self, vertex, distance):
        self.vertex = vertex
        self.distance = distance

    def __eq__(self, other):
        return self.distance == other.distance

    def __lt__(self, other):
        self.distance < other.distance

def dijkstra(weighted_graph, root_vertex):
    """
    Dijkstra's algorithm for computing the path with the minimum weight from
    root_vertex to every other vertex in a weighted graph.

    Parameters
    ----------
    weighted_graph : graph.WeightedGraph
        Weighted graph over which search will be conducted.
    root_vertex : Generic
        Vertex in weighted_graph from which paths will originate.

    Returns
    -------
    distances : tuple
        Minimum distances (weights) from root to every other vertex
    path_dict : dict
        Dictionary of weighted edges mapping the shortest edge between each
        node
    """
    # Starting point
    first = weighted_graph.index_of(root_vertex)
    # Initialized distances to all other vertices
    distances = [None] * weighted_graph.vertex_count
    distances[first] = 0
    # Initialize mapping of vertices to their min paths
    path_dict = {}
    # Initialize search queue
    node_queue = PriorityQueue()
    node_queue.push(DijkstraNode(first, 0))

    while not node_queue.empty:
        # Known node and distance
        u = node_queue.pop().vertex
        dist_u = distances[u]
        for we in weighted_graph.edges_for_index(u):
            # Get previous distance to this vertex
            dist_v = distances[we.v]
            # If the vertex hasn't been visited yet, or the new distance is 
            # lower than the original, update the distance to the node
            if dist_v is None or dist_v > dist_u + we.weight:
                distances[we.v] = dist_u + we.weight
                # Update edge on shortest path to this vertex
                path_dict[we.v] = we
                # Explore it soon
                node_queue.push(DijkstraNode(we.v, dist_u + we.weight))
    return distances, path_dict

def distances_to_vertex_dict(weighted_graph, distances):
    """
    Convert the sequence of distances returned by dijstra() to a dictionary
    whose keys are the vertices in the weighted_graph, and whose values are
    the minimum distances from root -> vertex.
    """
    wg = weighted_graph
    return { wg.vertex_at(i) : distances[i] for i in range(len(distances)) }

def path_dict_to_path(start, end, path_dict):
    """
    Given a start index and an ending index, as well as the path_dict 
    returned by dijkstra(), return the shortest path from *start* to *end*
    """
    # Handle edge case: empty path dict
    if len(path_dict) == 0:
        return []
    
    path = []
    edge = path_dict[end]
    path.append(edge)
    while edge.u != start:
        edge = path_dict[edge.u]
        path.append(edge)
    return list(reversed(path))
