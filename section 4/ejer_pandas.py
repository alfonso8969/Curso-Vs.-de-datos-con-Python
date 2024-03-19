import pandas as pd


df = pd.read_csv("../../../NIVEL0/dataset.csv", index_col="id")

df_filter = df.fillna(0)
df_filter.head()


df.iloc[0]
df.loc[[183721, 183722], ["full_text", "favorites"]]

df[df['favorites'] > 400]

df[(df['favorites'] > 400) & (df['mentions'] > 20)]

df[df['full_text'].str.contains("programming")]

import random


def calculateWins(retweets):
    win = retweets * random.randint(3, 5)
    return win


df["ganancias"] = df["retweets"].apply(calculateWins)
df.fillna(0).head()


def population(row):
    return row["followees"] / row["followers"]


df["popularidad"] = df.apply(population, axis=1)
df.fillna(0).head()

df = df.drop(columns=["full_text"])
df.fillna(0).head()

df = df.drop(columns=["user"])
df.fillna(0)

df.groupby("country").mean()

result = df.groupby("country").agg({
    "followers": "sum",
    "followees": "sum",
    "retweets": "max",
    "favorites": "mean"
})
result.to_csv("../../../NIVEL0/result.csv")
