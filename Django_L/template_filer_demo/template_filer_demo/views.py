from django.shortcuts import render
from datetime import datetime


def index(request):
    return render(request, 'index.html')


def addAndCut(request):
    content = {
        'value1': [1, 2, 3],
        'value2': [7, 8, 8],
        'str1': 'abc',
        'str2': 'jkl',
        'int_str1': '1',
        'int_str2': '2',
        'int1': 100,
        'int2': 200,
        'word': 'hello world'
    }
    return render(request, 'addAndCut.html', context=content)


def data_view(request):
    t = datetime.now()
    content = {
        'time': t
    }
    return render(request, 'date.html', context=content)


def default_view(request):
    context = {
        'value1': '',
        'value2': [],
        'value3': {},
        'value4': None
    }
    return render(request, 'default.html', context=context)


def first_view(request):
    context = {
        'value': [1, 2, 3]
    }
    return render(request, 'first.html', context=context)


def floatformat_view(request):
    content = {
        'value': 123.5451,
        'value0': 3.0,
        'value1': 3.1,
        'value2_1': 3.14,
        'value2_2': 3.15
    }
    return render(request, 'floatformat.html', context=content)


def join_view(request):
    context = {
        'value': ['w', 'a', 'z', 'd']
    }
    return render(request, 'join.html', context=context)


def length_view(request):
    context = {
        'value1': [1, 2, 3],
        'value2': 'hello',
        'value3': ('a', 'b', 'cda')
    }
    return render(request, 'length.html', context=context)


def lower_view(request):
    context = {
        'value_low': 'hello',
        'value_up': 'HELLO',
    }
    return render(request, 'lower_up.html', context=context)


def random_view(request):
    context = {
        'value': list(range(32))
    }
    return render(request, 'random.html', context=context)


def safe_view(request):
    context = {
        'value': '<div style="background: aqua">safe成功</div>'
    }
    return render(request, 'safe.html', context=context)


def slice_view(request):
    context = {
        'value': list(range(32))
    }
    return render(request, 'slice.html', context=context)


def striptags_view(request):
    context = {
        'value': '<p>是我dio哒</p>'
    }
    return render(request, 'striptags.html', context=context)


def truncatechars_view(request):
    context = {
        'value': '北京欢迎你~',
        'value1': '<p>北京欢迎你~</p>'
    }
    return render(request, 'truncatechars.html', context=context)

