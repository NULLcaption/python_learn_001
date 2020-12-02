"""
城市级别的出库分销数据可视化
"""
import pandas as pd
from numpy import *
from pyecharts import Bar, Geo, WordCloud, Pie

df = pd.read_excel("D:\Backup\Downloads\data_14.xlsx", sheet_name='出库')

# 计算变量
a = df["国家城市"]
b = df["标箱量"]
c = df["品项"]
d = df["品牌"]


def pie_test(d, b):
    name = pd.Series(unique(d)).values
    g1 = b.groupby(d).sum().round(2).values
    value = pd.Series(g1).values
    pie = Pie("各品牌出库数据")
    pie.add("", name, value, is_label_show=True)
    pie.show_config()
    pie.render("E:\\py_data_html\\bar_test015_5.html")
    print("生成完成")


def worldCould_test(c, b):
    name = pd.Series(unique(c)).values
    g1 = b.groupby(c).sum().round(2).values
    value = pd.Series(g1).values
    worldCoule = WordCloud(width=1200, height=400)
    worldCoule.add("2018年10月到2019年10月香飘飘各品项出库数据-云词分布", name, value, word_size_range=[20, 100])
    worldCoule.show_config()
    worldCoule.render("E:\\py_data_html\\bar_test015_4.html")
    print("生成完成")


def bar_test(c, b):
    X = pd.Series(unique(c)).values
    g1 = b.groupby(c).sum().round(2).values
    Y = pd.Series(g1).values
    bar = Bar("2018年10月到2019年10月香飘飘各品项出库数据-柱状分布")
    bar.add("", X, Y, mark_point=["average"])
    bar.render("E:\\py_data_html\\bar_test015_3.html")
    print("生成完成")


# type有scatter, effectScatter, heatmap三种模式可选
def geo_test(a, b):
    attr = pd.Series(unique(a)).values
    g1 = b.groupby(a).sum().round(2).values
    value = pd.Series(g1).values
    geo = Geo("2018年10月到2019年10月香飘飘各城市出库数据-散点分布", width=1200, height=900)
    geo.add("", attr, value,
            maptype='china',
            type='effectScatter',
            symbol_size=15,
            is_visualmap=True,
            is_roam=True,
            visual_range=[200000, 500000],
            visual_text_color="#fff")
    geo.render("E:\\py_data_html\\bar_test015_1.html")
    print("生成完成")


def geo_test01(a, b):
    attr = pd.Series(unique(a)).values
    g1 = b.groupby(a).sum().round(2).values
    value = pd.Series(g1).values
    geo = Geo("2018年10月到2019年10月香飘飘各城市出库数据-热力分布", width=1200, height=900)
    geo.add("", attr, value,
            maptype='china',
            type='heatmap',
            symbol_size=15,
            is_visualmap=True,
            is_roam=True,
            visual_range=[200000, 500000],
            visual_text_color="#fff")
    geo.render("E:\\py_data_html\\bar_test015_2.html")
    print("生成完成")


# geo_test(a, b)
# geo_test01(a, b)
# bar_test(c, b)
# worldCould_test(c, b)
pie_test(d, b)
