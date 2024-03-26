import pandas as pd

df = pd.read_csv("../../../data/penguins.csv", index_col=0)
df = df.dropna()

df.plot.scatter(
    x="flipper_length_mm", 
    y="culmen_length_mm"
)

import seaborn as sns

sns.jointplot(
    data=df,
    x="flipper_length_mm",
    y="culmen_length_mm",
    kind="hist",
    joint_kws={
        "bins": 20
    },
    marginal_kws={
        "bins": 20,
        'fill': False
    },
    cbar=True
)
sns.jointplot(
    data=df,
    x="flipper_length_mm",
    y="culmen_length_mm",
    kind="hex",
    joint_kws={
        "bins": 20
    },
    marginal_kws={
        "bins": 20,
        'fill': False
    },
    gridsize=30
)

df.plot.hexbin(
    x="flipper_length_mm",
    y="culmen_length_mm",
    gridsize=30
)