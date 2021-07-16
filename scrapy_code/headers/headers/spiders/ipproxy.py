# -*- coding: utf-8 -*-
import scrapy
import json


class IpproxySpider(scrapy.Spider):
    name = 'ipproxy'
    allowed_domains = ['www.avecelle.fi/']
    start_urls = ['http://www.avecelle.fi/ip']

    def parse(self, response):
        origin = json.loads(response.text)
        print(origin['origin'])
