#coding=utf-8

import socket 
import select 
import sys 
import signal 
import cPickle 
import struct 
import argparse 

SERVER_HOST = 'localhost'
class ChatClient(object):
	"""An command line chat client using select"""

	def __init__(self,name,port,host=SERVER_HOST):
		"""
		"""
		self.name = name 
		self.connected = False 
		self.host = host 
		self.port = port
		#Initial prompt 
		self.prompt = '[' + '@'.join((name,socket.gethostname().split('.')[0])) + ']>'
		#Connected to server at port 
		try:
			self.sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
			self.sock.connect((host,self.port))
			print 'Now connected to char server@  port %d ' % self.port 
			self.connected = True
			#Send my name ...
			send(self.sock,'NAME: ' + self.name)
			data = receive(self.sock)
			#Contains client address,set it 
			addr = data.split('CLIENT: ')[1]
			slef.prompt = '[' + '@'.join((self.name, addr)) + ']> '
		except socket.error,e:
			print "Failed to connect to chat server @ port %d" % self.port 
			sys.exit(1)

	def run(self):
		"""Chat client main loop"""
		while self.connected:
			try:
				sys.stdout.write(self.prompt)
				sys.stdout.flush()

				#Wait for input from stdin and socket 
				readable,writable,exceptional = select.select([0,self.sock],[],[])
				for sock in readable:
					if sock == 0:
						data = sys.stdin.readline().strip()
						if data:send(self.sock,data)
					elif sock == self.sock:
						data = receive(self.sock)
						if not data:
							print 'CLient shutting down '
							self.connected = False 
							break

						else:
							sys.stdout.write(data + '\n')
							sys.stdout.flush()
			except KeyboardInterrupt:
				print " Client interrupted"
				self.sock.close()
				break
