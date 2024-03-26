import pandas as pd
import seaborn as sns


sns.set_style('whitegrid')
# Load the data
df = pd.read_csv('../../../data/penguins.csv')
df = df.dropna()

# Create a pair plot
sns.pairplot(
    data=df, 
    hue='species',
    kind='hist'
)