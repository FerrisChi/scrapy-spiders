import pandas as pd
import matplotlib.pyplot as plt

#打开CSV文件
fileNameStr = 'result2021.csv'
df = pd.read_csv(fileNameStr,encoding='utf-8')

print(df.describe())  #查看统计信息

plt.rcParams['font.sans-serif'] = ['SimHei'] #支持中文的细黑体

f = df.boxplot(column='totalprice', by='district',return_type='dict',meanline=True,showmeans=True)

plt.show()