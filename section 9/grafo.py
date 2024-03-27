import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt

nodos = pd.read_csv("../../../data/grafo_interaccion/nodes.csv")
nodos
ejes = pd.read_csv("../../../data/grafo_interaccion/edges.csv")
ejes

G = nx.from_pandas_edgelist(ejes, source="src", target="dst", edge_attr="weight")
plt.rcParams["figure.figsize"] = (15, 8)
nx.draw(G)

nx.draw_networkx(G)

nx.draw_random(G)

# También se le denomina "Diagrama de Cuerdas sin Lazos"
nx.draw_circular(G)

nx.draw_planar(G)

nx.draw_spring(G)

# https://networkx.org/documentation/stable/reference/generated/networkx.drawing.nx_pylab.draw_networkx.html
nx.draw_spring(
    G,
    with_labels=True,
    node_size=300,
    node_color="red",  # alpha=0.5,
    width=1,
    style=":",  # solid, dashed | mismos que matplotlib
    font_size=16,
)

# Con tamaño variable dependiendo de atributo numérico de los nodos
nx.draw_spring(
    G,
    with_labels=True,
    nodelist=list(nodos['id']),
    node_size=list(nodos['pagerank'] * 200),
    node_color='red'
)

# Con tamaño y color variable dependiendo de atributo numérico de los nodos
nx.draw_spring(
    G,
    with_labels=True,
    nodelist=list(nodos['id']),
    node_size=list(nodos['pagerank'] * 200),
    node_color=list(nodos['community']),
    cmap='tab10'
)

# Con tamaño ancho de ejes variables dependiendo del peso de la conexión
nx.draw_spring(
    G,
    with_labels=True,
    nodelist=list(nodos['id']),
    node_size=list(nodos['pagerank'] * 200),
    node_color=list(nodos['community']),
    cmap='tab10',
    width=list(ejes['weight'] / 7)
)

# Rápidamente se pueden volver ilegibles si tenemos muchos nodos o ejes...
nodos2 = pd.read_csv('../../../data/grafo_interaccion_gephi/nodes.csv')
ejes2 = pd.read_csv('../../../data/grafo_interaccion_gephi/edges.csv')
G2 = nx.from_pandas_edgelist(
    ejes2,
    source='Source',
    target='Target',
    edge_attr='weight'
)
plt.rcParams["figure.figsize"] = (25, 16)
nx.draw(G2)