import networkx as nx
import matplotlib.pyplot as plt
from grafo import G

# Ejercicio 4
a = 0.6

# en data viene un diccionario con los pesos
for u, v, data in G.edges(data=True):
    data["peso"] = a * data["costo"] + (1 - a) * data["tiempo"]


plt.figure(figsize=(12, 8))
layout = nx.spring_layout(G, seed=1)
nx.draw_networkx_nodes(G, layout, node_color="orange", node_size=500)
nx.draw_networkx_labels(G, layout, font_weight="bold", font_size=7)

labels = {(u, v): f"{d['peso']:.2f}" for u, v, d in G.edges(data=True)}
nx.draw_networkx_edges(G, layout, edgelist=G.edges, edge_color="green", width=2.5)
nx.draw_networkx_edge_labels(G, layout, edge_labels=labels)
plt.show()