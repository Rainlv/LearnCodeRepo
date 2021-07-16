import json

json_str = '[{"username": "hello", "age": "16", "country": "china"}, {"username": "hey", "age": "15", "country": "US"}, {"username": "张三", "age": "14", "country": "Africa"}]'

# json转python对象
person = json.loads(json_str)
print(type(person))
for per in person:
    print(per)

# 从json文件中取值转python对象
with open(r'per.json','r',encoding='utf-8') as r:
    person = json.load(r)
    print(person)
    print(type(person))


# json.loads()  json字符串转Python对象
# json.load()    json文件解析为Python对象