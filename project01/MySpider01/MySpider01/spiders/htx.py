# -*- coding: utf-8 -*-
import scrapy
from MySpider01.items import ItcastItem
from copy import deepcopy

class HtxSpider(scrapy.Spider):
	name = 'htx'
	allowed_domains = ['htx5.com']
	start_urls = ['https://htx5.com/']
	# start_urls = ['https://htx5.com/mengmeizi']


	def parse(self, response):
		self.URL = """https://htx5.com/""" 
		item = ItcastItem()

		# with open(r"file\test.html" ,"w",encoding='utf-8') as f:
		# 	f.write(response.text)
			#open("teacher.html","wb").write(response.body).close()
		print("---"*100)
		items = []
		lis = response.xpath("//ul[@class='update_area_lists cl']/li")
		# 1.处理每一页的主要URL
		for each in lis:
			# 将我们得到的数据封装到一个 `ItcastItem` 对象
			# item = ItcastItem()
			#extract()方法返回的都是字符串
			pic_path = self.URL + str(each.xpath(".//a/@href").extract()[0])
			name = each.xpath(".//a/@title").extract()

			# #xpath返回的是包含一个元素的列表
			item['pic_path'] = pic_path
			item['name'] = name
			# 2.获取每张图片的详细地址
			if item['pic_path'] is not None:
				yield scrapy.Request(
				item['pic_path'],
				callback=self.get_detail_pic_add,
				meta={"item":deepcopy(item)}
				)	
			# yield item
			# items.append(item)
		# 3.翻页
		next_page = self.URL + response.xpath("//a[@class='next page-numbers']/@href").extract()[0]
		yield scrapy.Request(next_page, callback=self.parse)

	def get_detail_pic_add(self,response):
		item = response.meta["item"]
		item["name"] = response.xpath("//div[@class='item_title']/h1/text()").extract_first()
		item['pic_path'] = response.xpath("//div[@class='content_left']//img/@src")
		yield item
