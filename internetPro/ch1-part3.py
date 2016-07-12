#coding=utf-8
"""
reuse socket address 
如果在某个端口上运行一个pythonsocket service, 链接一次之后便stop running ,then you can never use this port again,if you retry connect this port ,it will throw exception,such as address already in use 
after you create socket object,we can query the reuse status of socket address,such as old status ,then,use setsockopt method ,modify the value of address reuse status 
再按照常规步骤，把套接字绑定到一个地址上，监听进入的客户端链接
p34 dont ljie 
using telnet to connect the socket server ???

SO_REUSEADDR 1  can reuse 
SO_REUSEADDR 0  can not reuse 
"""
import sys 
import socket 
def reuse_socket_addr():
	sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
	#GET the old status of the SO_REUSEADDR option 
	old_state = sock.getsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR)
	print "Old socket state: %s" % old_state

	#Enable the SO_REUSEADDR option 
	sock.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
	new_state = sock.getsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR)
	print "new socket state : %s" % new_state

	local_port = 8287

	srv = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
	srv.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1) #####
	# print srv.getsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR)
	# sys.exit(0)
	srv.bind(('',local_port))
	srv.listen(1)
	print "Listening ON the port %s "  % local_port
	while True:
		try:
			connection,addr = srv.accept()
			print 'Connected by %s:%s' % (addr[0],addr[1])
		except KeyboardInterrupt:
			break
		except socket.error,msg:
			print '%s' % msg 

reuse_socket_addr()
"""
其实我认为是否可重用只是针对与当前建立的这次socket实例而已
"""
