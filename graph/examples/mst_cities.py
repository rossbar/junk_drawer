"""
Example using a graph comprising the top 15 metro areas in the US to illustrate
the Jarnik algorithm for finding the minimum spanning tree of a weighted 
graph.

See Classic Computer Science Problems in Python, Ch. 4
"""
import sys
sys.path.append('..')

from cities import top_15_metro_areas_in_US_weighted_by_distance
from minimum_spanning_tree import jarnik, print_weighted_path, is_spanning_tree

weighted_city_graph = top_15_metro_areas_in_US_weighted_by_distance()

path_mst = jarnik(weighted_city_graph)
if not is_spanning_tree(weighted_city_graph, path_mst):
    print("Warning: {} is not a spanning tree".format(path_mst))

print_weighted_path(weighted_city_graph, path_mst)
