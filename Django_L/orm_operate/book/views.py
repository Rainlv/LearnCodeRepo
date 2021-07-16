from django.http import HttpResponse
from .models import Book


def index(request):
    # 添加数据
    # way1
    # book = Book(name='西游记', author='施耐庵', price=200)
    # way2
    # Book.objects.create(name='西游记', author='施耐庵', price=200)

    # book.save()

    # 查询
    book = Book.objects.get(pk=2)  # pk:primary key
    books = Book.objects.all()
    book_1 = Book.objects.filter(id__gt=2)
    id_name = Book.objects.all().values('id', 'name')
    list = Book.objects.all().values_list('id', 'name')
    print(book)  # 西游记,施耐庵,125.0
    print(books)  # <QuerySet [<Book: 西游记,施耐庵,125.0>, <Book: 三国演义,罗贯中,250.0>]>
    print(book_1)  # <QuerySet [<Book: 三国演义,罗贯中,250.0>]>
    print(id_name)  # <QuerySet [{'id': 2, 'name': '西游记'}, {'id': 3, 'name': '三国演义'}]>
    print(list)  # <QuerySet [(2, '西游记'), (3, '三国演义')]>

    for i in list:
        print(i)  # (2, '西游记') (3, '三国演义')

    # 删除数据
    # book = Book.objects.get(pk=1)
    # book.delete()

    # # 修改数据
    # book = Book.objects.get(pk=2)
    # book.price = 125
    # book.save()
    return HttpResponse('图书操作完成')
