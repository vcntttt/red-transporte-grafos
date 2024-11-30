import networkx as nx

COSTOG = 4,32


G = nx.DiGraph()

ciudades = [
    "Los Angeles", "San Francisco", "San Diego", "Sacramento", 
    "Reno", "Las Vegas", "Carson City", "Fresno", 
    "Bakersfield", "Oakland", "San Jose", "Santa Barbara", 
    "Stockton", "Modesto", "Chico", "Palm Springs",
    "Elko", "Eureka", "Henderson", "Lake Tahoe"
]
G.add_nodes_from(ciudades)

rutas = [
    ("Los Angeles", "San Diego", {"costo": 200, "tiempo": 2}),
    ("Los Angeles", "Las Vegas", {"costo": 300, "tiempo": 4}),
    ("San Francisco", "Reno", {"costo": 400, "tiempo": 5}),
    ("San Francisco", "Sacramento", {"costo": 150, "tiempo": 1}),
    ("Sacramento", "Reno", {"costo": 250, "tiempo": 3}),
    ("Las Vegas", "Henderson", {"costo": 50, "tiempo": 0.5}),
    ("Reno", "Carson City", {"costo": 100, "tiempo": 1}),
    ("Oakland", "San Jose", {"costo": 100, "tiempo": 1}),
    ("Fresno", "Bakersfield", {"costo": 120, "tiempo": 1.5}),
    ("Palm Springs", "Los Angeles", {"costo": 180, "tiempo": 2}),
    ("Elko", "Carson City", {"costo": 500, "tiempo": 6}),
    ("Lake Tahoe", "Reno", {"costo": 130, "tiempo": 1.5}),
    ("Santa Barbara", "Los Angeles", {"costo": 100, "tiempo": 1.5}),
    ("Stockton", "Modesto", {"costo": 90, "tiempo": 1}),
    ("Chico", "Sacramento", {"costo": 200, "tiempo": 2}),
]

G.add_edges_from(rutas)
print(nx.shortest_path(G, "Los Angeles", "San Francisco"))