"""
饿了吗爬虫数据分析-杭州市多家奶茶店
技术栈：Python3和pyecharts （是一个用于生成 Echarts 图表的类库（EchartsJS））
"""
import pandas as pd
from numpy import *
import matplotlib.pyplot as plt
from pyecharts import Bar
from pyecharts import Scatter

data = pd.read_excel("D:\Backup\Downloads\data_7.xlsx")
data1 = pd.read_excel("D:\Backup\Downloads\data_8.xlsx")
a = data["城市"]
b = data["店铺名称"]
c = data["店铺ID"]
a1 = data["城市"]
b1 = data1["店铺名称"]
e = data1["店铺名称_a"]


# 散点图
def bar_test(c, b):
    X = pd.Series(unique(c)).values
    Y = pd.Series(b.groupby(c).count()).values
    scatter = Scatter("杭州市奶茶门店经营品类数量")
    scatter.add("数量", X, Y)
    scatter.show_config()
    scatter.render("E:\\py_data_html\\ele_data_3.html")


def bar_test(e, b1):
    X = pd.Series(unique(e)).values
    Y = pd.Series(data1.groupby('店铺名称_a')['店铺名称'].nunique()).values
    plt.subplot(1, 1, 1)
    plt.rcParams['font.sans-serif'] = ['SimHei']
    plt.title("杭州市奶茶连锁门店(抽样数据)数量", loc='center')
    plt.bar(X, Y)
    plt.xticks(X, rotation=90)
    for a_1, b_1 in zip(X, Y):
        plt.text(a_1, b_1, b_1, ha='center', va='bottom', fontsize=10)
    plt.show()


# bar_test(c, b)
bar_test(e, b1)
# print(pd.Series(data1.groupby('店铺名称_a')['店铺名称'].nunique()).values)
