import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px

# Load the data
df = pd.read_csv("../../../data/penguins.csv")
df = df.dropna()

fig = plt.figure(figsize=(15, 10))
ax = plt.axes(projection="3d")

# Scatter plot
ax.scatter(
    df["culmen_length_mm"],
    df["culmen_depth_mm"],
    df["flipper_length_mm"],
    c="green",
    s=50,
)

ax.set_xlabel("Culmen Length (mm)")
ax.set_ylabel("Culmen Depth (mm)")
ax.set_zlabel("Flipper Length (mm)")
plt.title("Penguin Dimensions")
plt.show()

fig = px.scatter_3d(
    df,
    x="culmen_length_mm",
    y="culmen_depth_mm",
    z="flipper_length_mm",
    color="species",
    symbol="species",
    size_max=10,
    opacity=0.7,
    width=800,
    height=800,
    title="Penguin Dimensions",
)
fig.show()
