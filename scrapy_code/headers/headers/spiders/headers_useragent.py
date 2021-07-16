# -*- coding: utf-8 -*-
import scrapy
import json

class HeadersUseragentSpider(scrapy.Spider):
    name = 'headers_useragent'
    allowed_domains = ['http://www.avecelle.fi']
    start_urls = ['http://www.avecelle.fi/user-agent']

    def parse(self, response):
        print(json.loads(response.text)['user-agent'])
        yield scrapy.Request(self.start_urls[0], dont_filter=True) # dont_filter参数是过滤重复链接用的，True表示不过滤
