from django.shortcuts import render


def index(request):
    # content = {
    #     'heroes': [
    #         '鲁班一号',
    #         '孙悟空',
    #         '武则天'
    #     ]
    # }
    content = {
        'age': 190
    }
    return render(request, 'index.html', context=content)
