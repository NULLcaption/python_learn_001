"""
码上赢数据可是展示data_1
"""
import pandas as pd
from numpy import *
from pyecharts import Bar, Geo, WordCloud, Pie, Line

"""
读取合并后的execl文件
"""
df = pd.read_csv("F:\\test_data\\dataSource.csv")

"""
读取表头
可以只选择自己有用的的列名即可
门店ID	省	市	区	商品条码	商品名称	品牌	销量	销售额(元)	销售月份	销售所在周	销售日期
"""
a = df["门店ID"]
b = df["省"]
c = df["市"]
d = df["区"]
e = df["商品条码"]
f = df["商品名称"]
i = df["销售额(元)"]
j = df["销售月份"]
k = df["销售所在周"]
l = df["销售日期"]
g = df["品牌"]
h = df["销量"]

"""根据筛选条件生成新的数据表"""


# 1、筛选出品牌为香飘飘的数据生成data0.csv
def data_1(g):
    result = df[g == "香飘飘"]
    result.head()
    result.shape
    result.to_csv('F:\\test_data\\data0.csv', sep=',', index=False, encoding="utf_8_sig")
    print("生成完成")


# 2、筛选出销量小于10的所有数据生成data1.csv
def data_2(h):
    result = df[h < 10]
    result.head()
    result.shape
    result.to_csv('F:\\test_data\\data1.csv', sep=',', index=False, encoding="utf_8_sig")
    print("生成完成")


# 3、筛选出浙江的香飘飘的所有数据生成data2.csv
def data_3(b, g):
    result = df[b.str.contains("浙江") & g.str.contains("香飘飘")]
    result.head()
    result.shape
    result.to_csv('F:\\test_data\\data2.csv', sep=',', index=False, encoding="utf_8_sig")
    print("生成完成")


# 4、筛选出香飘飘和优乐美的所有数据生成data3.csv
def data_4(g):
    result = df[g.str.contains("优乐美") | g.str.contains("香飘飘")]
    result.head()
    result.shape
    result.to_csv('F:\\test_data\\data3.csv', sep=',', index=False, encoding="utf_8_sig")
    print("生成完成")


# 5、筛选出销量在100以上的数据，并生成data4
def data_5(h):
    result = df[h > 100]
    result.head()
    result.shape
    result.to_csv('F:\\test_data\\data4.csv', sep=',', index=False, encoding="utf_8_sig")
    print("生成完成")


# 6、筛选出销量在40到60中间的数据，并生成data5
def data_6(h):
    result = df[(h >= 40) & (h < 60)]
    result.head()
    result.shape
    result.to_csv('F:\\test_data\\data5.csv', sep=',', index=False, encoding="utf_8_sig")
    print("生成完成")


# 7、筛选出香飘飘字眼的品牌，并生成data6
def data_7(g):
    result = df[g.str.contains("香飘飘")]
    result.head()
    result.shape
    result.to_csv('F:\\test_data\\data6.csv', sep=',', index=False, encoding="utf_8_sig")
    print("生成完成")


# data_1(g)
# data_2(h)
# data_3(b, g)
# data_4(g)
# data_5(h)
# data_6(h)
data_7(g)
"""开始数据分析"""


def bar_test(b, h):
    X = pd.Series(unique(b)).values
    g_1 = h.groupby(b).sum().round(2).values
    Y = pd.Series(g_1).values
    bar = Bar("统计各省销量柱状图-柱状分布")
    bar.add("", X, Y, mark_point=["average"])
    bar.render("F:\\py_data_html\\bar_test018_1.html")
    print("生成完成")


def bar_test01(g, h):
    X = pd.Series(unique(g)).values
    g_1 = h.groupby(g).sum().round(2).values
    Y = pd.Series(g_1).values
    bar = Bar("统计各品牌销量柱状图-柱状分布")
    bar.add("", X, Y, mark_point=["average"])
    bar.render("F:\\py_data_html\\bar_test018_2.html")
    print("生成完成")


def bar_test02(g, h):
    name = pd.Series(unique(g)).values
    g_1 = h.groupby(g).sum().round(2).values
    value = pd.Series(g_1).values
    pie = Pie("统计各品牌销量饼状图-饼状分布")
    pie.add("", name, value,
            label_text_color=None,
            is_legend_show=False,
            is_label_show=True,
            is_more_utils=True,
            legend_orient="vertical",
            legend_pos="left", )
    pie.render("F:\\py_data_html\\bar_test018_3.html")
    print("生成完成")

# bar_test(b, h)
# bar_test01(g, h)
# bar_test02(g, h)
