import re 

# [123456][568993]
#     一个[]表示pattern中的一个字符，[]里面的内容表示这个字符可能出现的值
# [0-9][a-z]
#     表示范围[0-9]==[0123456789]
# [a-z0-9A-Z_] ==\w 匹配数字字母下划线


# *       0次以上
# +       1次以上
# {m,}    m次以上

# {n}     n次
# {m,n}   m-n次   

# ?       0次 或 1次

msg = 'as5dha7sjk45as123a'

# 匹配as5 ha7 jk4
result = re.findall('[a-z][a-z][0-9]',msg)
print(result)

# 匹配s5d a7s k45a s123a
result = re.findall('[a-z][0-9]+[a-z]',msg)
print(result)

""" 
qq号验证
     1、首位非0
     2、位数 5-11位
"""
""" qq = input('输入要判断的qq号')
result = re.match('[1-9][0-9]{4,10}$',qq)
        # $表示字符串结束
if result:
    print(result.group())
else:
    print('无效的qq号')
 """

# 匹配0-100的数字

n =str(input('请输入0-100的数字'))

result = re.match('[1-9]?[0-9]$|100$',n)
if result:
    print(result.group()) 
else:
    print('非数字或数字格式错误或范围溢出')