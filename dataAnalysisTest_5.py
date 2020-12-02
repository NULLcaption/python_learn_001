"""
测试散点分布：
数据模型--100个质数数散点分布
"""
from numpy import *
import matplotlib.pyplot as plt
import pandas as pd


# 100个素数函数
def call_back_value():
    arr = []
    for i in range(2, 100):
        flag = 0
        for j in (2, i-1):
            if not(i%j):
                flag = 1
                break
        if flag == 0:
            arr.append(i)
    return arr


group = call_back_value()

X = pd.Series(group).values
Y = pd.Series(group).values

fig = plt.figure()
plt.scatter(X, Y, marker='o', s=100)
plt.show()
