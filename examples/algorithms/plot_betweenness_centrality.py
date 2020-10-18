"""
=====================
Betweeness Centrality
=====================

Betweenness centrality measures of positive gene functional associations
using WormNet v.3-GS.

Data from: https://www.inetbio.org/wormnet/downloadnetwork.php
"""

import networkx as nx
import matplotlib.pyplot as plt

# Gold standard data of positive gene functional associations
# from https://www.inetbio.org/wormnet/downloadnetwork.php
G = nx.read_edgelist("WormNet.v3.benchmark.txt")

# largest connected component
components = nx.connected_components(G)
largest_component = max(components, key=len)
H = G.subgraph(largest_component)

# compute centrality
centrality = nx.betweenness_centrality(H, k=10, endpoints=True)

#### draw graph ####
fig, ax = plt.subplots(figsize=(20, 15))
pos = nx.spring_layout(H, k=0.15, seed=4552321)
node_color = [d * 10 for n, d in H.degree()]
node_size = [v * 20000 for v in centrality.values()]
# node_size = [d * 20000 for n, d in H.degree()]
# node_color = [v * 10000 for v in centrality.values()]
nx.draw_networkx(
    H,
    pos=pos,
    with_labels=False,
    cmap=plt.get_cmap("hot"),
    node_color=node_color,
    node_size=node_size,
    edge_color="gray",
    alpha=0.4,
)

# Title/legend
font = {"color": "k", "fontweight": "bold", "fontsize": 16}
ax.set_title(
    "Gold standard data of positive gene functional associations (C. elegans)", font
)
# Change font color for legend
font["color"] = "r"

ax.text(
    0.80,
    0.10,
    "node color = degree",
    horizontalalignment="center",
    transform=ax.transAxes,
    fontdict=font,
)
ax.text(
    0.80,
    0.06,
    "node size = betweeness centrality",
    horizontalalignment="center",
    transform=ax.transAxes,
    fontdict=font,
)

# Resize figure for label readibility
ax.margins(0.1, 0.05)
fig.tight_layout()
plt.axis("off")
plt.show()
