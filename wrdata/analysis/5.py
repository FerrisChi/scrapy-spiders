import pandas as pd
import numpy as np
from pandas.core.frame import DataFrame
import matplotlib.pyplot as plt

df1 = pd.read_csv('2confirmedcases_ratio.csv', encoding='utf-8')
df1 = df1[df1['day'] == 23]

df1 = df1.sort_values(by=['confirmedcases_ratio'], ascending=False).head(10)
print(df1)

x = []
y = []
for id, row in df1.iterrows():
    x.append(row['country'])
    y.append(row['confirmedcases_ratio'])

for a, b in zip(x, y):
    plt.text(a,
             b,
             f'{b}',
             horizontalalignment='center',
             verticalalignment='bottom')

plt.bar(x, y, tick_label=x, color='red')
plt.xlabel('Country')
plt.ylabel('Confirmed cases(per 1M population)')
plt.title('Max 10 comfirmed case countries (per 1M population)')
plt.show()
# plt.savefig('5.png')