from igraph import *

g = Graph(directed=True)
g.add_vertices(3)
g.add_edges([[0, 1], [1, 2], [0, 2]])
print(g.isoclass())
