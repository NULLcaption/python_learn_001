"""
测试散点分布：
数据模型--心形函数
x=a*(2*cos(t)-cos(2*t))
y=a*(2*sin(t)-sin(2*t))
"""
import numpy as np
import matplotlib.pyplot as plt

a = 1
t = np.linspace(0, 2*np.pi, 2048)

x = a*(2*np.cos(t)-np.cos(2*t))
y = a*(2*np.sin(t)-np.sin(2*t))

plt.plot(y, x, color='R')
plt.show()