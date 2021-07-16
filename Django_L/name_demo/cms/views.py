from django.http import HttpResponse
from django.shortcuts import render, redirect, reverse
# Create your views here.


def index(request):
    username = request.GET.get('username')
    if username:
        return HttpResponse('CMS首页')
    else:
        current_namespace = request.resolver_match.namespace  # 获得访问页面的实例命名
        return redirect(reverse('%s:login' % current_namespace))


def login(request):
    return HttpResponse('CMS登录页面')
