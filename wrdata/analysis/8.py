import pandas as pd
import numpy as np
from pandas.core.frame import DataFrame
import matplotlib.pyplot as plt

df1 = pd.read_csv('1confirmed_cases.csv', encoding='utf-8')
df1 = df1[df1['day'] == 23]
Top10 = [
    'United States', 'China', 'Japan', 'Germany', 'United Kingdom', 'India',
    'France', 'Italy', 'Canada', 'South Korea'
]
df1 = df1[df1['country'].isin(Top10)]
print(df1)

avg = df1['confirmedcases'].mean()
#选取GDP前10国家
df1 = df1[df1['day'] == 23]
plt.figure()
plt.xlabel('Confirmed cases')
plt.title(f'GDP Top 10 Confirmed Cases country (Average: {avg})')
df1.boxplot(column='confirmedcases',
            showmeans=True,
            vert=True,
            patch_artist=True)  #绘制箱型图
plt.show()
