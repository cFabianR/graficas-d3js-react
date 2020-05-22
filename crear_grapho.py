import json
import numpy as np
import networkx as nx
import matplotlib.pyplot as plt

g = nx.karate_club_graph()
fig, ax = plt.subplots(1, 1, figsize=(8, 6))
nx.draw_networkx(g, ax=ax)

with open('karate_club_graph.json', 'w') as outfile1:
    outfile1.write(json.dumps(nx.node_link_data(g)))
