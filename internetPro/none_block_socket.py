#coding=utf-8
####把套接字改成阻塞或非阻塞模式
"""
in default case ,the socket of tcp are in block mode !!!that to say,the tcp socket will not return controll power to the program,except for finish his task !!
such as,when you use connect() API ,the connect operation will prevent the program from conitune runing downward,util connect successfully!
you dont not  want to program waiting the server responce or waiting connect exception!
例如如果编写了一个网页浏览器客户端链接服务器，你应该考虑取消功能，以便于在操作过程中取消链接,这时就要把套接字设置为非阻塞模式

using setblocking(0) to  set the socket in not  block mode 
using setblocking(1) to set the socket in  block mode 

"""
import socket
def test_socket_modes():
	s  = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
	s.setblocking(1)
	s.settimeout(0.5)
	s.bind(("127.0.0.1",0))

	socket_address = s.getsockname()
	print "Trivaial Server launched on socket %s " % str(socket_address)

	while(1):
		s.listen(1)

test_socket_modes()
"""
Trivaial Server launched on socket ('127.0.0.1', 46720) 

"""



