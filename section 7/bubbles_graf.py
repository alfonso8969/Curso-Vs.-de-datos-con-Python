import pandas as pd

df = pd.read_csv("../../../data/paises_vida.csv", index_col=0)
df = df.dropna()

df_2002 = df.loc[df["year"] == 2002]
df_2002

import plotly.express as px

fig = px.scatter(
    df_2002,
    x="gdpPercap",
    y="lifeExp",
    size="pop",
    color="continent",
    hover_name="country",
    log_x=True,
    size_max=60,
)

fig.show()

import seaborn as sns
import matplotlib.pyplot as plt

sns.set_style("whitegrid")

sns.scatterplot(
    data=df_2002,
    x="gdpPercap",
    y="lifeExp",
    size="pop",
    hue="continent",
    sizes=(30, 1300),
    legend=True,
)

plt.xscale("log")
plt.legend(bbox_to_anchor=(1.05, 1), loc="upper left")
plt.title("Life Expectancy vs GDP per Capita in 2002")
