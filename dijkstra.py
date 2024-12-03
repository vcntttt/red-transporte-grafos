import sys, networkx as nx
import matplotlib.pyplot as plt
from grafo import G

def dijkstra(g, nodoInicio):
    nodosSinVisitar = list(g.nodes)
    valorMaximo = sys.maxsize
    caminoCorto = {nodo: valorMaximo for nodo in nodosSinVisitar}
    tiempoCorto = {nodo: valorMaximo for nodo in nodosSinVisitar}
    caminoCorto[nodoInicio] = 0
    tiempoCorto[nodoInicio] = 0
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
            tiempo = tiempoCorto[nodoMinimo] + g[nodoMinimo][vecino]["tiempo"]
            if valorTentativo < caminoCorto[vecino]:
                caminoCorto[vecino] = valorTentativo
                tiempoCorto[vecino] = tiempo
                nodosPrevios[vecino] = nodoMinimo
 
        nodosSinVisitar.remove(nodoMinimo)
    
    return nodosPrevios, caminoCorto, tiempoCorto

nodoInicial = "Los Angeles"

nodosPrevios, distancias, tiempos = dijkstra(G, nodoInicial)
posicionNodos = nx.spring_layout(G, seed=5)
plt.figure(figsize=(12,8))
nx.draw_networkx_nodes(G, posicionNodos, node_color="orange", node_size=1000)
nx.draw_networkx_labels(G, posicionNodos, font_weight="bold", font_size=7)
#etiquetasAristas = {(u, v): f"${d['costo']}" for u, v, d in G.edges(data=True)}

for nodo, nodoPrevio in nodosPrevios.items():
    nx.draw_networkx_edges(G, posicionNodos, edgelist=[(nodoPrevio, nodo)], edge_color="green", width=2.5)

#nx.draw_networkx_edge_labels(G, posicionNodos, edge_labels=etiquetasAristas, font_color="green", font_size=8)

for nodo in G.nodes():
    distancia = distancias.get(nodo, "∞")
    tiempo = tiempos.get(nodo, "∞")
    plt.text(posicionNodos[nodo][0], posicionNodos[nodo][1] + 0.05, s=f"{distancia} (mi) {tiempo:.1f} (h)", bbox=dict(facecolor="yellow", alpha=0.5), horizontalalignment="center", fontsize=8)

plt.show()
