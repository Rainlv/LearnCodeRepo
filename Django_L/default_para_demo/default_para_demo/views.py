from django.http import HttpResponse


book_list = [
    '三国演义',
    '水浒传',
    '红楼梦',
    '西游记'
]


def books(request, page=1):
    return HttpResponse(book_list[page-1])
