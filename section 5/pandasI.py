import pandas as pd
import matplotlib.pyplot as plt


df = pd.read_csv("../../../data/tiendas_procesado.csv", index_col='fecha')
df

plt.rcParams['figure.figsize'] = (10, 5)
# Temas https://matplotlib.org/stable/gallery/style_sheets/style_sheets_reference.html
plt.style.use('bmh')
df.plot.line(
    # figsize=(10, 5)
)


import seaborn as sns

plt.figure(figsize=(10, 5))

sns.set_style("ticks")
sns.set_theme("paper")

sns.lineplot(
    data=df
)

import plotly.express as px

px.line(
    df,
    width=800,
    height=500,
    template='plotly_dark'
)
