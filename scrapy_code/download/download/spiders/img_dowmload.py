# -*- coding: utf-8 -*-
import scrapy
from download.items import ImagesPipeline

class ImgDowmloadSpider(scrapy.Spider):
    name = 'img_dowmload'
    allowed_domains = ['car.autohome.com.cn']
    start_urls = ['https://car.autohome.com.cn/pic/series/65.html']

    def parse(self, response):
        uiboxs = response.xpath('//div[@class="uibox"]')[1:]
        for uibox in uiboxs:
            title = uibox.xpath('.//div[@class="uibox-title"]/a/text()').get()
            img = uibox.xpath('.//ul/li/a/img/@src').getall()
            img = list(map(lambda x: response.urljoin(x), img))  # .urljoin自动拼接url
            item = ImagesPipeline(title=title, image_urls=img)
            yield item

