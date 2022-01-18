import pandas as pd
import matplotlib.pyplot as plt

#打开CSV文件
#fileNameStr = 'result2020-2021.csv'
fileNameStr1 = 'result2020.csv'
df1 = pd.read_csv(fileNameStr1,encoding='gbk')

fileNameStr2 = 'result2021.csv'
df2 = pd.read_csv(fileNameStr2,encoding='utf-8')

print(df1.describe())  #查看统计信息
print(df2.describe())  #查看统计信息

plt.rcParams['font.sans-serif'] = ['SimHei'] #支持中文的细黑体
fig=plt.figure()

ax1 = fig.add_subplot(121)
ax2 = fig.add_subplot(122)

#ax = ax1.boxplot(column='totalprice', by='DataYear',return_type='dict',meanline=True,showmeans=True)
ax1.set_ylim(0,2000)
ax2.set_ylim(0,2000)
ax1.grid(True, linestyle='--', alpha=0.8) #设置网格线
ax2.grid(True, linestyle='--', alpha=0.8) #设置网格线

ax1.set_title('2020房价')
ax1.boxplot(df1['totalprice'],meanline=True,showmeans=True)
df1=df1.loc[df1['district'] == "朝阳"]
ax1.text(1.1,df1['totalprice'].mean(),df1['totalprice'].mean())
ax1.text(1.1,df1['totalprice'].median(),df1['totalprice'].median())

ax2.set_title('2021房价')
ax2.boxplot(df2['totalprice'],meanline=True,showmeans=True)
df2=df2.loc[df2['district'] == "朝阳"]
ax2.text(1.1,df2['totalprice'].mean(),df2['totalprice'].mean())
ax2.text(1.1,df2['totalprice'].median(),df2['totalprice'].median())

plt.show()