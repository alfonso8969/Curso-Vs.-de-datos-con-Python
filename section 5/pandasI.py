import pandas as pd
import matplotlib.pyplot as plt


df = pd.read_csv("../../../data/tiendas_procesado.csv", index_col='fecha')
df

plt.rcParams['figure.figsize'] = (10, 5)
# Temas https://matplotlib.org/stable/gallery/style_sheets/style_sheets_reference.html
plt.style.use('bmh')
df.plot.line(
    # figsize=(10, 5)
)

import seaborn as sns

plt.figure(figsize=(12, 5))

sns.lineplot(
    data=df
)
