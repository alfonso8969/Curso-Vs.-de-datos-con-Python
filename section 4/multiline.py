import pandas as pd

# import matplotlib.pyplot as plt

df = pd.read_csv("../../../data/tienda_ventas.csv", index_col="id")
df

df["mes"] = df["date"].apply(lambda x: x[:7])
df

sell_by_month = df.groupby("mes").agg({"sales": "sum"})

sell_by_month

df["year"] = df["date"].apply(lambda x: x[0:4])
df

df_2015 = df[
    (df["year"] == "2015") & (df["family"].isin(["SEAFOOD", "MEATS", "DAIRY"]))
]
df_2015

df_2015_grouped = df_2015.groupby(["mes", "family"]).agg({"sales": "sum"})
df_2015_grouped

df_2015_pivot = df_2015_grouped.reset_index()
df_2015_pivot = df_2015_pivot.pivot(index="mes", columns="family", values="sales")
df_2015_pivot.plot.line(subplots=True)
