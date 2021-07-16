"""template_filer_demo URL Configuration

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
from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name='index'),
    path('addAndCut/', views.addAndCut, name='addAndCut'),
    path('date/', views.data_view, name='date'),
    path('default/', views.default_view, name='default'),
    path('first/', views.first_view, name='first'),
    path('floatformat/', views.floatformat_view, name='floatformat'),
    path('join/', views.join_view, name='join'),
    path('length/', views.length_view, name='length'),
    path('lower/', views.lower_view, name='lower'),
    path('random/', views.random_view, name='random'),
    path('safe/', views.safe_view, name='safe'),
    path('striptags/', views.striptags_view, name='striptags'),
    path('truncatechars/', views.truncatechars_view, name='truncatechars'),
    path('slice/', views.slice_view, name='slice'),
]

