# Looking at shiny Diamonds

# importing the pandas, numpy and matplotlib
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# read the diamonds csv file
# build a Dataframe from the data
df = pd.read_csv('diamonds.csv')

carat = df.carat
clarity = df.clarity

plt.scatter(clarity, carat)
plt.show()
