"""
测试散点分布：
数据模型--斐切那波数列
"""
from numpy import *
import matplotlib.pyplot as plt
import pandas as pd


# 斐波那契函数
def fib_loop_while(max):
    a, b = 0, 1
    while max > 0:
        a, b = b, a + b
        max -= 1
        yield a


# 返回值
def call_back_value():
    arr = []
    for i in fib_loop_while(50):
        arr.append(i)
    return arr


group = call_back_value()

X = pd.Series(group).values
Y = pd.Series(group).values

fig = plt.figure()
plt.scatter(X, Y, marker='o', s=100)
plt.show()
