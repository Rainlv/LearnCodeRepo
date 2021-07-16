from django.http import HttpResponse
from django.shortcuts import render
from django.template.loader import render_to_string


def index(request):
    # html = render_to_string('index.html')
    # return HttpResponse(html)
    return render(request, 'index.html')
