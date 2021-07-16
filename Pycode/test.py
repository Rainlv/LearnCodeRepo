# import requests
# import random
# from selenium import webdriver
# from lxml import etree
# from selenium.webdriver.support import expected_conditions as Ec
# from selenium.webdriver.common.by import By

# headers = [{
#         'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'
#     },{'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/46.0.2486.0 Safari/537.36Edge/13.10586'},
#         {'User-Agent':'Mozilla/5.0 (compatible; MSIE 10.0; Windows Phone 8.0; Trident/6.0; IEMobile/10.0; ARM; Touch; NOKIA; Lumia 920)'
#         },{'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/27.0.1453.93 Safari/537.36'
#     }]
# header = random.choice(headers)
# proxy = {'http':'119.180.182.2:8060'}
# url = 'http://www.budejie.com/1'
# # url = 'https://www.bilibili.com/'
# html = requests.get(url,headers=header)
# html = html.text
# print(html)
# htmlElm = etree.HTML(html)
from time import sleep

from selenium import webdriver
from selenium.webdriver.chrome.options import Options

path = r'E:\Anaconda\chromedriver.exe'

chrome_options = Options()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--disable-gpu')

# 创建浏览器对象
driver = webdriver.Chrome(executable_path=path, chrome_options=chrome_options)

driver.get('https://www.lagou.com/jobs/list_python/p-city_0?&cl=false&fromSearch=true&labelWords=&suginput=')
source = driver.page_source
print(source)
sleep(2)
driver.close()
