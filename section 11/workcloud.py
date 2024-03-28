from matplotlib import pyplot as plt
import pandas as pd
from wordcloud import WordCloud, ImageColorGenerator


df = pd.read_csv("../../../data/marcas_mensajes_twitter.csv")
df

text = " ".join(df["tokenized"])

wc = WordCloud(
    width=1000,
    height=700,
    margin=0,
    background_color='white'   
).generate(text)

plt.imshow(wc)
plt.axis("off")

from PIL import Image
import numpy as np

tw_color = np.array(Image.open("../../../data/nuevo-logotipo-twitter-x-sombra/twitter.jpeg"))
tw_mask = tw_color.copy()
tw_mask[tw_mask.sum(axis=2) == 0] = 255

# We create a mask to make this image in the shape of a twitter bird logo
wc = WordCloud(
    width=1000,
    height=700,
    margin=0,
    background_color='black',
    mask=tw_mask
).generate(text)

image_colors = ImageColorGenerator(tw_color)
wc.recolor(color_func=image_colors)

plt.figure(figsize=(10, 10))  # Arbitrary figure size
plt.imshow(wc)
plt.axis("off")
plt.savefig('wordcloud_twitter.png', dpi=300)