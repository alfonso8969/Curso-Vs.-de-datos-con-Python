import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Load the data
df = pd.read_csv('../../../data/covid_data.csv')
df

grouped = df[['date', 'continent', 'new_cases']].groupby(['date', 'continent']).sum()
grouped = grouped.unstack(1)
grouped = grouped.fillna(0)  # Fill missing values with zero
grouped = grouped.droplevel(0, axis=1)  # Drop the new_cases column level # type: ignore
grouped

continents = df['continent'].dropna().unique()

values = np.array([grouped[continent] for continent in continents])

fig, ax = plt.subplots()
fig.set_size_inches(15, 10)
ax.stackplot(
    grouped.index.values,
    values,
    baseline='wiggle',
    labels=continents,
    colors=plt.cm.viridis(np.linspace(0, 1, len(continents)))
)

ax.legend(loc='upper left')
ax.set_title('Stream graph of new cases of Covid by continent')
ax.set_xlabel('Day')
ax.set_ylabel('New cases')
ax.axhline(0, color='black', ls='--', linewidth=0.8)
fig.autofmt_xdate()
plt.xticks(np.arange(0, len(grouped.index), 30))
fig.show()
