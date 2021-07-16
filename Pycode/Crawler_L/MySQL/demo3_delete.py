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

sql = '''
delete from user where id = 3
'''
cursor.execute(sql)
# 插入、删除、更新等对数据库数据更改的操作都需要commit()
conn.commit()
conn.close()