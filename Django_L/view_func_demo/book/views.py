from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
def book(request):
    return HttpResponse('图书首页')


def book_detail(request, book_id, category_id):
    text = '图书id为%s，分类为%s' % (book_id, category_id)
    return HttpResponse(text)


def author_detail(request):
    author_id = request.GET.get('id')
    text = '作者的id是%s' % author_id
    return HttpResponse(text)


def publisher_detail(request, publisher_id):
    text = '出版社的id是%s' % publisher_id
    return HttpResponse(text)
