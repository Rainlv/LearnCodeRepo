from django.shortcuts import render, redirect, reverse
from django.db import connection


def get_cursor():
    return connection.cursor()


def index(request):
    cursor = get_cursor()
    cursor.execute("select id,name,author from book")
    books = cursor.fetchall()
    # 取出来的数据：[(1,'三国演义,罗贯中),(),()...]
    return render(request, 'index.html', context={'books': books})


def add_books(request):
    if request.method == 'GET':
        return render(request, 'add_book.html')
    elif request.method == 'POST':
        cursor = get_cursor()
        name = request.POST.get('name')
        author = request.POST.get('author')
        cursor.execute("insert into book(id,name,author) values(null,'%s','%s')" % (name, author))
        return redirect(reverse('index'))


def book_detail(request, book_id):
    cursor = get_cursor()
    cursor.execute("select id,name,author from book where id=%s" % book_id)
    book = cursor.fetchone()
    # 取出的数据类型：(1,'三国演义','罗贯中')
    return render(request, 'book_detail.html', context={'book': book})


def delete_book(request):
    book_id = request.POST.get('book_id')
    cursor = get_cursor()
    cursor.execute("delete from book where id=%s" % book_id)
    return redirect(reverse('index'))
