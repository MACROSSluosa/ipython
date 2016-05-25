#!/usr/bin/python
import threading
import time
import os

## This funtion could be any function 
def doChore():
	time.sleep(0.5)

#####function for each thread
class BoothThread(threading.Thread):
	def __init__(self,tid,monitor):
		self.tid=tid
		self.monitor=monitor
		threading.Thread.__init__(self)
	def run(self):
		while True:
			monitor['lock'].acquire() #lock ; or wait for other thread is holding the lock
			if monitor['tick']!=0:
				monitor['tick']=monitor['tick']-1 #self one tickets
				print(self.tid,'now left:',monitor['tick'])
				doChore()
			else:
				print("Thread_id",self.tid,"no tickets left")
				os._exit(0)
			monitor['lock'].release()
			doChore()

##start of main function
monitor={'tick':100,'lock':threading.Lock()}

for k in range(10):
	new_thread = BoothThread(k,monitor)

	new_thread.start()






