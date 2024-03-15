import pandas as pd
# import matplotlib.pyplot as plt

df = pd.read_csv("../../data/tienda_ventas.csv", index_col='id')
df

df["mes"] = df["date"].apply(lambda x: x[:7])
df