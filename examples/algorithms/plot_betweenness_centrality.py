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
central_nodes = sorted(centrality, key=centrality.get, reverse=True)

#### draw graph ####
fig, ax = plt.subplots(figsize=(20, 15))
pos = nx.spring_layout(H, k=0.15, seed=4552321)
# Set color bounds
deg = [d for _, d in H.degree()]
vmin, vmax = min(deg), max(deg)

# Plot largest connected component with low alpha as background
nx.draw_networkx(
    H,
    pos=pos,
    with_labels=False,
    node_size=10,
    node_color=deg,
    cmap=plt.get_cmap("hot"),
    vmin=vmin,
    vmax=vmax,
    edge_color="gray",
    alpha=0.1,
)
# Highlight the n most central nodes
n = 10
most_central_nodes = central_nodes[:n]

nx.draw_networkx_nodes(
    H,
    pos=pos,
    nodelist=most_central_nodes,
    node_size=50,
    node_color=[d for _, d in H.degree(most_central_nodes)],
    cmap=plt.get_cmap("hot"),
    vmin=vmin,
    vmax=vmax,
    alpha=1.0,
)
# Highlight all edges connected to the n most central nodes
edgelist = []
for node in most_central_nodes:
    edgelist.extend(list(H.edges(node)))
nx.draw_networkx_edges(H, pos=pos, edgelist=edgelist)


# Title/legend
font = {"color": "k", "fontweight": "bold", "fontsize": 16}
ax.set_title(
    "Gold standard data of positive gene functional associations (C. elegans)", font
)

# Change font for inset text
font["fontweight"] = None
ax.text(
    0.80,
    0.06,
    f"Bolded nodes & black edges highlight the {n} nodes with highest betweenness centrality",
    horizontalalignment="center",
    transform=ax.transAxes,
    fontdict=font,
)

# Resize figure for label readibility
ax.margins(0.1, 0.05)
fig.tight_layout()
plt.axis("off")
plt.show()
