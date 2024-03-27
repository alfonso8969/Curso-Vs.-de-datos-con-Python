import pandas as pd
import plotly.express as px

# token = open(".mapbox_token").read()  # you will need your own token


# Load the data
df = pd.read_csv("../../../data/terremotos_mundo.csv")
df

df["year"] = df["Date"].apply(lambda x: x[-4:])
df

fig = px.density_mapbox(
    df,
    lat="Latitude",
    lon="Longitude",
    z="Magnitude",
    mapbox_style="open-street-map",
    color_continuous_scale=px.colors.sequential.Inferno,
    zoom=0,
    radius=5,
    opacity=0.8,
    center=dict(lat=11.571147, lon=-24.679272),
)
# fig.update_layout(mapbox_accesstoken=token)
fig.update_layout(margin={"r": 0, "t": 0, "l": 0, "b": 0})
fig.show()
