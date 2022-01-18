import numpy as np
import pandas as pd
from matplotlib import pyplot as plt

#1.打开CSV文件
fileNameStr = 'sy3.csv'
df = pd.read_csv(fileNameStr,encoding='utf-8',usecols=[2,3,4,5,6,20,21,22,23])

print("--------------head--------------")
print(df.head())
print("--------------describe--------------")
print(df.describe())
print("--------------info--------------")
print(df.info())
print("================================")
#2.查看是否有缺失值
print(df.isnull().sum().sort_values(ascending=False))

#3.生成画布和子图
fig = plt.figure()
ax = fig.add_subplot()

df["date"]=df["year"].astype(str)+df["month"].astype(str).str.pad(2,side="left",fillchar="0")\
           +df["day"].astype(str).str.pad(2,side="left",fillchar="0")
print("---------------------------")
print(df["date"])
df_date=df.groupby("date").mean() #求每日的均值
print(df_date)
#ax.plot(df_date.index,df_date["ave"])  #图形显示很慢，横坐标挤在一起

ax.plot(np.arange(1095),df_date["ave"]) #横坐标替换为数字
ax.plot(np.arange(1095),df_date["DEWP_new"])
ax.plot(np.arange(1095),df_date["HUMI_new"])
ax.plot(np.arange(1095),df_date["PRES_new"])
ax.legend(["ave",'DEWP','HUMI','PRES'])
df_date.to_csv('sy8.csv')

plt.show()



