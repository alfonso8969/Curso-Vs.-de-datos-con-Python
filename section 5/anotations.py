import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


df = pd.read_csv("../../../data/tiendas_procesado.csv", index_col="fecha")

plt.style.use("ggplot")
ax = df.plot.line(figsize=(10, 4))

ax.set_title(
    "Ventas de 3 Tipos de Productos por Año",
    fontdict={"size": 18, "name": "Times new Roman"},
)

ax.set_xlabel(
    "Período", fontdict={"name": "Times new Roman", "color": "black", "size": 12}
)


ax.set_ylabel(
    "Ventas (en Millones de Dólares)",
    fontdict={"name": "Times new Roman", "color": "black", "size": 12},
)

ax.set_xticks(np.arange(0, len(df)))
ax.set_xticklabels(df.index.values, rotation=45, fontdict={"color": "grey", "size": 10})

ax.annotate(
    "Inicio crisis financiera",
    xy=(10, 1250000),
    xytext=(10, 1000000),
    size=10,
    horizontalalignment="center",
    color="red",
    arrowprops={"width": 1, "headwidth": 5, "headlength": 5, "color": "red"},
)

max_dairy = df["DAIRY"].max()
ax.axhline(y=int(max_dairy), color="green", linestyle="--")

ax.annotate(
    "Umbral máximo de ventas de lácteos",
    fontstyle="italic",
    alpha=0.8,
    size=8,
    xy=(11, int(max_dairy) + 10000),
    horizontalalignment="right",
    color="green",
)

import plotly.express as px


fig = px.line(
    df,
    width=800,
    height=500,
    template="ggplot2",
    title="Ventas de 3 Tipos de Productos por Año",
    labels={
        "fecha": "Periodo",
        "value": "Ventas por año (en millones de $)",
        "variable": "Tipo de Producto",
    },
)

fig.update_layout(font_family="Rockwell", font_color="black")

fig.update_xaxes(
    tickangle=45,
    tickmode="array",
    tickvals=df.index.values,
    tickfont={"color": "grey", "size": 10},
)

fig.update_yaxes(tickfont={"color": "grey", "size": 10})

fig.update_yaxes(nticks=20)

# Anotaciones en Plotly
# https://plotly.com/python/text-and-annotations/#styling-and-coloring-annotations
fig.add_annotation(
    x="2015-11",  # Debido a que este es el valor original
    y=1300000,
    text="Noviembre",
    showarrow=True,
    arrowhead=3,  # Tipos de flecha: numero del 0 al 8
    arrowsize=1,  # Tamaño de la cabeza de la flecha
    arrowwidth=2,  # Ancho de la flecha en pixeles
    arrowcolor="grey",
    opacity=1,
    font={"family": "Arial", "size": 10, "color": "black"},
)
fig.add_annotation(
    x="2015-2",  # Debido a que este es el valor original
    y=1050000,
    text="Febrero",
    showarrow=True,
    arrowhead=3,  # Tipos de flecha: numero del 0 al 8
    arrowsize=1,  # Tamaño de la cabeza de la flecha
    arrowwidth=2,  # Ancho de la flecha en pixeles
    arrowcolor="grey",
    opacity=1,
    font={"family": "Arial", "size": 10, "color": "black"},
)

# Marcas en Plotly
# https://plotly.com/python/horizontal-vertical-shapes/#adding-text-annotations
fig.add_hline(
    y=1400000,
    line_dash="dot",
    annotation_text="Límite",  # Puedo incluir al mismo tiempo una anotación
    annotation_position="top left",  # "top left", "top right", "bottom left", "bottom", "top"
    annotation_font_size=10,
    annotation_font_color="red",
    opacity=0.8,
    line_width=1,
    line_color="red",
)

fig.show()
