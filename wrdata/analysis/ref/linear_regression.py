#from statsmodels.tsa.arima_model import ARIMA
import pandas as pd
import numpy as np
import random
from matplotlib import pylab as plt

#1.打开CSV文件
fileNameStr = 'result2020.csv'
df = pd.read_csv(fileNameStr,encoding='gbk')

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

#原始数据，面积和总价，散点图
x=df['area']
y=df['totalprice']

ax.scatter(x,y,s=20)
plt.show()

# 回归方程求取函数
def fit(x,y):
    if len(x) != len(y):
        return
    numerator = 0.0  #定义分子
    denominator = 0.0  #定义分母
    x_mean = np.mean(x)
    y_mean = np.mean(y)
    for i in range(len(x)):
        numerator += (x[i]-x_mean)*(y[i]-y_mean)
        denominator += np.square((x[i]-x_mean))
    print('numerator:',numerator,'denominator:',denominator)
    a = numerator/denominator
    b = y_mean - a*x_mean
    return a,b

# 定义预测函数
def predit(x,a,b):
    return a*x + b

# 求取回归方程
a,b = fit(x,y)
print('Line is:y = %2.0fx + %2.0f'%(a,b))

# 生成预测点
x_test = np.random.randint(500, size=50) #产生50个随机数
y_test = np.zeros((1,len(x_test)))
for i in range(len(x_test)):
    y_test[0][i] = predit(x_test[i],a,b)

# 绘制图像
xx = np.linspace(0, 500)
yy = a*xx + b
plt.plot(xx,yy,'k-',color="#FFA500") #画线

plt.scatter(x,y,s=5) #显示原始数据的散点图
plt.scatter(x_test,y_test[0],c='r') #显示测试数据
plt.text(500,500*a+b,'y = %2.0fx + %2.0f'%(a,b),fontsize=15) #显示相关性的线性方程式
plt.show()