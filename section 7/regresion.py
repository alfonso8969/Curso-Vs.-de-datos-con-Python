import pandas as pd
import seaborn as sns

sns.set_style("whitegrid")

df = pd.read_csv("../../../data/penguins.csv")
df = df.dropna()

sns.regplot(
    data=df,
    x="flipper_length_mm",
    y="culmen_length_mm",
    scatter_kws={"s": 10},
)

import scipy as sp

r, p = sp.stats.pearsonr(df["flipper_length_mm"], df["culmen_length_mm"])

r
p

import matplotlib.pyplot as plt

r = 'r=' + str(r)[0:4]  # radius of the circle in cm

plt.text(220, 35, r, color='black')