# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html


# 在该文件中处理数据


# 处理结果是每个字典一行，不是正常的json格式
from scrapy.exporters import JsonLinesItemExporter


class QsbkPipeline(object):
    def __init__(self):
        self.fp = open('duanzi.json', 'wb')  # 二进制写入，不需要指定编码
        # 创建对象，指定参数ensure_ascii参数保证写中文时不会乱码
        self.exporter = JsonLinesItemExporter(self.fp, ensure_ascii=False, encoding='utf-8')

    def open_spider(self, spider):  # 爬虫开始时运行，参数记得加spider
        print('爬虫开始了')

    def process_item(self, item, spider):  # 处理spider返回的数据
        self.exporter.export_item(item)  # 导出文件
        return item

    def close_spider(self, spider):  # 爬虫结束时运行,参数记得加spider
        self.fp.close()
        print('爬虫结束了...')

# 导出大量数据较慢，所有字典放在列表中，是json格式

# from scrapy.exporters import JsonItemExporter
# # 在该文件中处理数据
# class QsbkPipeline(object):
#     def __init__(self):
#         self.fp = open('duanzi.json', 'wb')  # 二进制写入，不需要指定编码
#         # 创建对象，指定参数ensure_ascii参数保证写中文时不会乱码
#         self.exporter = JsonItemExporter(self.fp,ensure_ascii=False,encoding='utf-8')
#         self.exporter.start_exporting() # 标示开始导出数据
#
#     def open_spider(self,spider):  # 爬虫开始时运行，参数记得加spider
#         print('爬虫开始了')
#
#     def process_item(self, item, spider):  # 处理spider返回的数据
#         self.exporter.export_item(item)     # 导出文件
#         return item
#
#     def close_spider(self,spider):  # 爬虫结束时运行,参数记得加spider
#         self.exporter.finish_exporting()  # 标示结束导出
#         self.fp.close()
#         print('爬虫结束了...')
#

# 传统方法处理数据

# import json
# # 在该文件中处理数据
# class QsbkPipeline(object):
#     def __init__(self):
#         self.fp = open('duanzi.json', 'w', encoding='utf-8')
#
#     def open_spider(self,spider):  # 爬虫开始时运行，参数记得加spider
#         print('爬虫开始了')
#
#     def process_item(self, item, spider):  # 处理spider返回的数据
#         item_json = json.dumps(dict(item), ensure_ascii=False)
#         self.fp.write(item_json + '\n')
#         return item
#
#     def close_spider(self,spider):  # 爬虫结束时运行,参数记得加spider
#         self.fp.close()
#         print('爬虫结束了...')
