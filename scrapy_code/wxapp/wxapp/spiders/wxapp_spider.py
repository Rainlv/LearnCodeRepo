# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from wxapp.items import WxappItem

class WxappSpiderSpider(CrawlSpider):
    name = 'wxapp-spider'
    allowed_domains = ['wxapp-union.com']
    start_urls = ['http://www.wxapp-union.com/portal.php?mod=list&catid=2&page=1']

    rules = (
        Rule(LinkExtractor(allow=r'.+mod=list&catid=2&page=\d'), follow=True),
        Rule(LinkExtractor(allow=r'.+article-.+\.html'), follow=False, callback="parse_item")
    )

    def parse_item(self, response):
        author_p = response.xpath('//p[@class="authors"]')
        author = author_p.xpath('.//a/text()').get()
        pub_time = author_p.xpath('.//span/text()').get()
        content = response.xpath('//td[@id="article_content"]//text()').getall()
        content = ''.join(content).strip()
        title = response.xpath('//h1[@class="ph"]/text()').get()
        item = WxappItem(content=content,author=author,pub_time=pub_time,title=title)
        return item
