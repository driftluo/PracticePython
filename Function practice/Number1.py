#! usr/bin/env python3
#--*--coding:utf8--*--

'''
编写一个函数，实现摄氏度和华氏度之间的换算，换算公式：F=1.8*C + 32
要求：输入单位是摄氏度的值，能够显示相应的华氏度值，反之亦然
'''

def f_and_d(tem):
	try:
		if tem[-1] == 'C':
			F = float(tem[:-1])*1.8 + 32
			print('\nThe corresponding Fahrenheit is %s.\n' %(str(round(F,2))+'F'))
		elif tem[-1] == 'F':
			C = (float(tem[:-1])-32)/1.8
			print('\nThe corresponding degrees Celsius is %s.\n' %(str(round(C,2))+'C'))
		else:
			print("\nThere seems to be something wrong\n")
	except Exception as a:
		return False

if __name__ == '__main__':
	while True:
		print('you should input the tempreture like: 23C or 32F, NOTE: F and C is upper.')
		t = input("input the tempreture:('q'-exit)")
		if t == 'q':
			break
		else:
			f_and_d(t)