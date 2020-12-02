"""
实际案例分析：
数据来源： 香飘飘2019/04到2019/05月的分销提报数据
"""
import pandas as pd
from matplotlib.font_manager import FontProperties
from numpy import *
import matplotlib.pyplot as plt
from datetime import datetime

# 数据源处理
data = pd.read_excel("D:\Backup\Downloads\data_4.xlsx")
a = data["大区"]
b = data["省份"]
c = data["经销商"]
d = data["SKU名称"]
e = data["货龄"]
num = data['数量']


# 各经销商分销量
def c_data(c):
    X = pd.Series(unique(c)).values
    X_1 = X.reshape(73, 20)
    Y = pd.Series(num.groupby(c).sum()).values
    Y_1 = Y.reshape(73, 20)
    plt.subplot(1, 1, 1)
    plt.rcParams['font.sans-serif'] = ['SimHei']
    plt.title("香飘飘2019/04到2019/05月各经销商分销量", loc='center')
    plt.plot(X_1[20], Y_1[20])
    plt.xticks(X_1[20], rotation=90)
    plt.show()


# 各SKU分销量
def d_data(d):
    X = pd.Series(unique(d)).values
    Y = pd.Series(num.groupby(d).sum()).values
    plt.subplot(1, 1, 1)
    plt.rcParams['font.sans-serif'] = ['SimHei']
    plt.title("香飘飘2019/04到2019/05月各SKU分销量", loc='center')
    plt.bar(X, Y)
    plt.xticks(X, rotation=90)
    plt.show()


# 省份经销商分销量
def b_data(b):
    X = pd.Series(unique(b)).values
    Y = pd.Series(num.groupby(b).sum()).values
    plt.subplot(1, 1, 1)
    plt.rcParams['font.sans-serif'] = ['SimHei']
    plt.title("香飘飘2019/04到2019/05月各省份经销商分销量", loc='center')
    plt.plot(X, Y)
    plt.xticks(X, rotation=90)
    for a1, b1 in zip(X, Y):
        plt.text(a1, b1, b1, ha='center', va='bottom', fontsize=10)
    plt.show()


# 大区经销商分销量
def a_data(a):
    X = pd.Series(unique(a)).values
    Y = pd.Series(num.groupby(a).sum()).values
    plt.subplot(1, 1, 1)
    plt.rcParams['font.sans-serif'] = ['SimHei']
    plt.title("香飘飘2019/04到2019/05月各大区经销商分销量", loc='center')
    plt.bar(X, Y, width=0.5, align='center', label='分销量')
    for a1, b1 in zip(X, Y):
        plt.text(a1, b1, 1, ha='center', va='bottom', fontsize=10)
    plt.show()


b_data(b)
# c_data(d)
# c_data(c)