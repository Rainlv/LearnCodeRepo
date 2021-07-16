from queue import Queue
from time import sleep

import requests
import threading
from lxml import etree
import csv
import random
# from Crawler_L.basic_code.Crawler00_get_proxy import generate_proxy

t = 0


class Producer(threading.Thread):
    headers = [
        {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/27.0.1453.93 Safari/537.36'
        },
        {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/27.0.1453.93 Safari/537.36'
        },
        {
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/535.11 (KHTML, like Gecko)Ubuntu/11.10 Chromium/27.0.1453.93 Chrome/27.0.1453.93 Safari/537.36'
        }]
    headers = random.choice(headers)

    def __init__(self, q_page, q_content, *args, **kwargs):
        super(Producer, self).__init__(*args, **kwargs)
        self.q_content = q_content
        self.q_page = q_page

    def run(self):
        global t
        while True:
            if self.q_page.empty():
                print('{}网页解析完成'.format(threading.current_thread()))
                break
            url = self.q_page.get()
            self.parse_page(url)
            t += 1
            print('第{}页爬取完成'.format(t))

    def parse_page(self, url):
        domain_url = 'http://www.budejie.com'
        # print(proxy)
        try:
            proxy = generate_proxy()
            # print(proxy)
            html = requests.get(url, headers=self.headers, timeout=15)
            text = html.text
            # print(text)
            text = etree.HTML(text)
            a_list = text.xpath('//div[@class="j-r-list-c-desc"]//a')
            for a in a_list:
                a_href = a.get('href')
                a_href = domain_url + a_href
                content = a.text
                self.q_content.put((a_href, content))
                # print(a_href, content)
                # print('获取成功')
        except:
            print('重试中..')
            self.parse_page(url)


class Consumer(threading.Thread):
    lock = threading.Lock()

    def __init__(self, q_page, q_content, *args, **kwargs):
        super(Consumer, self).__init__(*args, **kwargs)
        self.q_content = q_content
        self.q_page = q_page

    def run(self):
        sleep(1)
        while True:
            if self.q_content.empty() and self.q_page.empty():
                print('{}写入完成'.format(threading.current_thread()))
                break
            self.write_csv()

    def write_csv(self):
        a_href, content = self.q_content.get()
        # print(a_href, content)
        values = [a_href, content]
        with open('budejie.csv', 'a', encoding='utf-8', newline='') as w:
            self.lock.acquire(timeout=5)
            writer = csv.writer(w)
            writer.writerow(values)
            self.lock.release()
        # print('一行写入')


def main():
    head = ['url', 'content']

    with open('budejie.csv', 'w') as w:
        writer = csv.writer(w)
        writer.writerow(head)

    q_content = Queue(1000)
    q_page = Queue(10)
    for i in range(1, 10):
        url = 'http://www.budejie.com/{}'.format(i)
        q_page.put(url)
        # break

    url = 'http://www.budejie.com/1'

    for i in range(3):
        t = Producer(q_page, q_content)
        t.start()
        # for i in range(5):
        t = Consumer(q_page, q_content)
        t.start()


if __name__ == '__main__':
    main()
