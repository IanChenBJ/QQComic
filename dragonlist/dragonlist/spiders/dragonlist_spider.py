from scrapy.spiders import Spider
from ..items import DragonlistItem



class DragonlistSpider(Spider):
    name = 'dragonlist'
    allowed_domains=[]
    start_urls = [
        'http://m.ac.qq.com/comic/chapterList/id/505436'
    ]

    def parse(self, response):
        block = response.xpath('//ul[@class="chapter-list reverse"]/li')
        for sel in block:
            item = DragonlistItem()
            item['chapter_url'] = 'http://m.ac.qq.com' + sel.xpath('./a/@href').extract()[0]
            item['chapter_index'] = sel.xpath('./a/@data-seq').extract()[0]
            yield item
