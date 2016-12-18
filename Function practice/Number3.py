#! usr/bin/env python3
#--*--coding:utf8--*--

'''
为老师们编写一个处理全班考试成绩的程序：
要求：（1）能够依次录入班级同学的姓名和分数；（2）录入完毕，则打印出全班的平均分，最高分的同学姓名和分数
'''

def ave(dic):
	a = len(dic)
	b = 0
	for k,v in dic.items():
		b +=v
	return round(b/a,2)

def max_i(dic):
	name = ''
	value = 0
	for k,v in dic.items():
		if v > value:
			value = v
			name = k
	return (name, value)

if __name__ == '__main__':
	d = {}
	print('"q"-exit')
	while True:
		a = input('please input name: ')
		if a == 'q':
			break
		else:
			b = input('please input score: ')
			d[a] = float(b)
	n,j = max_i(d)
	print('the average is:%s' %(ave(d)))
	print('the best is %s, his/her score is %s' %(n, j))