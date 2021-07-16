import csv


def csv_writer():
    head = ['name', 'age', 'height']
    values = [
        ('张三', '16', '166'),
        ('王五', '15', '186'),
        ('李四', '17', '176')
    ]

    with open(r'Crawler_L\csv\student.csv', 'w', newline='', encoding='utf-8') as w:  # newline参数是在换行时默认\n，会出现多余空行
        writer = csv.writer(w)
        writer.writerow(head)  # 写入一行数据
        writer.writerows(values)  # 写入多行数据


def csv_dicwrite():
    head = ['name', 'age', 'height']

    values = [
        {'name': '张三', 'age': '16', 'height': '166'},
        {'name': '李四', 'age': '15', 'height': '176'},
        {'name': '王五', 'age': '17', 'height': '186'}
    ]

    with open(r'Crawler_L\csv\student1.csv', 'w', encoding='utf-8', newline='') as w:
        writer = csv.DictWriter(w, head)  # 传参时要穿两个参数,第一个文件，第二个表头
        writer.writeheader()  # 写入表头
        writer.writerows(values)  # 写入数据
