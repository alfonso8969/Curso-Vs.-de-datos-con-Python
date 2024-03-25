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

ax.legend(
    title="Tipo de Producto",
    labels=["Lácteos", "Carnes", "Comida marítima"],
    labelcolor=["red", "blue", "purple"],
    loc="center",
    bbox_to_anchor=(0.4, 0.6),
    fontsize=10,
    title_fontproperties={"size": 10},
    ncol=3,
)

import plotly.express as px

fig = px.line(
    df,
    width=800,
    height=500,
    template="ggplot2",
    title="Ventas de 3 Tipos de Productos por Año",
    labels={
        "x": "Periodo",
        "sales": "Ventas por año (en millones de $)",
        "family": "Tipo de Producto",
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

fig.add_annotation(
    x="2015-11",
    y=1300000,
    text="Noviembre",
    showarrow=True,
    arrowhead=3,
    arrowsize=1,
    arrowwidth=2,
    arrowcolor="grey",
    opacity=1,
    font={"family": "Arial", "size": 10, "color": "black"},
)

fig.add_hline(
    y=1400000,
    line_dash="dot",
    annotation_text="Límite",
    annotation_position="top left",
    annotation_font_size=10,
    annotation_font_color="red",
    opacity=0.8,
    line_width=1,
    line_color="red",
)

fig.update_layout(
    # showlegend=False # Ocultar leyenda,
    legend_title_text="Leyenda",  # Titulo de la leyenda
    legend=dict(
        y=0.5,  # Posicionamiento de la leyenda
        x=1.05,
        font=dict(  # Puedo darle estilos a mis leyendas: https://plotly.com/python/legend/#styling-legends
            family="Courier", size=12, color="black"
        ),
        bgcolor="LightGrey",
        bordercolor="Black",
        borderwidth=2,
    ),
)

fig.show()
