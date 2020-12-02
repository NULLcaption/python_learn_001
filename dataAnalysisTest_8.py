"""
数据可视化试验：
技术栈：Python3和pyecharts （是一个用于生成 Echarts 图表的类库（EchartsJS））
各种可视化图表测试
"""
import pandas as pd
from numpy import *
from pyecharts import Bar
from pyecharts import WordCloud
from pyecharts import Line

# 数据源处理
data = pd.read_excel("D:\Backup\Downloads\data_4.xlsx")
a = data["大区"]
b = data["省份"]
b1 = data["城市"]
c = data["经销商"]
d = data["SKU名称"]
e = data["货龄"]
f1 = data["品类"]
num = data['数量']


# 折线图
def line_test(b, num):
    X = pd.Series(unique(b)).values
    Y = pd.Series(num.groupby(b).sum()).values
    line = Line("香飘飘2019/04到2019/05月各省区经销商分销量")
    line.add("", X, Y, mark_point=["average"])
    line.show_config()
    line.render("E:\\py_data_html\\line_test.html")


# WordCloud（词云图）
# 根据香飘飘2019/04到2019/05月各大区经销商分销量生成sku名称云词图
def world_cloud_test2(b1, num):
    X = pd.Series(unique(b1)).values
    Y = pd.Series(num.groupby(b1).sum()).values
    wordcloud = WordCloud("", width=1300, height=620)
    wordcloud.add("", X, Y, word_size_range=[20, 100])
    wordcloud.show_config()
    wordcloud.render("E:\\py_data_html\\world_cloud_test_2.html")


def world_cloud_test1(b, num):
    X = pd.Series(unique(b)).values
    Y = pd.Series(num.groupby(b).sum()).values
    wordcloud = WordCloud("", width=1300, height=620)
    wordcloud.add("", X, Y, word_size_range=[20, 100])
    wordcloud.show_config()
    wordcloud.render("E:\\py_data_html\\world_cloud_test_1.html")


def world_cloud_test(d, num):
    X = pd.Series(unique(d)).values
    Y = pd.Series(num.groupby(d).sum()).values
    wordcloud = WordCloud("", width=1300, height=620)
    wordcloud.add("", X, Y, word_size_range=[20, 100])
    wordcloud.show_config()
    wordcloud.render("E:\\py_data_html\\world_cloud_test.html")


# 柱状图
def bar_test(a, num):
    X = pd.Series(unique(a)).values
    Y = pd.Series(num.groupby(a).sum()).values
    bar = Bar("香飘飘2019/04到2019/05月各大区经销商分销量")
    bar.add("", X, Y, mark_point=["average"])
    bar.render("E:\\py_data_html\\bar_test.html")


# # 测试
# bar_test(a, num)
# world_cloud_test(d, num)
# world_cloud_test1(b, num)
# world_cloud_test2(b1, num)
line_test(b, num)