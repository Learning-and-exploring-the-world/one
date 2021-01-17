# -*- coding: utf-8 -*-
# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


class AvSpider(CrawlSpider):
    name = 'av'
    allowed_domains = ['z.cnjdmm.pw']
    # start_urls = ['http://z.cnjdmm.pw/']
    start_urls = ['https://z.cnjdmm.pw/pw/thread.php?fid=21']

    page_every_link = LinkExtractor(allow=(r'html_data\/\d+\/\d+\/\d+\.html'))

    rules = (
        Rule(page_every_link, callback='parse_item', follow=True),   #不能直接调用 parse x需要重写一个 比如 自动生成的parse_item 
    )

    def parse_item(self, response):  #
        i = {}
        #i['domain_id'] = response.xpath('//input[@id="sid"]/@value').extract()
        #i['name'] = response.xpath('//div[@id="name"]').extract()
        print("0"*100)
        print(response)
        print("0"*100)
        #i['description'] = response.xpath('//div[@id="description"]').extract()
        return i

# https://z.cnjdmm.pw/pw/html_data/21/2008/4904482.html
# https://z.cnjdmm.pw/pw/
# /html_data/21/2008/4904539.html
# html_data\/21\/d+\/d+\.html
# <a href="html_data/21/2008/4904537.html" id="a_ajax_4904537">[08.08] 邹晶晶美艳红衣诱人 [33P]</a>
# <a href="html_data/21/2008/4904538.html" id="a_ajax_4904538">[08.08] 等公車的黑丝袜美女 [14P]</a>

    # parse() 方法不需要重写     
    # def parse(self, response):                                              
    #     pass
