import requests


# 1、get请求

""" res = requests.get("https://www.baidu.com")

    # 解码问题
print(res.text) # 自动解码，可能出现乱码 str类型
print(res.content)  #未解码，为bytes类型，可手动解码.decode('utf-8')

print(res.url) # 请求的网址
print(res.encoding) #猜测编码方式
print(res.status_code) # 状态码 200正常 

    # 传参访问 
url = 'https://www.baidu.com/s'  #加了/s

params = {
    'wd': '中国'
}
headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'
}

res = requests.get(url,params=params,headers=headers) #传参用params关键字
print(res.content.decode())"""


# 2、post请求

""" url = 'https://www.lagou.com/jobs/positionAjax.json?needAddtionalResult=false'

headers = {
    'Referer':'https://www.lagou.com/jobs/list_python?labelWords=&fromSearch=true&suginput=',
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'
}

data = {
    'first':'true',
    'pn':'1',
    'kd':'python'
}

resp = requests.post(url,data=data,headers=headers) # 传参用data关键字
print(resp.content.decode())# 爬取失败，被反了

# 若提取到的是json数据：
    # res.json()可转换为列表或字典类型 """


# 3、添加代理
""" headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'
}
proxy = {
    'http':'163.204.244.39:9999'
}
url = 'http://45.32.164.128/ip.php'
resp = requests.get(url,proxies=proxy,headers=headers)
print(resp.text) """

# 4、证书信任问题

# 若网站ssl证书未被信任，添加verify = False 参数
# resp = requests.get(url,verify=False)