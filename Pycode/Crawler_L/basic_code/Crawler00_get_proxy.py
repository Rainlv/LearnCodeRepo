import re
import requests
import time
import random


t = 0

def generate_proxy():

    with open(r'E:\Code\Pycode\Crawler_L\ip_list.txt','r') as r:
        ip_address = r.readlines()
    ip_list = list(map(lambda x: x.replace('\n',''),ip_address))

    proxy = {
        'http':random.choice(ip_list)
    }
    return proxy


def get_html(url):
    global t
    t += 1
    headers = {
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'
        # ,'Referer':'https://www.xicidaili.com/nt/'
    }

    proxy =generate_proxy()

    resp = requests.get(url,headers=headers,proxies=proxy)

    if resp.status_code == 200:
        print('第{}页访问成功'.format(t))
    else:
        print(resp.status_code)

    resp = resp.content.decode()
    return resp

def get_IpAndPort(html):

    ip_list = re.findall(r'<td data-title="IP">\d{1,}\.\d{1,}\.\d{1,}\.\d{1,}</td>',html)
    port_list = re.findall(r'<td data-title="PORT">\d{,10}</td>',html)
    # print(port_list)

    newIp_list = []
    for ip_num in ip_list:
        ip = re.search(r'<td data-title="IP">(\d{1,}\.\d{1,}\.\d{1,}\.\d{1,})</td>',ip_num)
        ip = ip.group(1)
        newIp_list.append(ip)

    newPort_list = []
    for port_num in port_list:
        port = re.search(r'<td data-title="PORT">(\d{,10})</td>',port_num)
        port = port.group(1)
        newPort_list.append(port)
    return newIp_list,newPort_list

def show_result(ip_list,port_list):
    ip_port = []
    n = 0 
    for ip in ip_list:
        iport = ip + ':' + port_list[n]
        ip_port.append(iport)
        n += 1
    with open('Crawler_L/New_ip_list.txt','a') as w:
        for ip in ip_port:
            w.writelines(ip + '\n')


if __name__ == "__main__":
    with open('Crawler_L/New_ip_list.txt', "w+") as f:
        read_data = f.read()
        f.seek(0)
        f.truncate()   #清空文件

    for n in range(1,10):

        try:
            url = 'https://www.kuaidaili.com/free/inha/' + str(n) +'/'
            html = get_html(url)
            ip_list = get_IpAndPort(html)[0]
            port_list = get_IpAndPort(html)[1]
            show_result(ip_list,port_list)
            time.sleep(3)
        except Exception as e:
            print(e)
    
    else:
        print('爬取完成')