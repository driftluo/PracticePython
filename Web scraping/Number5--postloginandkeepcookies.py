#! usr/bin/env python3
#--*--coding:utf8--*--

'''
登录表单,保留cookies
-----来自Web Scraping with Python
'''

import requests

params = {'firstname':'Ryan', 'lastname':'Mitchell'}
r = requests.post("http://pythonscraping.com/files/processing.php", data = params)
#登录界面 http://pythonscraping.com/pages/files/form.html
#源码,注意提交数据给action所在地址
'''
<form method="post" action="processing.php">
First name: <input type="text" name="firstname"><br>
Last name: <input type="text" name="lastname"><br>
<input type="submit" value="Submit">
</form>
'''

#提交文件和图像
files = {'uploadFile': open('../files/Python-logo.png', 'rb')}
r = requests.post("http://pythonscraping.com/pages/processing2.php",files=files)

#处理cookies

params = {'username':'Ryan', 'password':'password'}
r = requests.post("http://pythonscraping.com/pages/cookies/welcome.php", params)
r.cookies.get_dict()
r = requests.get("http://pythonscraping.com/pages/cookies/profile.php", cookies=r.cookies)

#session 处理 cookies
session = requests.Session()
params = {'username': 'username', 'password': 'password'}
s = session.post("http://pythonscraping.com/pages/cookies/welcome.php", params)
print("Cookie is set to:")
print(s.cookies.get_dict())
print("-----------")
print("Going to profile page...")
s = session.get("http://pythonscraping.com/pages/cookies/profile.php")
print(s.text)

#Requests 库有一个 auth 模块专门用来处理 HTTP 认证：
from requests.auth import AuthBase
from requests.auth import HTTPBasicAuth
auth = HTTPBasicAuth('ryan', 'password')
r = requests.post(url="http://pythonscraping.com/pages/auth/login.php", auth=auth)
print(r.text)

#Simulate the browser login
session = requests.Session()
headers = {"User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_5) AppleWebKit 537.36 (KHTML, like Gecko) Chrome", 
			"Accept":"text/html,application/xhtml+xml,application/xml; q=0.9,image/webp,*/*;q=0.8"}
url = "https://www.whatismybrowser.com/developers/what-http-headers-is-my-browser-sending"
req = session.get(url, headers=headers)