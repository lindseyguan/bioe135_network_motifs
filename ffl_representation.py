import networkx as nx
import numpy as np
import itertools


# Code adapted from https://gist.github.com/tpoisot/8582648 

def mcounter(gr, mo):
    """Counts motifs in a directed graph
    :param gr: A ``DiGraph`` object
    :param mo: A ``dict`` of motifs to count
    :returns: A ``dict`` with the number of each motifs, with the same keys as ``mo``
    This function is actually rather simple. It will extract all 3-grams from
    the original graph, and look for isomorphisms in the motifs contained
    in a dictionary. The returned object is a ``dict`` with the number of
    times each motif was found.::
        >>> print mcounter(gr, mo)
        {'S1': 4, 'S3': 0, 'S2': 1, 'S5': 0, 'S4': 3}
    """
    #This function will take each possible subgraphs of gr of size 3, then
    #compare them to the mo dict using .subgraph() and is_isomorphic
    
    #This line simply creates a dictionary with 0 for all values, and the
    #motif names as keys

    mcount = dict(zip(mo.keys(), list(map(int, np.zeros(len(mo))))))
    nodes = gr.nodes()

    #We use iterools.product to have all combinations of three nodes in the
    #original graph. Then we filter combinations with non-unique nodes, because
    #the motifs do not account for self-consumption.

    triplets = list(itertools.product(*[nodes, nodes, nodes]))
    triplets = [trip for trip in triplets if len(list(set(trip))) == 3]
    triplets = map(list, map(np.sort, triplets))
    u_triplets = []
    [u_triplets.append(trip) for trip in triplets if not u_triplets.count(trip)]

    #The for each each of the triplets, we (i) take its subgraph, and compare
    #it to all fo the possible motifs
    print('motif matching')
    print(len(u_triplets))
    for trip in u_triplets:
        sub_gr = gr.subgraph(trip)
        mot_match = map(lambda mot_id: nx.is_isomorphic(sub_gr, mo[mot_id]), motifs.keys())
        match_keys = [mo.keys()[i] for i in xrange(len(mo)) if mot_match[i]]
        if len(match_keys) == 1:
            mcount[match_keys[0]] += 1

    return mcount

# We define each motif as a directed graph in networkx
motifs = {
    'FFL': nx.DiGraph([(1,2),(1,3),(2,3)]),
    }

G_tf_tf = nx.read_gml('tf_tf_graph_all.gml')
G_tf_operon = nx.read_gml('tf_operon_graph_all.gml')
ER_tf = nx.erdos_renyi_graph(nx.number_of_nodes(G_tf_tf), 0.05)
ER_operon = nx.erdos_renyi_graph(nx.number_of_nodes(G_tf_operon), 0.005)

print(mcounter(G_tf_tf, motifs))
print(mcounter(G_tf_operon, motifs))
print(mcounter(ER_tf, motifs))
print(mcounter(ER_operon, motifs))
