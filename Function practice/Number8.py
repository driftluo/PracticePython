#! usr/bin/env python3
#--*--coding:utf8--*--
'''
调用百度API查询天气,http://apistore.baidu.com/apiworks/servicedetail/478.html
'''
import urllib.request
import json

def wheather(city):
	url = 'http://apis.baidu.com/heweather/weather/free?city={}'.format(city)

	req = urllib.request.Request(url)
	req.add_header('apikey', '0a10dbaa3c8d61ce661a6d44ce0ad0a7')

	resp = urllib.request.urlopen(req)
	content = resp.read()
	if content:
		return content

if __name__ == '__main__':
	city_name = 'nanchang'
	r = wheather(city_name)
	r_str = r.decode(encoding='utf-8', errors='strict')
	r_dict = json.loads(r_str)
	today_forecast = r_dict['HeWeather data service 3.0'][0]['daily_forecast'][0]
	tomorrow_forecast = r_dict['HeWeather data service 3.0'][0]['daily_forecast'][1]
	today_date = today_forecast['date']
	tomorrow_date = tomorrow_forecast['date']
	today_temperatrue = today_forecast['tmp']['min'] + '-' + today_forecast['tmp']['max']
	today_wheather = '白天'+ today_forecast['cond']['txt_d'] + '夜晚' + today_forecast['cond']['txt_n']
	cityname = r_dict['HeWeather data service 3.0'][0]['basic']['city']
	print('{0}日{1}的温度是{2},天气状况{3}'.format(today_date, cityname, today_temperatrue, today_wheather))