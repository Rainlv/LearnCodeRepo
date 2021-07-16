from django.shortcuts import render


class Person:
    def __init__(self, username):
        self.username = username


def index(request):
    # content = {
    #     'person': '鲁班大师'
    # }

    # p = Person('wxh')
    # content = {
    #     'person': p
    # }

    # content = {
    #     'person': [
    #         '鲁班一号',
    #         '程咬金',
    #         '李白',
    #         '刘禅'
    #     ]
    # }

    content = {
        'person': {
            'user': 'wxh',
            'admin': 'wxhnb'
        }
    }
    return render(request, 'index.html', context=content)
