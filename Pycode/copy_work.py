import requests
import re
import os
from lxml import etree
from urllib import request
from queue import Queue
import threading


class Producer(threading.Thread):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/27.0.1453.93 Safari/537.36'
    }

    def __init__(self, page_queue, img_queue, *args, **kwargs):
        super(Producer, self).__init__(*args, **kwargs)
        self.page_queue = page_queue
        self.img_queue = img_queue

    def run(self):
        while True:
            if self.page_queue.empty():
                break
            url = self.page_queue.get()
            self.parse_page(url)

    def parse_page(self, url):

        response = requests.get(url, headers=self.headers)
        text = response.text
        html = etree.HTML(text)
        imgs = html.xpath('//div[@class="page-content text-center"]//img')
        for img in imgs:
            if img:
                img_url = img.get('data-original')
                alt = img.get('alt')
                alt = re.sub(r'[\?,\.，\*。！!]', '', alt)
                suffix = os.path.splitext(img_url)[1]
                filname = alt + suffix
                request.urlretrieve(img_url, 'img/' + filname)
                self.img_queue.put((img_url, filname))
            else:
                continue


class Consumer(threading.Thread):

    def __init__(self, page_queue, img_queue, *args, **kwargs):
        super(Consumer, self).__init__(*args, **kwargs)
        self.page_queue = page_queue
        self.img_queue = img_queue

    def run(self):
        while True:
            if self.page_queue.empty() and self.img_queue.empty():
                break
            img_url, filename = self.img_queue.get()
            request.urlretrieve(img_url, r'E:\Code\Pycode\Crawler_L\threadingLib\img\\' + filename)
            print(filename + '下载完成！')


def main():
    page_queue = Queue(100)
    img_queue = Queue(1000)
    for x in range(1, 100):
        url = 'http://www.doutula.com/photo/list/?page={}'.format(x)
        page_queue.put(url)

    for x in range(5):
        t = Producer(page_queue,img_queue)
        t.start()
    for x in range(5):
        t = Consumer(page_queue,img_queue)
        t.start()

if __name__ == '__main__':
    print('开始运行')
    main()
