import pandas as pd 
import numpy as np 
# pd方法

    # .join方法，合并标签相同的行
t1 = pd.DataFrame(np.arange(20).reshape((4,5)),index=list('abcd'),columns=list('uvxyz'))
# 	u	v	x	y	z
# a	0	1	2	3	4
# b	5	6	7	8	9
# c	10	11	12	13	14
# d	15	16	17	18	19
t2 = pd.DataFrame(np.arange(12).reshape((4,3)),index=list('ABcd'),columns=list('XYZ'))
#   X	Y	Z
# A	0	1	2
# B	3	4	5
# c	6	7	8
# d	9	10	11
t1.join(t2)
#    u	v	x	y	z	X	Y	Z
# a	0	1	2	3	4	NaN	NaN	NaN
# b	5	6	7	8	9	NaN	NaN	NaN
# c	10	11	12	13	14	6.0	7.0	8.0
# # d	15	16	17	18	19	9.0	10.0	11.0
t2.join(t1)
# 	X	Y	Z	u	v	x	y	z
# A	0	1	2	NaN	NaN	NaN	NaN	NaN
# B	3	4	5	NaN	NaN	NaN	NaN	NaN
# c	6	7	8	10.0	11.0	12.0	13.0	14.0
# d	9	10	11	15.0	16.0	17.0	18.0	19.0

    # merge，合并标签相同列（默认类似数据库的自然连接）

t1.merge(t2,left_on='x',right_on='X',how='outer')

    # 数据分组
grouped = t1.groupby(by='name') # 返回的是对象，可遍历
grouped.count()