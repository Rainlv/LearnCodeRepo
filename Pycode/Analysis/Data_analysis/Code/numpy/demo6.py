import numpy as np
# 数组操作

    # 数组拼接
t1 = np.arange(12).reshape((2,6))
t2 = np.arange(12,24).reshape((2,6))

t = np.vstack((t1,t2)) # 竖直拼接，t1在上t2在下
print(t)
t = np.hstack((t1,t2)) # 水平拼接，t1在左t2在右
print(t)
    # 某行列交换，赋值操作

    # 创建全为0或1的数组
zeros = np.zeros((3,4))
ones = np.ones((2,5))
print(zeros)
print(ones)

    # 创建对角线为1的正方形数组
sq = np.eye(5) # 参数决定维度
print(sq)

