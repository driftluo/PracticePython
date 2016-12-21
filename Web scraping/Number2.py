#! usr/bin/env python3
#--*--coding:utf8--*--
'''
利用API查询wiki历史匿名编辑者的IP所在地---来自Web Scraping with Python
'''

from urllib.request import urlopen
from urllib.request import HTTPError
from bs4 import BeautifulSoup
import datetime
import random
import re
import json

random.seed(datetime.datetime.now())

def getlink(articleUrl):
	html = urlopen('http://en.wikipedia.org' + articleUrl)
	bsobj = BeautifulSoup(html, 'lxml')
	return bsobj.find('div', {'id':'bodyContent'}).findAll('a',
						href=re.compile('^(/wiki/)((?!:).)*$'))

def getHistoryIps(pageUrl):
	#编辑历史页面URL链接格式是：
	#http://en.wikipedia.org/w/index.php?title=Title_in_URL&action=history
	pageUrl = pageUrl.replace('/wiki/', '')
	historyUrl = 'http://en.wikipedia.org/w/index.php?title='+ pageUrl + '&action=history'
	print('history url is: '+historyUrl)
	html = urlopen(historyUrl)
	bsobj = BeautifulSoup(html, 'lxml')
	# 找出class属性是'mw-anonuserlink'的链接
	# 它们用IP地址代替用户名
	ipAddresses = bsobj.findAll('a', {'class':'mw-anonuserlink'})
	addressList = set()
	for ipAddress in ipAddresses:
		addressList.add(ipAddress.get_text())
	return addressList

def getContry(ipAddress):
	try:
		response = urlopen('http://freegeoip.net/json/'+ipAddress).read().decode('utf-8')
	except HTTPError as e:
		print(e)
		return None
	responseJson = json.loads(response)
	return responseJson.get('country_code')

links = getlink('/wiki/Python_(programming_language)')

while(len(links) > 0):
	for link in links:
		print('-'*20)
		historyIPs = getHistoryIps(link.attrs['href'])
		for historyIP in historyIPs:
			country = getContry(historyIP)
			if country is not None:
				print(historyIP+' is from '+country)

newLink = links[random.randint(0, len(links)-1)].attrs['href']
links = getlink(newLink)