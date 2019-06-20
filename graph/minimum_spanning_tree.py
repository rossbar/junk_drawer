"""
Algorithm for computing the minimum spanning tree of a weighted graph.

See Classic Computer Science Problems in Python Ch. 4.5
"""
import sys
sys.path.append('..')
sys.path.append('../..')

from data_structures import PriorityQueue
from edge import total_weight

def jarnik(weighted_graph):
    """
    Return the minimum spanning tree of the given weighted graph.

    See CCSPiP Listing 4.11
    """
    result = []
    edge_queue = PriorityQueue()
    visited = [False] * weighted_graph.vertex_count

    # Procedure for visiting a vertex at the given index
    def visit(index):
        visited[index] = True
        for edge in weighted_graph.edges_for_index(index):
            if not visited[edge.v]:
                edge_queue.push(edge)

    # Start the problem
    visit(0)
    while not edge_queue.empty:
        edge = edge_queue.pop()
        # Never revisit any vertex
        if visited[edge.v]:
            continue
        # Because we're popping from a priority queue, the edge that is popped
        # must have the lowest weight
        result.append(edge)
        # Visit the next vertex
        visit(edge.v)
    return result

def is_spanning_tree(weighted_graph, path):
    """
    Check that the path through is a spanning-tree, i.e. that all the vertices
    are accounted for in the path.
    """
    verts_in_path = []
    for edge in path:
        verts_in_path.append(weighted_graph.vertex_at(edge.u))
        verts_in_path.append(weighted_graph.vertex_at(edge.v))
    verts_in_path = set(verts_in_path)
    return len(verts_in_path) == weighted_graph.vertex_count

def print_weighted_path(weighted_graph, path):
    """
    Print a path (list of edges) through a weighted graph.
    """
    for edge in path:
        print("{} -({})> {}".format(weighted_graph.vertex_at(edge.u),
                                  edge.weight,
                                  weighted_graph.vertex_at(edge.v)))
    print("Total weight of path: {}".format(total_weight(path)))
