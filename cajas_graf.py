import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("../../data/titanic.csv")
df = df.dropna(subset=["Age"], axis="index")  # remove rows with missing Age data
df
df.boxplot(column="Age")

df.boxplot(by="Sex", column=["Age"], grid=False)


import seaborn as sns

sns.boxplot(data=df, x="Sex", y="Age")

plt.show()
