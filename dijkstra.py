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

nodo = "Los Angeles"

nodosPrevios, distancias = dijkstra(G, nodo)
