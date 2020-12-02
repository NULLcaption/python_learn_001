"""
饿了吗爬虫数据分析
技术栈：Python3和pyecharts （是一个用于生成 Echarts 图表的类库（EchartsJS））
"""
import pandas as pd
from numpy import *
from pyecharts import Bar
from pyecharts import Geo
from pyecharts import WordCloud
from pyecharts import Line

data = pd.read_excel("D:\Backup\Downloads\data_6.xlsx")
a = data["城市"]
b = data["店铺名称"]
c = data["店铺ID"]


# 柱状图
def bar_test(a, b):
    X = pd.Series(unique(data["店铺ID"])).values
    Y = pd.Series(pd.Series(data.groupby('店铺ID')['店铺名称'].nunique()).values).values
    bar = Bar("全国各个城市的门店汇总")
    bar.add("", X, Y, mark_point=["average"])
    bar.show_config()
    bar.render("E:\\py_data_html\\ele_data_1.html")


# 地图数据
def geo_test(a, b):
    attr = pd.Series(unique(a)).values
    value = pd.Series(b.groupby(a).count()).values
    data = [("上海", 47647),
            ("北京", 21454),
            ("南京", 849),
            ("南充", 15745),
            ("南通", 16352),
            ("合肥", 11895),
            ("广州", 43589),
            ("延安", 3180),
            ("成都", 19979),
            ("杭州", 33143),
            ("武汉", 6465),
            ("沧州", 13223),
            ("深圳", 31281),
            ("湖州", 22433),
            ("牡丹江", 20526),
            ("西安", 30548),
            ("金华", 22799),
            ("阜阳", 12004)]
    geo = Geo("全国各个城市的门店分布", "数据来源：香飘飘-饿了么爬虫原始数据",
              title_color="#fff", title_pos="center", width=1200, height=600, background_color="#404a59")
    attr_x, value_y = geo.cast(data)
    geo.add("", attr_x, value_y, visual_range=[0, 200], visual_text_color="#fff", symbol_size=15, is_visualmap=True)
    geo.show_config()
    geo.render("E:\\py_data_html\\ele_data_2.html")
    geo


# bar_test(a, b)
# geo_test(a, b)
print(unique(a))
print(pd.Series(data.groupby('店铺ID')['店铺名称'].nunique()))