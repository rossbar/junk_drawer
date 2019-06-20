"""
Functions that return manually-constructed networks of cities in the US

See CCSPiP, Ch. 4 for data source
"""
import sys
sys.path.append('..')
from graph import UndirectedGraph, WeightedGraph

def top_15_metro_areas_in_US():
    """
    Manual creation of graph of top 15 metropolitan areas in US.

    See Fig. 4.2 of CCSPiP for definition.
    """
    city_graph = UndirectedGraph(["Seattle",
                                  "San Francisco",
                                  "Los Angeles",
                                  "Riverside",
                                  "Phoenix",
                                  "Chicago",
                                  "Boston",
                                  "New York",
                                  "Atlanta",
                                  "Miami",
                                  "Dallas",
                                  "Houston",
                                  "Detroit",
                                  "Philadelphia",
                                  "Washington"])
    # Manually add edges according to CCSPiP fig. 4.2
    city_graph.add_edge_by_vertices("Seattle", "Chicago")
    city_graph.add_edge_by_vertices("Seattle", "San Francisco")
    city_graph.add_edge_by_vertices("San Francisco", "Riverside")
    city_graph.add_edge_by_vertices("San Francisco", "Los Angeles")
    city_graph.add_edge_by_vertices("Los Angeles", "Riverside")
    city_graph.add_edge_by_vertices("Los Angeles", "Phoenix")
    city_graph.add_edge_by_vertices("Riverside", "Phoenix")
    city_graph.add_edge_by_vertices("Riverside", "Chicago")
    city_graph.add_edge_by_vertices("Phoenix", "Dallas")
    city_graph.add_edge_by_vertices("Phoenix", "Houston")
    city_graph.add_edge_by_vertices("Dallas", "Chicago")
    city_graph.add_edge_by_vertices("Dallas", "Atlanta")
    city_graph.add_edge_by_vertices("Dallas", "Houston")
    city_graph.add_edge_by_vertices("Houston", "Atlanta")
    city_graph.add_edge_by_vertices("Houston", "Miami")
    city_graph.add_edge_by_vertices("Atlanta", "Chicago")
    city_graph.add_edge_by_vertices("Atlanta", "Washington")
    city_graph.add_edge_by_vertices("Atlanta", "Miami")
    city_graph.add_edge_by_vertices("Miami", "Washington")
    city_graph.add_edge_by_vertices("Chicago", "Detroit")
    city_graph.add_edge_by_vertices("Detroit", "Boston")
    city_graph.add_edge_by_vertices("Detroit", "Washington")
    city_graph.add_edge_by_vertices("Detroit", "New York")
    city_graph.add_edge_by_vertices("Boston", "New York")
    city_graph.add_edge_by_vertices("New York", "Philadelphia")
    city_graph.add_edge_by_vertices("Philadelphia", "Washington")
    return city_graph

def top_15_metro_areas_in_US_weighted_by_distance():
    """
    Manual creation of weighted graph of top 15 metropolitan areas in US.

    See Ch 4.4 of CCSPiP.
    """
    city_graph = WeightedGraph(["Seattle",
                                "San Francisco",
                                "Los Angeles",
                                "Riverside",
                                "Phoenix",
                                "Chicago",
                                "Boston",
                                "New York",
                                "Atlanta",
                                "Miami",
                                "Dallas",
                                "Houston",
                                "Detroit",
                                "Philadelphia",
                                "Washington"])
    # Manually add edges according to CCSPiP fig. 4.4
    city_graph.add_edge_by_vertices("Seattle", "Chicago", 1737)
    city_graph.add_edge_by_vertices("Seattle", "San Francisco", 678)
    city_graph.add_edge_by_vertices("San Francisco", "Riverside", 386)
    city_graph.add_edge_by_vertices("San Francisco", "Los Angeles", 348)
    city_graph.add_edge_by_vertices("Los Angeles", "Riverside", 50)
    city_graph.add_edge_by_vertices("Los Angeles", "Phoenix", 357)
    city_graph.add_edge_by_vertices("Riverside", "Phoenix", 307)
    city_graph.add_edge_by_vertices("Riverside", "Chicago", 1704)
    city_graph.add_edge_by_vertices("Phoenix", "Dallas", 887)
    city_graph.add_edge_by_vertices("Phoenix", "Houston", 1015)
    city_graph.add_edge_by_vertices("Dallas", "Chicago", 805)
    city_graph.add_edge_by_vertices("Dallas", "Atlanta", 721)
    city_graph.add_edge_by_vertices("Dallas", "Houston", 225)
    city_graph.add_edge_by_vertices("Houston", "Atlanta", 702)
    city_graph.add_edge_by_vertices("Houston", "Miami", 968)
    city_graph.add_edge_by_vertices("Atlanta", "Chicago", 588)
    city_graph.add_edge_by_vertices("Atlanta", "Washington", 543)
    city_graph.add_edge_by_vertices("Atlanta", "Miami", 604)
    city_graph.add_edge_by_vertices("Miami", "Washington", 923)
    city_graph.add_edge_by_vertices("Chicago", "Detroit", 238)
    city_graph.add_edge_by_vertices("Detroit", "Boston", 613)
    city_graph.add_edge_by_vertices("Detroit", "Washington", 396)
    city_graph.add_edge_by_vertices("Detroit", "New York", 482)
    city_graph.add_edge_by_vertices("Boston", "New York", 190)
    city_graph.add_edge_by_vertices("New York", "Philadelphia", 81)
    city_graph.add_edge_by_vertices("Philadelphia", "Washington", 123)
    return city_graph

if __name__ == "__main__":
    city_graph = top_15_metro_areas_in_US()
    print(city_graph)
    weighted_city_graph = top_15_metro_areas_in_US_weighted_by_distance()
    print(weighted_city_graph)
