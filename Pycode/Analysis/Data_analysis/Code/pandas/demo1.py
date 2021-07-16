import pandas as pd
import numpy as np
# 创建数组
t1 = pd.Series([1,2,55,33,48,6]) # 默认索引012345
print(t1)

t1 = pd.Series([1,23,12,313,13],index=list('abcde')) # 自定义索引
print(t1)

    # 字典传入建立数组
dic1 = {
    'name' : 'lihua',
    'age' : 22,
    'tel' : '10086'
}
t1 = pd.Series(dic1)
print(t1) # key对应index，value对应值

# 数据类型及操作方法同numpy

# 取值，key取值和下标取值
# t1['b']
# t1[['a','c']]
# t1[1]
# t1[0]
# t1[t1>2] # 布尔索引

# t1.index # ['a', 'b', 'c', 'd', 'e']
# t1.values # [  1,  23,  12, 313,  13]

# 创建二维数组
t2 = pd.DataFrame(np.arange(20).reshape((4,5)))
# print(t2) # 二维数组，有行索引和列索引
t3 = pd.DataFrame(np.arange(20).reshape((4,5)),index=list('abcd'),columns=list('ABCDE'))
print(t3)  # 自定义行列索引，传入列表

    # 字典创建二维数组  key作为列索引
d1 = {
    'name':['zhang','wang'],
    'age':['16','18'],
    'tel':['10086','10011']
}
t = pd.DataFrame(d1)
    # 列表创建二维数组 缺失属性nan替代
l1 = [
    {'name':'zhang','age':22,'tel':'12344'},
    {'name':'wang','age':12,'tel':'15684'},
    {'name':'gang','tel':'66684'},
    {'name':'zhao','age':92},
]
t = pd.DataFrame(l1)
print(t)