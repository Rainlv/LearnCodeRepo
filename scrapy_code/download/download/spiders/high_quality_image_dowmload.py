# 进化成Crawl爬虫 导入这俩东西，class继承改成CrawlSpider，写入rule，class下的类不能命名成parse比如底层会调用
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
import scrapy
from download.items import ImagesPipeline


class ImgDowmloadSpider(CrawlSpider):
    name = 'high_quality_image_dowmload'
    allowed_domains = ['car.autohome.com.cn']
    start_urls = ['https://car.autohome.com.cn/pic/series/65.html']

    rules = (
        Rule(LinkExtractor(allow='https://car.autohome.com.cn/pic/series/65.+'), callback='parse_page', follow=True),
    )

    def parse_page(self, response):
        title = response.xpath('//div[@class="uibox"]/div[@class="uibox-title"]/text()').get()
        row_img_urls = response.xpath('//div[contains(@class,"uibox-con")]/ul/li/a/img/@src').getall()
        img_urls = list(map(lambda x: response.urljoin(x.replace('240x180_0_q95_c42_', '')), row_img_urls))
        item = ImagesPipeline(title=title, image_urls=img_urls)
        yield item

    def test_page(self, response):
        uiboxs = response.xpath('//div[@class="uibox"]')[1:]
        for uibox in uiboxs:
            title = uibox.xpath('.//div[@class="uibox-title"]/a/text()').get()
            img = uibox.xpath('.//ul/li/a/img/@src').getall()
            img = list(map(lambda x: response.urljoin(x), img))  # .urljoin自动拼接url
            item = ImagesPipeline(title=title, image_urls=img)
            yield item
