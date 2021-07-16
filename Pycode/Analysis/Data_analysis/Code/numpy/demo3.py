import numpy as np
import random
# 数组索引切片
    #索引取前不取后
t1 = [random.randint(1,100) for i in range(56)]
t1 = np.array(t1).reshape((7,8))
print(t1)
print('这是原数组')

# 取连续多行、单行————同列表操作
# 取不连续多行 把下标放在列表里
# print(t1[[2,3,5]])

# 取行、列
    # 用逗号分割行列下标,前面是行，后面是列
print(t1[1,:])  # 取第二行的所有列
print('*'*20)
print(t1[[2,6],:]) # 取3,7行的所有列
print('*'*20)
print(t1[:,2]) # 取3列的所有行

    #取多个不相邻点
print(t1[[0,2,5],[0,2,7]]) # 只有三个点(0,0)(2,2)(5,7)

print('*'*20)

# 赋值
t2 = np.arange(15).reshape((3,5))
print(t2<3) # 返回一个布尔数组
t2[t2<3] = 3  # 给所有小于3的赋值
print(t2)

    # np中的三元运算符
t3 = np.arange(20).reshape((4,5))
t4 = np.where(t3<10,0,10) # 满足t3<10的元素等于0，不满足的等于10
print(t4)

t5 = t3.clip(5,10) # 小于5的数变成5，大于10的数变成10，但nan不会被替换
print(t5)