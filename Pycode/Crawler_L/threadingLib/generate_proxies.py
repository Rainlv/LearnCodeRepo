import random

def generate_proxy():

    with open('Crawler_L/ip_list.txt','r') as r:
        ip_address = r.readlines()
    ip_list = list(map(lambda x: x.replace('\n',''),ip_address))

    proxy = {
        'http':random.choice(ip_list)
    }
    return proxy