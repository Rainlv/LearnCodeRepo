from django.shortcuts import render


def index(request):
    content = {
        'books': [
            '三国演义',
            '水浒传',
            '西游记',
            '红楼梦'
        ],
        'empty': [],
        'persons': [
            {
                'name': 'jim',
                'age': 18,
                'height': 190
            },
            {
                'name': 'tim',
                'age': 19,
                'height': 199
            },
            {
                'name': 'jack',
                'age': 28,
                'height': 178
            },
            {
                'name': 'tom',
                'age': 22,
                'height': 169
            }
        ],
        'goods': {
            'name': '苹果',
            'price': '$20',
            'weight': '18kg'
        }
    }
    return render(request, 'index.html', context=content)
