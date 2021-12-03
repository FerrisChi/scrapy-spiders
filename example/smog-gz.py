import numpy as np
import pandas as pd
#import time
#import scipy
#from matplotlib import pyplot as plt
#from scipy import interpolate
#1.打开CSV文件
fileNameStr = 'BeijingPM20100101_20151231.csv'
df = pd.read_csv(fileNameStr,encoding='utf-8',usecols=[0,1,2,3,4,5,11])

print("--------------head--------------")
print(df.head())
print("--------------describe--------------")
print(df.describe())
print("--------------info--------------")
print(df.info())
print("================================")

#2.查看HUMI列的异常值，并将异常值的行号，放入一个列表temp_list
temp_list = df[df.HUMI < 0].index.tolist()
print(temp_list)

#3.赋值HUMI的内容并新生成一列，将其中异常值的单元格置为空，为插值做准备
df["HUMI_new1"]=df["HUMI"]
for i in temp_list:
    df["HUMI_new1"][i]=np.nan

#4.利用插值，将空单元格进行填充
df["HUMI_new2"]=df["HUMI_new1"].interpolate()

#5.保存至文件
df.to_csv("gz1.csv")

print("--------------describe--------------")
print(df.describe())

print("---------------------done--------------------")

