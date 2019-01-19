import random
import base64
# from settings import PROXIES
from Settings import PROXIES;



#https://luzhijun.github.io/2016/10/29/%E5%BE%AE%E5%8D%9A%E8%AF%9D%E9%A2%98%E7%88%AC%E5%8F%96%E4%B8%8E%E5%AD%98%E5%82%A8%E5%88%86%E6%9E%90/#section-2



print(PROXIES);
class RandomUserAgent(object):
	"""Randomly rotate user agents based on a list of predefined ones"""
	def __init__(self, agents):
		self.agents = agents
	@classmethod
	def from_crawler(cls, crawler):
		return cls(crawler.settings.getlist('USER_AGENTS'))
	def process_request(self, request, spider):
		#随机选个agent
		request.headers.setdefault('User-Agent', random.choice(self.agents))
class ProxyMiddleware(object):
	def process_request(self, request, spider):
		proxy = random.choice(PROXIES)
		if proxy['user_pass'] is not None:
			request.meta['proxy'] = "http://%s" % proxy['ip_port']
			encoded_user_pass = base64.encodestring(proxy['user_pass'])
			request.headers['Proxy-Authorization'] = 'Basic ' + encoded_user_pass
		else:
			request.meta['proxy'] = "http://%s" % proxy['ip_port']