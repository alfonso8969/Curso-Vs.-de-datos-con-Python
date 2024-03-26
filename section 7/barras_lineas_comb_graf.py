import pandas as pd

# Crear un DataFrame
df = pd.read_csv("../../../data/paises_vida.csv", index_col=0)
df = df.dropna()

df_africa = df[df["continent"] == "Africa"]
df_africa = df_africa.sort_values(by="lifeExp", ascending=False)
df_africa_grouped = df_africa.groupby("year").agg(
    {"lifeExp": "mean", "pop": "sum", "gdpPercap": "mean"}
)

df_africa_grouped = df_africa_grouped.reset_index()
df_africa_grouped

import seaborn as sns
import matplotlib.pyplot as plt

fig, ax1 = plt.subplots(figsize=(8, 4))

sns.set_style("whitegrid")

ax = sns.barplot(
    x="year", y="lifeExp", 
    data=df_africa_grouped, 
    color="skyblue", 
    alpha=0.8,
    ax=ax1
)
plt.title("Life Expectancy in Africa", loc='center', color='blue', fontsize=15)
plt.suptitle("GPD per Capita in Africa", color="red", fontsize=15, y=1.05)


ax.tick_params(
    axis='y',
    labelcolor='blue'
)
ax.set_ylabel("Life Expectancy", color="blue")
ax.set_xlabel("Year", color="black")

ax2 = ax1.twinx()
ax2.tick_params(axis="y", labelcolor="red")
ax2.set_ylabel("GDP per Capita", color="red")
ax2.grid(visible=False)

sns.lineplot(
    data=df_africa_grouped["gdpPercap"],  # type: ignore
    color="red",
    linewidth=2,
    marker="D",
    ax=ax2,
)
plt.show()
