"""
利用Python快速合并多个excel文件
"""
import os
import pandas as pd
import numpy as np

dir = "F:\\test_data"  # 设置工作路径

# 新建列表，存放文件名（可以忽略，但是为了做的过程能心里有数，先放上）
filename_excel = []

# 新建列表，存放每个文件数据框（每一个excel读取后存放在数据框）
frames = []

for root, dirs, files in os.walk(dir):
    for file in files:
        filename_excel.append(os.path.join(root, file))
        df = pd.read_excel(os.path.join(root, file))  # excel转换成DataFrame
        frames.append(df)
# 打印文件名
print(filename_excel)
# 合并所有数据
result = pd.concat(frames, sort=False)

# 查看合并后的数据
result.head()
result.shape

# 保存合并的数据到电脑D盘的merge文件夹中，并把合并后的文件命名为dataSource.csv
result.to_csv('F:\\test_data\\dataSource.csv', sep=',', index=False, encoding="utf_8_sig")

print("合并完成")