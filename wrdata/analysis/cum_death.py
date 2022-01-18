import pandas as pd
import numpy as np
from pandas.core.frame import DataFrame
import matplotlib.pyplot as plt
from pyecharts import options as opts
from pyecharts.charts import Map
from pyecharts.faker import Faker
from pyecharts.render import make_snapshot
from selenium import webdriver
from pyecharts.charts import Map
from pyecharts import options as opts
import requests
import json
import re
import datetime

df1 = pd.read_csv('4confirmed_death.csv', encoding='utf-8')
df1 = df1[df1['day'] == 23]
print(df1)
import os

# 基础数据

value = []
attr = []
for id, row in df1.iterrows():
    attr.append(row['country'])
    value.append(row['confirmeddeath'])

data = []
for index in range(len(attr)):
    city_ionfo = [attr[index], value[index]]
    data.append(city_ionfo)

# c = (Map().add("世界地图", data, "world").set_series_opts(
#     label_opts=opts.LabelOpts(is_show=False)).set_global_opts(
#         title_opts=opts.TitleOpts(title="世界地图示例"),
#         visualmap_opts=opts.VisualMapOpts(max_=200),
#     ).render())

# 打开html
os.system("render.html")

#数据处理
# today = datetime.date.today().strftime('%Y%m%d')
# with open('../data/'+today+'.json','r',encoding='utf8')as f:
#     jsondata = json.load(f)
# listprovince = []
# listcount = []
# for data in jsondata:
#     listprovince.append(data['provinceShortName'])
#     listcount.append(data['confirmedCount'])
# print(listprovince)
# print(listcount)
pieces = [
    {
        'min': 20001,
        'color': '#540d0d'
    },
    {
        'max': 20000,
        'min': 10001,
        'color': '#9c1414'
    },
    {
        'max': 10000,
        'min': 5001,
        'color': '#d92727'
    },
    {
        'max': 5000,
        'min': 1001,
        'color': '#ed3232'
    },
    {
        'max': 1000,
        'min': 101,
        'color': '#f27777'
    },
    {
        'max': 100,
        'min': 1,
        'color': '#f7adad'
    },
    {
        'max': 0,
        'color': '#f7e4e4'
    },
]
# map = Map()
# map.add('vaccine',[list(z) for z in zip(attr,value)],'world')
# map.set_global_opts(visualmap_opts=opts.VisualMapOpts(pieces=pieces,is_piecewise=True,is_show=True),
#                     legend_opts=opts.LegendOpts(is_show=False))

map = Map(init_opts=opts.InitOpts(width='100%', height='1200px'))
map.add("Total death", [list(z) for z in zip(attr, value)], 'world')
map.set_global_opts(
    title_opts=opts.TitleOpts(title='Total Death in the whole world (Till 2021.12.23)'),
    #题⽬
    visualmap_opts=opts.VisualMapOpts(min_=1,max_=816699))

#热⼒图数值区间
map.set_series_opts(label_opts=opts.LabelOpts(is_show=True))  #热⼒图图例
map.render("death.html")  #导出html