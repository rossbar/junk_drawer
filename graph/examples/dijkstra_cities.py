"""
Example illustrating Dijkstra's algorithm on a graph of 15 US cities weighted 
by their distance from one another.
"""
import sys
sys.path.append('..')

from cities import top_15_metro_areas_in_US_weighted_by_distance
from dijkstra import dijkstra, distances_to_vertex_dict, path_dict_to_path
from minimum_spanning_tree import print_weighted_path

weighted_city_graph = top_15_metro_areas_in_US_weighted_by_distance()

root = "Los Angeles"
distances, path_dict = dijkstra(weighted_city_graph, root)

# Print minimum distance from root to every other city
name2dist = distances_to_vertex_dict(weighted_city_graph, distances)
for k, v in name2dist.items():
    print("Minimum distance from {} to {}: {}".format(root, k, v))

# Shortest path from root to end
end = "Boston"
path = path_dict_to_path(weighted_city_graph.index_of(root),
                         weighted_city_graph.index_of(end),
                         path_dict)
print("Shortest path from {} to {}:".format(root, end))
print_weighted_path(weighted_city_graph, path)
