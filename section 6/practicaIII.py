import pandas as pd

df = pd.read_csv("../../../data/viajes_surfistas.csv")
df

len(df["homecountry"].unique())

grouped = df.groupby("homecountry").agg({"homename": "count"})

sort_grouped = grouped.sort_values("homename", ascending=False)
top_4 = sort_grouped.head(4)


df_otros: pd.DataFrame = sort_grouped.drop(index=top_4.index.values)  # type: ignore
df_otros["país"] = "Otros"
df_otros

df_otros_grouped: pd.DataFrame = df_otros.groupby("país").agg({"homename": "sum"})
df_otros_grouped = df_otros_grouped.reset_index()
df_otros_grouped
top_4 = top_4.reset_index()
top_4.columns = ["país", "homename"]
top_4

df_final = pd.concat([top_4, df_otros_grouped])

df_final = df_final.set_index("país")
ax = df_final.plot.pie(
    y="homename",
    autopct="%1.1f%%",
    startangle=90,
    title="Porcentaje de Surfistas por País de Procedencia",
    figsize=(10, 10),
    fontsize=14,
    explode=(0.1, 0, 0, 0, 0),
    shadow=True,
    colors=["#ff9999", "#66b3ff", "#99ff99", "#ffcc99", "#c2c2f0"],
)

ax.set_ylabel('')
ax.legend(
    title="País de surfistas",
    bbox_to_anchor=(0.8, 1),
    loc=2,
    borderaxespad=0.0,
)
