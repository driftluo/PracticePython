#! usr/bin/env python3
#--*--coding:utf8--*--

'''
2.制作一个加法计算器
要求：用户先后输入两个数字，能够计算出结果，并打印出来加法算式。
'''

def add(num1, num2):
	try:
		a = float(num1) + float(num2)
		print('\n%s + %s = %s\n' %(num1, num2, str(a)))
	except Exception as e:
		print('\nThere seems to be something wrong\n')

if __name__ == '__main__':
	while True:
		print('please input two number and then the program will add them."q"-exit')
		a = input('input the first number: ')
		b = input('input the second number: ')
		if a == 'q' or b == 'q':
			break
		else:
			add(a, b)