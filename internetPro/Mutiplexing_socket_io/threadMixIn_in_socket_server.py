#coding=utf-8
"""
或许基于某些原因你不想编写基于进程的应用程序，而更愿意编写多线程应用程序。可能的
原因有：在线程之间共享应用的状态，避免进程间通信的复杂操作，等等。遇到这种需求，如果
想使用SocketServer库编写异步网络服务器，就得使用ThreadingMixIn类。

和前一节中基于ForkingMixIn的套接字服务器一样，使用ThreadingMixIn编写的套接字
服务器要遵循相同的回显服务器编程模式，不过仍有几点不同。首先， ThreadedTCPServer继
承自TCPServer和TheadingMixIn。客户端连接这个多线程版服务器时，会创建一个新线程。

套接字服务器的请求处理类ThreadedTCPRequestHandler在一个新线程中把消息回显
给客户端。在这个类中可以获取线程的信息。

这个攻略首先创建一个服务器线程，并在后台启动。然后启动三个测试客户端，向服务器发
送消息。作为响应，服务器把消息回显给客户端。在服务器请求处理类的handle()方法中，我
们取回了当前线程的信息并将其打印出来，这些信息在每次客户端连接中都不同。
"""
import os 
import socket 
import threading 
import SocketServer 

SERVER_HOST = 'localhost'
SERVER_PORT = 0 #tell teh kernel to pickup a port dynamically 
BUF_SIZE  = 1024 

def client(ip,port,message): 
	"""
	a client to test threading minin server 
	"""
	#connect to server 
	sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
	sock.connect((ip,port))
	try:
		sock.sendall(message)
		response = sock.recv(BUF_SIZE)
		print "Client received : %s " % response 
	except Exception as e:
		print 'error acurr in client :' + str(e)
	finally:
		sock.close()

class ThreadedTCPRequestHandler(SocketServer.BaseRequestHandler):
	"""
	An example of threaded TCP request handler
	"""
	def handle(self):
		data = self.request.recv(1024)
		current_thread = threading.current_thread()
		response = " %s : %s " % (current_thread.name,data)
		self.request.sendall(response)

class ThreadTCPServer(SocketServer.ThreadingMixIn,SocketServer.TCPServer):
	"""
	nothing to do here ,inherited everything necessary  from parent 
	"""
	pass

if __name__ == "__main__":
	###ok we can get the pid of this process 
	pid = os.getpid()
	print "All thread running under pid %s " % pid 
	#Run Server 
	server = ThreadTCPServer((SERVER_HOST,SERVER_PORT),ThreadedTCPRequestHandler)
	ip,port = server.server_address#recevive ip address 

	#start a theard with the server ---one thread per request 
	server_thread = threading.Thread(target=server.serve_forever)
	#Exit the server thread when the main thread exists 
	server_thread.deamon = True 
	server_thread.start()
	print "Server loop running on thread: %s" % server_thread.name 

	#Run client(s)
	client(ip,port,"Hello from client 1 ")
	client(ip,port,"Hello from client 2 ")
	client(ip,port,"Hello from client 3")

	# Server cleanup 
	server.shutdown()



"""
All thread running under pid 13151 
Server loop running on thread: Thread-1
Client received :  Thread-2 : Hello from client 1   
Client received :  Thread-3 : Hello from client 2   
Client received :  Thread-4 : Hello from client 3  

"""