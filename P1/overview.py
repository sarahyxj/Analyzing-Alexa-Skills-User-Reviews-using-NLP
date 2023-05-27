# -*- coding: utf-8 -*-
"""
Created on Mon Oct  3 19:35:51 2022

General understanding of Alexa Skills dataset UQ-AAS21-I & UQ-AAS21-II

@author: Xiaojia Yu
"""


import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.ticker import MaxNLocator
import numpy as np
import matplotlib.ticker as ticker



#download data
data = pd.read_excel (r'../Data/UQ-AAS21-I.xlsx')

print('There are {} rows and {} columns in this report'
      .format(data.shape[0],data.shape[1]))

data.describe(include="all")

plt.style.use("ggplot")

colors = plt.cm.Blues(np.linspace(0, 1, 10))


# Category distribution
ax = data.groupby("Category").count()["Index"].nlargest(10).plot(kind="pie", 
                                    figsize=(8, 5),
                                    title="Alexa skills Top 10 Category",
                                    autopct='%1.1f%%',
                                    colors=colors)

ax.set_ylabel('')

plt.show()


# Top 10 Alexa skills average rating per brand
colors = plt.cm.Blues(np.linspace(0.2, 1, 10))

data = data[data["Average Rating"] != 0]

ax = data.groupby("Category").mean()["Average Rating"].nlargest(10).sort_values().plot(kind="barh",
                        figsize=(8,5), 
                        title="Alexa skills Top 10 Category Average Rating",
                        color=colors)

ax.xaxis.set_major_locator(MaxNLocator(integer=True))


plt.show()


# Top 10 most popular skills (calculate by with average rating * number of ratings)
ax = data.groupby("Skill Name").mean()["Rating*Number"].nlargest(10).sort_values().plot(kind="barh",
                                    figsize=(8,5), 
                                    title="Top 10 most popular skills",
                                    color=colors)
# plt.xlabel("Average rating X number of ratings") 

ax.xaxis.set_major_formatter(ticker.FuncFormatter(lambda x, pos: '{:,.0f}'.format(x/1000)))
plt.xlabel("Average Rating x No. of ratings (x 1,000s)") 

plt.rcParams["font.family"] = "Times New Roman"
plt.rcParams["font.size"] = 10


plt.show()

