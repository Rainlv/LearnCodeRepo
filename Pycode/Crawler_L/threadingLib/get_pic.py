import threading
import requests
import random
from lxml import etree
import re
import os
import queue
from urllib import request
from time import sleep


def parse_page(url, q):
    url = url.get()
    # print(url)
    if url:
        headers = [
            {
                'User-Agent': 'Mozilla/4.0 (compatible; MSIE 7.0; Windows Phone OS 7.0; Trident/3.1; IEMobile/7.0; LG; GW910)'
            },
            {
                'User-Agent': 'Mozilla/5.0 (compatible; MSIE 9.0; Windows Phone OS 7.5; Trident/5.0; IEMobile/9.0; SAMSUNG; SGH-i917)'
            },
            {
                'User-Agent': "Mozilla/5.0 (compatible; MSIE 10.0; Windows Phone 8.0; Trident/6.0; IEMobile/10.0; ARM; Touch; NOKIA; Lumia 920)"
            }
        ]
        header = {}
        header = random.choice(headers)
        header['Refer'] = 'http://www.doutula.com/photo/list/?page=1'
        header['Upgrade-Insecure-Requests'] = '1'

        resp = requests.get(url, headers=header)
        text = resp.text
        # print(text)
        html = etree.HTML(text)
        img_list = html.xpath('//div[@class="page-content text-center"]//img')
        # print(img_list)
        # print(img_list[1])
        for img_elm in img_list:
            img_url = img_elm.get('data-backup')
            if img_url:
                img_type = os.path.splitext(img_url)[1]
                img_name = img_elm.get('alt')
                img_name = re.sub(r'[\.\*\?\？\=。，、,]', '', img_name)
                filename = img_name + img_type
                q.put((img_url, filename))
            else:
                continue


def save_img(q_page, q_img):
    while True:
        if not q_img.empty() and not q_page.empty():
            img_url, filename = q_img.get()
            request.urlretrieve(img_url, r'img\{}'.format(filename))
            print(filename + '下载完成')
        else:
            print('2222222')
            break


if __name__ == "__main__":
    q_url_list = queue.Queue(100)
    q_img = queue.Queue(10000)
    for pagenum in range(1, 10):
        url = 'http://www.doutula.com/photo/list/?page={}'.format(pagenum)
        q_url_list.put(url)

    for i in range(2):
        t1 = threading.Thread(target=parse_page, args=(q_url_list, q_img))
        t1.start()

    sleep(2)

    for i in range(5):
        t2 = threading.Thread(target=save_img, args=(q_url_list, q_img))
        t2.start()
    # parse_page(q_url_list,q_img)
