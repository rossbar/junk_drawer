"""
Example using breadth-first search to find shortest path between two nodes on
an un-weighted graph.

Uses graph of top 15 US metropolitan areas as example: see CCSPiP Ch. 4.3
"""
# Hack path
import sys
sys.path.append('../..') # For search
sys.path.append('..')    # For graph

from search import Node, bfs, node_to_path
from graph import graph_of_top_15_metro_areas_in_US

start = "Boston"
end = "Miami"

city_graph = graph_of_top_15_metro_areas_in_US()

solution = bfs(start, lambda x : x == end, city_graph.neighbors_for_vertex)

if solution is None:
    print("No solution found for getting from {} to {}".format(start, end))
else:
    path = node_to_path(solution)
    print("Path from {} to {}:".format(start, end))
    print(path)
