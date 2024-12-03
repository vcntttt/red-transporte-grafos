import networkx as nx
import matplotlib.pyplot as plt
from grafo import G

class Node:
    def __init__(self, id):
        self.id = id
        self.parent = self
        self.rank = 0

def find(node):
    if node.parent != node:
        node.parent = find(node.parent)
    return node.parent

def union(N_A, N_B):
    root1 = find(N_A)
    root2 = find(N_B)
    if root1 != root2:
        if root1.rank > root2.rank:
            root2.parent = root1
        else:
            root1.parent = root2
            if root1.rank == root2.rank:
                root2.rank += 1

def kruskal(graph):
    edges = []
    for N_a, N_b, datos in graph.edges(data=True):
        edges.append((datos["costo"], datos["tiempo"], N_a, N_b))
    edgess = sorted(edges, key=lambda x: x[0])
    mst = []
    nodes = {node: Node(node) for node in graph.nodes}
    for costo, tiempo, N_a, N_b in edgess:
        if find(nodes[N_a]) != find(nodes[N_b]):
            mst.append((N_a, N_b, costo, tiempo))
            union(nodes[N_a], nodes[N_b])
    return mst

mst = kruskal(G)

posicionNodos = nx.spring_layout(G, seed=5)
plt.figure(figsize=(12,8))
nx.draw_networkx_nodes(G, posicionNodos, node_color="orange", node_size=1000)
nx.draw_networkx_labels(G, posicionNodos, font_weight="bold", font_size=7)
etiquetasAristas = {(u, v): f"${d['costo']}" for u, v, d in G.edges(data=True)}

nx.draw_networkx_edges(G, posicionNodos, edgelist=mst, edge_color="green", width=2.5)

nx.draw_networkx_edge_labels(G, posicionNodos, edge_labels=etiquetasAristas, font_color="green", font_size=8)

plt.show()
