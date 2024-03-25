from matplotlib.figure import Figure
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("../../../data/tienda_ventas.csv", index_col="id")
len(df["store_nbr"].unique())

len(df["date"].unique())

df["mes"] = df["date"].apply(lambda x: x[:7])
df["mes"].unique()

sell_by_shop = df.groupby("store_nbr").agg({"sales": "sum"})
sell_by_shop.drop(sell_by_shop[(sell_by_shop["sales"] <= 0)].index, inplace=True)
sell_by_shop
sell_by_shop.describe()

sell_by_shop.plot.box()
sell_by_shop.plot.hist(bins=20)

sell_by_shops_sorted = sell_by_shop.sort_values("sales", ascending=False)
sell_by_shops_sorted

index_top_5: list[int] = sell_by_shops_sorted.index[:5].to_list()
index_top_5

df_top_5 = df[df["store_nbr"].isin(index_top_5)]
df_top_5

df_top_5_by_month = df_top_5.groupby(["store_nbr", "mes"]).agg({"sales": "sum"})
df_top_5_by_month = df_top_5_by_month.reset_index()
df_top_5_by_month

import seaborn as sns

ax = sns.lineplot(
    data=df_top_5_by_month,
    x="mes",
    y="sales",
    hue="store_nbr",
    style="store_nbr",
    markers=True,
)

ax.tick_params(axis="x", labelrotation=90, labelsize=8)

ax.tick_params(axis="y", labelsize=8)

ax.grid(visible=True, axis="x", alpha=0.2)
ax.grid(visible=True, axis="y", alpha=0.2)

ax.legend(title="Top 5 Tiendas", fontsize=8)

ax.set_ylabel("Ventas")
ax.set_xlabel("Meses")

fig = ax.get_figure()
fig.set_size_inches(11, 3)

# Puedo manejar los estilos en un diccionario que tenga como claves las categorías (tiendas) y como valor
# los estilos de las líneas que quiero que tenga cada tienda en el siguiente orden:
# [color, opacidad, marcador, estilo de linea, ancho de linea]
estilos_por_tienda = {
    44: ["grey", 0.4, "+", "--", 1],
    45: ["grey", 0.4, "s", "--", 1],
    47: ["grey", 0.4, "x", "--", 1],
    3: ["red", 1, "o", "-", 1.5],
    46: ["grey", 0.4, "D", "--", 1],
}

# Creo un canvas vacío
fig2, ax2 = plt.subplots()

# Itero sobre mis tiendas
for tienda in index_top_5:
    print(tienda)
    # Obtengo el estilo de esa tienda
    estilos = estilos_por_tienda[tienda]
    # Filtro el dataframe con la tienda que estoy iterando actualmente
    df_tmp = df_top_5_by_month[df_top_5_by_month["store_nbr"] == tienda]

    # Hago un gráfico de lineas solo de esa tienda
    ax2.plot(
        df_tmp["mes"],
        df_tmp["sales"],
        label=tienda,
        markersize=4,
        color=estilos[0],
        alpha=estilos[1],
        marker=estilos[2],
        linestyle=estilos[3],
        linewidth=estilos[4],
    )

    # En la siguiente iteración avanzaré a la siguiente tienda
    # El truco esta en que estoy dibujando todo en el mismo ax2!

# Copiamos las mismas configuraciones de personalización...
ax2.tick_params(axis="x", labelrotation=90, labelsize=8)

ax2.tick_params(axis="y", labelsize=8)

ax2.grid(visible=True, axis="x", alpha=0.2)

ax2.grid(visible=True, axis="y", alpha=0.2)

ax2.legend(
    title="Top 5 tiendas",
    labels=index_top_5,
    bbox_to_anchor=(0, 1),
    fontsize=8,
    loc="upper left",
)

ax2.set_ylabel("Ventas")
ax2.set_xlabel("Mes")
ax2.set_title("Ventas Históricas por mes del TOP 5 Tiendas")

fig2.set_size_inches(11, 3)
