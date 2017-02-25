# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html


import pymongo



class DragonlistPipeline(object):

    def __init__(self):
        self.client = pymongo.MongoClient(host='localhost',port=27017)
        self.db = self.client['dragonball']
        self.col = self.db['chapterlist']


    def process_item(self, item, spider):
        postitem = dict(item)
        self.col.insert(postitem)


        return item
