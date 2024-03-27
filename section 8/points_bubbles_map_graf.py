import pandas as pd

pd.set_option("display.max_columns", None)
pd.set_option("display.max_rows", None)
# Load the data
data = pd.read_csv("../../../data/madrid_metro/estaciones.csv")
data

data_grouped = data.groupby("DENOMINACION").agg(
    {
        "latitude": "first",
        "longitude": "first",
        "ENCUESTADOMICILIARIA": "sum",
        "GRADOACCESIBILIDAD": "first",
    }
)
data_grouped


import plotly.express as px

fig = px.scatter_mapbox(
    data_grouped,
    lat="latitude",
    lon="longitude",
    mapbox_style="carto-positron",
    zoom=10,
    hover_name=data_grouped.index.values,
    color="GRADOACCESIBILIDAD",
    size="ENCUESTADOMICILIARIA",
    size_max=20
)
# fig.update_traces(marker=dict(size=12))
fig.update_layout(margin={"r": 0, "t": 0, "l": 0, "b": 0})
fig.show()

