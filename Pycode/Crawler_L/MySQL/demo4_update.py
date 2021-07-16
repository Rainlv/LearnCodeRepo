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

sql ='''
update user set username = 'spider' where id = 1
'''
# 不加where的过滤条件，所有username都会变成spider


cursor.execute(sql)
conn.commit()

conn.close()