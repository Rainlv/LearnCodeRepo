"""view_func_demo URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.http import HttpResponse
from django.urls import path
from book import views


def index(request):
    return HttpResponse('首页')


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index),
    path('book/', views.book),
    path('book/detail/<book_id>/<category_id>/', views.book_detail),  # <>中的参数与book_detail函数中的参数保持一致
    path('book/author/', views.author_detail),
    path('book/publisher/<int:publisher_id>/', views.publisher_detail)  # <int:publisher_id>指定参数为int类型，输入其他类型会找不到页面
]
