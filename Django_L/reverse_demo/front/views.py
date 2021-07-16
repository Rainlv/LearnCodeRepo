from django.http import HttpResponse
from django.shortcuts import redirect,reverse


def index(request):
    username = request.GET.get('username')
    if username:
        return HttpResponse('图书首页')
    else:
        # login_url = reverse('login')
        # return redirect(login_url)

        # 带参url
        # detail_url = reverse('detail', kwargs={'article_id': 1})
        # return redirect(detail_url)

        # 查询字符串url
        login_url = reverse('login') + '?next=/'
        return redirect(login_url)


def article_detail(request, article_id):
    text = '图书id为%s' % article_id
    return HttpResponse(text)


def login(request):
    return HttpResponse('登陆页面')
