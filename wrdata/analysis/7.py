import pandas as pd
import numpy as np
from pandas.core.frame import DataFrame
import matplotlib.pyplot as plt

df1 = pd.read_csv('5vaccinated.csv', encoding='utf-8')
df1 = df1[df1['day'] == 23]
df1 = df1.sort_values(by=['vaccinated'], ascending=True).head(10)
print(df1.info())

x=[]
y=[]
for id, row in df1.iterrows():
    x.append(row['country'])
    btb = round(row['vaccinated'] * 100, 2)
    y.append(str(btb)+'%')

for a, b in zip(x, y):
    plt.text(a,
             b,
             f'{b}',
             horizontalalignment='center',
             verticalalignment='bottom')
plt.xlabel('country')
plt.ylabel('Vaccination rate(%)')
plt.bar(x, y, tick_label=x, color='red')
plt.title('Min 10 vaccinated country')
plt.show()