from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
def index(request):
    return HttpResponse('图书首页')


def detail(request,book_id):
    text = '图书id为%s' % book_id
    return HttpResponse(text)
