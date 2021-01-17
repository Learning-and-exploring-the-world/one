# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


class TencentSpider(CrawlSpider):
    name = 'tencent'
    # allowed_domains = ['z.cnjdmm.pw']
    # start_urls = ['http://z.cnjdmm.pw/']

    # rules = (
    #     Rule(LinkExtractor(allow=r'Items/'), callback='parse_item', follow=True),
    # )

    # def parse_item(self, response):
    #     i = {}
    #     #i['domain_id'] = response.xpath('//input[@id="sid"]/@value').extract()
    #     #i['name'] = response.xpath('//div[@id="name"]').extract()
    #     #i['description'] = response.xpath('//div[@id="description"]').extract()
    #     return i
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

        C:\\Users\\LTD\Desktop\\test\\save_pic_dir