import numpy as np
# nan和inf 
# nan：not a number ，在数据缺失或不合适计算时出现，如inf-inf
# inf：正无穷大，0/0会出现
# 两者都是浮点型

# print(np.nan == np.nan) # False
# nan与任何数进行计算值都为nan

# 构造nan
t1 = np.arange(20).reshape((4,5))
t1 = t1.astype('float')
t1[3,3] = np.nan
# print(t1)

# 统计nan的个数
    # 利用nan互不相等 统计非0元素个数方法，False是0，其他非0
print(np.count_nonzero(t1!=t1)) # t1!=t1只有在nan时成立
print(np.count_nonzero(np.isnan(t1))) # isnan方法，在为nan时返回true


