import numpy as np
import pandas as pd
#import time
#import scipy
#from matplotlib import pyplot as plt
#from scipy import interpolate
#1.打开CSV文件
fileNameStr = 'gz1.csv'
df = pd.read_csv(fileNameStr,encoding='utf-8',usecols=(1,2,3,4,5,6,9))

print("--------------head--------------")
print(df.head())
print("--------------describe--------------")
print(df.describe())
print("--------------info--------------")
print(df.info())
print("================================")

#2.计算出HUMI_new2列均值和标准差
# 的异常值，并将异常值的行号，放入一个列表temp_list
HUMI_mean=df.HUMI_new2.mean()
HUMI_std=df.HUMI_new2.std()
print(HUMI_mean - 3 * HUMI_std, HUMI_mean + 3 * HUMI_std)

#3.求出HUMI_new2列中数据小于3倍标准差的数据
index_list = df[df.HUMI_new2 < HUMI_mean - 3 * HUMI_std ].index.tolist()
value_list = df[df.HUMI_new2 < HUMI_mean - 3 * HUMI_std ]

print("there are {} items:".format(len(index_list)))
print(index_list)
print(value_list)

#4.对这些数据进行修改，改为3倍标准差的数值
df["HUMI_new3"] = df["HUMI_new2"]
for i in index_list:
    df["HUMI_new3"][i] = HUMI_mean - 3 * HUMI_std

#5.保存至文件
df.to_csv("gz2.csv")

print("---------------------done--------------------")