"""
描述性统计和数据建模
目标：演示如何是使用pandas和statsmodels生成标准的描述性统计量和模型
关键词解释：
statsmodels是一个有很多统计模型的python库，能完成很多统计测试，数据探索以及可视化。它也包含一些经典的统计方法，比如贝叶斯方法和一个机器学习的模型。
pandas 是基于NumPy 的一种工具，该工具是为了解决数据分析任务而创建的。Pandas 纳入了大量库和一些标准的数据模型，提供了高效地操作大型数据集所需的工具。
数据：葡萄酒的质量
文件：D:\Backup\Downloads\winequality-both.csv
"""
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# 将数据导入到pandas中
wine = pd.read_csv("D:\Backup\Downloads\winequality-both.csv", sep=',', header=0)
wine.columns = wine.columns.str.replace(' ', '_')
print(wine.head())
# 显示所有变量的描述性统计
print(wine.describe())
# 找出唯一值
print(sorted(wine.quality.unique()))
# 计算值的频率
print(wine.quality.value_counts())

# 按照葡萄酒类型显示质量的描述统计
print(wine.groupby('type')[['quality']].describe().unstack('type'))
# 按照葡萄酒类型显示质量的特定分位数值
print(wine.groupby('type')[['quality']].quantile([0.25, 0.75]).unstack('type'))
# 按照葡萄酒的类型查看质量分布
red_wine = wine.loc[wine['type'] == 'red', 'quality']
white_wine = wine.loc[wine['type'] == 'white', 'quality']
sns.set_style('dark')
print(sns.distplot(red_wine, norm_hist=True, kde=False, color='red', label='Red Wine'))
print(sns.distplot(white_wine, norm_hist=True, kde=False, color='white', label='white wine'))
plt.title("Distribution of Quality by wine Type", loc='center')
plt.xlabel('Quality Score')
plt.ylabel('Density')
plt.legend()
plt.show()

# 检验两种葡萄酒的平均质量是有有所不同
print(wine.groupby(['type'])[['quality']].agg(['std']))
