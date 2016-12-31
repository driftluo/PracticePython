#! usr/bin/env python3
#--*--coding:utf8--*--

import _thread, time, queue

numconsumers = 1
numproducers = 4
nummessages = 4

safeprint = _thread.allocate_lock()
dataQueue = queue.Queue()

def producer(idnum):
	for msgnum in range(nummessages):
		time.sleep(idnum)
		dataQueue.put('[producer id=%d, count=%d]' %(idnum, msgnum))

def consumer(idnum):
	while True:
		time.sleep(0.1)
		try:
			data = dataQueue.get(block=False)
		except queue.Empty:
			pass
		else:
			with safeprint:
				print('consumer', idnum, 'got =>', data)

if __name__ == '__main__':
	for i in range(numconsumers):
		_thread.start_new_thread(consumer, (i,))
	for i in range(numproducers):
		_thread.start_new_thread(producer, (i,))
	time.sleep(((numproducers-1)*nummessages)+1)
	print('main thread exit')