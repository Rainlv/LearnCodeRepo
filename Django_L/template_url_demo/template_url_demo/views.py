from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return render(request, 'index.html')


def books(request):
    return HttpResponse('图书首页')


def movie(request):
    return HttpResponse('电影首页')


def city(request):
    return HttpResponse('同城首页')


def book_detail(request, book_id, category):
    text = '图书id为%s，分类为%s' % (book_id, category)
    return HttpResponse(text)


def login(request):
    next = request.GET.get('next')
    text = '登陆后跳转的页面为%s' % next
    return HttpResponse(text)
