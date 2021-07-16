import csv

# 通过迭代器下标获取
def read_csv():

    with open(r'Crawler_L\csv\test.csv','r') as r:
        reader = csv.reader(r) # reader是个迭代器
        next(reader)  # 跳过第一行(即标题)，从第二行开始遍历
        for x in reader:
            date = x[0]
            number = x[1]
            name = x[2]
            print({
                'date':date,
                'number':number,
                'name':name
            })

# 通过字典迭代器key获取value
def Dicread_csv():
    with open(r'Crawler_L\csv\test.csv','r') as r:
        reader = csv.DictReader(r) # 创建一个迭代器，不包含第一行标题数据，遍历返回的是字典
        for x in reader:
            value = {
                'name' : x['name'],
                'date' : x['date']
            }
            print(value)