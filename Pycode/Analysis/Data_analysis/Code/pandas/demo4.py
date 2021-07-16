import pandas as pd
import numpy as np
# NaN处理   .isnull、.notnull

t2 = pd.DataFrame(np.arange(20).reshape((4,5)))
t2.iloc[2:,:2] = np.nan
# 0	1	2	3	4
# 0	0.0	1.0	2	3	4
# 1	5.0	6.0	7	8	9
# 2	NaN	NaN	12	13	14
# 3	NaN	NaN	17	18	19

t2.isnull() # NaN值为True，其余为False
# 	0	1	2	3	4
# 0	False	False	False	False	False
# 1	False	False	False	False	False
# 2	True	True	False	False	False
# 3	True	True	False	False	False
t2.notnull() # 结果与t2.isnull()相反

t2.dropna(axis=0,how='any',inplace=False) # how为any时，删除存在nan的所在行/列（axis值决定，axis=0删行）,inplace属性如果为True时，直接将返回的结果赋值给当前数组
t2.dropna(axis=0,how='all') # how为all时，当整行全为nan时才删除行

t2.fillna(0) # 用0来替代nan的值

t2.fillna(t2.mean()) # mean取平均是按列取平均，会跳过nan