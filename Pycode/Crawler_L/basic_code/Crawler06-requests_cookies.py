import requests

# 人人无法访问，仅作为参考代码

# 储存cookies

url = 'http://renren.com/PLogin.do'
data = {
    'email':'970138074@qq.com'
    ,'password':'pythonspider'
}

header = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36'
}

session = requests.session()

session.post(url, data=data, headers=header)

res = session.get('http://www.renren.co,/880151247/profile')