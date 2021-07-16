import pymongo

# 连接数据库
client = pymongo.MongoClient("127.0.0.1",port=27017)

# 获取数据库，若没有则新建
db = client.zhihu

# 获取数据库中的集合(也就是MySQL中的表)
collection = db.qa

# 写入数据      单行写入.insert_one
def writeOneLine():
    collection.insert_one({"username":"aaa"})        

# 写入数据      多行写入.insert_many
def writeAll():
    collection.insert_many([
    {
        'username':'11',
        'password':'22'
                            },
    {
        'username':'1223',
        'password':'sjkdha'
    }
    ])

# 查找数据      .find()返回一个可迭代对象,包含collection下所有数据
def searchAll():
    cursor = collection.find()
    # print(type(cursor))
    for x in cursor:
        print(x)

# 查找数据
def searchOne():
    # result = collection.find_one()  返回第一行数据
    result = collection.find_one({'password':"22"})  # 加入过滤条件
    print(result)


# 更新数据  前面是原来的数据，后面是修改后数据
def update():
    collection.update_one({"username":'11'},{"$set":{"username":'i'}})
    collection.update_many({"username":'aaa'},{"$set":{"username":'iderhua'}})

# 删除数据
def delete():
    collection.delete_one({"username":'1223'})
    collection.delete_many({"username":'iderhua'})