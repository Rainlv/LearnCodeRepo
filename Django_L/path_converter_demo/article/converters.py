from django.urls import converters


# converter的写法，照着源码改就行
class CategoryConverter:
    regex = r'\w|(\w+\+\w+)+'

    # to_python 是用在path路径转换时
    def to_python(self, value):
        # value : python + django + flask
        result = value.split('+')
        return result

    # to_url是用在反转（reverse）时
    def to_url(self, value):
        # value : [python, django, flask]
        if isinstance(value, list):
            return '+'.join(value)
        else:
            raise RuntimeError('转换url时出错')


converters.register_converter(CategoryConverter, 'cate')
