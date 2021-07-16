from django.shortcuts import render


def index(request):
    content = {
        'info': '<a href="www.baidu.com">百度</a>'
    }
    return render(request, 'index.html', context=content)
