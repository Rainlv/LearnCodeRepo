from django.db import models


class Article(models.Model):
    # 默认null=False，即数据不能为空

    # 自增长，数据范围较大，映射到数据库中是bigint类型
    id = models.BigAutoField(primary_key=True)

    # BooleanField是布尔类型，映射到字符串中是tinyint类型，0/1，不能为空
    # 要为空的话要用removed = models.NullBooleanField()，默认为空值
    # removed = models.BooleanField()
    removed = models.NullBooleanField()

    # CharField:字符类型，必须传max_length参数
    # 如果超过了254个字符，建议使用TextField
    title = models.CharField(max_length=100, null=True)

    creat_time = models.DateTimeField(null=True)
    # creat_time = models.DateTimeField(auto_now_add=True)  # 创建时，该条属性自动添加为当前时间 --> 创建时间
    # creat_time = models.DateTimeField(auto_now=True) # 每次save时，自动添加属性为当前时间 --> 更新时间


class Page(models.Model):
    name = models.CharField(max_length=100)
    creat_time = models.DateTimeField(auto_now=True)
    title = models.CharField(max_length=100)

    def __str__(self):
        return 'id：%s，name：%s，creat_time：%s，title：%s' % (self.id, self.name, self.creat_time, self.title)

    class Meta:
        db_table = 'page'  # 表名
        ordering = ['-creat_time', 'id']  # 排序，前面加'-'表示降序，默认升序
