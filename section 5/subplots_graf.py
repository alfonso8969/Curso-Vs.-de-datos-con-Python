import pandas as pd
import matplotlib.pyplot as plt

# Algunos ambientes van a necesitar este modo para poder visualizar los graficos de Plotly
import plotly

plotly.offline.init_notebook_mode(connected=True)

df = pd.read_csv("../../../data/tiendas_procesado.csv", index_col="fecha")

plt.style.use("ggplot")

# Subgráficos
# https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplots.html
fig, axes = plt.subplots(3, 1)

fig, axes = plt.subplots(2, 2)

fig, (ax1, ax2, ax3) = plt.subplots(3, 1, constrained_layout=True)  # Constrained Layout


df.plot.line(y="DAIRY", ax=ax1, color="blue")

df.plot.line(y="MEATS", ax=ax2, color="red")

df.plot.line(y="SEAFOOD", ax=ax3, color="purple")

ax1.set_xticklabels([])
ax2.set_xticklabels([])

ax1.set_xlabel("")
ax2.set_xlabel("")
ax3.set_xlabel("")

ax1.set_title("Lácteos", fontdict={"size": 8, "color": "blue"})
ax2.set_title("Carnes", fontdict={"size": 8, "color": "red"})
ax3.set_title("Pescados", fontdict={"size": 8, "color": "purple"})

ax1.legend().set_visible(False)
ax2.legend().set_visible(False)
ax3.legend().set_visible(False)

fig.suptitle(
    "Ventas de tres tipos de productos", fontdict={"size": 12, "color": "green"}
)

fig.supylabel("Ventas en millones de $", fontdict={"size": 12, "color": "green"})
fig.supxlabel("Periodo", fontdict={"size": 12, "color": "green"})

from plotly.subplots import make_subplots
import plotly.graph_objects as go

fig = make_subplots(rows=3, cols=1, shared_xaxes=True)

fig.append_trace(
    go.Scatter(x=df.index.values, y=df["DAIRY"], name="LACTEOS"), row=1, col=1
)

fig.append_trace(
    go.Scatter(x=df.index.values, y=df["MEATS"], name="CARNES"), row=2, col=1
)

fig.append_trace(
    go.Scatter(x=df.index.values, y=df["SEAFOOD"], name="COMIDA DE MAR"), row=3, col=1
)


fig.update_layout(
    height=600, width=700, title_text="Ventas de 3 Tipos de Productos por Año"
)
fig.show()
