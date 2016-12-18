#! usr/bin/env python3
#--*--coding:utf8--*--

'''
已知：字母序列【d,g,e,c,f,b,o,a】，将['bed','dog','dear','eye']按照该序列顺序重新排序
'''

def char_to_number(by_list, char):
	try:
		return by_list.index(char)
	except:
		return 1000

def sort_by_list(by_list, input_list):
	result = {}
	for word in input_list:
		number_list = [char_to_number(by_list, word[i]) for i in range(len(word))]
		result[word] = number_list
	return [v[0] for v in sorted(result.items(), key=lambda x:x[1])]

word=['bed', 'dog', 'dear', 'eye']
by_string=['d', 'g', 'e', 'c', 'f', 'b', 'o', 'a']
print('the word list is:')
print(word)
print('\nwill sorted by:')
print(by_string)
print('\nthe result is:')
print(sort_by_list(by_string, word))