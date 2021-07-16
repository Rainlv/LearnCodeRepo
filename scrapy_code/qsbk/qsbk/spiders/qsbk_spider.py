# -*- coding: utf-8 -*-
import scrapy
from qsbk.items import QsbkItem


class QsbkSpiderSpider(scrapy.Spider):
    name = 'qsbk_spider'
    allowed_domains = ['yicommunity.com']
    start_urls = ['http://www.yicommunity.com/remen/index.html']
    base_domain = 'http://www.yicommunity.com'

    def parse(self, response):
        print('=' * 30)
        duanzi_divs = response.xpath('//div[@class="block untagged mb15 bs2"]')
        for duanzi_div in duanzi_divs:
            author = duanzi_div.xpath('.//div[@class="author"]/text()').get()
            content = duanzi_div.xpath('.//div[@class="content"]/text()').get().strip()
            item = QsbkItem(author=author, content=content)  # 调用items中构造的数据模型
            yield item  # 返回生成器对象，yield是不终止函数，并返回结果

        next_url = response.xpath('//div[@class="pagebar"]/a[last()]/@href').get()
        if next_url:
            yield scrapy.Request(self.base_domain + next_url, callback=self.parse)
        else:
            return
