"""
城市级别的出库分销数据可视化
"""
import pandas as pd
from numpy import *
from pyecharts import Geo, Map
import numpy as np

df = pd.read_excel("D:\Backup\Downloads\data_15.xlsx", sheet_name='制图')

# 计算变量
a = df["城市"]
b = df["冲泡出库-经典（含税万元）"]
c = df["冲泡出库-好料（含税万元）"]
d = df["2019财年计划金额-冲泡万元"]
e = df["果汁茶出库（含税万元）"]
f = df["2019财年计划金额-即饮万元"]
g = df["理论终端门店家数"]
h = df["社会消费品零售总额(亿元)"]
i = df["常住人口（万人）"]
j = df["乳制品消费总额（亿元）"]


# type有scatter, effectScatter, heatmap三种模式可选
def geo_test(a, b):
    attr = pd.Series(unique(a)).values
    g1 = b.groupby(a).sum().round(2).values
    value = pd.Series(g1).values
    geo = Geo("各个城市冲泡出库-经典（单位：万元）", width=1200, height=900)
    geo.add("", attr, value,
            maptype='china',
            type='effectScatter',
            symbol_size=15,
            is_visualmap=True,
            is_roam=True,
            visual_range=[200, 5000],
            visual_text_color="#fff")
    geo.render("E:\\py_data_html\\bar_test016_1.html")
    print("生成完成")


def geo_test01(a, b):
    attr = pd.Series(unique(a)).values
    g1 = b.groupby(a).sum().round(2).values
    value = pd.Series(g1).values
    geo = Geo("各个城市冲泡出库-经典（单位：万元）", width=1200, height=900)
    geo.add("", attr, value,
            maptype='china',
            type='heatmap',
            symbol_size=15,
            is_visualmap=True,
            is_roam=True,
            visual_range=[200, 5000],
            visual_text_color="#fff")
    geo.render("E:\\py_data_html\\bar_test016_2.html")
    print("生成完成")


def geo_test02(a, c):
    attr = pd.Series(unique(a)).values
    g1 = c.groupby(a).sum().round(2).values
    value = pd.Series(g1).values
    geo = Geo("各个城市冲泡出库-好料（单位：万元）", width=1200, height=900)
    geo.add("", attr, value,
            maptype='china',
            type='effectScatter',
            symbol_size=15,
            is_visualmap=True,
            is_roam=True,
            visual_range=[200, 5000],
            visual_text_color="#fff")
    geo.render("E:\\py_data_html\\bar_test016_3.html")
    print("生成完成")


def geo_test03(a, d):
    attr = pd.Series(unique(a)).values
    g1 = d.groupby(a).sum().round(2).values
    value = pd.Series(g1).values
    geo = Geo("各个城市2019财年计划金额-冲泡（单位：万元）", width=1200, height=900)
    geo.add("", attr, value,
            maptype='china',
            type='effectScatter',
            symbol_size=15,
            is_visualmap=True,
            is_roam=True,
            visual_range=[200, 5000],
            visual_text_color="#fff")
    geo.render("E:\\py_data_html\\bar_test016_4.html")
    print("生成完成")


def geo_test04(a, e):
    attr = pd.Series(unique(a)).values
    g1 = e.groupby(a).sum().round(2).values
    value = pd.Series(g1).values
    geo = Geo("各个城市果汁茶出库（单位：万元）", width=1200, height=900)
    geo.add("", attr, value,
            maptype='china',
            type='effectScatter',
            symbol_size=15,
            is_visualmap=True,
            is_roam=True,
            visual_range=[200, 5000],
            visual_text_color="#fff")
    geo.render("E:\\py_data_html\\各个城市果汁茶出库.html")
    print("生成完成")


def geo_test05(a, f):
    attr = pd.Series(unique(a)).values
    g1 = f.groupby(a).sum().round(2).values
    value = pd.Series(g1).values
    geo = Geo("各个城市2019财年计划金额-即饮（单位：万元）", width=1200, height=900)
    geo.add("", attr, value,
            maptype='china',
            type='effectScatter',
            symbol_size=15,
            is_visualmap=True,
            is_roam=True,
            visual_range=[200, 5000],
            visual_text_color="#fff")
    geo.render("E:\\py_data_html\\各个城市2019财年计划金额-即饮.html")
    print("生成完成")


def geo_test06(a, g):
    attr = pd.Series(unique(a)).values
    g1 = g.groupby(a).sum().round(2).values
    value = pd.Series(g1).values
    geo = Geo("各个城市理论终端门店家数（单位：家）", width=1200, height=900)
    geo.add("", attr, value,
            maptype='china',
            type='effectScatter',
            symbol_size=15,
            is_visualmap=True,
            is_roam=True,
            visual_range=[5000, 10000],
            visual_text_color="#fff")
    geo.render("E:\\py_data_html\\各个城市理论终端门店家数（5000, 10000）.html")
    print("生成完成")


def geo_test07(a, h):
    attr = pd.Series(unique(a)).values
    g1 = h.groupby(a).sum().round(2).values
    value = pd.Series(g1).values
    geo = Geo("2019年各个城市社会消费品零售总额（单位：亿元）", width=1200, height=900)
    geo.add("", attr, value,
            maptype='china',
            type='effectScatter',
            symbol_size=15,
            is_visualmap=True,
            is_roam=True,
            visual_range=[200, 5000],
            visual_text_color="#fff")
    geo.render("E:\\py_data_html\\各个城市社会消费品零售总额.html")
    print("生成完成")


def geo_test08(a, i):
    attr = pd.Series(unique(a)).values
    g1 = i.groupby(a).sum().round(2).values
    value = pd.Series(g1).values
    geo = Geo("2019年各个城市常住人口（单位：万人）", width=1200, height=900)
    geo.add("", attr, value,
            maptype='china',
            type='effectScatter',
            symbol_size=15,
            is_visualmap=True,
            is_roam=True,
            visual_range=[500, 1000],
            visual_text_color="#fff")
    geo.render("E:\\py_data_html\\各个城市常住人口(500, 1000).html")
    print("生成完成")


def geo_test09(a, j):
    attr = pd.Series(unique(a)).values
    g1 = j.groupby(a).sum().round(2).values
    value = pd.Series(g1).values
    geo = Geo("2019年各个城市乳制品消费总额(单位：亿元）", width=1200, height=900)
    geo.add("", attr, value,
            maptype='china',
            type='effectScatter',
            symbol_size=15,
            is_visualmap=True,
            is_roam=True,
            visual_range=[5, 50],
            visual_text_color="#fff")
    geo.render("E:\\py_data_html\\各个城市城市乳制品消费总额(5, 50).html")
    print("生成完成")


# geo_test(a, b)
# geo_test01(a, b)
# geo_test02(a, b)
# geo_test03(a, d)
# geo_test04(a, e)
# geo_test05(a, f)
# geo_test06(a, g)
# geo_test07(a, h)
# geo_test08(a, i)
geo_test09(a, j)
