# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html


from scrapy.pipelines.images import ImagesPipeline
from scrapy.http import Request
from scrapy.exceptions import DropItem

class DragontestPipeline(ImagesPipeline):
    def get_media_requests(self, item, info):
        meta = {
            'item':item
        }
        return Request(url=item['image_url'],meta=meta)

    def item_completed(self, results, item, info):
        image_path = [ x['path'] for ok,x in results if ok ]
        if not image_path:
            raise DropItem('图片下载失败！')
        item['image_path'] = image_path
        return item
    def file_path(self, request, response=None, info=None):

        item = request.meta['item']
        filepath = 'Dragon/' +  '{0}/{1}.jpg'.format(item['chapter'],item['index'])
        return filepath


