import json

# json本质是个字符串
# json字符串中只能用双引号，不能单引号

# www.json.cn


p_list = [
    {
        'username': 'hello',
        'age': '16',
        'country': 'china'
    },
    {
        'username': 'hey',
        'age': '15',
        'country': 'US'
    },
    {
        'username': '张三',
        'age': '14',
        'country': 'Africa'
    }
]

# python对象转json

json_str = json.dumps(p_list)  # 将python对象转换为json对象（单双引号转换等）
print(json_str)
print(type(json_str))

# python对象转json并保存

with open(r'Crawler_L\json\per.json', 'w', encoding='utf-8') as w:
    json.dump(p_list, w, ensure_ascii=False)  # 第一个参数传python对象，第二个传文件,第三个是字符串中有中文时把默认编码方式关掉

# json.dump(list)   列表转json
# json.dumps(list,file,ensure_ascii=False)  列表转json并存文件
