import pandas as pd


df = pd.read_csv("../../../data/tienda_ventas.csv", index_col=0)
df = df.dropna()
df["periodo"] = df["date"].apply(lambda x: x[:7])
df

tiendas_agrupadas = (
    df[
        (df["family"] == "BEVERAGES")
        & (df["store_nbr"].isin([3, 44, 45, 46, 47, 48, 49, 50]))
    ]
    .groupby(["periodo", "store_nbr"])
    .agg({"sales": 'sum'})
)
tiendas_agrupadas

pivote = tiendas_agrupadas.unstack().droplevel(0, axis=1).transpose()  # type: ignore
pivote

import seaborn as sns
import matplotlib.pyplot as plt

plt.figure(figsize=(15, 8))
sns.heatmap(
    pivote, 
    cmap="Blues",
    square=True, 
    linewidths=0.1,
    # annot=True
)
plt.title("Ventas por tienda y mes")

plt.show()