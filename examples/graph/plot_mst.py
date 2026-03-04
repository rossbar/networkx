"""
=====================
Minimum Spanning Tree
=====================

A minimum spanning tree (MST) is a subset of edges in a weighted,
connected graph that connects all vertices together with the
minimum possible total edge weight. The `minimum_spanning_tree`
function is used to compare the original graph with its MST.

"""

import networkx as nx
import matplotlib.pyplot as plt

# Create a graph
G = nx.Graph()
G.add_edges_from(
    [
        (0, 1, {"weight": 4}),
        (0, 7, {"weight": 8}),
        (1, 7, {"weight": 11}),
        (1, 2, {"weight": 8}),
        (2, 8, {"weight": 2}),
        (2, 5, {"weight": 4}),
        (2, 3, {"weight": 7}),
        (3, 4, {"weight": 9}),
        (3, 5, {"weight": 14}),
        (4, 5, {"weight": 10}),
        (5, 6, {"weight": 2}),
        (6, 8, {"weight": 6}),
        (7, 8, {"weight": 7}),
    ]
)

# Find the minimum spanning tree
T = nx.minimum_spanning_tree(G)

# Visualize the graph and the minimum spanning tree
pos = nx.spring_layout(G)
nx.set_node_attributes(G, pos, name="pos")
nx.set_node_attributes(T, pos, name="pos")
display_opts = {"node_color": "lightblue", "node_size": 500, "edge_color": "gray"}

nx.display(G, node_label=True, edge_label="weight", **display_opts)
nx.display(T, node_visible=False, edge_color="green", edge_width=2)
plt.axis("off")
plt.show()
