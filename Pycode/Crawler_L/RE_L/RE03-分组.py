import re

# ()表示分组  (163|126|qq)


# """
# 邮箱匹配
# email = input('请输入邮箱号：')
# result = re.match(r'\w{5,20}@(qq|163|126)\.(com|cn)$',email)
# print(result) 
# """


# """
# 号码和区号分别同时提取
# phone_num = input('输入带区号的手机号码：')
# result = re.match(r'(\d{3,4})-(\d{11})',phone_num)
# if result:
#     print('区号是：{}'.format(result.group(1)))
#     print('号码是：{}'.format(result.group(2)))
# else:
#     print('号码出错') 
# """


# 网页标签匹配

msg = '<html>asdc</html>'

result = re.match(r'<([0-9a-zA-Z]+)>(.+)</\1>$',msg)
        # \1表示引用分组1的内容，即与分组1的内容相同
print(result)
print(result.group(1))
print(result.group(2))
print('-----------')
msg = '<html><h1>hello</h1></html>'
result = re.match(r'<([0-9a-zA-Z]+)><([0-9a-zA-Z]+)>(.+)</\2></\1>$',msg)
print(result)
print(result.group(1))
print(result.group(2))
print(result.group(3))

print('-----------------------')

msg = '<html><h1>hello</h1></html>'
result = re.match(r'<(?P<name1>\w+)><(?P<name2>\w+)>(.+)</(?P=name2)></(?P=name1)>',msg)
# (?P<name1>.....)对分组进行命名，name1可以自己填;(?P=name1)表示引用分组内容
print(result)
print(result.group(1))
print(result.group(2))
print(result.group(3))