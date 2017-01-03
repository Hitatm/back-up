# -*- coding: utf-8 -*-
# @Author: Guoxuenan
# @Date:   2016-12-30 22:41:04
# @Last Modified by:   Guoxuenan
# @Last Modified time: 2017-01-02 19:29:25
#!/usr/bin/env python

import serial
import time
import thread

class MSerialPort:
	message=''
	def __init__(self,port,buand):
		self.port=serial.Serial(
			port,
			buand
			)
		self.port.flushInput()
		self.port.flushOutput()
		self.counter=0
		# print self.port.bytesize
		if not self.port.is_open:
			self.port.open()
	def port_open(self):
		if not self.port.is_open:
			self.port.open()
	def port_close(self):
		self.port.close()
	def send_data(self,data):
		number=self.write(data)
		return number
	def read_data(self):
		while True:
			data=''
			while self.port.inWaiting()>0:
				data+=self.port.read(1)
				self.counter+=1
			if data !='':
				timestamp=str( time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time.time())) )+ " "
				savedata('/tmp/mySerialdata',timestamp+data_handle(data))
				data =''
def savedata(path,data):
	savefile=open(path,'a+')
	savefile.write(data)
	savefile.close()

def data_handle(data):
	result=''
	for x in xrange(len(data)):
		result+= (hex(ord(data[x]))[2:]+' ')
	return result+'\n'
if __name__=='__main__':
	mSerial=MSerialPort('/dev/ttyUSB0',9600)
	thread.start_new_thread(mSerial.read_data,())
	print "Process Runing...."
	mSerial_log_file="/tmp/mSerial.log"
	while True:
		time.sleep(5)
		templog_data = str( time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time.time())) )+": "+ str(mSerial.counter)+'\n'
		savedata(mSerial_log_file,templog_data)

# import serial

# ser=serial.Serial('/dev/ttyUSB0',9600)
# # ser.open()
# ser.flushOutput()
# ser.flushInput()
# while True:
# 	bytestoread=ser.inWaiting()
# 	data_raw=ser.read(bytestoread)
# 	if len(data_raw)!=0:
# 		print len(data_raw),
# ser.close()


