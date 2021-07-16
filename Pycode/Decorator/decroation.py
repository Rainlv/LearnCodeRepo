
def decorator1(fun):
    print('装饰器外部1,调用装饰器时就执行，不需要调用')

    def warpper(*args,**kwargs):
        fun(*args,**kwargs)
        print('我是装饰器1')

    print('装饰器外部2,调用装饰器时就执行，不需要调用')
    return warpper

def decorator2(fun):

    def warpper(*args,**kwargs):
        print('我是装饰器2')
        fun(*args,**kwargs)

    return warpper

# 多层装饰器优先执行近的装饰器，也就是decorator1
@decorator2
@decorator1  # 此时就已经执行warpper外部的语句
def house(n): 

    print('我是原函数', n)

# house函数地址装饰完毕后与装饰器中warpper函数地址相同，house = warpper

house(1)    # 此时执行warpper内部函数

print('-----------------------')
 
def outer(a):   # 负责接收装饰器参数
    def decorator(fun):     # 负责接收函数
        def warpper(*args,**kwargs):    # 负责接收函数参数
            print('刷漆')
            print('铺地砖{}块'.format(a))
        return warpper
    return decorator


# 带参装饰器
@outer(10)
def house1():

    print('我是毛坯房')

house1()