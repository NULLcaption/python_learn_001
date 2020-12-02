import pandas as pd
from numpy import *
from pyecharts import Bar
from pyecharts import WordCloud
from pyecharts import Line

# 数据源处理
data = pd.read_excel("D:\Backup\Downloads\data_11.xlsx", index=False, float_format='%.4f')
a = data["大区"]
a_1 = data["省区"]
b = data["影响目标消费者单位成本"]
c = data["影响目标消费者人次"]
d = data["购买人次"]

a1 = data["执行费用-人员费用（元）"]
a2 = data["执行费用-派赠费用（元） "]
a3 = data["执行费用-场地费（元）"]
a4 = data["执行费用-运输费(元)"]


# 柱状图
def bar_test(a, c):
    X = pd.Series(unique(a)).values
    e1 = a1.groupby(a).sum().round(2).values
    e2 = a2.groupby(a).sum().round(2).values
    e3 = a3.groupby(a).sum().round(2).values
    e4 = a4.groupby(a).sum().round(2).values
    c1 = c.groupby(a).sum().round(2)
    g1 = ((e1+e2+e3+e4)/c1).round(2)
    Y = pd.Series(g1).values
    bar = Bar("2019/06到2019/10月各大区推广活动影响目标消费者单位成本(执行费用总和/影响目标消费者人次)")
    bar.add("", X, Y, mark_point=["average"])
    bar.render("E:\\py_data_html\\bar_test001.html")


def bar_test2(a, c, d):
    X = pd.Series(unique(a)).values
    e = c.groupby(a).sum().round(2)
    f = d.groupby(a).sum().round(2)
    g = (f/e).round(2)
    Y = pd.Series(g*100).values
    bar = Bar("2019/06到2019/10月各大区推广活动转化率(%)汇总")
    bar.add("", X, Y, mark_point=["average"])
    bar.render("E:\\py_data_html\\bar_test002.html")


# 柱状图
def bar_test_1(a_1, c):
    X = pd.Series(unique(a_1)).values
    e1 = a1.groupby(a_1).sum().round(2).values
    e2 = a2.groupby(a_1).sum().round(2).values
    e3 = a3.groupby(a_1).sum().round(2).values
    e4 = a4.groupby(a_1).sum().round(2).values
    c1 = c.groupby(a_1).sum().round(2)
    g1 = ((e1+e2+e3+e4)/c1).round(2)
    Y = pd.Series(g1).values
    bar = Bar("2019/06到2019/10月各省区推广活动影响目标消费者单位成本(执行费用总和/影响目标消费者人次)")
    bar.add("", X, Y, mark_point=["average"])
    bar.render("E:\\py_data_html\\bar_test001_1.html")


def bar_test2_1(a_1, c, d):
    X = pd.Series(unique(a_1)).values
    e = c.groupby(a_1).sum().round(2)
    f = d.groupby(a_1).sum().round(2)
    g = (f/e).round(2)
    Y = pd.Series(g*100).values
    bar = Bar("2019/06到2019/10月各省区推广活动转化率(%)汇总")
    bar.add("", X, Y, mark_point=["average"])
    bar.render("E:\\py_data_html\\bar_test002_1.html")


# bar_test_1(a_1, c)
bar_test2_1(a_1, c, d)
# bar_test(a, c)
# bar_test2(a, c, d)
