import networkx as nx
import random
from networkx.algorithms.isomorphism.VF2pp import isomorphic_VF2pp


def assign_labels(G1, G2, mapped_nodes=None):
    colors = [
        "white",
        "black",
        "green",
        "purple",
        "orange",
        "red",
        "blue",
        "pink",
        "yellow",
        "none",
    ]
    for node in G1.nodes():
        color = colors[random.randrange(0, len(colors))]
        G1.nodes[node]["label"] = color
        if mapped_nodes:
            node = mapped_nodes[node]
        G2.nodes[node]["label"] = color

    return G1, G2


def get_labes(G1, G2):
    return nx.get_node_attributes(G1, "label"), nx.get_node_attributes(G2, "label")


class TestVF2pp:
    def test_both_graphs_empty(self):
        G = nx.Graph()
        H = nx.Graph()
        isomorphic, mapping = isomorphic_VF2pp(G, H, {}, {})
        assert isomorphic
        assert mapping == {}

    def test_first_graph_empty(self):
        G = nx.Graph()
        H = nx.Graph([(0, 1)])
        isomorphic, mapping = isomorphic_VF2pp(G, H, {}, {})
        assert not isomorphic
        assert mapping is None

    def test_second_graph_empty(self):
        G = nx.Graph([(0, 1)])
        H = nx.Graph()
        isomorphic, mapping = isomorphic_VF2pp(G, H, {}, {})
        assert not isomorphic
        assert mapping is None

    def test_disconnected_graph(self):
        num_nodes = [100, 330, 579, 631, 799]
        for Vi in num_nodes:
            nodes = [i for i in range(Vi)]
            G1 = nx.Graph()
            G2 = nx.Graph()

            G1.add_nodes_from(nodes)
            G2.add_nodes_from(nodes)

            G1, G2 = assign_labels(G1, G2)
            l1, l2 = get_labes(G1, G2)

            isomorphic, mapping = isomorphic_VF2pp(G1, G2, l1, l2)
            assert isomorphic
            assert len(set(mapping)) == G1.number_of_nodes()

    def test_custom_graph1(self):
        G1 = nx.Graph()
        G2 = nx.Graph()

        edges1 = [(1, 2), (1, 3), (1, 4), (2, 3), (3, 4), (5, 1), (5, 2), (5, 4)]
        edges2 = [("A", "B"), ("A", "C"), ("A", "D"), ("B", "C"), ("C", "D"), ("Z", "A"), ("Z", "B"),
                  ("Z", "D")]
        G1.add_edges_from(edges1)
        G2.add_edges_from(edges2)

        mapped = {1: "A", 2: "B", 3: "C", 4: "D", 5: "Z"}
        G1, G2 = assign_labels(G1, G2, mapped)
        l1, l2 = get_labes(G1, G2)

        isomorphic, mapping = isomorphic_VF2pp(G1, G2, l1, l2)
        assert isomorphic
        assert mapping == mapped

    def test_complete_graph_exhaustive(self):
        num_nodes = [100, 330, 411]
        for Vi in num_nodes:
            G1 = nx.complete_graph(Vi)
            G2 = nx.complete_graph(Vi)

            G1, G2 = assign_labels(G1, G2)
            l1, l2 = get_labes(G1, G2)

            isomorphic, mapping = isomorphic_VF2pp(G1, G2, l1, l2)
            assert isomorphic

    def test_custom_graph2(self):
        G1 = nx.Graph()
        G2 = nx.Graph()

        edges1 = [(1, 2), (1, 5), (5, 6), (2, 3), (2, 4), (3, 4), (4, 5), (2, 7)]
        edges2 = [("A", "C"), ("C", "D"), ("C", "B"), ("C", "E"), ("D", "E"), ("E", "G"), ("G", "F"), ("A", "G")]

        G1.add_edges_from(edges1)
        G2.add_edges_from(edges2)

        mapped = {1: "A", 2: "C", 3: "D", 4: "E", 5: "G", 7: "B", 6: "F"}

        G1, G2 = assign_labels(G1, G2, mapped)
        l1, l2 = get_labes(G1, G2)

        isomorphic, mapping = isomorphic_VF2pp(G1, G2, l1, l2)
        assert isomorphic
        assert mapping == mapped

    def test_custom_graph2_cases(self):
        G1 = nx.Graph()
        G2 = nx.Graph()

        edges1 = [(1, 2), (1, 5), (5, 6), (2, 3), (2, 4), (3, 4), (4, 5), (2, 7)]
        edges2 = [("A", "C"), ("C", "D"), ("C", "B"), ("C", "E"), ("D", "E"), ("E", "G"), ("G", "F"), ("A", "G")]

        colors = [
            "white",
            "black",
            "green",
            "purple",
            "orange",
            "red",
            "blue"
        ]
        G1.add_edges_from(edges1)
        G2.add_edges_from(edges2)

        mapped = {1: "A", 2: "C", 3: "D", 4: "E", 5: "G", 7: "B", 6: "F"}
        for node in G1.nodes():
            color = colors.pop()
            G1.nodes[node]["label"] = color
            G2.nodes[mapped[node]]["label"] = color

        # Adding new nodes
        G1.add_node(0)
        G2.add_node("Z")
        G1.nodes[0]["label"] = G1.nodes[1]["label"]
        G2.nodes["Z"]["label"] = G1.nodes[1]["label"]
        l1, l2 = get_labes(G1, G2)
        mapped.update({0: "Z"})

        isomorphic, mapping = isomorphic_VF2pp(G1, G2, l1, l2)
        assert isomorphic
        assert mapping == mapped

        # Change the color of one of the nodes
        G2.nodes["Z"]["label"] = G1.nodes[2]["label"]
        l1, l2 = get_labes(G1, G2)

        isomorphic, mapping = isomorphic_VF2pp(G1, G2, l1, l2)
        assert not isomorphic
        assert not mapping

        # Add an extra edge
        G1.nodes[0]["label"] = "blue"
        G2.nodes["Z"]["label"] = "blue"
        l1, l2 = get_labes(G1, G2)
        G1.add_edge(0, 0)

        isomorphic, mapping = isomorphic_VF2pp(G1, G2, l1, l2)
        assert not isomorphic
        assert not mapping

        # Add extra edge to both
        G2.add_edge("Z", "Z")
        isomorphic, mapping = isomorphic_VF2pp(G1, G2, l1, l2)
        assert isomorphic
        assert mapping == mapped

    def test_random_graph_cases(self):
        # Two isomorphic GNP graphs
        G1 = nx.gnp_random_graph(300, 0.4, 23)
        G2 = nx.gnp_random_graph(300, 0.4, 23)

        G1, G2 = assign_labels(G1, G2)
        l1, l2 = get_labes(G1, G2)

        isomorphic, mapping = isomorphic_VF2pp(G1, G2, l1, l2)
        assert isomorphic

        # Add one node per graph and give different labels
        G1.add_node(400)
        G2.add_node(400)
        G1.nodes[400]["label"] = "blue"
        G2.nodes[400]["label"] = "red"
        l1.update({400: "blue"})
        l2.update({400: "red"})

        isomorphic, mapping = isomorphic_VF2pp(G1, G2, l1, l2)
        assert not isomorphic

        # Add same number of edges between the new node and the rest of the graph
        G1.add_edges_from([(400, i) for i in range(73)])
        G2.add_edges_from([(400, i) for i in range(73)])

        isomorphic, mapping = isomorphic_VF2pp(G1, G2, l1, l2)
        assert not isomorphic

        # Assign same label to the new node in G1 and G2
        G2.nodes[400]["label"] = "blue"
        l2.update({400: "blue"})

        isomorphic, mapping = isomorphic_VF2pp(G1, G2, l1, l2)
        assert isomorphic

        # Add an extra edge between the new node and itself in one graph
        G1.add_edge(400, 400)
        isomorphic, mapping = isomorphic_VF2pp(G1, G2, l1, l2)
        assert not isomorphic

        # Add two edges between the new node and itself in both graphs
        G1.add_edge(400, 400)
        G2.add_edge(400, 400)
        G2.add_edge(400, 400)

        isomorphic, mapping = isomorphic_VF2pp(G1, G2, l1, l2)
        assert isomorphic
