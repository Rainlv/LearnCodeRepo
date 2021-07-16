from django.urls import path,re_path
from . import views

urlpatterns = [
    path('', views.index),
    re_path(r'list/(?P<year>\d{4})', views.article_list_y),
    re_path(r'list/(?P<month>\d{2})', views.article_list_m)
]
