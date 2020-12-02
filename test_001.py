import pandas as pd
from numpy import *
from pyecharts import Bar, Geo, WordCloud, Pie, Line

df = pd.read_excel("F:\\test\\XPP\\5.3.xlsx")

d = df["业务类型"]


def data_4(d):
    result = df[d.str.contains("交易付款") | d.str.contains("在线支付") | d.str.contains("退款")]
    result.head()
    result.shape
    result.to_csv('F:\\test_001\\data002.csv', sep=',', index=False, encoding="utf_8_sig")
    print("生成完成")


data_4(d)
