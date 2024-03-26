import pandas as pd
import plotly.graph_objects as go

# Load the data
df = pd.read_csv('../../../data/restaurantes.csv')
df 

categories = df.columns.values[1:]

fig = go.Figure()

# Add traces
fig.add_trace(
    go.Scatterpolar(
        r=df.iloc[0, 1:],
        theta=categories,
        fill='toself',
        name='Restaurante 1'
    )
)

fig.add_trace(
    go.Scatterpolar(
        r=df.iloc[1, 1:],
        theta=categories,
        fill='toself',
        name='Restaurante 2'
    )
)

fig.add_trace(
    go.Scatterpolar(
        r=df.iloc[2, 1:],
        theta=categories,
        fill='toself',
        name='Restaurante 3'
    )
)

fig.show()

df2 = pd.read_csv('../../../data/penguins.csv')
df2 = df2.dropna()
df2

grouped = df2.groupby('species').mean(numeric_only=True)
grouped

categories = grouped.columns.values
species = df2['species'].unique()

fig2 = go.Figure()

# Add traces
fig2.add_trace(
    go.Scatterpolar(
        r=grouped.iloc[0, :],
        theta=categories,
        fill='toself',
        name=species[0]
    )
)

fig2.add_trace(
    go.Scatterpolar(
        r=grouped.iloc[1, :],
        theta=categories,
        fill='toself',
        name=species[1]
    )
)

fig2.add_trace(
    go.Scatterpolar(
        r=grouped.iloc[2, :],
        theta=categories,
        fill='toself',
        name=species[2]
    )
)

fig2.show()

# normalización min max
grouped = df2.groupby('species').mean(numeric_only=True)
df_norm = df2[grouped.columns.values]
df_norm = (df_norm - df_norm.min()) / (df_norm.max() - df_norm.min())
df_norm['species'] = df2['species']
df_norm 

grouped_norm = df_norm.groupby('species').mean(numeric_only=True)

fig3 = go.Figure()

# Add traces
fig3.add_trace(
    go.Scatterpolar(
        r=grouped_norm.iloc[0, :],
        theta=categories,
        fill='toself',
        name=species[0]
    )
)

fig3.add_trace(
    go.Scatterpolar(
        r=grouped_norm.iloc[1, :],
        theta=categories,
        fill='toself',
        name=species[1]
    )
)

fig3.add_trace(
    go.Scatterpolar(
        r=grouped_norm.iloc[2, :],
        theta=categories,
        fill='toself',
        name=species[2]
    )
)

fig3.show()