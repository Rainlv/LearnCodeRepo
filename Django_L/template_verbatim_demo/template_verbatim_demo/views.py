from django.shortcuts import render


def index(request):
    content = {
        'info': 'hello'
    }
    return render(request, 'index.html', context=content )