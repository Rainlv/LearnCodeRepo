# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import os
from urllib import request
from scrapy.pipelines.images import ImagesPipeline

from download import settings


# class DownloadPipeline(object):
#     def __init__(self):
#         self.path = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'image')
#         if not os.path.exists(self.path):
#             os.mkdir(self.path)
#
#     def process_item(self, item, spider):
#         title = item['title']
#         urls = item['image_urls']
#
#         title_path = os.path.join(self.path, title)
#         if not os.path.exists(title_path):
#             os.mkdir(title_path)
#         for url in urls:
#             image_name = url.split('_')[-1]
#             request.urlretrieve(url, os.path.join(title_path, image_name))
#         return item


class BMWImagesPipeline(ImagesPipeline):
    def get_media_requests(self, item, info):
        # 这个方法是发送请求时调用的，其实就是用来发送请求的。
        request_objs = super(BMWImagesPipeline, self).get_media_requests(item, info)
        for request_obj in request_objs:
            request_obj.item = item  # 这里是为了获取request对象的item属性，供下面的函数调用
        return request_objs
    
    def file_path(self, request, response=None, info=None):
        # 这个方法是在请求完成时，存储文件时调用的。
        path = super(BMWImagesPipeline, self).file_path(request, response, info)
        title = request.item.get('title')
        images_store = settings.IMAGES_STORE
        title_path = os.path.join(images_store, title)
        if not title_path:
            os.mkdir(title_path)
        image_name = path.replace('full/', '')
        image_path = os.path.join(title_path, image_name)
        return image_path