import numpy as np

# 数组维度
t1 = np.arange(12)
print(t1.shape)  # (10,) 一维数组

t2 = [[1,2,5],[5,1,9]]
t2 = np.array(t2)
print(t2.shape) # (2,3) 二维数组

t3 = [
    [
        [1,2,3],
        [5,8,9],
        [6,3,0]
    ],
    [
        [1,2,3],
        [5,8,9],
        [6,3,0]
    ]
]
t3 = np.array(t3)
print(t3.shape) # (2, 3, 3) 三维数组 2个块（二维数组），块中数组3行3列

print('='*20 + '以上是数组维度' + '='*20)

t = np.arange(12)
t = t.reshape((3,4)) # 数组维度转换
print(t)
tq = t.reshape((12,)) # 转换为一维
print(tq)
print(t)
tw = t.flatten() # 数组展开为一维
print(tw)

print('='*20 + '以下是数组计算' + '='*20)

# 数组计算
te = np.arange(12)
te = te.reshape((3,4))
print(te+2) # 数组内每个元素+2

tr = np.arange(100,112).reshape(3,4)
print(tr+te) # 同形数组相加，对应位置相加

# 数组转置方法（行列转化）
print('下面是t数组转置：')
t = np.arange(12)
t = t.reshape((3,4))
    #三种转置方法 
print(t.transpose())
print(t.T)
print(t.swapaxes(1,0))  #交换1和0轴