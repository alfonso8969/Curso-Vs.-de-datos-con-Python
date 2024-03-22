import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


df = pd.read_csv("../../../data/tiendas_procesado.csv", index_col="fecha")
df

plt.style.use("ggplot")
ax = df.plot.line(
    figsize=(10, 5)
)

ax.set_title(
    label="Tiendas Procesadas por tipos de producto y meses 2015",
    fontdict={
        "fontsize": 16,
        "fontweight": "bold",
        "color": "green"
    }
)

ticks_positions = np.arange(0, len(df))

ax.set_xticks(ticks_positions)
ax.set_xticklabels(
    df.index.values,
    rotation=45,
    fontdict={
        "fontsize": 10,
        "fontweight": "bold",
        "color": "red"
    })

ax.set_xlabel(
    "Período",
    fontdict={
        "fontsize": 12,
        "fontweight": "bold",
        "color": "red"
    })

ax.set_ylabel(
    "Ventas (en millones de dólares)",
    fontdict={
        "fontsize": 12,
        "fontweight": "bold",
        "color": "blue"
    })


plt.yticks(
    color="blue",
    name="Times New Roman",
    size=12,
    weight='bold'
)


import plotly.express as px

fig = px.line(
    df,
    width=800,
    height=500,
    template="ggplot2",
    title="Tiendas Procesadas para tres productos y meses 2015",
    labels={
        "fecha": "Período meses",
        "value": "Ventas productos (en millones de $)",
        "variable": "Tipo de producto",
    },
)

fig.update_xaxes(
    tickangle=-45,
    tickvals=df.index.values,
    tickwidth=3,
    tickmode="array",
    tickfont={
        "size": 12,
        "color": "brown",
        "family": "Rockwell"
    })

fig.update_yaxes(nticks=5, dtick=250000)

fig.update_layout(
    xaxis_title="PERÍODO MESES",
    yaxis_title="VENTAS",
    title="TIENDAS PROCESADAS PARA TRES PRODUCTOS Y MESES 2015",
    xaxis_tickangle=-45,
    font_color='blue',
    font_family="Courier New",
    title_font_size=16,
    legend_font_color="green",

)

fig.show()
