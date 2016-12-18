#! usr/bin/env python3
#--*--coding:utf8--*--

'''
菲波那切数列
'''
def fib1(n):
	result = [0,1]
	for i in range(n-2):
		result.append(result[-2]+result[-1])
	return result[1:]

def fib2(n):
	if n == 0:
		return 0
	elif n == 1:
		return 1
	else:
		return fib2(n-1) + fib2(n-2)

def fib3(max):
	n, a, b = 0, 0, 1
	while n < max:
		yield b
		a, b = b, a + b
		n += 1