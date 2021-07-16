# map()函数接收两个参数，一个是函数，一个是Iterable，map将传入的函数依次作用到序列的每个元素，并把结果作为新的Iterator返回

li = [1,2,3,4,5,6,7,8,9]
print(list(map(lambda x:x*x,li)))




# reduce()把一个函数作用在一个序列[x1, x2, x3, ...]上，这个函数必须接收两个参数，reduce把结果继续和序列的下一个元素做累积计算
# 接受一个list并利用reduce()求积

from functools import reduce
li = [1,2,3,4,5,6,7,8,9]
print(reduce(lambda x,y:x * y,li))
# 结果=1*2*3*4*5*6*7*8*9 = 362880



# filter()把传入的函数依次作用于每个元素，然后根据返回值是True还是False决定保留还是丢弃该元素。
# 对于序列中的元素进行筛选，最终获取符合条件的序列
# 在一个list中，删掉偶数，只保留奇数

li = [1, 2, 4, 5, 6, 9, 10, 15]
print(list(filter(lambda x:x % 2==1,li)))  # [1, 5, 9, 15]

# 回数是指从左向右读和从右向左读都是一样的数，例如12321，909。请利用filter()筛选出回数
li = list(range(1, 200))
print(list(filter(lambda x:int(str(x))==int(str(x)[::-1]),li)))
[1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 22, 33, 44, 55, 66, 77, 88, 99, 101, 111, 121, 131, 141, 151, 161, 171, 181, 191]



# sorted(iterable,key=None, reverse=False)
# 接收一个key函数来实现对可迭代对象进行自定义的排序
# 可迭代对象：主要与列表，字符串，元祖，集合和字典
# key：接受一个函数，根据此函数返回的结果，进行排序
# reverse：排序方向，默认为从小到大，reverse=True为逆向
# 对列表按照绝对值进行排序

li= [-21, -12, 5, 9, 36]
print(sorted(li, key = lambda x:abs(x)))
# [5, 9, -12, -21, 36]
"""
sorted()函数按照keys进行排序，并按照对应关系返回list相应的元素：

keys排序结果 => [5, 9,  12,  21, 36]
                |  |    |    |   |
最终结果     => [5, 9, -12, -21, 36]
"""
# 假设我们用一组tuple表示学生名字和成绩：

L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]
# 请用sorted()对上述列表分别按名字排序
print(sorted(L, key = lambda x : x[0]))
# 输出[('Adam', 92), ('Bart', 66), ('Bob', 75), ('Lisa', 88)]

# 再按成绩从高到低排序
print(sorted(L, key = lambda x : x[1], reverse=True))
# 输出[('Adam', 92), ('Lisa', 88), ('Bob', 75), ('Bart', 66)]