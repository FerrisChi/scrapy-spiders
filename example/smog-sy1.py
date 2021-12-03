import numpy as np
import pandas as pd
from pandas import Series, DataFrame
import time

#1.打开CSV文件
fileNameStr = 'BeijingPM20100101_20151231.csv'
df = pd.read_csv(fileNameStr,encoding='utf-8',dtype=str)

#fileNameStr = 'BeijingPM20100101_20151231.csv'
#df = pd.read_csv(fileNameStr,encoding='utf-8',usecols=[11,12,13])


#2.查看数据集的基本情况
print("2:head============================================================================")
print(df.head())
print("2:describe============================================================================")
print(df.describe())
print("2:info============================================================================")
print(df.info())

#3.查看是否有缺失值
print("3============================================================================")
print(df.isnull().sum().sort_values(ascending=False))

#4.计算
df['sum'] = df['PM_Dongsihuan']+df['PM_US Post']+df['PM_Dongsi'] #直接加是按照字符串相加的
print("df[sum] is :\n",df['sum'])

print(type(df['PM_Dongsihuan'][52582]))
print(type(df['PM_Dongsihuan'][52583]))
print(type(df['PM_US Post'][52583]))

print("4============================================================================")
df['sum']=0
df['count']=0
start = time.time()
print("start:",end='')

#方案1，使用循环，计算sum和count
for i in range(len(df['PM_Dongsihuan'])):
    sum = count = 0
    if not(df['PM_Dongsihuan'][i] is np.nan):
        sum+=int(df['PM_Dongsihuan'][i])
        count+=1
    if not (df['PM_US Post'][i] is np.nan):
        sum += int(df['PM_US Post'][i])
        count += 1
    if not(df['PM_Dongsi'][i] is np.nan):
        sum+=int(df['PM_Dongsi'][i])
        count+=1

    df['sum'][i]=sum
    df['count'][i] = count
    #df['ave'][i]=sum/count
    if i%5000 == 0:
        print('-',end="")

print('\n',count)
print(df['sum'],df['count'])

#两列直接相除，求得平均值
df['ave']=round(df['sum']/df['count'],2)

end = time.time()
print("-------duration:",end-start)

#5.输出到文件
df.to_csv("smog-sy1.csv")
print("****** done ******")

print(df.groupby("year").mean())




