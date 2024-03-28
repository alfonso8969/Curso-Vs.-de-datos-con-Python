import pandas as pd
import plotly.express as px

# Load the data
df = pd.read_csv("../../../data/tienda_ventas.csv")
df

df_days = df[["date", "sales"]]
df_days = df_days.groupby("date").sum()
df_days

df_days.plot.line(
    y="sales", xlabel="Date", ylabel="Sales", title="Sales per day", figsize=(10, 6)
)

fig = px.line(df_days, x=df_days.index.values, y="sales", title="Sales per day")
fig.show()

df2 = pd.read_csv("../../../data/marcas_mensajes_twitter.csv")
df2

df2["fecha_parseada"] = pd.to_datetime(
    df2["created_at"], format="%a %b %d %H:%M:%S %z %Y"
)
df2

df2 = df2.sort_values("fecha_parseada")
df2["periodo"] = df2["fecha_parseada"].apply(lambda x: x.strftime("%Y-%m-%d"))
df2

df2_agrupado = df2[["periodo", "idx"]].groupby("periodo").count()
df2_agrupado = df2_agrupado.reset_index()
df2_agrupado

# Gráfico de Lineas con Plotly
# https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.plot.line.html
fig = px.line(df2_agrupado, x="periodo", y="idx", title="Mensajes por dia")
fig.show()
