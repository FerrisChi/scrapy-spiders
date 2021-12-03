import pandas as pd

f = pd.read_csv(r'V:\Code\Py_projects\spiders\homework2\1_lianjia\result.csv')

mxid = f['price'].idxmax()
miid = f['price'].idxmin()
mid = f['price'].median()
print(f"\n总价最贵：\n{f.iloc[mxid]}")
print(f"\n总价最便宜：{f.iloc[miid]}")
print(f"\n总价中位数：{mid}")

mxid = f['perunit'].idxmax()
miid = f['perunit'].idxmin()
mid = f['perunit'].median()
print(f"\n均价最贵：\n{f.iloc[mxid]}")
print(f"\n均价最便宜：{f.iloc[miid]}")
print(f"\n均价中位数：{mid}")