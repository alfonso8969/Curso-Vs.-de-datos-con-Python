import pandas as pd
import seaborn as sns

sns.set_style("whitegrid")

df = pd.read_csv("../../../data/penguins.csv", index_col=0)
df = df.dropna()

agrupado = df.groupby(["species", "island"]).count()[["sex"]]
agrupado

pivote = agrupado.unstack().droplevel(0, axis=1)  # type: ignore
pivote

# Heatmap de variables categóricas que codifican una variable numérica
# https://seaborn.pydata.org/generated/seaborn.heatmap.html
sns.heatmap(
    pivote,
    annot=True,
    cmap="crest",
    linewidth=0.5,
    fmt=".1f"
)

# Heatmap de Correlación
# https://seaborn.pydata.org/generated/seaborn.heatmap.html

# Calculo los coeficientes de correlación lineal entre mis variables
df_cor = df[
    ["culmen_length_mm", "culmen_depth_mm", "flipper_length_mm", "body_mass_g"]
].corr()
df_cor

palette = sns.color_palette("rocket_r", as_cmap=True)


sns.heatmap(df_cor, annot=True, cmap=palette, square=True)
