import pandas as pd


df = pd.read_csv("../../data/titanic.csv")
passengers = df.groupby("Sex").agg({"PassengerId": "count"})
passengers
passengers.plot.pie(
    y="PassengerId",
    startangle=90,
    autopct="%1.1f%%",  # Format the percentages to show one decimal
)


import plotly.express as px


passengers_index = passengers.reset_index()
passengers_index

fig = px.pie(
    passengers_index,
    values="PassengerId",
    names="Sex",
    title="Passengers per Sex",
    hole=0.3
)
fig.show()
