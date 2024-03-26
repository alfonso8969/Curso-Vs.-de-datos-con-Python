import pandas as pd
import seaborn as sns

sns.set_style('whitegrid')
df = pd.read_csv('../../../data/penguins.csv')
df = df.dropna()


g = sns.jointplot(
    data=df,
    x='flipper_length_mm',
    y='culmen_length_mm',
    hue='species',
    kind='kde'
)
sns.move_legend(g.ax_joint, "lower right", title='Species', frameon=False)