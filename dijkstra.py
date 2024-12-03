import sys, networkx as nx
import matplotlib.pyplot as plt
from grafo import G

def dijkstra(g, nodoInicio):
    nodosSinVisitar = list(g.nodes)
    valorMaximo = sys.maxsize
    caminoCorto = {nodo: valorMaximo for nodo in nodosSinVisitar}
    caminoCorto[nodoInicio] = 0
    nodosPrevios = {}

    while nodosSinVisitar:
        nodoMinimo = None
        for node in nodosSinVisitar: 
            if nodoMinimo == None:
                nodoMinimo = node
            elif caminoCorto[node] < caminoCorto[nodoMinimo]:
                nodoMinimo = node
                
        vecinos = g.neighbors(nodoMinimo)
        for vecino in vecinos:
            valorTentativo = caminoCorto[nodoMinimo] + g[nodoMinimo][vecino]["costo"]
            if valorTentativo < caminoCorto[vecino]:
                caminoCorto[vecino] = valorTentativo
                nodosPrevios[vecino] = nodoMinimo
 
        nodosSinVisitar.remove(nodoMinimo)
    
    return nodosPrevios, caminoCorto

nodoInicial = "Los Angeles"

nodosPrevios, distancias = dijkstra(G, nodoInicial)
posicionNodos = nx.spring_layout(G, seed=5)
plt.figure(figsize=(12,8))
nx.draw(G, posicionNodos, with_labels=True, node_color="lightblue", font_weight="bold", node_size=1500, font_size=10)
etiquetasAristas = {(u, v): f"${d['costo']}" for u, v, d in G.edges(data=True)}

for nodo, nodoPrevio in nodosPrevios.items():
    nx.draw_networkx_edges(G, posicionNodos, edgelist=[(nodoPrevio, nodo)], edge_color="red", width=2.5)

nx.draw_networkx_edge_labels(G, posicionNodos, edge_labels=etiquetasAristas, font_color="green", font_size=8)

for nodo, distancia in distancias.items():
    plt.text(posicionNodos[nodo][0], posicionNodos[nodo][1] + 0.05, s=f"{distancia} (mi)", bbox=dict(facecolor="yellow", alpha=0.5), horizontalalignment="center", fontsize=8,)

plt.show()
