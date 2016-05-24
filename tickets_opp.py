#!/usr/bin/python
import threading
import time
import os

## This funtion could be any function 
def doChore():
	time.sleep(0.5)

#####function for each thread
class BoothThread(threading.Thread)：
	def __init__(self,tid,monitor)
		self.tid=tid
		self.monitor=monitor
		threading.Thread.__init__(self)
	def run(self):
		while True
		




