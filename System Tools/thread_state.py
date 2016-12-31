#! usr/bin/env python3
#--*--coding:utf8--*--

import threading
import _thread

def action(i):
	print(i ** 32)

#subclass with state
class Mythread(threading.Thread):
	def __init__(self, i):
		self.i = i
		threading.Thread.__init__(self)

	def run(self):
		print(self.i ** 32)
Mythread(2).start()

# pass action in 
thread = threading.Thread(target=(lambda:action(2)))
thread.start()

# same but no lambda wrapper for state
threading.Thread(target=action, args=(2,)).start()

# basic thread module
_thread.start_new_thread(action, (2,))