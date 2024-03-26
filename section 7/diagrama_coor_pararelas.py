import pandas as pd


df = pd.read_csv('../../../data/penguins.csv')
df = df.dropna()
df

df['species_id'] = df['species'].astype('category').cat.codes
df
import plotly.express as px

fig = px.parallel_coordinates(
    df,
    color='species_id',
    dimensions=['culmen_length_mm', 'culmen_depth_mm', 'flipper_length_mm', 'body_mass_g'],
    color_continuous_scale=px.colors.diverging.Tealrose
)
fig.show()