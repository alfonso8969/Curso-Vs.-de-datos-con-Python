import pandas as pd
import numpy as np
import plotly.express as px

# Load the data
df = pd.read_csv("../../../data/viajes_surfistas.csv")
df

nodes1 = df[["homecountry", "homelat", "homelon"]]
nodes1.columns = ["label", "lat", "lon"]
nodes1_agg = nodes1.groupby(["lat", "lon"]).first().reset_index()
nodes1_agg


nodes2 = df[["travelcountry", "travellat", "travellon"]]
nodes2.columns = ["label", "lat", "lon"]
nodes2_agg = nodes2.groupby(["lat", "lon"]).first().reset_index()
nodes2_agg

nodes = pd.concat([nodes1_agg, nodes2_agg])
nodes = nodes.groupby(["lat", "lon"]).first().reset_index()
nodes

fig = px.scatter_mapbox(
    nodes,
    lat="lat",
    lon="lon",
    mapbox_style="carto-positron",
    zoom=1,
    color="label",
)
fig.update_traces(marker=dict(size=4))
fig.update_layout(margin={"r": 0, "t": 0, "l": 0, "b": 0})
fig.show()

lats = np.empty(len(df) * 2)
lats[::2] = df['homelat']
lats[1::2] = df['travellat']
lats[2::3] = None

lons = np.empty(len(df) * 2)
lons[::2] = df['homelon']
lons[1::2] = df['travellon']
lons[2::3] = None

import plotly.graph_objects as go

fig = go.Figure()

fig.add_trace(
    go.Scattermapbox(
        mode="markers+lines",
        lat=lats,
        lon=lons,
        marker={"size": 5},
        line={"width": 1},
        opacity=0.05,
    )
)
fig.update_layout(
    margin={"r": 0, "t": 0, "l": 0, "b": 0},
    showlegend=False,
    mapbox={"style": "carto-darkmatter", "zoom": 1, "center": {"lat": 10, "lon": 10}},
)

fig.show()
