#! usr/bin/env python3
#--*--coding:utf8--*--

'''
编写工资额计算器，要求如下：
1、确定每月基本工资
2、输入每月的实际应当工作天数
3、输入当月请假天数，如果请假天数小于两天，对工资无影响；大于2天小于等于7天，扣除当月基本工资
  的10%；大于7天小于等于14天，扣除当月基本工资的50%；大于14天，扣除全月工资
4、如果当月实际工作天数和应当工作天数一样（不算加班），则增加基本工资的20%
5、如果当月有加班，则按照加班的天数和当月的日工工资（基本工资/实际工作天数）计算加班费
6、输出最终应得工资
'''

def salary(basic, leaveday, basicday, realday):
	if basicday == realday:
		a = float(basic) * 1.2
	elif int(leaveday) < 2:
		a = float(basic)
	elif 2 < int(leaveday) <= 7:
		a = float(basic) * 0.8
	elif 7 < int(leaveday) < 14:
		a = float(basic) * 0.5
	else:
		a = 0
	return float(a)

def add_salary(add_day, basic, basicday):
	add = float(add_day) * float(basic)/float(basicday)
	return float(add)

if __name__ == '__main__':
	while True:
		basic = input('the basic salary: ')
		leaveday = input('the leave days: ')
		basicday = input('the basic days: ')
		realday = input('the real days: ')
		add_day = input('the add days: ')
		if basic == 'q':
			break
		else:
			a = salary(basic, leaveday, basicday, realday)
			b = add_salary(add_day, basic, basicday)
			final = str(round(a+b,2))
			print('\nthe salary is %s\n' %(final))