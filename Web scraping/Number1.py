#! usr/bin/env python3
#--*--coding:utf8--*--
'''
根据起始页面的外链不断获取外链进行随机跳转，如果当前页面没有外链，先进入一个内链，查找这个内链上的
所有外链，随机跳转，未处理异常(如加载未完成导致的bsobj对象为str、碰到google等国内无法访问
403forbidden等等)
'''

from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
import datetime
import random

page = set()
random.seed(datetime.datetime.now())

#获取页面所有内链的列表
def getInternalLinks(bsobj, includeUrl):
	internalLinks = []
	#找出所有以"/"开头的连接
	for link in bsobj.findAll('a', href=re.compile("^(/|.*"+includeUrl+")")):
		if link.attrs['href'] is not None:
			if link.attrs['href'] not in internalLinks:
				internalLinks.append(links.attre['href'])
	return internalLinks

#获取页面所有外链的列表
def getExternalLinks(bsobj, excludeUrl):
	externalLinks = []
	#找出所有以'http'、'https'、'www'开头且不包含当前URL的链接
	for link in bsobj.findAll('a',
						href = re.compile('^(http|https|www)((?!"+excludeUrl+").)*$')):
		if link.attrs['href'] is not None:
			if link.attrs['href'] not in externalLinks:
				externalLinks.append(link.attrs['href'])
	return externalLinks

def getNextExternalLink(startingPage):
	html = urlopen(startingPage)
	bsobj = BeautifulSoup(html, 'lxml')
	externalLinks = getExternalLinks(bsobj, splitAddress(startingPage)[0])
	return externalLinks[random.randint(0, len(externalLinks)-1)]

def splitAddress(address):
	addressParts = address.replace('http://','').split('/')
	return addressParts

def getRandomExternalLink(startingPage):
	html = urlopen(startingPage)
	bsobj = BeautifulSoup(html,'lxml')
	print(startingPage)
	externalLinks = getExternalLinks(bsobj, splitAddress(startingPage)[0])
	if len(externalLinks) ==0:
		internalLinks = getInternalLinks(startingPage, splitAddress(startingPage)[0])
		return getNextExternalLinks(internalLinks[random.randint(0, len(internalLinks)-1)])
	else:
		return externalLinks[random.randint(0, len(externalLinks)-1)]

def followExternalOnly(startingSite):
	externalLink = getRandomExternalLink(startingSite)
	print('随机外链是:' + externalLink)
	followExternalOnly(externalLink)

followExternalOnly("http://oreilly.com")