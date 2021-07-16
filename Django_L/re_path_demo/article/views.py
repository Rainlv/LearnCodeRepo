from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.

def index(request):
    return HttpResponse('文章首页')


def article_list_y(request, year):
    text = '输入的年份是%s' % year
    return HttpResponse(text)


def article_list_m(request, month):
    text = '输入的月份是%s' % month
    return HttpResponse(text)