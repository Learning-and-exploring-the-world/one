# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


import requests,re
from io import BytesIO,StringIO
from PIL import Image
import random,time,os


from requests.packages.urllib3.exceptions import InsecureRequestWarning
#header = {"User-Agent" : "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0;"}

#############  1.考虑是否忽略
#from requests.packages.urllib3.exceptions import InsecureRequestWarning
#requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
#r = requests.get('https://www.baidu.com/', verify=False)

requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

proxies = [
	{"http":"http://113.128.27.168:9999" },		
	{"http":"http://175.44.108.220:9999" },		
	{"http":"http://180.119.83.88:9999"  },		
	{"http":"http://110.243.14.20:9999"  },		
	{"http":"http://114.230.105.156:9999"},		
	{"http":"http://110.243.2.196:9999"  },		
	{"http":"http://118.126.107.41:8118" },		
	{"http":"http://121.232.199.115:9000"},		
	{"http":"http://171.11.29.153:9999"  },		
	{"http":"http://115.221.246.69:9999" },		
	{"http":"http://125.108.96.153:9000" },		
	{"http":"http://183.195.106.118:8118"},		
	{"http":"http://106.42.217.123:9999" },		
	{"http":"http://113.121.41.0:9999"   },		
	{"http":"http://121.232.199.76:9000" },
	{"http":"http://163.204.244.164:9999"},
	{"http":"http://221.227.72.129:9999"},
	{"http":"http://112.111.217.3:9999"},
	{"http":"http://113.121.36.43:9999"},
	{"http":"http://117.69.13.180:9999"},
	{"http":"http://113.194.130.117  9999"},
	{"http":"http://113.194.131.175:9999"},
	{"http":"http://175.42.123.28:9999"},
	{"http":"http://117.68.195.92:9999"},
	{"http":"http://113.194.137.42:9999	"},
	{"http":"http://125.108.72.92:9000"},
	{"http":"http://110.243.15.253:9999	"},
	{"http":"http://171.35.149.223:9999	"},
	{"http":"http://125.108.108.150:9000"},
	{"http":"http://123.163.116.56:9999	"},
	{"http":"http://123.54.52.37:9999 "},
	{"http":"http://113.124.87.85:9999"},
	{"http":"http://171.11.29.66:9999 "},
	{"http":"http://163.204.92.79:9999"},
	{"http":"http://117.57.48.102:8118"},
	{"http":"http://125.108.110.245:9000"},
	{"http":"http://115.218.6.85:9000"},
	{"http":"http://219.146.127.6:8060"},
	{"http":"http://120.83.101.249:9999"},
	{"http":"http://223.242.225.19:9999"},
	{"http":"http://121.8.146.99:8060"},
	{"http":"http://110.243.7.237:9999"},
	{"http":"http://115.218.2.104:9000"},
	{"http":"http://183.195.106.118:8118"},
	{"http":"http://49.86.176.16:9999"},
	{"http":"http://222.89.32.141:9999"},
	{"http":"http://1.198.73.202:9999"},
	{"http":"http://136.228.128.6:43117 "},
	{"http":"http://123.163.115.42:9999"},
	{"http":"http://123.168.138.157:9999"},
	{"http":"http://113.194.133.76:9999"},
	{"http":"http://161.35.4.201:80"},
	{"http":"http://175.43.178.75:9999"},
	{"http":"http://125.110.83.67:9000"},
	{"http":"http://123.169.166.181:9999"},
	{"http":"http://218.244.159.10:8118"},
	{"http":"http://125.108.91.232:9000"},
	{"http":"http://117.131.235.198:8060"},
	{"http":"http://115.221.243.131:9999"},
	{"http":"http://113.194.28.88:9999"},
	{"http":"http://27.43.185.186:9999"},
	{"http":"http://113.128.122.131:9999"},
	{"http":"http://123.169.115.180:9999"},
	{"http":"http://163.204.245.204:9999"},
	{"http":"http://110.243.26.245:9999"},
	{"http":"http://218.58.193.98:8060"},
	{"http":"http://123.169.125.114:9999"},
	{"http":"http://1.198.72.73:9999 "},
	{"http":"http://115.218.214.75:9000"},
	{"http":"http://171.13.137.32:9999"},
	{"http":"http://183.166.103.19:9999"},
	{"http":"http://220.249.149.137:9999"},
	{"http":"http://113.194.137.166:9999"},
	{"http":"http://110.243.12.85:9999"},
	{"http":"http://115.221.244.4:9999"},
	{"https":"https://220.249.149.10:9999"},
	{"https":"https://182.148.206.5:9999"},
	{"https":"https://183.166.111.119:9999"}

]

