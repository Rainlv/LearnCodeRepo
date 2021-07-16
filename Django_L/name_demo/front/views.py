from django.http import HttpResponse
from django.shortcuts import render,redirect,reverse
# Create your views here.


def index(request):
    username = request.GET.get('username')
    if username:
        return HttpResponse('front首页')
    else:
        return redirect(reverse('front:login'))
        # redirect 重定向, front:login(app_name:name)
        # reverse 反转，把name变成对应的url


def login(request):
    return HttpResponse('front登录页面')
