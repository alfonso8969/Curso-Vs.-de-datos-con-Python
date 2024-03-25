import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("../../../data/algorithm_comparison.csv", index_col="dataset")

fields = ["algoritmo1", "algoritmo2"]

ax = df.plot.bar(
    figsize=(12, 6),
    y=fields,  # type: ignore
    title="Evaluación Algoritmo1 vs Algoritmo2",
)

ax.legend(
    loc="upper left", bbox_to_anchor=(0, 1), labels=["Algoritmo 1", "Algoritmo 2"]
)

ax.set_xlabel("Dataset", fontdict={"color": "black", "size": 12})

ax.set_ylabel("Rendimiento", fontdict={"color": "black", "size": 12})

ax.set_xticklabels(df.index.values, rotation=45)

ax.set_axisbelow(True)

ax.xaxis.grid(
    color="blue",
    alpha=0.2,
)

ax.yaxis.grid(
    color="blue",
    alpha=0.2,
)

plt.savefig("ejercicio1barras.png", format="png", bbox_inches="tight")
