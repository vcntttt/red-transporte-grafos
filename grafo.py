import networkx as nx
import matplotlib.pyplot as plt

COSTO_GALON = 4.32  # costo del galón EEUU
EFICIENCIA = 5.7  # millas por galón

G = nx.Graph()

ciudades = [
    "Los Angeles",
    "San Francisco",
    "San Diego",
    "Sacramento",
    "Reno",
    "Las Vegas",
    "Carson City",
    "Fresno",
    "Bakersfield",
    "Oakland",
    "San Jose",
    "Santa Barbara",
    "Stockton",
    "Modesto",
    "Chico",
    "Palm Springs",
    "Elko",
    "Henderson",
    "Lake Tahoe",
    "Riverside"
]
G.add_nodes_from(ciudades)

# costos: dolares
# tiempo: horas
rutas = [
    # Los Angeles
    ("Los Angeles", "San Diego", {"costo": 90, "tiempo": 2}),
    ("Los Angeles", "Las Vegas", {"costo": 203, "tiempo": 4}),
    ("Los Angeles", "Santa Barbara", {"costo": 30, "tiempo": 0.6}),
    ("Los Angeles", "Palm Springs", {"costo": 82, "tiempo": 1.5}),
    ("Los Angeles", "Bakersfield", {"costo": 86, "tiempo": 1.6}),

    # Las Vegas
    ("Las Vegas", "Henderson", {"costo": 13, "tiempo": 0.4}),

    # San Diego
    ("San Diego", "Riverside", {"costo": 73, "tiempo": 1.5}),

    # Bakersfield
    ("Bakersfield", "Riverside", {"costo": 125, "tiempo": 2.5}),
    ("Bakersfield", "Fresno", {"costo": 82, "tiempo": 1.5}),
    #("Bakersfield", "Stockton", {"costo": 177, "tiempo": 3.5}),

    # Stockton
    ("Stockton", "Modesto", {"costo": 21, "tiempo": 0.5}),
    ("Stockton", "San Jose", {"costo": 60, "tiempo": 1}),
    ("Stockton", "Sacramento", {"costo": 34, "tiempo": 0.8}),

    # San Francisco
    ("San Francisco", "Reno", {"costo": 168, "tiempo": 3.5}),
    ("San Francisco", "Sacramento", {"costo": 64, "tiempo": 1.5}),
    ("San Francisco", "San Jose", {"costo": 36, "tiempo": 1}),

    # San Jose
    ("San Jose", "Oakland", {"costo": 30, "tiempo": 0.7}),

    # Reno
    ("Reno", "Lake Tahoe", {"costo": 28, "tiempo": 0.8}),
    ("Reno", "Carson City", {"costo": 23, "tiempo": 0.5}),
    ("Reno", "Sacramento", {"costo": 99, "tiempo": 2}),

    # Carson City
    ("Carson City", "Elko", {"costo": 239, "tiempo": 4.5}),

    # Sacramento
    ("Sacramento", "Chico", {"costo": 68, "tiempo": 1.5}),

    # Oakland
    ("Oakland", "Palm Springs", {"costo": 362, "tiempo": 7.5}),

]

G.add_edges_from(rutas)

plt.figure(figsize=(12, 8))  # Ajustar tamaño del gráfico
pos = nx.spring_layout(G, seed=7)  # Elegir un layout para los nodos (opciones: spring, circular, random, etc.)
nx.draw_networkx_nodes(G, pos, node_color="orange", node_size=500)
nx.draw_networkx_labels(G, pos, font_weight="bold", font_size=7)

# # Opcional: Añadir etiquetas con pesos de las aristas
edge_labels = {(u, v): f"{d['costo']} / {d['tiempo']}" for u, v, d in G.edges(data=True)}
nx.draw_networkx_edges(G, pos, edgelist=G.edges, edge_color="green", width=2.5)
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_size=8)

# # Mostrar el gráfico
plt.title("Mapa de ciudades y rutas", fontsize=14)
plt.show()