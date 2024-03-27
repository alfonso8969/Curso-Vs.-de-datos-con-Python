import pandas as pd
import holoviews as hv
from holoviews import opts, dim
hv.extension("bokeh")
hv.output(size=200)

nodes = pd.read_csv("../../../data/grafo_interaccion/nodes.csv")
nodes
edges = pd.read_csv("../../../data/grafo_interaccion/edges.csv")
edges

hv.Chord(edges)

nodos = hv.Dataset(nodes, "id")
chord = hv.Chord((edges, nodos))
chord.opts(
    opts.Chord(
        labels='label',
        edge_color=dim('src').str(),  # 'src' es el origen de la conexión
        node_color=dim('label').str(),  # 'label' es el nombre del nodo
        cmap='Category20',
        edge_cmap='Category20',
    )
)