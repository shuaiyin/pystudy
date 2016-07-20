#coding=utf-8
"""
使用 select.epoll 多路复用 Web 服务器
Python的select模块中有很多针对特定平台的网络事件管理函数。在Linux设备中可以使用
epoll。这个函数利用操作系统内核轮询网络事件，让脚本知道有事件发生了。这听起来比前面介绍的select.select方案更高效。

我们来编写一个简单的Web服务器，向每一个连接服务器的网页浏览器返回一行文本。
这个脚本的核心在Web服务器的初始化过程中，我们要调用方法select.epoll()，注册服
务器的文件描述符，以达到事件通知的目的。在Web服务器执行的代码中，套接字事件由下述代
码监控。
"""

import socket 
import select
import argparse 

SERVER_HOST = 'localhost'
EOL1 = b'\n\n'
EOL2 = b'\n\n'

SERVER_RESPONSE = b"""HTTP/1.1 200 OK\r\nDate: Mon,1 Apr 2013 01:01:01 GMT\r\nContent-Length: 25\r\n\r\n Hello from Epoll Server!"""

class EpollServer(object): 
	""" A socket server using Epoll"""

	def __init__(self,host=SERVER_HOST,port=0):
		self.sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
		self.sock.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
		self.sock.bind((host,port))
		self.sock.listen(1)
		self.sock.setblocking(0)
		self.sock.setsockopt(socket.IPPROTO_TCP,socket.TCP_NODELAY,1)
		print "Started Epoll Server"
		self.epoll = select.epoll()
		self.epoll.register(self.sock.fileno(),select.EPOLLIN)

	def run(self):
		""" Executes epoll server operation """
		try:
			connections = {};requests={};responses = {}
			while True:
				events = self.epoll.poll(1)
				for fileno,event in events:
					if fileno == self.sock.fileno()
						connection,address = self.sock.accept()
						connection.setblocking(0)
						self.epoll.register(connection.fileno(),select.EPOLLIN)
						


