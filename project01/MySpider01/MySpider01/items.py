# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class Myspider01Item(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass


# import scrapy

class ItcastItem(scrapy.Item):
    pic_path = scrapy.Field()
    name = scrapy.Field()
    info = scrapy.Field()