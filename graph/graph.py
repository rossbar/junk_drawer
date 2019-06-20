"""
Specifies classes for describing graph problems.

See Classic Computer Science Problems in Python, Ch. 4
"""
from edge import Edge, WeightedEdge

class UndirectedGraph(object):
    """
    Base class for an undirected graph.
    """
    def __init__(self, vertices):
        """
        Create a graph object with a list of vertices.
        """
        # List of vertices
        self._vertices = vertices
        # List of list of edges, where each entry in _edges represents a
        # list of connections (edges) with other vertices
        self._edges = [[] for v in vertices]

    def __str__(self):
        out = ""
        for i in range(self.vertex_count):
            out += "{} -> {}\n".format(self.vertex_at(i), 
                                     self.neighbors_for_index(i))
        return out

    @property
    def vertex_count(self):
        return len(self._vertices)

    @property
    def edge_count(self):
        return sum(map(len, self._edges))

    def add_vertex(self, vertex):
        """
        Add a new vertex to graph and return its index.
        """
        self._vertices.append(vertex)
        self._edges.append([])
        return self.vertex_count - 1

    def add_edge(self, edge):
        """
        Add an edge between two vertices.
        """
        self._edges[edge.u].append(edge)
        self._edges[edge.v].append(edge.reversed())

    def add_edge_by_indices(self, u, v):
        """
        Convenience method: Add an edge between _vertices[u] and _vertices[v]
        """
        edge = Edge(u, v)
        self.add_edge(edge)

    def add_edge_by_vertices(self, vert1, vert2):
        """
        Convenience method: Add an edge between two vertices.
        """
        # Look up index for vertices
        u = self._vertices.index(vert1)
        v = self._vertices.index(vert2)
        self.add_edge_by_indices(u, v)

    def vertex_at(self, index):
        """
        Find vertex at specific index.
        """
        return self._vertices[index]

    def index_of(self, vertex):
        """
        Find index of specific vertex.
        """
        return self._vertices.index(vertex)

    def neighbors_for_index(self, index):
        """
        Return all vertices connected to vertex at given index.
        """
        edges = self._edges[index]
        return list(map(self.vertex_at, [e.v for e in self._edges[index]]))

    def neighbors_for_vertex(self, vertex):
        """
        Return all vertices connect to given vertex.
        """
        return self.neighbors_for_index(self.index_of(vertex))

    def edges_for_index(self, index):
        """
        Return all edges associated with given index.
        """
        return self._edges[index]

    def edges_for_vertex(self, vertex):
        """
        Return all edges for given vertex.
        """
        return self._edges[self.index_of(vertex)]

class WeightedGraph(UndirectedGraph):
    """
    An undirected graph with weighted edges.
    """
    def __init__(self, vertices):
        super().__init__(vertices)

    def __str__(self):
        out = ""
        for i in range(self.vertex_count):
            out += "{} -> {}\n".format(self.vertex_at(i), 
                                       self.neighbors_for_index_with_weights(i))
        return out
        

    def add_edge_by_indices(self, u, v, weight):
        edge = WeightedEdge(u, v, weight)
        self.add_edge(edge)

    def add_edge_by_vertices(self, v1, v2, weight):
        u = self.index_of(v1)
        v = self.index_of(v2)
        self.add_edge_by_indices(u, v, weight)

    def neighbors_for_index_with_weights(self, index):
        return [(self.vertex_at(edge.v), edge.weight) for edge in self.edges_for_index(index)]
