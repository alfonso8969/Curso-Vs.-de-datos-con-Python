import pandas as pd
import matplotlib.pyplot as plt


df = pd.read_csv("../../../data/tiendas_procesado.csv", index_col="fecha")
df

plt.rcParams["figure.figsize"] = (15, 3)
plt.style.use("bmh")

# ax = df.plot.line(figsize=(10, 5))

# ax.xaxis.grid(color='g', linestyle='-', linewidth=0.5)
# ax.yaxis.grid(color='b', linestyle='--', linewidth=0.5)

import seaborn as sns

plt.figure(figsize=(10, 5))

sns.set_style("ticks")
sns.set_theme("paper")

plt.grid(
    visible=False,
    axis='x'
)

bx = sns.lineplot(data=df)

import plotly.express as px

fig = px.line(
    df, width=800,
    height=500,
    template='plotly_dark'
)

fig.update_xaxes(showgrid=False)
fig.update_yaxes(
    showgrid=True,
    secondary_y=True
)