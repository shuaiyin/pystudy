#coding=utf-8

"""
其实我认为是否可重用只是针对与当前建立的这次socket实例而已
the time in your device may not acurrate,so you need to synchron,, to the time server 

Network Time Potocol  Ntp   其实我认为是否可重用只是针对与当前建立的这次socket实例而已

"""

import ntplib 
from time import ctime
"""
如何从网络时间服务器上获取当前时间并打印
"""
def print_time():
	ntp_client = ntplib.NTPClient()
	response = ntp_client.request('pool.ntp.org')
	print response
	print ctime(response.tx_time)

print_time()
"""
<ntplib.NTPStats instance at 0x7ff571652518>

Mon Jul  4 19:26:19 2016
"""




"""
some times we don not need to get acurrate time from ntp server ,facing this situation,we can use  the simplify version of NTP, we can call it " simple Network time Protocol "(sntp)
now,we dont rely any onther third part lib to wrirte a sntp client 

"""
import socket 
import struct 
import sys 
import time 
NTP_SERVER = "0.uk.pool.ntp.org"
TIME1970 = 2208988800L

def sntp_client():
	client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
	print client
	data = '\x1b' + 47 * '\0'
	client.sendto(data,(NTP_SERVER,123))
	data,address = cleint.recvfrom(1024)
	if data:
		print 'response received from :' % address 
	t = struct.unpack('!12I',data)[10]
	t -= TIME1970
	print '\tTime=%s' % time.ctime(t)
 
sntp_client()

"""
somthing wrong with is p 37 
"""