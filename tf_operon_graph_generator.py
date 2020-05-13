import csv
import networkx as nx
import re

G_all = nx.DiGraph() # supports directed graphs but no parallel edges allowed
G_strong = nx.DiGraph() # for interactions supported with "Strong" evidence
tf_gene_edge_full = []
tf_dict = {}
nodes = []

with open('Data/network_tf_operon_data_only.txt', newline='') as tf_data:
    tf_data_lines = csv.reader(tf_data, delimiter='\n')
    for row in tf_data_lines:
        source = row[0].split('\t')[0:1]

        targets = row[0].split('\t')[1:2][0]
        pattern = "\[(.*?)\]"
        substring = re.search(pattern, targets).group(1)
        targets_list = substring.split(', ')
        print(targets_list)

        effect = row[0].split('\t')[2:3]
        evidence = row[0].split('\t')[4:5]

        for t in targets_list:
            t_as_list = [t]
            entry = source + t_as_list + effect + evidence
            tf_gene_edge_full.append(entry)

node_label = 0
for interaction in tf_gene_edge_full:
    tf1 = interaction[0].lower()
    tf2 = interaction[1].lower()
    evidence = interaction[3].lower()

    if tf1 in tf_dict.keys():
        pass
    else:
        tf_dict[tf1] = node_label
        node_label += 1
        nodes.append(tf1)
    
    if tf2 in tf_dict.keys():
        pass
    else:
        tf_dict[tf2] = node_label
        node_label += 1
        nodes.append(tf2)

    G_all.add_edge(tf_dict[tf1], tf_dict[tf2])
    with open('tf_operon_graph.txt', 'a') as write_tf:
        write_tf.write(tf1 + '\t' + tf2 + '\n')

    if (evidence == 'strong'):
        G_strong.add_edge(tf_dict[tf1], tf_dict[tf2])
        with open('tf_operon_graph_strong.txt', 'a') as write_tf:
            write_tf.write(tf1 + '\t' + tf2 + '\n')

for n in nodes:
    with open('operon_nodes.txt', 'a') as write_tf:
        write_tf.write(n + '\n')

# nx.write_gml(G_all, 'tf_operon_graph_all.gml')
# nx.write_gml(G_strong, 'tf_operon_graph_strong.gml')
