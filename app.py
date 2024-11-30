import networkx as nx

COSTOG = 4,32


G = nx.DiGraph()

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

rutas = [
    # Los angeles
    ("Los Angeles", "San Diego", {"costo": 200, "tiempo": 2}),
    ("Los Angeles", "Las Vegas", {"costo": 300, "tiempo": 4}),
    ("Los Angeles", "santa barbara", {"costo": 300, "tiempo": 4}),
    ("Los Angeles", "Palm Springs", {"costo": 300, "tiempo": 4}),
    ("Los Angeles", "Bakersfield", {"costo": 300, "tiempo": 4}),

    # Las Vegas
    ("Las Vegas", "Henderson", {"costo": 50, "tiempo": 0.5}),
    
    # san diego
    ("San Diego", "Riverside", {"costo": 50, "tiempo": 0.5}),
    
    # Bakersfield
    ("Bakersfield", "Riverside", {"costo": 50, "tiempo": 0.5}),
    ("Bakersfield", "Fresno", {"costo": 50, "tiempo": 0.5}),
    ("Bakersfield", "Stockton", {"costo": 50, "tiempo": 0.5}),
    
    # Stockton
    ("Stockton", "Modesto", {"costo": 50, "tiempo": 0.5}),
    ("Stockton", "San Jose", {"costo": 50, "tiempo": 0.5}),
    ("Stockton", "Sacramento", {"costo": 50, "tiempo": 0.5}),

    # San Francisco
    ("San Francisco", "Reno", {"costo": 400, "tiempo": 5}),
    ("San Francisco", "Sacramento", {"costo": 150, "tiempo": 1}),
    ("San Francisco", "San Jose", {"costo": 150, "tiempo": 1}),

    # san jose
    ("San Jose", "Oakland", {"costo": 150, "tiempo": 1}),

    # reno
    ("Reno", "Lake Tahoe", {"costo": 150, "tiempo": 1}),
    ("Reno", "Carson City", {"costo": 150, "tiempo": 1}),
    ("Reno", "Sacramento", {"costo": 150, "tiempo": 1}),

    #Carson City
    ("Carson City", "Elko", {"costo": 150, "tiempo": 1}),
    
    #sacramento
    ("Sacramento", "Chico", {"costo": 150, "tiempo": 1}),

    #Oakland
    ("Oakland", "Palm Springs", {"costo": 150, "tiempo": 1}),

]

G.add_edges_from(rutas)
print(nx.shortest_path(G, "Los Angeles", "San Francisco"))