#! usr/bin/env python3
#--*--coding:utf8--*--

'''
This web scraping write by me and waiting for improvement. 
missing={'Storage','Multithreading','Read data from datebase','GUI display','Proxy ip'}
'''

from selenium import webdriver
#from selenium.webdriver.common.keys import Keys
import time,datetime

driver = webdriver.PhantomJS(executable_path=r'E:\webdriver\phantomjs-2.1.1-windows\bin\phantomjs')
#driver = webdriver.Chrome(executable_path=r'E:\webdriver\chromedriver')
driver.get('http://www.qidian.com')
def findNewUpdate(bookname):
	driver.switch_to_window(driver.window_handles[0])
	driver.find_element_by_class_name("search-box").send_keys(bookname)
	driver.find_element_by_id("search-btn").click()
	a = driver.window_handles		#获取当前所有窗口的句柄(ID)，根据打开时间排序，返回list
	driver.switch_to_window(a[-1])  #转换到最新的一个窗口
	time.sleep(2)
	f = driver.find_element_by_xpath('//*[@id="result-list"]/div/ul/li[1]/div[2]/h4/a').click()
	a = driver.window_handles
	driver.switch_to_window(a[-1])
	#bsobj = BeautifulSoup(driver.page_source, 'lxml')
	#b = bsobj.find("a", href=re.compile('//book.qidian.com/info/(\d+)')).attrs['href']
	#driver.get('http:'+b)
	name = driver.find_element_by_xpath('/html/body/div[2]/div[6]/div[4]/div[1]/div[2]/ul/li[2]/a').text
	dd = driver.find_element_by_xpath('/html/body/div[2]/div[6]/div[4]/div[1]/div[2]/ul/li[2]/em').text
	Today = datetime.date.today().__str__()
	yesterday = (datetime.date.today() - datetime.timedelta(days=1)).__str__()
	dd = dd.replace('今天', Today+' ')
	dd = dd.replace('昨日', yesterday+' ')
	for handles in driver.window_handles[1:]:
		driver.switch_to_window(handles)
		driver.close()
	return name,dd

booknames = ['']
t = {}
for bookname in booknames:
	x=findNewUpdate(bookname)
	t[bookname] = x
	time.sleep(5)
print(t)
driver.switch_to_window(driver.window_handles[0])
driver.close()