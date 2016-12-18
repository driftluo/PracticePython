#! usr/bin/env python3
#--*--coding:utf8--*--

'''
编写一个函数，判断电子信箱是否合法，并用在程序中
'''

import re

def validate_email(email):
	if len(email) > 4:
		if re.match('^[a-zA-z0-9._%-]+@[a-zA-Z0-9._%-]+\.[a-zA-Z]{2,6}$', email) != None:
			return True
	else:
		return False

if __name__ == '__main__':
	while True:
		e = input('input your email("q"-exit): ')
		if e == 'q':
			break
		else:
			r = validate_email(e)
			if r:
				print('the email is right.')
			else:
				print('sorry, the email is wrong.')