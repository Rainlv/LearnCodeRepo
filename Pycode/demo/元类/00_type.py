# type函数 创建类
# type(类名, 父类的元组（针对继承的情况，可以为空），包含属性的字典（名称和值）)


# 元类就是用来创建类的。也可以换个理解方式就是：元类就是类的类。
# str 是用来创建字符串对象的类，而 int 是用来创建整数对象的类。
# type 就是创建类对象的类。type 就是内建的元类。也就是 Python 自带的元类。



def printHello(self, name='Py'):
    # 定义一个打印 Hello 的函数
    print('Hello,', name)


# 创建一个 Hello 类
Hello = type('Hello', (object,), dict(hello=printHello))

# 实例化 Hello 类
h = Hello()
# 调用 Hello 类的方法
h.hello()
# 查看 Hello class 的类型
print(type(Hello))
# 查看实例 h 的类型
print(type(h))


