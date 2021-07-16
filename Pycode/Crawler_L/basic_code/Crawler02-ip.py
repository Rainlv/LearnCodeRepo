import urllib.request
import urllib.parse
import easygui as g

url = 'http://45.32.164.128/ip.php'
proxy_support = urllib.request.ProxyHandler({'http':'182.46.114.142:9999'})

opener = urllib.request.build_opener(proxy_support)
# header = {
#     'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36'
# }
opener.addheaders = [('User-Agent','Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36')]

res = opener.open(url)
html = res.read().decode('utf-8')

print(html)