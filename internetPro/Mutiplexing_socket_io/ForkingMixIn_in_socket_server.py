#coding=utf-8
import os 
import socket 
import threading 
import SocketServer
from time import sleep
SERVER_HOST = 'localhost'
SERVER_PORT = 0 #tell the kernel to pick up a port dynamically 
BUF_SIZE = 1024
ECHO_MSG = 'Hello echo server!'


"""
对于之前我们所使用的都是服务器解决方案都是同步的,：即一次只能连接一个客户机并处理他的请求，如果每个请求只是花费很少的时间,
，比如，一个完整的聊天会话，那么同时能处理多个连接就很重要 ,there has three method to handle this purpose,
(1)分叉  forking 
(2)线程  threading 
(3)异步I/O  asynchronous i/o


Q:what is forking and what is threading ????
A:(1)当分叉一个进程（一个运行的程序）的时候，基本上是复制了他，并且分叉后的两个进程都是从当前的执行点继续进行，并且每个进程都有自己的内存副本（比如变量）。一个进程（原来的那个）成为父进程，
另外一个（复制的）成为子进程。分叉操作在时间线（timeline—）上创建了一个分支，最后得到了两个独立存在的进程.幸好进程可以判断哪个是原进程，哪个是子进程（通过查看fork函数的返回值），因此它
们所执行的操作不同(如果相同，那么还有什么意义？两个进程会做同样的工作，会使你自己的电脑停顿)在一个使用分叉的服务器中，每一个客户端机连接都利用分叉创造了一个子进程，父进程继续监听新的连接，
同时子进程处理客户端,当客户端的请求结束之后，子进程就退出了，因为分叉的进程是并行运行的，客户端之间不必相互等待,因为分叉有点耗费资源（每个分叉出来的教程都需要自己的内存），这就出现了另外
一种方法:线程!!!
(2)线程，线程是轻量级的进程或子进程，所有的线程都存在相同的（真正的）进程中，共享内存。资源消耗的下降伴随着一个缺陷，因为线程共享内存，所以必须保证他们的变量不会冲突，或者是在同一个时间
修改同一内容。这就会造成混乱，这些问题都可以归结为同步问题
(3)modern system ,such as windows do not support forking,bug forking is rather quick,though it may consume lots of source ,and for the reason  modern hardware has
improved a lot ,so forking is a good idea !!



"""
##下面是采用分叉方式来处理多个连接的

class ForkingClient():
	"""
	A client to test forking server 
	若想测试ForkingServer类，可以启动多个回显客户端，看看服务器如何响应客户端。
	"""
	def __init__(self,ip,port):
		#create a socket 
		self.sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
		#connet to server 
		self.sock.connect((ip,port))

	def run(self):
		"""client playing with the server"""
		#sending the data to server 
		current_process_id = os.getpid()
		print 'PID %s sending echo message to the server : "%s"' % (current_process_id,ECHO_MSG)
		sent_data_length = self.sock.send(ECHO_MSG)
		print "Sent: %d characters,so far..." % sent_data_length

		#display server response 
		response = self.sock.recv(BUF_SIZE)
		print "PID %s received : %s"  % (current_process_id,response[5:])

	def shutdown(self):
		"""cleanup the client socket """
		self.sock.close()

class ForkingServerRequestHandler(SocketServer.BaseRequestHandler):
	def handle(self):
		#send the echo back to the client 
		data = self.request.recv(BUF_SIZE)
		current_process_id = os.getpid()
		response = '%s: %s' % (current_process_id,data)
		print "Server sending response [current_process_id:data] = [%s]" % response
		self.request.send(response)
		return 

class ForkingServer(SocketServer.ForkingMixIn,SocketServer.TCPServer):
	"""
	Nonthing to add here ,inherited everything necessary from parents 
	我们可以创建ForkingServer类，继承TCPServer和ForkingMixIn类。前一个父类让ForkingServer类实现了之前手动完成的所
    有服务器操作，例如创建套接字、绑定地址和监听进入的连接。我们的服务器还要继承ForkingMixIn类，异步处理客户端。
    ForkingMixIn会为每个客户端请求派生一个新进程
	"""
	pass


def main():
	#Launch the server 
	server = ForkingServer((SERVER_HOST,SERVER_PORT),ForkingServerRequestHandler)
	print server #<__main__.ForkingServer instance at 0x7f2dd10de950>
	ip,port = server.server_address#Retrieve the port um 
	server_thread = threading.Thread(target=server.serve_forever)
	server_thread.setDaemon(True) #do not hang on exit
	server_thread.start()
	print 'Server loop running pid :%s' % os.getpid()

	#Launch the client(s)
	client1 = ForkingClient(ip,port)
	client1.run()

	client2 = ForkingClient(ip,port)
	client2.run()

	# client3 = ForkingClient(ip,port)
	# client3.run()
	# client4 = ForkingClient(ip,port)
	# client4.run()
	# client5 = ForkingClient(ip,port)
	# client5.run()


	#clean them up 
	server.shutdown()
	client1.shutdown()
	client2.shutdown()
	server.socket.close()

if __name__ == '__main__':
	main()

"""
[root@localhost Mutiplexing_socket_io]# python ForkingMixIn_in_socket_server.py 
<__main__.ForkingServer instance at 0x7fe6ecf93950>
Server loop running pid :82988
PID 82988 sending echo message to the server : "Hello echo server!"
Sent: 18 characters,so far...
Server sending response [current_process_id:data] = [82992: Hello echo server!]
PID 82988 received : : Hello echo server!
PID 82988 sending echo message to the server : "Hello echo server!"
Sent: 18 characters,so far...
Server sending response [current_process_id:data] = [82993: Hello echo server!]
PID 82988 received : : Hello echo server!

"""
