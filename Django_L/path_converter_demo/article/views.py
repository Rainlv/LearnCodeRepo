from django.http import HttpResponse
from django.shortcuts import reverse

def index(request):
    return HttpResponse('图书首页')


def article_detail(request, article_id):

    text = '图书id为%s' % article_id
    return HttpResponse(text)


def article_list(request, categories):
    print(reverse('list', kwargs={'categories': categories}))
    print(categories)
    text = '图书分类为%s' % categories
    return HttpResponse(text)
