"""
Specifies an Edge class to represent edge in a generic graph problem.

See Classic Computer Science Problems in Python, Ch. 4
"""
class Edge(object):
    def __init__(self, u, v):
        """
        Edge object specifying link between two vertices by their integer
        indices in a graph.
        """
        self.u = u  # Index of "from" vertex
        self.v = v  # Index of "to" vertex

    def __str__(self):
        return "{} -> {}".format(self.u, self.v)

    def reversed(self):
        return Edge(self.v, self.u)

