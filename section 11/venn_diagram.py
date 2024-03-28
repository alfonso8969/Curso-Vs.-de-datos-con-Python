import pandas as pd
from matplotlib_venn import venn2
from matplotlib_venn import venn3, venn3_unweighted
import matplotlib.pyplot as plt

df = pd.read_csv('../../../data/animales_caracteristicas.csv')
df

respira = set(df[df['respira'] == 1]['animal'])
piernas = set(df[df['piernas'] == 1]['animal'])
nada = set(df[df['nada'] == 1]['animal'])


# Aquí se pueden ver las intersecciones de los conjuntos de animales que respiran,
# que tienen piernas y que nadan.
# Aquí se pueden ver las intersecciones de los conjuntos de animales que respiran, 
# que tienen piernas y que nadan.
# La intersección de los conjuntos de animales que respiran y que tienen piernas es el conjunto de animales
# que respiran y tienen piernas.
# Venn diagrama con etiquetas de animales que respiran, tienen piernas y nadan.
venn3([respira, piernas, nada], ('Respira aire', 'Tiene piernas', 'Puede Nadar'))
plt.rcParams["figure.figsize"] = (15, 15)
plt.title('Animales que respiran, tienen piernas y nadan')
plt.show()

venn3_unweighted(
    [
        set(respira),
        set(piernas),
        set(nada)
    ],
    set_labels=('Respira Aire', 'Tiene Piernas', 'Puede Nadar')
)
plt.title('Animales')
plt.show()

venn2([30, 10, 5], ('A', 'B'))
plt.title('Sólo dos características')
plt.show()
