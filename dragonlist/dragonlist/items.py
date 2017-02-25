# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class DragonlistItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    chapter_index = scrapy.Field()
    chapter_url = scrapy.Field()
