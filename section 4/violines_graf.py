import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("../../data/titanic.csv")
df = df.dropna(subset=["Age"], axis="index")  # remove rows with missing Age data
df


import seaborn as sns

sns.violinplot(
    data=df,
    x="Sex",
    y="Age",
    inner="quartiles"
)

plt.show()
