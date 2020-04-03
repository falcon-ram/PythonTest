# Diamonds heat map

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Build dataframe
df = pd.read_csv('diamonds.csv')

# drop the index column
df = df.drop('Unnamed: 0', axis=1)
f, ax = plt.subplots(figsize=(10,8))
corr = df.corr()
print(corr)
mymask = np.zeros_like(corr, dtype=np.bool)
mycmap = sns.diverging_palette(220, 10, as_cmap=True)
sns.heatmap(corr, mask=mymask, cmap=mycmap, square=True, ax=ax)
# plt.show()