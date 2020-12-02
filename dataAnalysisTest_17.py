"""
省份级别的出库分销数据可视化
"""
import pandas as pd
from numpy import *
from pyecharts import Geo, Map
import numpy as np

df = pd.read_excel("D:\Backup\Downloads\data_14.xlsx", sheet_name='分销')

a = df["省份"]
b = df["累计"]


def map_city(a, b):
    areas = pd.Series(unique(a)).values
    values = b.groupby(a).sum().round(2).values
    test_map = Map("2019年7月到10月各个省份分销数据汇总", width=1200, height=600)
    test_map.add("", areas, values,
                 maptype='china',
                 is_visualmap=True,
                 visual_text_color='#000',
                 visual_range=[5000000, 50000000],
                 is_label_show=True)
    test_map.render("E:\\py_data_html\\2019年7月到10月各个省份分销数据汇总.html")
    print("生成完成")


map_city(a, b)
