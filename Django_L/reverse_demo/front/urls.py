from django.urls import path

from front import views

urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.login, name='login'),
    path('detail/<article_id>/', views.article_detail, name='detail')
]