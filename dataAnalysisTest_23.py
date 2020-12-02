import pandas as pd
from numpy import *
from pyecharts import Bar, Geo, WordCloud, Pie
from wordcloud import wordcloud

df = pd.read_excel("F:\\test_data\\data_001.xlsx", sheet_name='data_1')

a = df["口味"]
a1 = df["喜好度"]
b = df["冷热双泡"]
b_1 = df["原因"]
b_2 = df["新口味"]


# 根据口味计算喜好度
def test_001(a, a1):
    X = pd.Series(unique(a1)).values
    Y = pd.Series(df.loc[df['口味'] == '杨枝甘露水果茶', '喜好度'].groupby(a1).sum()).sort_values().values
    Y_1 = pd.Series(df.loc[df['口味'] == '百香凤梨水果茶', '喜好度'].groupby(a1).sum()).sort_values().values
    bar = Bar("香飘飘新品水果茶喜好度", "时间：2020年5月—2020年6月")
    bar.add("杨枝甘露水果茶", X, Y,
            mark_point=["max", "min"],
            mark_line=["average"],
            is_datazoom_show=True,
            is_label_show=True)
    bar.add("百香凤梨水果茶", X, Y_1,
            mark_point=["max", "min"],
            mark_line=["average"],
            is_datazoom_show=True,
            is_label_show=True)
    bar.render("F:\\py_data_html\\香飘飘水果茶喜好度.html")
    print("生成完成")


# test_001(a, a1)

# 云词分析
def worldCould_test(a, b_1):
    name = pd.Series(unique(a)).values
    g1 = b_1.groupby(a).count().values
    value = pd.Series(g1).values
    worldCoule = WordCloud(width=1200, height=400)
    worldCoule.add("香飘飘新品水果茶喜好原因", name, value, word_size_range=[20, 100])
    worldCoule.render("F:\\py_data_html\\香飘飘新品水果茶喜好原因.html")
    print("生成完成")


worldCould_test(a, b_1)
