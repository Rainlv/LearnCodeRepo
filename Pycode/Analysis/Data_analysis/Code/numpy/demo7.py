import numpy as np
# np生成随机数组

t1 = np.random.randint(10,20,(4,5)) # float类型。参数： 最小值，最大值（取不到），维度
t1 = np.random.rand(4,5) # 0-1间的均匀分布的随机数组，float类型，参数决定维度
t1 = np.random.randn(4,5) # 标准正态分布随机数，float类型，标准差1，平均数0
t1 = np.random.uniform(10,20,(4,5)) # 均匀分布随机数组。float类型。参数： 最小值，最大值（取不到），维度
print(t1)


np.random.seed(10) # 随机数种子，使之后相同手段产生的随机数相同，参数是随机数编号
# 写完seed后每次随机随机数不会改变,都与第一次相同
t2 = np.random.rand(4,5)
print(t2)
