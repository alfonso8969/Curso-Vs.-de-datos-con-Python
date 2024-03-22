import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


df = pd.read_csv("../../../data/tiendas_procesado.csv", index_col="fecha")
df

plt.style.use("ggplot")
ax = df.plot.line(
    figsize=(10, 5), title="Tiendas Procesadas por 3 tipos de producto y meses 2015"
)

ticks_positions = np.arange(0, len(df))

ax.set_xticks(ticks_positions)
ax.set_xticklabels(df.index.values, rotation=45)

ax.set_xlabel("Período", loc="left")

ax.set_ylabel("Ventas (en millones de dólares)", loc="bottom")

import seaborn as sns

plt.figure(figsize=(10, 5))

plt.title("Tiendas Procesadas por tipos de producto y meses 2015")
plt.xlabel("Período")
plt.ylabel("Ventas (en millones de dólares)")

""" fig, pltax = plt.subplots()
print(pltax) """

sns.set_style("ticks")
sns.set_theme("paper")


bx = sns.lineplot(data=df)
bx.set(
    xlabel="Período meses",
    ylabel="Ventas productos (en millones de dólares)",
    title="Tiendas Procesadas para tres productos y meses 2015",
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

fig.update_xaxes(tickangle=-45, tickvals=df.index.values, tickwidth=3, tickmode="array")

fig.update_yaxes(nticks=5, dtick=250000)

fig.update_layout(
    xaxis_title="PERÍODO MESES",
    yaxis_title="VENTAS",
    title="TIENDAS PROCESADAS PARA TRES PRODUCTOS Y MESES 2015",
    xaxis_tickangle=-45,
)

fig.show()
