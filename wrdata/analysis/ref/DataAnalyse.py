import numpy as np
import pandas as pd
from pandas import Series,DataFrame
import matplotlib.pyplot as plt
import math

#part1 展示总价和单价的分布直方图
#生成2个子图
fig = plt.figure()
ax1 = fig.add_subplot(121)  #展示总价信息
ax2 = fig.add_subplot(122)  #展示单价信息

#打开CSV文件
fileNameStr = 'MyData202112hd_new.csv'
df = pd.read_csv(fileNameStr,encoding='gbk',nrows=3000)
print("------------describe---------------")
print(df.describe())  #查看统计信息

def count_elements(scores): #定义转换函数，统计每个数值对应多少个
    scorescount = {}  #定义一个字典对象
    for i in scores:
        scorescount[int(i)] = scorescount.get(int(i), 0) + 1 #累加每个整数数值的个数
    return scorescount
'''
#part1 展示总价和单价的分布直方图
counted1 = count_elements(df["totalprice"])
ax1.set_title("Total_Price")
ax1.bar(counted1.keys(),counted1.values(),0.8,alpha=0.5,color='b')

counted2 = count_elements(df["unitprice"])
ax2.set_title("Unit_Price")
ax2.bar(counted2.keys(),counted2.values(),0.8,alpha=0.5,color='r')

plt.show()
#part1 展示总价和单价的分布直方图 结束

'''
#part2，对总价信息进行区间化的处理
ax1.set_title("Total_Price")
max_tp = math.ceil(df["totalprice"].max()/100)*100
interval_len=50

sections = list(np.arange(0,max_tp,interval_len))
print(len(sections))
mylabels = list(np.arange(50,max_tp,interval_len))  #生成x轴上的标签
#mylabels = list(np.arange(interval_len/2,max_tp-interval_len,interval_len))  #生成x轴上的标签
print(len(mylabels))
#result1 = pd.cut(df.totalprice,sections) #使用cut函数分组汇总
result1 = pd.cut(df.totalprice,sections,labels=mylabels) #使用cut函数分组汇总
print("------------result1--------------")
print(result1)
print(type(result1))

print("------------result1.value_counts--------------")
print(result1.value_counts())

result2=result1.value_counts().sort_index()  #按照索引值进行排序
print("------------result2-------------")
print(result2)

#ax1.set_xlim(0,max_tp) #设定x轴的起止范围
ax1.bar(result2.index,result2.values,interval_len*0.8,alpha=0.5,color='b')  #表示取值宽度50*0.8

counted2 = count_elements(df["unitprice"])
ax2.set_title("Unit_Price")
ax2.bar(counted2.keys(),counted2.values(),0.8,alpha=0.5,color='r')

plt.show()
#part2:结束


#part3: 二八定律

plt.figure()
df_counts = pd.Series(result2.values)  #频数，每个区间中房子的个数
print("----------df_counts-------------")
print(df_counts)

df_freq = df_counts/df_counts.sum()    #频率，每个区间的房子个数/总个数，即每个区间的占比
print("----------df_freq-------------")
print(df_freq)

cum_ratio = df_freq.cumsum()           #累计频率，累计百分比
print("----------df_cum_freq-------------")
print(cum_ratio)

df_counts.plot(kind = 'bar', color = 'b', alpha = 0.8, width = 0.6)  #频数的直方图

key = cum_ratio[cum_ratio>0.8].index[0]  #找到大于80%的累计频率对应的索引号
key_num = df_counts.index.tolist().index(key)  #找到对应的索引序号
print('超过80%累计占比的节点值：' ,(key+1)*interval_len)
print('超过80%累计占比的节点值索引位置为：' ,key_num)
print('------')
cum_ratio.plot(style = '-.r2', secondary_y=True)  #累计频率的曲线图,--代表虚线，k代表黑色，o代表圆点
plt.axvline(key_num,  color = 'r', linestyle = '--', alpha = 0.8) #把80%占比的参考线画出来，直接是key_num，因为它是X轴的索引值
plt.text(key_num+1,cum_ratio[key],'cumsum is: %.3f%%' % (cum_ratio[key]*100), color = 'r')  # 文字提示信息

plt.show()
#part3: 结束
