import pandas as pd

df = pd.read_csv("../../../data/tienda_ventas.csv", index_col='id')
df

df['mes'] = df['date'].apply(lambda x: x[:7])
df

sell_by_month = df.groupby('mes').agg({
    'sales': 'sum'
})

sell_by_month

sell_by_month.plot.line(
    y='sales',
    style='.-',
    linestyle='dotted'
)

sell_by_month.reset_index()

import plotly.express as px

fig = px.line(
    sell_by_month,
    x=sell_by_month.index.values,
    y='sales'
)
fig
