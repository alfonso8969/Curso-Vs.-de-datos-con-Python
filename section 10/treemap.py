import pandas as pd
import plotly.express as px

df = pd.read_csv('../../../data/paises_vida.csv', index_col=0)
df = df.dropna()
df = df[df['year'] == 2007]
df

fig = px.treemap(
    df,
    path=[px.Constant('World'), 'continent', 'country'],
    values='pop',
    color='lifeExp',
    color_continuous_scale='RdBu',
)
fig.update_layout(margin={"r": 0, "t": 0, "l": 0, "b": 0})
fig.show()

df2 = pd.read_csv('../../../data/marcas_mensajes.csv')
df2

fig2 = px.treemap(
    df2,
    path=[px.Constant('All'), 'tipo', 'marca'],
    values='n_mensajes',

)

fig2.update_layout(margin={"r": 0, "t": 0, "l": 0, "b": 0})
fig2.data[0].textinfo = 'label+text+value'
fig2.show()
