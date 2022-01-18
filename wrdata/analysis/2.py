import pandas as pd
import numpy as np
from pandas.core.frame import DataFrame
import matplotlib.pyplot as plt

df1 = pd.read_csv('3confirmed_cases_perday.csv', encoding='utf-8')
# print(df1.info())
df2 = df1.groupby(by=['country']).agg({'confirmedcases_perday': 'sum'},
                                      sort=True)
# print(df2)
df3 = df2.sort_values(by=['confirmedcases_perday'], ascending=False).head(10)
df3.rename(columns={"confirmedcases_perday": "casesin15"}, inplace=True)
print(df3.info())

for i, row in df3.iterrows():
    print(i)

# plt_label = 0
# for link in range(len(num)):
#     plt_label += 1
#     plt.plot(num[0], num[link], label='第' + str(plt_label) + '条线段')
plt_label = 1
x = [i for i in range(9, 24)]
markes = [
    '-o', '-s', '-^', '-p', '-^', '-v', '-p', '-d', '-h', '-2', '-8', '-6'
]
for ctr, row in df3.iterrows():
    ytmp = []
    dftmp = df1[df1['country'] == ctr]
    for itmp, rowtmp in dftmp.iterrows():
        ytmp.append(rowtmp['confirmedcases_perday'])
    # print(ytmp)
    plt.plot(x, ytmp, markes[plt_label - 1], label=f'{ctr} {plt_label}th')
    plt_label += 1
plt.legend()
plt.xlabel('Day(December, 2021)')
plt.ylabel('Confirmed cases per day')
plt.show()
# plt.savefig('2.png')
