"""
数据数据分析测试二：
1、读取数据源
2、生成折现图
案例：某几个个经销商某几个月份的分销量的折线图
"""
import pandas as pd
from matplotlib.font_manager import FontProperties
from numpy import *
import matplotlib.pyplot as plt

# 中文设置
font_set = FontProperties(fname=r"c:\windows\fonts\simsun.ttc", size=12)

df = pd.read_excel("D:\Backup\Downloads\data_1.xlsx")
df_1 = pd.read_excel("D:\Backup\Downloads\data_2.xlsx")
df_2 = pd.read_excel("D:\Backup\Downloads\data_3.xlsx")

num = df['数量']
p_ages = df['货龄']
num_1 = df_1['数量']
p_ages_1 = df_1['货龄']
num_2 = df_2['数量']
p_ages_2 = df_2['货龄']

plt.subplot(1, 1, 1)

# 用来正常显示中文标签
plt.rcParams['font.sans-serif'] = ['SimHei']

# X/Y 轴坐标设置
X = pd.Series(unique(p_ages)).values
Y = pd.Series(num.groupby(p_ages).sum()).values
Y1 = pd.Series(num_1.groupby(p_ages_1).sum()).values
Y2 = pd.Series(num_2.groupby(p_ages_2).sum()).values

# 绘图
plt.plot(X, Y, color="b", linestyle="dashdot", marker="o", markersize=5, label="铜仁市霖瑞丰商贸有限公司")
plt.plot(X, Y1, color="g", linestyle="dashdot", marker="o", markersize=5, label="杭州盛世商贸有限公司")
plt.plot(X, Y2, color="r", linestyle="dashdot", marker="o", markersize=5, label="兰州兴升源商贸有限责任公司")

# 标题设置
plt.title('2018年1月-2019年4月经销商分销提报汇总', loc='center', fontproperties=font_set)

# 设置x轴Y轴的名称
plt.xlabel('提报月份', fontproperties=font_set)
plt.ylabel('提报数量', fontproperties=font_set)

# 设置数据标签
for a, b in zip(X, Y):
    plt.text(a, b, b, ha='center', va='bottom', fontsize=10)

for a, b in zip(X, Y1):
    plt.text(a, b, b, ha='center', va='bottom', fontsize=10)

for a, b in zip(X, Y2):
    plt.text(a, b, b, ha='center', va='bottom', fontsize=10)

plt.grid(False)

plt.legend()

plt.show()
