import pandas as pd
import numpy as np
from pandas.core.frame import DataFrame
import matplotlib.pyplot as plt

df1 = pd.read_csv('1confirmed_cases.csv', encoding='utf-8')
df1 = df1[df1.country != 'World']
df1 = df1[df1['day'] == 23]

sizes = []
labels = []
explode = []
other = 0
for id, row in df1.iterrows():
    if row['confirmedcases'] < 4e6:
        other += row['confirmedcases']
        continue
    sizes.append(row['confirmedcases'])
    labels.append(row['country'])
    explode.append(0)

sizes.append(other)
labels.append('other')
explode.append(0)

fig1, ax1 = plt.subplots()
ax1.pie(sizes,
        explode=explode,
        labels=labels,
        autopct='%1.1f%%',
        shadow=True,
        startangle=90)
ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

# plt.savefig('4.png')
plt.show()