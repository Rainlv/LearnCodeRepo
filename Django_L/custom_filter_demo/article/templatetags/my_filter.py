from django import template
from datetime import datetime

# def greet(value, word):
#     return value + word
#
#
# # 创建一个注册对象
register = template.Library()


# # 使用对象注册自定义的过滤器
# register.filter('greet', greet)  # 第一个参数写调用时的名称，第二个参数是过滤器对应的函数

# 或者使用装饰器注册，会直接用函数名当成调用名注册
@register.filter
def greet(value, word):
    return value + word


# 若想自定义调用名，可在装饰器传参
# @register.filter('my_greet')
# def greet(value, word):
#     return value + word

@register.filter
def time_since(value):
    if not isinstance(value, datetime):
        return value
    time_now = datetime.now()
    # timedelay.total_seconds()
    timestamp = (time_now - value).total_seconds()
    if timestamp < 60:
        return '刚刚'
    elif (timestamp >= 60) and timestamp < 60 * 60:
        minutes = int(timestamp/60)
        return '%s分钟前' % minutes
    elif (timestamp >= 60 * 60) and timestamp < 60 * 60 * 24:
        hours = int(timestamp/60/60)
        return '%s小时前' % hours
    elif (timestamp >= 60 * 60 * 24) and timestamp < 60 * 60 * 24 * 30:
        days = int(timestamp/60/60/24)
        return '%s天前' % days
    else:
        return value.strftime('%Y/%m/%d %H:%M')

