import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("../../../data/datasets_top_4.csv", index_col="dataset")
df

plt.style.use("ggplot")

df1 = df.iloc[0:13:]
df2 = df.iloc[13:, :]


fig, (ax1, ax2) = plt.subplots(
    1,
    2,
    constrained_layout=True,
)

df1.plot.barh(
    stacked=True,
    ax=ax1,
    width=0.4,
    color={
        'cat1': '#000086',
        'cat2': '#5396f4',
        'cat3': '#a1dbe8',
        'otros': '#DADADA'
    }
)
df2.plot.barh(
    stacked=True,
    ax=ax2,
    width=0.4,
    color={
        'cat1': '#000086',
        'cat2': '#5396f4',
        'cat3': '#a1dbe8',
        'otros': '#DADADA'
    }
)

fig.set_size_inches(14, 6)

fig.suptitle(
    "Como se distribuyen las categorías\ndentro de los dataset?",
    fontsize=20
)
fig.supylabel("Datasets", fontsize=20)

ax2.set_ylabel('')
ax1.set_ylabel('')
ax1.set_xlabel('Porcentaje')
ax2.set_xlabel('Porcentaje')
ax1.legend().remove()

# ax1.legend(
#     ["Categoría 1", "Categoría 2", "Categoría 3", "Otros"],
#     ncol=4,
#     loc="upper left",
#     bbox_to_anchor=(-0.3, 1.15),
# )
ax2.legend(
    ["Categoría 1", "Categoría 2", "Categoría 3", "Otros"],
    ncol=4,
    loc="upper left",
    bbox_to_anchor=(0, 1.15),
)

ax2.yaxis.tick_right()

ax1.text(
    20, 13.5,
    "Algunos datasets han sido ignorados del análisis",
    fontsize=6,
    bbox={
        "facecolor": "orange",
        "alpha": 0.5
    }
)


