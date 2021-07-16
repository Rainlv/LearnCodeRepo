import numpy as np
import random

# 生成np数组对象
a =np.array([1,2,3,4,5])
b = np.array(range(1,6))
c = np.arange(1,6)
print(type(a),type(b),type(c))
print('='*20)

# 查看数组内原始数据类型
print(a.dtype)
print('='*20)

# np数据类型
    # int8 
t1 = np.array(range(1,4),dtype='i1')
print(t1)
print(t1.dtype)
print('='*20)
    # 布尔类型
t2 = np.array([1,0,1,1,0,0],dtype=bool)
print(t2)
print(t2.dtype)
    # 类型转换
t3 = t2.astype('i2')
print(t3)
print(t3.dtype)

print('='*20)

# np中的小数
    # random.random()产生0-1的随机小数
a1 = np.array([random.random() for i in range(4)])
print(np.round(a1,2))  # np中小数保留
    
a2 = random.random()
print(round(a2,2))  # python语法中的小数保留

