"""
数据数据分析测试一：
1、读取数据源
2、生成散点分布图

案例：微信推广活动领取人数和活动的散点分布
"""
import pandas as pd
from numpy import *
import matplotlib.pyplot as plt

df = pd.read_excel("D:\Backup\Downloads\data_11.xls")

user_count = df["领取人数"]
detail_id = df["活动明细ID"]
plan_id = df['活动ID']

# 用来正常显示中文标签
plt.rcParams['font.sans-serif'] = ['SimHei']

# X/Y 轴坐标设置
X = pd.Series(user_count).values
print(X)
Y = pd.Series(plan_id).values
print(Y)

# 绘制坐标系
plt.scatter(Y, X, marker='o', s=100)

# 标题设置
plt.title('微信推广活动领取人数和活动的散点分布', loc='center')

# 设置x轴Y轴的名称
plt.xlabel('活动')
plt.ylabel('领取人数')

# 不设置网格
plt.grid(False)

plt.show()




