import pandas as pd

df = pd.read_csv("../../../data/paises_vida.csv", index_col=0)
df = df.dropna()

df_asia = df[df["continent"] == "Asia"]
df_asia = df_asia.sort_values(by="lifeExp")
df_asia_grouped = df_asia.groupby("year").agg({"lifeExp": "mean", "gdpPercap": "mean"})

df_asia_grouped.plot.line(
    y=["lifeExp", "gdpPercap"],  # type: ignore
    grid=True,
)

import matplotlib.pyplot as plt

fig, ax = plt.subplots()
plt.style.use('ggplot')

ax.plot(
    df_asia_grouped.index.values, 
    df_asia_grouped["gdpPercap"],
    color='red',
    marker='s'
)
plt.legend(['GDP per Capita'], loc='lower right')
ax.set_ylabel('GDP per Capita', color='red')
ax.set_xlabel('Year')
ax.tick_params(axis='y', labelcolor='red')

ax1 = ax.twinx()
ax1.plot(
    df_asia_grouped.index.values, 
    df_asia_grouped["lifeExp"],
    color='blue', 
    marker='o',
)

plt.legend(['Life Expectancy'], loc='upper left')
ax1.set_ylabel('Life Expectancy', color='blue')
ax1.tick_params(axis='y', labelcolor='blue')

# método alternativo
from mpl_toolkits.axes_grid1 import host_subplot

host = host_subplot(111)
par = host.twinx()

host.set_xlabel("Distance")
host.set_ylabel("Density")
par.set_ylabel("Temperature")

p1, = host.plot([0, 1, 2], [0, 1, 2], label="Density")
p2, = par.plot([0, 1, 2], [0, 3, 2], label="Temperature")

host.legend(labelcolor="linecolor")

host.yaxis.get_label().set_color(p1.get_color())
par.yaxis.get_label().set_color(p2.get_color())

plt.show()