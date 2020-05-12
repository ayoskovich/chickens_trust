#!/usr/bin/env python
# coding: utf-8

# # Claims made about poultry, pork, and beef.
# 
# Article [here](https://www.bloomberg.com/news/articles/2020-05-11/why-chicken-is-plentiful-during-the-pandemic-and-beef-is-not?srnd=premium&utm_medium=social&utm_source=twitter&utm_campaign=socialflow-organic&utm_content=markets&cmpid%3D=socialflow-twitter-markets&sref=XQtHDW1P).

# ### “poultry costs U.S. consumers 62% less in inflation-adjusted terms than it did in 1935”
# 
# ### “Pork, now also raised mostly at factory scale indoors, is 12% cheaper”
# 
# ### “Beef, which isn’t, costs 63% more. “
# 
# I'm going to go to FRED and get the price of Chicken, Fresh, Whole, Per Lb. (453.6 Gm) in U.S. City Average. [Here](https://fred.stlouisfed.org/series/APU0000706111#0) This way I can download the data in a nice clean format. 
# 
# Series ID APU0000706111
# 
# I'll need to adjust for inflation, so I'll use the CPI: [CPIAUCSL](https://fred.stlouisfed.org/series/CPIAUCSL).
# 
# **Also, I can't find where he got data going all the way back to the 30s??**

# In[2]:


import pandas as pd
import matplotlib.pyplot as plt
from datetime import date

%config InlineBackend.figure_format = 'retina'
%run ./helpers.ipynb

cpi = pd.read_csv('data/CPIAUCSL.csv')

# Get most recent cpi
MOST_RECENT = cpi.loc[cpi['DATE'] == cpi['DATE'].max(), 'CPIAUCSL'].values[0]

df = (
    beef()
    .pipe(pd.merge, chicken(), how='outer')
    .pipe(pd.merge, pork(), how='outer')
    .pipe(pd.merge, cpi, how='outer', on='DATE')
    .rename(columns={'APU0000703112':'beef',
                     'APU0000706111':'chicken',
                     'APU0000FD3101':'pork',
                     'CPIAUCSL':'cpi',
                     'DATE':'date'})
)

df['date'] = pd.to_datetime(df['date'])
df['beef'] = pd.to_numeric(df['beef'],errors='coerce')
df.sort_values(by=['date'], inplace=True)

df['new_pork'] = apply_adjust(df, 'pork', MOST_RECENT)
df['new_chicken'] = apply_adjust(df, 'chicken', MOST_RECENT)
df['new_beef'] = apply_adjust(df, 'beef', MOST_RECENT)

plt.plot(df['date'], df['new_chicken'], label='chicken');
plt.plot(df['date'], df['new_pork'], label='pork');
plt.plot(df['date'], df['new_beef'], label='beef')
plt.legend(loc="upper left");
plt.title("Price adjusted for inflation");
