import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import numpy as np

# Algunos ambientes van a necesitar este modo para poder visualizar los gráficos de Plotly
import plotly

plotly.offline.init_notebook_mode(connected=True)

# Preprocesamiento de datos
raw = pd.read_csv("../../../data/tienda_ventas.csv")
raw["fecha"] = raw["date"].apply(lambda x: x[:7])
raw["anio"] = raw["date"].apply(lambda x: x[:4])
df_2015 = raw[
    (raw["anio"] == "2015") & (raw["family"].isin(["SEAFOOD", "MEATS", "DAIRY"]))
]
agrup = df_2015[["fecha", "family", "sales"]].groupby(["fecha", "family"]).sum()
df2 = agrup.reset_index(1)  # Para seaborn y plotly
df = agrup.unstack()  # Para pandas
df.columns = df.columns.droplevel()

plt.style.use("ggplot")

fig, ((ax1), (ax2), (ax3)) = plt.subplots(3, 1, constrained_layout=True)

fig.set_size_inches(8, 7)
fig.suptitle("Venta de 3 tipos de productos")
fig.supylabel("Ventas en Millones de Dólares")
fig.supxlabel("Periodo")

df.plot.line(y="DAIRY", ax=ax1, color="blue")
df.plot.line(y="MEATS", ax=ax2, color="red")
df.plot.line(y="SEAFOOD", ax=ax3, color="green")

title_font = {"size": 10, "name": "Helvetica"}

ax1.set_title("Lacteos", fontdict=title_font)
ax2.set_title("Carnes", fontdict=title_font)
ax3.set_title("Comida de Mar", fontdict=title_font)

ax1.set_xticklabels([])
ax2.set_xticklabels([])

ax1.set_xlabel("")
ax2.set_xlabel("")
ax3.set_xlabel("")

ax3.set_xticks(np.arange(0, len(df)))
ax3.set_xticklabels(
    df.index.values, rotation=45, fontdict={"color": "grey", "size": 10}
)

ax1.legend().set_visible(False)
ax2.legend().set_visible(False)
ax3.legend().set_visible(False)

# Guardado de Figura - Es importante hacerlo antes de plt.show()
# https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.savefig.html
plt.savefig("../../../NIVEL1/nivel_1.5_matplotlib.png", format="png", dpi=1200)

plt.show()
