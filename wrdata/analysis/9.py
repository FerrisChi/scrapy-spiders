import pandas as pd
import numpy as np
from pandas.core.frame import DataFrame
import matplotlib.pyplot as plt

df1 = pd.read_csv('6confirmed_death_ratio.csv', encoding='utf-8')
df1 = df1[df1['day']==23].sort_values(by=['confirmeddeath_ratio'], ascending=False).head(10)

x=[]
y=[]
for id, row in df1.iterrows():
    x.append(row['country'])
    y.append(row['confirmeddeath_ratio'])

for a,b in zip(x,y):
    plt.text(a,b,f'{b}', horizontalalignment='center', verticalalignment='bottom')
plt.bar(x, y, tick_label=x,color = 'red')
plt.xlabel('Country')
plt.ylabel('Death rate (Death per 1M population)')
plt.title('Highest 10 Death rate countries')
plt.show()

