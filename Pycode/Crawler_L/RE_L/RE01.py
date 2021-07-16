import re
# 正则要的是字符串，数字要转

print('------------------match--------------------')

msg = '今天是个大晴天啊！晴天好啊！'
pattern = re.compile('晴天')
    # re.compile('')    建立一个正则规则对象
match_result = pattern.match(msg)  
        # 不使用compile()方法：
            # re.match('晴天',msg)
    # match()方法从头开始匹配，没匹配到返回None
print('match_result:',match_result)    # None


print('---------------search---------------------')


search_result = pattern.search(msg)
    # 匹配整个msg，寻找符合pattern规则的部分,只匹配一次
    # 要多匹配用findall方法，返回的是列表
print('search_result:',search_result)   # <re.Match object; span=(0, 2), match='晴天'>
print(search_result.span()) # 返回匹配对象的位置    (0, 2) 位置包前不包后
print(search_result.group())# 返回成功匹配的对象的内容  晴天


print('--------------sub--------------------')

msg = 'java:60,python:70'
sub_result = re.sub(r'\d+','100',msg)
    #re.sub('pattern定义正则规则','用这个字符替换符合规则的字符','目标字符串')是替换符合正则规则的字符串    
print('sub_result:',sub_result)    # sub_result: java:100,python:100

# re.sub()替换用字符串可传函数
def add(temp):
    num = temp.group()  
    # 调用group将对象<re.Match object; span=(5, 7), match='60'>转换为'60'
    num1 = int(num) +1
    return str(num1)

result = re.search(r'\d+',msg)
print(result)
sub_result = re.sub(r'\d+',add,msg)
        # 调用函数时不加括号
        # 将符合正则的对象<re.Match object; span=(5, 7), match='60'>作为参数传入函数
print('sub_result:',sub_result)    



print('-----------------split----------------')

msg = 'java:60,python:70'

split_result = re.split(r'[,:]',msg)
# re.split('正则规则','目标字符串') 按正则规则匹配到的字符，将字符串切割成列表 
print(type(split_result))
print(split_result)
