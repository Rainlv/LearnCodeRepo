import requests

ip = {'http': '123.163.27.90:9999'}

html = requests.get('http://45.32.164.128/ip.php', proxies=ip)
print(html.text)
