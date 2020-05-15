import networkx as nx
import matplotlib.pyplot as plt

G1 = nx.read_gml("tf_operon_graph_all.gml")
plt.subplot(121)
nx.draw(G1, with_labels=True, font_weight='bold')
plt.subplot(122)
nx.draw_shell(G1, nlist=[range(5, 10), range(5)], with_labels=True, font_weight='bold')
