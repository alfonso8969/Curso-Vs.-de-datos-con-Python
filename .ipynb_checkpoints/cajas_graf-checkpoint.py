import pandas as pd


df = pd.read_csv("../../data/titanic.csv")
df = df.dropna(subset=["Age"], axis='index')  # remove rows with missing Age data
df
df.boxplot(column="Age")

