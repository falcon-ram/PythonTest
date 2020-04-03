# Looking a shiny Diamonds

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('diamonds.csv')

clarityindexes = df['clarity'].value_counts().index.tolist()
claritycount = df['clarity'].value_counts().values.tolist()

print(clarityindexes)
print(claritycount)

plt.bar(clarityindexes, claritycount)
plt.show()
