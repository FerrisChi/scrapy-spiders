import numpy as np
import pandas as pd
from pandas import Series,DataFrame
import matplotlib.pyplot as plt

#打开CSV文件
fileNameStr = 'result2021.csv'
df = pd.read_csv(fileNameStr,encoding='utf-8')
print("------------describe---------------")
print(df.describe())  #查看统计信息

#df.boxplot(column='totalprice')  #生成箱型图
df.boxplot(column=['totalprice','unitprice'])
plt.show()

#突出展示均值线
f = df.boxplot(column=['totalprice'],meanline=True,showmeans=True,vert=False,return_type='dict') #修改True的设置
#print(f)False
#print(len(ax['means']))

for mean in f['means']:
    mean.set(color='r', linewidth=2)
plt.show()

#添加文本注释
res = df.boxplot(column=['totalprice'],meanline=True,showmeans=True,vert=True) #修改True的设置
res.text(1.1,df['totalprice'].mean(),df['totalprice'].mean())
res.text(1.1,df['totalprice'].median(),df['totalprice'].median())
res.text(0.9,df['totalprice'].quantile(0.25),df['totalprice'].quantile(0.25))
res.text(0.9,df['totalprice'].quantile(0.75),df['totalprice'].quantile(0.75))

plt.show()