from selenium import webdriver
from scrapy.spiders import Spider
import os,time
from scrapy.http import HtmlResponse
from ..items import DragontestItem
import pymongo

# ----------------------------------------------------------------------------------------------------------------------

#                                                  运  行  成  功 ！
#                           结   论：
#                                   使用两个爬虫，用数据库传导数据，而不是在一个爬虫里，既爬取列表网址，
#                               又深度爬取列表中每个网址的内容。

#                                    重要！  重要！ 重要！ 重要！ 重要！ 重要！


# ----------------------------------------------------------------------------------------------------------------------






class DragonSpider(Spider):
    name = 'dragon'
    allowed_domains = [ 'm.ac.qq.com']
    start_urls = [
        'http://m.ac.qq.com'
    ]
    num_for_urgency = 1


    def chapterurl(self):
        client = pymongo.MongoClient(host='localhost',port=27017)
        db = client['dragonball']
        col = db['chapterlist']
        block = col.find()
        urls = []
        for sel in block:
            url = sel['chapter_url']
            urls.append(url)

        return urls


    def parse(self, response):
        chapterurls = self.chapterurl()
        for chapter in chapterurls:
            driver = webdriver.PhantomJS()
            driver.get(chapter)
            time.sleep(3)
            page = driver.page_source.encode('utf-8', 'ignore')
            res = HtmlResponse(url=chapter, body=page, encoding='utf-8')

            os.chdir('c:\\users\\cy\\desktop')
            with open('[TEST]dragontest.html', 'wb') as f:
                f.write(page)

            block = res.xpath('//section[@class="comic-pic-list-all"]/ul[@class="comic-pic-list"]/li')
            for sel in block:
                item = DragontestItem()
                item['image_url'] = sel.xpath('./div[@class="comic-pic-box"]/img/@data-src').extract()[0]

                try:
                    item['chapter'] = \
                    res.xpath('//section[@class="comic-pic-list-all"]/ul[@class="comic-pic-list"]/@data-seq').extract()[
                        0]
                    item['index'] = sel.xpath('./@data-index').extract()[0]
                except:
                    item['chapter'] = '未知'
                    item['index'] = '{}'.format(self.num_for_urgency)
                    self.num_for_urgency += 1

                yield item
        driver.quit()








    #  -----------------------------------------------------------------------------------------------------------------
    #                                                 每  章  的  爬  取
    #  -----------------------------------------------------------------------------------------------------------------
    '''
        driver = webdriver.PhantomJS()
        driver.get(self.start_urls[0])
        time.sleep(3)
        page = driver.page_source.encode('utf-8', 'ignore')
        res = HtmlResponse(url=self.start_urls[0],body=page,encoding='utf-8')

        os.chdir('c:\\users\\cy\\desktop')
        with open('[TEST]dragontest.html','wb') as f:
            f.write(page)



        block = res.xpath('//section[@class="comic-pic-list-all"]/ul[@class="comic-pic-list"]/li')
        for sel in block:
            item = DragontestItem()
            item['image_url'] = sel.xpath('./div[@class="comic-pic-box"]/img/@data-src').extract()[0]

            try:
                item['chapter'] = res.xpath('//section[@class="comic-pic-list-all"]/ul[@class="comic-pic-list"]/@data-seq').extract()[0]
                item['index'] = sel.xpath('./@data-index').extract()[0]
            except:
                item['chapter'] = '未知'
                item['index'] = '{}'.format(self.num_for_urgency)
                self.num_for_urgency += 1

            yield item
   '''

