import pymysql


# 创建数据库连接
conn = pymysql.connect(
    host = 'localhost',
    user = 'root',
    password = '172706002',
    database = 'pymysql_demo',
    port = 3306
)
cursor = conn.cursor()


# 插入数据

    # 直接插入
# sql = '''
#     insert into user(id,username,age,password) values(2,'he','17','222')
# '''
# cursor.execute(sql) # 执行sql语句

# conn.commit()   # 提交

# conn.close() # 断开连接

    # 格式化插入
sql = '''
insert into user(id,username,age,password) values(null,%s,%s,%s)  
'''     # %s占位符必须为%s，即使是数字也要是%s

username = 'she'
age = 19
password = '33'

cursor.execute(sql,(username,age,password)) # 执行sql语句
conn.commit()   # 提交
conn.close() # 断开连接
