from django.shortcuts import render
from datetime import datetime

def index(request):
    context = {
        'value': '张三',
        'mytime': datetime(year=2020, month=3, day=14, hour=17, minute=7, second=30),
        'time_now': datetime.now()
    }
    return render(request, 'index.html', context=context)
