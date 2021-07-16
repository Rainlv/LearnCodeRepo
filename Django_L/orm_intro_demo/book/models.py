from django.db import models


# 一个类代表数据库中的一张表
class Book(models.Model):
    # 一条属性代表一个字段

    # id:自增长，主键
    id = models.AutoField(primary_key=True)
    # name:最大长度100，varchar类型，不能为空
    name = models.CharField(max_length=100, null=False)
    # author:最大长度100，varchar类型，不能为空
    author = models.CharField(max_length=100, null=False)
    # price:float类型（在数据库中为double），不能为空，默认值为0
    price = models.FloatField(null=False, default=0)


class Publisher(models.Model):
    # 不设置主键，默认会生成一个id字段为主键
    # 相当于 id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, null=False)
    address = models.CharField(max_length=100, null=False)

# 两条命令创建迁移文件，应用到数据库：
# python manage.py makemigrations
# python manage.py migrate
