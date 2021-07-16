from django.shortcuts import render
from django.db import connection


def index(request):
    cursor = connection.cursor()
    sql = '''
    # insert into book(id,name,author) value(null,'三国演义','罗贯中')
    select id,name,author from book
    '''
    cursor.execute(sql)
    print(cursor.fetchone())
    return render(request, 'index.html')
