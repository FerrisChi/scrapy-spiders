import pandas as pd
import numpy as np
from pandas.core.frame import DataFrame
import matplotlib.pyplot as plt

df = pd.read_csv('1confirmed_cases.csv',encoding='utf-8', dtype=str)
df = df[df["country"]=='World']

# df.sort_values(by=['day'], ascending=True, inplace=True)

x=[]
y=[]
for A, B in zip(df['day'], df['confirmedcases']):
    x.append(A)
    y.append(B)
    # print(A, B)

plt.plot(x, y, color='blue', marker='o', linestyle='dashed')

for a, b in zip(x,y):
    plt.text(a, b, f'{b}', verticalalignment='top')

plt.xlabel('Day(December, 2021)')
plt.ylabel('Confirmed cases')
plt.title('World Epidemic situation')
plt.show()
# plt.savefig('1.png')

# print(df.info())