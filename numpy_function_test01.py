import numpy as np

# 生成3行4列的元素为1矩阵并
print(np.ones((3, 4))*2)
# 生成随机数矩阵
print(np.random.rand(3, 4))
# 生成正态分布的随机矩阵
print(np.random.randn(4, 4))
# 生成某个个指定数字以内的随机的矩阵
print(np.random.choice(100, (10, 10)))
# shuffle 为什么输出为none？？
# 因为shuffle函数是用来改变初始值a的，在源码中直接输出shuffle函数的值时返回为NONE。
a = np.arange(100)
np.random.shuffle(a)
print(a)

# 这里都是以为数组的下的操作
# 获取数组index为3的元素value
print(a[3])
# 获取数组index为-3即倒数第三个元素的value
print(a[-3])
# 获取数组中index为5到10的元素value数组，但是不包含index为10的元素value
# a[:10]或者a[10:]或者a[10:-2]
print(a[5:10])
print(a[10:-2])

# 多维数组的操作
arr = np.random.choice(100, (10, 10))
print(arr)
# 获取某行的数据
print(arr[1])
# 获取某几行的数据，注意不包含最后一行的index的value
print(arr[1:4])
# 获取某列的数据
print(arr[:, 1])
# 获取某几列的数据
print(arr[:, 1:4])
# 同时获取行和列
print(arr[1:3, 5:8])


# numpy 数据预处理
# 数据类型转换
arr_1 = np.arange(5)
# 数组类型原型 >>>int32
print(arr_1.dtype)
# 将arr_1的数据类型转换为float
arr_float = arr_1.astype(np.float64)
print(arr_float)
print(arr_float.dtype)
# 将arr_1装换为String类型
arr_string = arr_1.astype(np.string_)
print(arr_string)
print(arr_string.dtype)


# 缺失值处理
arr_2 = np.array([1, 20, np.nan, 50])
print(arr_2)
# 检查缺失值，缺失则返回true
print(np.isnan(arr_2))
# 将缺失值填充为0
arr_2[np.isnan(arr_2)] = 0
print(arr_2)

# 去取数组中的重复元素
arr_3 = np.array([1, 20, 20, 50])
print(np.unique(arr_3))

# numpy数组的数重塑
# 一维重塑
arr_4 = np.arange(12)
print(arr_4)
# 将一维数组重塑为3行4列的多维数组
print(arr_4.reshape(3, 4))
print(arr_4.reshape(4, 3))
# 多维数组重塑
arr_5 = np.random.choice(100, (4, 10))
print(arr_5)
print(arr_5.reshape(10, 4))
# 数组旋转
print(arr_5.T)


# numpy 数组合并
# 横向合并
arr_6 = np.random.choice(100, (4, 10))
arr_7 = np.random.choice(50, (4, 10))
print(arr_6)
print(arr_7)
# 参数 axis=1 表示向横向合并
print(np.concatenate([arr_6, arr_7], axis=1))
# 以元组的方式进行合并
print(np.hstack((arr_6, arr_7)))
print(np.column_stack((arr_6, arr_7)))

# 纵向合并
# 参数 axis=0 表示纵向合并
print(np.concatenate([arr_6, arr_7], axis=0))
# 以元组的方式进行合并
print(np.vstack((arr_6, arr_7)))
print(np.row_stack((arr_6, arr_7)))

# 常用数据分析函数
arr_8 = np.arange(8)
print(arr_8)
# 元素级函数
# 求0~7的平方根
print(np.sqrt(arr_8))
# 求0~7的平方
print(np.square(arr_8))

# 描述统计函数
arr_9 = np.random.choice(100, (4, 10))
print(arr_9)
# 求和
print(arr_9.sum())
# 每一行求和
print(arr_9.sum(axis=1))
# 每一列求和
print(arr_9.sum(axis=0))

# 求平均值
print(arr_9.mean())
# 求每一行的平均值
print(arr_9.mean(axis=1))
# 求每一列的平均值
print(arr_9.mean(axis=0))

# 条件函数
print(np.where(arr_9 > 60, "合格", "不合格"))
print(np.where(arr_9 > 60))

# 集合关系
arr_10 = np.array([1, 2, 3, 4])
arr_11 = np.array([1, 2])
# 包含
print(np.in1d(arr_10, arr_11))
# 交集
print(np.intersect1d(arr_10, arr_11))
# 并集
print(np.union1d(arr_10, arr_11))
# 差集
print(np.setdiff1d(arr_10, arr_11))