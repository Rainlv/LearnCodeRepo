from django.shortcuts import render


def index(request):
    return render(request, 'index.html')


def school(request):
    return render(request, 'school.html')


def company(request):
    return render(request, 'company.html')
