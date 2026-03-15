"""
================
Visibility Graph
================

Visibility Graph constructed from a time series
"""

import matplotlib.pyplot as plt

import networkx as nx

time_series = [0, 2, 1, 3, 2, 1, 3, 2, 1, 3, 2, 1, 3, 4, 0]
# or
# import random
# time_series = [random.randint(1, 10) for i in range(10)]

G = nx.visibility_graph(time_series)

labels = nx.get_node_attributes(G, "value")

fig, all_axes = plt.subplots(2, 1, num="Visibility Graph", figsize=(8, 12))
axs = all_axes.flat

layouts_params = {
    # a layout emphasizing the line-of-sight connectivity
    "Line-of-Sight Connectivity": {
        "pos": {x: (x, 0) for x in range(len(time_series))},
        "connectionstyle": "arc3,rad=-1.57079632679",
    },
    # a layout showcasing the time series values
    "Time Series values with Connectivity": {
        "pos": {i: (i, v) for i, v in enumerate(time_series)}
    },
}

# Two different layouts: one emphasizing line-of-sight connectivity and a
# second for highlighting the time series values
nx.set_node_attributes(
    G, {x: (x, 0) for x in range(len(time_series))}, name="Line-of-Sight Connectivity"
)
nx.set_node_attributes(
    G,
    {n: (n, v) for n, v in enumerate(time_series)},
    name="Time Series values with Connectivity",
)

for layout, connectionstyle, ax in zip(
    ("Line-of-Sight Connectivity", "Time Series values with Connectivity"),
    ("arc3,rad=-1.57", "arc3"),
    axs,
):
    ax.set_title(layout)
    ax.margins(0.10)
    ax.set_xlabel("Time", size=10)
    nx.display(
        G,
        canvas=ax,
        node_pos=layout,
        node_alpha=0.5,
        node_label="value",
        edge_curvature=connectionstyle,
        edge_arrowstyle="<->",
        edge_arrowsize=10,
    )

axs[1].set_ylabel("Value", size=10)

fig.suptitle("Visibility Graph")
fig.tight_layout()
plt.show()
