import numpy as np
import pandas as pd
import time

#1.打开CSV文件
fileNameStr = 'ShenyangPM20100101_20151231.csv'
df = pd.read_csv(fileNameStr,encoding='utf-8',usecols=[0,1,2,3,4,5,6,7,8]) #不加dtype=str，自动进行读取和转换
#,usecols=[0,1,2,3,4,5,6,7,8]
print("2:head============================================================================")
print(df.head())
print("2:describe============================================================================")
print(df.describe())
print("2:info============================================================================")
print(df.info())
print("================================")
#2.查看是否有缺失值
print(df.isnull().sum().sort_values(ascending=False))
print("================================")
#df.drop(['DEWP','HUMI','PRES','TEMP'],axis=1,inplace=True)
#df.drop(df.columns[[range(9,17)]],axis=1,inplace=True)
print(df.info())

#方案二，直接使用dataframe的方法
#3.去掉三列PM数据全部为空的行
print(df.info())
df.dropna(axis=0, how='all', subset=['PM_Taiyuanjie','PM_US Post','PM_Xiaoheyan'], inplace=True)

print("**************************")
print(df.info())
df.to_csv("sy.csv")

#4.计算平均值
start = time.time()
df['sum'] = df[['PM_Taiyuanjie','PM_Xiaoheyan','PM_US Post']].sum(axis=1)  #axis=1表示在行上进行操作
df['count'] = df[['PM_Taiyuanjie','PM_Xiaoheyan','PM_US Post']].count(axis=1)
df['ave']=round(df['sum']/df['count'],2)
end = time.time()
print("---------------duration:",end-start)

#5.输出到文件
df.to_csv("shenyang_ave.csv")
print("****** done ******")

#6.按照年做汇总，查看年的平均值
print(df.groupby("year").mean())


