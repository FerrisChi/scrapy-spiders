import pandas as pd
import numpy as np
from pandas.core.frame import DataFrame
import matplotlib.pyplot as plt

df1 = pd.read_csv('1confirmed_cases.csv', encoding='utf-8')
df1 = df1[df1.country != 'World']

df2 = df1[df1['day'] == 23]
df2 = df2.sort_values(by=['confirmedcases'], ascending=False).head(10)
print(df2)

x = []
y = []
for ctr, row in df2.iterrows():
    x.append(row['country'])
    y.append(row['confirmedcases'])

for a,b in zip(x,y):
    plt.text(a,b,f'{b}', horizontalalignment='center', verticalalignment='bottom')
plt.bar(x, y, tick_label=x,color = 'red')
plt.xlabel('Country')
plt.ylabel('Confirmed cases')
plt.title('Max 10 comfirmed cases countries')
plt.show()
# plt.savefig('3.png')