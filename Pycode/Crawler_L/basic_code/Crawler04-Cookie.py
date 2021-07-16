import urllib.request
import urllib.parse
from http.cookiejar import CookieJar,MozillaCookieJar

# 1、输入cookie访问
""" url = 'https://weibo.com/u/3176010690?topnav=1&wvr=6&topsug=1&is_all=1'

header = {
    'User-Agent':"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36"
    ,'Cookie':"login_sid_t=8d3a3519240d7eae00ef3a40492c6475; cross_origin_proto=SSL; Ugrow-G0=7e0e6b57abe2c2f76f677abd9a9ed65d; YF-V5-G0=27518b2dd3c605fe277ffc0b4f0575b3; _s_tentry=-; Apache=3608286164469.563.1581135441357; SINAGLOBAL=3608286164469.563.1581135441357; ULV=1581135441363:1:1:1:3608286164469.563.1581135441357:; WBStorage=42212210b087ca50|undefined; ALF=1612672639; SSOLoginState=1581136640; SUB=_2A25zOktQDeRhGeBJ61cQ9C3PyDyIHXVQTjuYrDV8PUNbmtAKLVCkkW9NRnaXqJH5WtVn7GHaPSJRDFbyyGzdfYnN; SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9WhSuJIoQ4o2Z1jBRP0F7Yva5JpX5KzhUgL.FoqNeh-pShe0e052dJLoI7UCIg4V9-pc; SUHB=0V5l1lFB7IOZao; UOR=,,login.sina.com.cn; wvr=6; wb_view_log_6705143330=1920*10801; YF-Page-G0=95d69db6bf5dfdb71f82a9b7f3eb261a|1581136931|1581136654; webim_unReadCount=%7B%22time%22%3A1581136940594%2C%22dm_pub_total%22%3A0%2C%22chat_group_client%22%3A0%2C%22allcountNum%22%3A0%2C%22msgbox%22%3A0%7D"
}

req = urllib.request.Request(url,headers=header)

html = urllib.request.urlopen(req)
html = html.read()
with open('wb.html','wb') as w:
    w.write(html) """

# 2、自动获取cookie(失败)
""" headers = {
    'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'
}
url = 'https://weibo.com/#_loginLayer_1581139318725'

# 创建cookiejar对象
cookieJar = CookieJar()
# 用cookiejar创建HTTPCookieProcessor对象
handler = urllib.request.HTTPCookieProcessor(cookieJar)
# 用上一步的handler创建一个opener
opener = urllib.request.build_opener(handler)


data = {
    'username' : '15858604775',
    'password' : '172706002'
}
data = urllib.parse.urlencode(data).encode('utf-8')
req = urllib.request.Request(url,headers=headers,data=data)
opener.open(req)  # 获取cookie
# 访问
visit_url = 'https://weibo.com/u/3176010690?nick=%E5%B8%A6%E5%B8%A6%E5%A4%A7%E5%B8%88%E5%85%84&is_all=1'
req = urllib.request.Request(visit_url,headers=headers)
result = opener.open(req)
result = result.read().decode('gbk')
with open('ddwb.html','wb') as w:
    w.write(result.encode()) """


# 3、导出导入cookie文件
CookieJar = MozillaCookieJar('Crawler_L/cookie.txt')
CookieJar.load()
handler = urllib.request.HTTPCookieProcessor(CookieJar)
opener = urllib.request.build_opener(handler)

resp = opener.open('http://www.baidu.com')

for cookie in CookieJar:
    print(cookie) 
# CookieJar.save()  # ignore_discard=True 可加这个参数防止cookie信息失效
