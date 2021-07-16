import numpy as np
# np中的常用统计函数

t1 = np.arange(20).reshape((4,5))
t1 = t1.astype('float')
t1[3,3] = np.nan
print(t1)
# 求和
print(t1.sum(axis=0)) # axis指定轴方向
# 均值
print(t1.mean(axis=1))
# 中值
print(np.median(t1,axis=0))
# 最小值，最大值
print(t1.max(axis=0))
print(t1.min(axis=0))
# 极差
print(np.ptp(t1,axis=1))
# 标准差
print(t1.std(axis=0))
# 获得最小值、最大值位置,返回各行或列位置的array
print(np.argmax(t1,axis=0))
print(np.argmin(t1,axis=0))