from django.urls import path, re_path
from . import views

urlpatterns = [
    path('', views.index, name='index'),

    # 自定义cate转换器
    path('list/<cate:categories>/', views.article_list, name='list'),

    path('detail/', views.article_detail, name='detail')
]
