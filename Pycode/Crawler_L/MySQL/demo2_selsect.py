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

# select username,age from user where id = 1    # where后面的参数控制过滤条件
# select * from user    #   *代表全选

sql = '''
select * from user
'''
cursor.execute(sql)
########### fetchone ############
# while True:
#     result = cursor.fetchone()  # 每次取出一行
#     if result:
#         print(result)
#     else:
#         break



############    fetchall    ###########
# results = cursor.fetchall()     # 返回元组((),(),())
# print(type(results))
# for result in results:
#     print(result)



############    fetchmany    ###########
results = cursor.fetchmany(2)     # 返回元组((),(),()),可以设定返回数量
print(type(results))
for result in results:
    print(result)




conn.close()