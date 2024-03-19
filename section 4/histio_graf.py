import pandas as pd
# import matplotlib.pyplot as plt

df = pd.read_csv("../../../data/titanic.csv")
df = df.dropna(subset=["Age"], axis="index")  # remove rows with missing Age data
df
df.hist(
    column="Age",
    by='Sex',
    bins=15
)

import seaborn as sns


sns.histplot(
    df,
    x="Age",
    kde=True,
    bins=20,
    hue="Sex"
)


sns.histplot(
    df,
    x="Age",
    cumulative=True,
    bins=20,
    fill=False,
    element="step"
)
