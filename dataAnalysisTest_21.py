"""
精品数据分析
"""
import pandas as pd
from numpy import *
from pyecharts import Pie
import seaborn as sns
import matplotlib.pyplot as plt


# 读取csv数据
df = pd.read_csv("F:\\test_data\\data3.csv")

a = df["销量"]
b = df["品牌"]
c = df["销售额(元)"]
d = df["销售所在周"]

# 读取表头
print(df.head())
# 显示销量变量的描述性统计
print(a.describe())
# 显示销量的唯一值
print(sorted(a.unique()))
# 计算销量唯一值出现的频率
print(a.value_counts())

# 按照品牌类型显示销量的描述性统计
print(df.groupby('品牌')[['销量']].describe().unstack('品牌'))
# 按照品牌显示销量对的特定分位数
print(df.groupby('品牌')[['销量']].quantile([0.25, 0.5, 0.75]).unstack('品牌'))


# 按照品牌查看销量的分布
# def function_1():
#     X = pd.Series(unique(b)).values
#     Y = pd.Series(a.groupby(b).sum()).values
#     plt.subplot(1, 1, 1)
#     plt.rcParams['font.sans-serif'] = ['SimHei']
#     plt.title("2020年1月-2月优乐美/香飘飘/香飘飘山寨品销量分布", loc='center')
#     plt.bar(X, Y)
#     plt.xticks(X, rotation=90)
#     plt.show()
def function_1():
    name = pd.Series(unique(b)).values
    g_1 = pd.Series(a.groupby(b).sum()).values
    value = pd.Series(g_1).values
    pie = Pie("2020年1月-2月优乐美/香飘飘/香飘飘山寨品销量分布")
    pie.add("", name, value,
            label_text_color=None,
            is_legend_show=False,
            is_label_show=True,
            is_more_utils=True,
            legend_orient="vertical",
            legend_pos="left", )
    pie.render("F:\\py_data_html\\2020年1月-2月优乐美香飘飘香飘飘山寨品销量分布.html")
    print("生成完成")


# function_1()
# 检验三种品牌之间的销量的平均值是否相同
print(df.groupby('品牌')[['销量']].describe().agg('std'))

# 计算所有变量的相关矩阵
print(df.corr())


# 从两个关键竞品中去除随机小样本进行绘图
# 统计图中的使用的样本，抽样
def tale_sample(data_frame, replace=False, n=200):
    return data_frame.loc[random.choice(data_frame.index, replace=replace, size=n)]


ylm_sample = tale_sample(df.loc[df['品牌'] == '优乐美', :])
xpp_sample = tale_sample(df.loc[df['品牌'] == '香飘飘', :])
sxpp_sample = tale_sample(df.loc[df['品牌'] == '香飘飘山寨品', :])
df_sample = pd.concat([ylm_sample, xpp_sample, sxpp_sample])
df['in_sample'] = where(df.index.isin(df_sample.index), 1., 0.)
print(pd.crosstab(df['in_sample'], df['品牌'], margins=True))
