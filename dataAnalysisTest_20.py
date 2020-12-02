"""
码上赢数据可是展示data_1
"""
import pandas as pd
from numpy import *
from pyecharts import Bar, Geo, WordCloud, Pie, Line

"""
读取合并后的execl文件
"""
df0 = pd.read_csv("F:\\test_data\\data0.csv")
df1 = pd.read_csv("F:\\test_data\\data1.csv")
df2 = pd.read_csv("F:\\test_data\\data2.csv")
df3 = pd.read_csv("F:\\test_data\\data3.csv")
df4 = pd.read_csv("F:\\test_data\\data4.csv")
df5 = pd.read_csv("F:\\test_data\\data5.csv")
df6 = pd.read_csv("F:\\test_data\\data6.csv")
"""
读取表头
可以只选择自己有用的的列名即可
门店ID	省	市	区	商品条码	商品名称	品牌	销量	销售额(元)	销售月份	销售所在周	销售日期
"""
b0 = df0["省"]
c0 = df0["市"]
d0 = df0["区"]
i0 = df0["销售额(元)"]
h0 = df0["销量"]

b3 = df3["省"]
c3 = df3["市"]
d3 = df3["区"]
g3 = df3["品牌"]
i3 = df3["销售额(元)"]
h3 = df3["销量"]

g1 = df1["品牌"]
h1 = df1["销量"]

g4 = df4["品牌"]
h4 = df4["销量"]

g5 = df5["品牌"]
h5 = df5["销量"]

b6 = df6["省"]
c6 = df6["市"]
d6 = df6["区"]
g6 = df6["品牌"]
i6 = df6["销售额(元)"]
h6 = df6["销量"]


def bar_test6():
    name = pd.Series(unique(g6)).values
    g_1 = h6.groupby(g6).sum().round(2).values
    value = pd.Series(g_1).values
    pie = Pie("2020年1月到2月香飘飘以及山寨品销量饼状分布")
    pie.add("", name, value,
            label_text_color=None,
            is_legend_show=False,
            is_label_show=True,
            is_more_utils=True,
            legend_orient="vertical",
            legend_pos="left", )
    pie.render("F:\\py_data_html\\2020年1月到2月香飘飘以及山寨品销量饼状分布.html")
    print("生成完成")


# bar_test6()


def bar_test3():
    X = pd.Series(unique(b3)).values
    Y = pd.Series(df3.loc[df3['品牌'] == '香飘飘', '销量'].groupby(b3).sum()).sort_values().values
    Y_1 = pd.Series(df3.loc[df3['品牌'] == '优乐美', '销量'].groupby(b3).sum()).sort_values().values
    bar = Bar("香飘飘/优乐美在各省销量柱状分布", "时间：2020年1月—2020年2月")
    bar.add("香飘飘", X, Y,
            mark_point=["max", "min"],
            mark_line=["average"],
            is_datazoom_show=True,
            is_label_show=True)
    bar.add("优乐美", X, Y_1,
            mark_point=["max", "min"],
            mark_line=["average"],
            is_datazoom_show=True,
            is_label_show=True)
    bar.render("F:\\py_data_html\\2020年一月到二月在各省销量柱状分布.html")
    print("生成完成")


# bar_test3()


def bar_test():
    X = pd.Series(unique(b0)).values
    g_1 = h0.groupby(b0).sum().round(2).sort_values().values
    Y = pd.Series(g_1).values
    bar = Bar("2020年一月到二月香飘飘在各省销量柱状分布")
    bar.add("", X, Y, mark_point=["average"])
    bar.render("F:\\py_data_html\\2020年一月到二月香飘飘在各省销量柱状分布.html")
    print("生成完成")


# bar_test(b0, h0)


def bar_test1():
    X = pd.Series(unique(b0)).values
    g_1 = i0.groupby(b0).sum().round(2).sort_values().values
    Y = pd.Series(g_1).values
    bar = Bar("2020年一月到二月香飘飘在各省销售额(元)柱状分布")
    bar.add("", X, Y, mark_point=["average"])
    bar.render("F:\\py_data_html\\2020年一月到二月香飘飘在各省销售额(元)柱状分布.html")
    print("生成完成")


#
# bar_test1(b0, i0)


def pie_test2(g1, h1):
    name = pd.Series(unique(g1)).values
    g_1 = h1.groupby(g1).sum().round(2).values
    value = pd.Series(g_1).values
    pie = Pie("2020年1月到2月各品牌单杯销量在小于10饼状分布")
    pie.add("", name, value,
            label_text_color=None,
            is_legend_show=False,
            is_label_show=True,
            is_more_utils=True,
            legend_orient="vertical",
            legend_pos="left", )
    pie.render("F:\\py_data_html\\2020年1月到2月各品牌单杯销量在小于10饼状分布.html")
    print("生成完成")


# pie_test2(g1, h1)


def pie_test4(g4, h4):
    name = pd.Series(unique(g4)).values
    g_1 = h4.groupby(g4).sum().round(2).values
    value = pd.Series(g_1).values
    pie = Pie("2020年1月到2月各品牌单杯销量大于100饼状分布")
    pie.add("", name, value,
            label_text_color=None,
            is_legend_show=False,
            is_label_show=True,
            is_more_utils=True,
            legend_orient="vertical",
            legend_pos="left", )
    pie.render("F:\\py_data_html\\2020年1月到2月各品牌单杯销量大于100饼状分布.html")
    print("生成完成")


# pie_test4(g4, h4)


def pie_test5(g5, h5):
    name = pd.Series(unique(g5)).values
    g_1 = h5.groupby(g5).sum().round(2).values
    value = pd.Series(g_1).values
    pie = Pie("2020年1月到2月各品牌单杯销量在40至60之间饼状分布")
    pie.add("", name, value,
            label_text_color=None,
            is_legend_show=False,
            is_label_show=True,
            is_more_utils=True,
            legend_orient="vertical",
            legend_pos="left", )
    pie.render("F:\\py_data_html\\2020年1月到2月各品牌单杯销量40至60之间饼状分布.html")
    print("生成完成")


pie_test5(g5, h5)
