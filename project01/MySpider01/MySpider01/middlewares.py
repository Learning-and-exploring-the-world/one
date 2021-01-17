# -*- coding: utf-8 -*-

# Define here the models for your spider middleware
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/spider-middleware.html

from scrapy import signals


class Myspider01SpiderMiddleware:
	# Not all methods need to be defined. If a method is not defined,
	# scrapy acts as if the spider middleware does not modify the
	# passed objects.

	@classmethod
	def from_crawler(cls, crawler):
		# This method is used by Scrapy to create your spiders.
		s = cls()
		crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
		return s

	def process_spider_input(self, response, spider):
		# Called for each response that goes through the spider
		# middleware and into the spider.

		# Should return None or raise an exception.
		return None

	def process_spider_output(self, response, result, spider):
		# Called with the results returned from the Spider, after
		# it has processed the response.

		# Must return an iterable of Request, dict or Item objects.
		for i in result:
			yield i

	def process_spider_exception(self, response, exception, spider):
		# Called when a spider or process_spider_input() method
		# (from other spider middleware) raises an exception.

		# Should return either None or an iterable of Request, dict
		# or Item objects.
		pass

	def process_start_requests(self, start_requests, spider):
		# Called with the start requests of the spider, and works
		# similarly to the process_spider_output() method, except
		# that it doesn’t have a response associated.

		# Must return only requests (not items).
		for r in start_requests:
			yield r

	def spider_opened(self, spider):
		spider.logger.info('Spider opened: %s' % spider.name)


class Myspider01DownloaderMiddleware:
	# Not all methods need to be defined. If a method is not defined,
	# scrapy acts as if the downloader middleware does not modify the
	# passed objects.

	@classmethod
	def from_crawler(cls, crawler):
		# This method is used by Scrapy to create your spiders.
		s = cls()
		crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
		return s

	def process_request(self, request, spider):
		# Called for each request that goes through the downloader
		# middleware.

		# Must either:
		# - return None: continue processing this request
		# - or return a Response object
		# - or return a Request object
		# - or raise IgnoreRequest: process_exception() methods of
		#   installed downloader middleware will be called
		return None

	def process_response(self, request, response, spider):
		# Called with the response returned from the downloader.

		# Must either;
		# - return a Response object
		# - return a Request object
		# - or raise IgnoreRequest
		return response

	def process_exception(self, request, exception, spider):
		# Called when a download handler or a process_request()
		# (from other downloader middleware) raises an exception.

		# Must either:
		# - return None: continue processing this exception
		# - return a Response object: stops process_exception() chain
		# - return a Request object: stops process_exception() chain
		pass

	def spider_opened(self, spider):
		spider.logger.info('Spider opened: %s' % spider.name)


class ProxyMiddleware(object):
	# overwrite process request
	def process_request(self, request, spider):
		# Set the location of the proxy
		request.meta['proxy'] = "https://183.166.111.119:9999"


class MYHTTPProxyMiddleware(object):
	import base64
	import random
	from six.moves.urllib.parse import unquote

	try:
		from urllib2 import _parse_proxy
	except ImportError:
		from urllib.request import _parse_proxy
		from six.moves.urllib.parse import urlunparse
		from scrapy.utils.python import to_bytes



    def _basic_auth_header(self, username, password):
        user_pass = to_bytes(
            '%s:%s' % (unquote(username), unquote(password)),
            encoding='latin-1')
        return base64.b64encode(user_pass).strip()

    def process_request(self, request, spider):
        PROXIES = [
            # "http://root:@WSX3edc@192.168.1.1:8000/",
	         "http://113.194.28.88:9999",
	         "http://27.43.185.186:9999",
	         "http://113.128.122.131:9999",
	         "http://123.169.115.180:9999",
	         "http://163.204.245.204:9999",
	         "http://110.243.26.245:9999",
	         "http://218.58.193.98:8060",
	         "http://123.169.125.114:9999",
	         "http://1.198.72.73:9999 ",
	         "http://115.218.214.75:9000",
	         "http://171.13.137.32:9999",
	         "http://183.166.103.19:9999",
	         "http://220.249.149.137:9999",
	         "http://113.194.137.166:9999",
	         "http://110.243.12.85:9999",
	         "http://115.221.244.4:9999",
        ]
        url = random.choice(PROXIES)

        orig_type = ""
        proxy_type, user, password, hostport = _parse_proxy(url)
        proxy_url = urlunparse((proxy_type or orig_type, hostport, '', '', '', ''))

        if user:
            creds = self._basic_auth_header(user, password)
        else:
            creds = None
        request.meta['proxy'] = proxy_url
        if creds:
            request.headers['Proxy-Authorization'] = b'Basic ' + creds
		
# ModuleNotFoundError: No module named 'scrapy.contrib'
# 原因是scrapy-1.6.0已删除scrapy.contrib
# pip uninstall Scrapy

# pip install Scrapy==1.5.2