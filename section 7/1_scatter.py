import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("../../../data/penguins.csv")
df

df = df.dropna()
df

plt.style.use("seaborn-v0_8-whitegrid")

df.plot.scatter(
    x="flipper_length_mm",
    y="culmen_length_mm",
    c="body_mass_g",
)

import plotly.express as px

fig = px.scatter(df, x="flipper_length_mm", y="culmen_length_mm", color="species")

fig.show()

import seaborn as sns

sns.set_style("whitegrid")

sns.catplot(
    data=df,
    x="flipper_length_mm",
    y="species",
    hue='island'
)