ua_list = [
    {"User-Agent" : "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0;"},
    {"User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61 Safari/537.36;"},
  {"User-Agent" : "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Win64; x64; Trident/5.0; .NET CLR 3.5.30729; .NET CLR 3.0.30729; .NET CLR 2.0.50727; Media Center PC 6.0)"},
  {"User-Agent" :"Mozilla/5.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; .NET CLR 1.0.3705; .NET CLR 1.1.4322)"},
  {"User-Agent" :"Mozilla/4.0 (compatible; MSIE 7.0b; Windows NT 5.2; .NET CLR 1.1.4322; .NET CLR 2.0.50727; InfoPath.2; .NET CLR 3.0.04506.30)"},
  {"User-Agent" :"Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN) AppleWebKit/523.15 (KHTML, like Gecko, Safari/419.3) Arora/0.3 (Change: 287 c9dfb30)"},
  {"User-Agent" :"Mozilla/5.0 (X11; U; Linux; en-US) AppleWebKit/527+ (KHTML, like Gecko, Safari/419.3) Arora/0.6"},
  {"User-Agent" :"Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8.1.2pre) Gecko/20070215 K-Ninja/2.1.1"},
  {"User-Agent" :"Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN; rv:1.9) Gecko/20080705 Firefox/3.0 Kapiko/3.0"},
  {"User-Agent" :"Mozilla/5.0 (X11; Linux i686; U;) Gecko/20070322 Kazehakase/0.4.5"},
]

user_agent = random.choice(ua_list)
proxy = random.choice(proxies)
# pipelines.py

# import json

class Myspider01PipelineLTD(object):

	def __init__(self):
		# self.file = open('teacher.json', 'wb')
		self.file = []
		self.words = ['萝','同','长','丝','模特','姐','少','妖','狐']
		# response = requests.get(url= 'https://htz1.com/1567168229192/ce650263ed1a4f3d98ef78a29672cf08.jpg' ,headers = user_agent, proxies=proxy, verify=False, timeout=120)
		# f = BytesIO(response.content)
		# img = Image.open(f)
		# # img.save('./file/'+str(item['name'])+str(URL.index(img_url))+'.jpg')
		# img.save('./file/1.jpg')
		# pattern = re.compile(r'([a-z]+)([a-z]+)', re.I)
		# m = pattern.match(self.name)
		self.save_pic_dir = './' + self.words[0] +self.words[1] +'/'
		if not os.path.exists(self.save_pic_dir):
			os.makedirs(self.save_pic_dir)
			print('创建文件夹 %s 成功' %self.save_pic_dir)

	def process_item(self, item, spider):
		# content = json.dumps(dict(item), ensure_ascii=False) + "\n"
		# self.file.write(content)
		URL = item['pic_path']
		name = item['name']
		for word in self.words: 
			if word in name:
			# if item['name'].count(word):
				"如果包含想要的字段那就继续"
				for i in URL:
					img_url = i.extract()
					# print(item['name'],img_url)
						# print( img_url)
					if URL.index(i)/1 ==0:
						print(img_url)
						# break
					user_agent = random.choice(ua_list)
					proxy = random.choice(proxies)
					# print(URL.index(i))
					try:
						response = requests.get(url= img_url ,headers = user_agent, proxies=proxy, verify=False, timeout=120)
						f = BytesIO(response.content)
						img = Image.open(f)
						# img.save('./file/'+str(item['name'])+str(URL.index(img_url))+'.jpg')
						img.save(self.save_pic_dir+str(name[:4])+ str(URL.index(i))+'.jpg')
						print('OK')
					except Exception as e:
						try:
							# time.sleep(1)
							print("wait 1 secondes ")
							response = requests.get(url= img_url ,headers = user_agent, proxies=proxy, verify=False, timeout=160)
							f = BytesIO(response.content)
							img = Image.open(f)
							img.save(self.save_pic_dir+str(name[:4])+ str(URL.index(i))+'.jpg')
							print('OK')

						except Exception as e:
							self.file.append(img_url)
							print("Fail ",img_url)

	def close_spider(self, spider):
		# self.file.close()
		if self.file == []:
			print('我本好色')
		# else:
		# 	self.