import pandas as pd
from pyecharts import options as opts
from pyecharts.charts import Map
from pyecharts.charts import Map
from pyecharts import options as opts
import os

df1 = pd.read_csv('5vaccinated.csv', encoding='utf-8')
df1 = df1[df1['day'] == 23]
print(df1)

value = []
attr = []
for id, row in df1.iterrows():
    attr.append(row['country'])
    value.append(row['vaccinated'] * 100)

data = []
for index in range(len(attr)):
    city_ionfo = [attr[index], value[index]]
    data.append(city_ionfo)
# 打开html
os.system("render.html")
pieces = [
    {
        'min': 100,
        'color': '#540d0d'
    },
    {
        'max': 8,
        'min': 61,
        'color': '#9c1414'
    },
    {
        'max': 60,
        'min': 41,
        'color': '#d92727'
    },
    {
        'max': 40,
        'min': 21,
        'color': '#ed3232'
    },
    {
        'max': 20,
        'min': 11,
        'color': '#f27777'
    },
    {
        'max': 10,
        'min': 1,
        'color': '#f7adad'
    },
    {
        'max': 0,
        'color': '#f7e4e4'
    },
]
map = Map(init_opts=opts.InitOpts(width='100%', height='1200px'))
map.add("vaccineRate", [list(z) for z in zip(attr, value)], 'world')
map.set_global_opts(
    title_opts=opts.TitleOpts(title='Vaccine Rate in the whole world'),
    visualmap_opts=opts.VisualMapOpts(pieces=pieces))
map.set_series_opts(label_opts=opts.LabelOpts(is_show=True))
map.render("new1.html")