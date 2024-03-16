import pandas as pd


df = pd.read_csv("../../../data/titanic.csv")


passengers = df.groupby("Sex").agg({"PassengerId": "count"})


import seaborn as sns

sns.barplot(passengers, x="Sex", y="PassengerId")


import matplotlib.pyplot as plt

plt.bar(passengers.index, passengers["PassengerId"])