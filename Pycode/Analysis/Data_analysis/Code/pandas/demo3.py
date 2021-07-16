import pandas as pd
import numpy as np
# pd相关属性方法

d1 = {
    'name':['zhang','wang','li','cai','xiong','qian','he','huang'],
    'age':[16,18,17,22,32,17,22,32],
    'tel':['10086','1111','521245','45641','15645','54552','56156','15646']
}
t = pd.DataFrame(d1)

# t.values 
#[['zhang', '16', '10086'],
# ['wang', '18', '10011']]

t.index # RangeIndex(start=0, stop=2, step=1)

t.columns # ['name', 'age', 'tel']

t.shape # (2, 3)

t.dtypes
# name    object
# age     int64
# tel     object
# dtype: object

t.ndim # 2   表示数组维度

print(t.head(2)) # 默认显示前五行，传参指明显示前几行
print(t.tail(2)) # 默认显示后五行，传参指明显示后几行

t.info()

t.info()  # 展示概览
# <class 'pandas.core.frame.DataFrame'>
# RangeIndex: 8 entries, 0 to 7
# Data columns (total 3 columns):
# name    8 non-null object
# age     8 non-null int64
# tel     8 non-null object
# dtypes: int64(1), object(2)
# memory usage: 320.0+ bytes

t.describe()

t.describe()   # 对数字类型数据进行统计分析
#       age
# count	8.000000
# mean	22.000000
# std	6.568322
# min	16.000000
# 25%	17.000000
# 50%	20.000000
# 75%	24.500000
# max	32.000000

t.sort_values(by='age',ascending=False) # 对某一列(by指定)进行默认升序排列,设置ascending=False降序
# 	name	age	tel
# 0	zhang	16	10086
# 2	li	17	521245
# 5	qian	17	54552
# 1	wang	18	1111
# 3	cai	22	45641
# 6	he	22	56156
# 4	xiong	32	15645
# 7	huang	32	15646

# 索引切片操作
    # []中写数字是行操作，写字符串是列操作
t[:4] # 取前四行
t['name'] # 取name列
t[:4]['name'] # 取前四行的name列


t2 = pd.DataFrame(np.arange(20).reshape((4,5)),index=list('ABCD'),columns=list('JKWYZ'))
# 索引标签取值
t2.loc[:,"Y"] # 取Y列
t2.loc['A'] # 取A行
    # 取多行
t2.loc[['A','C']] 
t2.loc['A':'C']

# 索引index位置取值
t2.iloc[1:,:2]

# 布尔索引
t[(t['age']>15) & (t['age']<20)]  # 多条件筛选用&、|分割，每个条件用()包裹

# dataframe中.str方法
t[t['name'].str.len()>4]  
    # 前面加.str.
        # .contains 
        # .len
        # .lower、.upper
        # .replace
        # .split