from django.http import HttpResponse
from .models import Article, Page
from django.shortcuts import render
from django.utils.timezone import now,localtime


def index(request):
    # article = Article(title='西游记')
    # article.save()
    article = Article(title='111', creat_time=now())
    article.save()
    context = {
        'creat_time': now(),
        'local_time': localtime(now())
    }
    return render(request, 'index.html', context=context)
