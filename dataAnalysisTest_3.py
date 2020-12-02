"""
K—近邻算法：测量不同特征之间的距离方法进行的分类。
优点：精度高，对异常数据不敏感，无数据假定
缺点：计算复杂度高，空间复杂高
使用数据范围：数值型和标称型
"""
import pandas as pd
from matplotlib.font_manager import FontProperties
from numpy import *
import matplotlib.pyplot as plt

df = pd.read_excel("D:\Backup\Downloads\data_1.xlsx")
df_1 = pd.read_excel("D:\Backup\Downloads\data_2.xlsx")
df_2 = pd.read_excel("D:\Backup\Downloads\data_3.xlsx")

num = df['数量']
p_ages = df['货龄']
num_1 = df_1['数量']
p_ages_1 = df_1['货龄']
num_2 = df_2['数量']
p_ages_2 = df_2['货龄']

X = pd.Series(unique(p_ages)).values
X1 = pd.Series(unique(p_ages_1)).values
X2 = pd.Series(unique(p_ages_2)).values
Y = pd.Series(num.groupby(p_ages).sum()).values
Y1 = pd.Series(num_1.groupby(p_ages_1).sum()).values
Y2 = pd.Series(num_2.groupby(p_ages_2).sum()).values

print(concatenate([Y, Y1, Y2]))
Y_1 = concatenate([Y, Y1, Y2])
X_1 = concatenate([X, X1, X2])


plt.subplot(1, 1, 1)
plt.scatter(X_1, Y_1.reshape(4, 12))

plt.show()