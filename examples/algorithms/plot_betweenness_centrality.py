"""
======================
Betweenness Centrality
======================

Betweenness centrality measures of positive gene functional associations
using WormNet v.3-GS.

Data from: https://www.inetbio.org/wormnet/downloadnetwork.php
"""

from random import sample
import networkx as nx
import matplotlib as mpl
import matplotlib.pyplot as plt

# Gold standard data of positive gene functional associations
# from https://www.inetbio.org/wormnet/downloadnetwork.php
G = nx.read_edgelist("WormNet.v3.benchmark.txt")

# remove randomly selected nodes (to make example fast)
num_to_remove = int(len(G) / 1.5)
nodes = sample(list(G.nodes), num_to_remove)
G.remove_nodes_from(nodes)

# remove low-degree nodes
low_degree = [n for n, d in G.degree() if d < 10]
G.remove_nodes_from(low_degree)

# largest connected component
components = nx.connected_components(G)
largest_component = max(components, key=len)
H = G.subgraph(largest_component)

# compute centrality
centrality = nx.betweenness_centrality(H, k=10, endpoints=True)

# compute community structure
lpc = nx.community.label_propagation_communities(H)
community_index = {n: i for i, com in enumerate(lpc) for n in com}

# Map community index to a color
node_colormap = mpl.colormaps["viridis"].resampled(max(community_index.values()))
nx.set_node_attributes(
    G, {n: node_colormap(v) for n, v in community_index.items()}, name="color"
)

# Scale nodes by centrality value
nx.set_node_attributes(G, {n: c * 20000 for n, c in centrality.items()}, name="size")

#### draw graph ####
fig, ax = plt.subplots(figsize=(20, 15))
pos = nx.spring_layout(H, k=0.15, seed=4572321)
nx.set_node_attributes(G, pos, name="pos")
nx.display(
    H,
    node_label=False,
    edge_color="gainsboro",
    node_alpha=0.4,
)

# Title/legend
font = {"color": "k", "fontweight": "bold", "fontsize": 20}
ax.set_title("Gene functional association network (C. elegans)", font)
# Change font color for legend
font["color"] = "r"

ax.text(
    0.80,
    0.10,
    "node color = community structure",
    horizontalalignment="center",
    transform=ax.transAxes,
    fontdict=font,
)
ax.text(
    0.80,
    0.06,
    "node size = betweenness centrality",
    horizontalalignment="center",
    transform=ax.transAxes,
    fontdict=font,
)

# Resize figure for label readability
ax.margins(0.1, 0.05)
fig.tight_layout()
plt.axis("off")
plt.show()
