"""
城市级别的出库分销数据可视化
"""
import pandas as pd
from numpy import *
from pyecharts import Line
from pyecharts import Map
from pyecharts import Geo

df = pd.read_excel("D:\Backup\Downloads\data_14.xlsx", sheet_name='分销')

# 计算变量
a = df["城市"]
a1 = df["国家省"]
b = df["累计"]
b_1 = df["7月"]
b_2 = df["8月"]
b_3 = df["9月"]
b_4 = df["10月"]


# type有scatter, effectScatter, heatmap三种模式可选
def geo_test(a, b):
    attr = pd.Series(unique(a)).values
    g1 = b.groupby(a).sum().round(2).values
    value = pd.Series(g1).values
    geo = Geo("2019年7月到10月各城市累计分销数据", width=1200, height=900)
    geo.add("", attr, value,
            maptype='china',
            type='effectScatter',
            symbol_size=15,
            is_visualmap=True,
            is_roam=True,
            visual_range=[1000000, 5000000],
            visual_text_color="#fff")
    geo.render("E:\\py_data_html\\bar_test014_2.html")
    print("生成完成")


def geo_test01(a, b):
    attr = pd.Series(unique(a)).values
    g1 = b.groupby(a).sum().round(2).values
    value = pd.Series(g1).values
    geo = Geo("2019年7月到10月各城市累计分销数据", width=1200, height=900)
    geo.add("", attr, value,
            maptype='china',
            type='heatmap',
            symbol_size=15,
            is_visualmap=True,
            is_roam=True,
            visual_range=[5000000, 10000000],
            visual_text_color="#fff")
    geo.render("E:\\py_data_html\\bar_test014_3.html")
    print("生成完成")


# geo_test(a, b)
# geo_test01(a, b)
