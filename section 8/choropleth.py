import pandas as pd
import json
import plotly.express as px


with open("../../../data/venezuela_tw_pob.geojson", encoding="utf-8") as shapes:
    data = json.load(shapes)

data

names = []
tweets = []
population = []

for feature in data["features"]:
    names.append(feature["properties"]["NOMBRE"])
    tweets.append(feature["properties"]["TWEETS"])
    population.append(feature["properties"]["POBLACION"])

df = pd.DataFrame({"name": names, "tweets": tweets, "population": population})

df

fig = px.choropleth(
    df,
    geojson=data,
    locations="name",
    featureidkey="properties.NOMBRE",
    color="tweets",
    color_continuous_scale=px.colors.sequential.Blues,
)

fig.update_layout(margin={"r": 0, "t": 0, "l": 0, "b": 0})
fig.update_geos(fitbounds="locations")
fig.add_scattergeo(
    geojson=data,
    text=df["tweets"],
    mode="text",
    locations=df["name"],
    featureidkey="properties.NOMBRE",
)

fig.show()

fig2 = px.choropleth_mapbox(
    df,
    geojson=data,
    locations="name",
    featureidkey="properties.NOMBRE",
    color="tweets",
    color_continuous_scale=px.colors.sequential.Blues,
    mapbox_style="carto-positron",
    zoom=5,
    center={"lat": 8.0, "lon": -66.0},
)

fig2.add_scattergeo(
    geojson=data,
    text=df["tweets"],
    mode="text",
    locations=df["name"],
    featureidkey="properties.NOMBRE",
)

fig2.update_layout(margin={"r": 0, "t": 0, "l": 0, "b": 0})
fig2.show()
    