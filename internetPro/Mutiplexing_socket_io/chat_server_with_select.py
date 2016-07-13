#coding=utf-8

"""
在大型网络服务器应用程序中可能有几百或几千个客户端同时连接服务器，此时为每个客户
端创建"单独"的线程或进程可能"不切实际"。由于内存可用量受限，且主机的CPU能力有限，我们需
要一种更好的技术来处理大量的客户端。幸好， Python提供的select模块能解决这一问题。

我们将编写一个高效的聊天室服务器，处理几百或更多数量的客户端连接。我们要使用
select模块提供的select()方法，让聊天室服务器和客户端所做的操作始终不会阻塞消息的发
送和接收。
这个攻略使用一个脚本就能启动客户端和服务器，执行脚本时要指定--name参数。只有在
命令行中传入了--name=server，脚本才启动聊天室服务器。 如果为--name参数指定了其他值，
例如client1或client2，则脚本会启动聊天室客户端。聊天室服务器绑定的端口在命令行参数
--port中指定。对大型应用程序而言，最好在不同的模块中编写服务器和客户端。



他山之石
1.上面我们已经知道网络中的进程是通过socket来通信的，那什么是socket呢？socket起源于Unix，而Unix/Linux基本哲学之一就是“一切皆文件”，
都可以用“打开open –> 读写write/read –> 关闭close”模式来操作。我的理解就是Socket就是该模式的一个实现，socket即是一种特殊的文件，
一些socket函数就是对其进行的操作（读/写IO、打开、关闭），这些函数我们在后面进行介绍

2.通常服务器在启动的时候都会绑定一个众所周知的地址（如ip地址+端口号），用于提供服务，客户就可以通过它来接连服务器；而客户端就不用指定，
有系统自动分配一个端口号和自身的ip地址组合。这就是为什么通常服务器端在listen之前会调用bind()，而客户端就不会调用，而是在connect()
时由系统随机生成一个。


3."网络字节序"与"主机字节序"
"主机"字节序就是我们平常说的大端和小端模式："不同"的CPU有"不同"的字节序类型，这些字节序是指"整数"在内存中保存的顺序，这个叫做主机序。引用标准的
Big-Endian和Little-Endian的定义如下：

　　a) Little-Endian就是低位字节排放在内存的低地址端，高位字节排放在内存的高地址端。

　　b) Big-Endian就是高位字节排放在内存的低地址端，低位字节排放在内存的高地址端。

"网络字节序"：4个字节的32 bit值以下面的次序传输：首先是0～7bit，其次8～15bit，然后16～23bit，最后是24~31bit。这种传输次序称作"大端字节"序
。由于TCP/IP"首部"中"所有"的二进制整数在网络中传输时"都"要求以这种次序，因此它又称作"网络字节序"。字节序，顾名思义字节的顺序，就是大于一个字节类型
的数据在内存中的存放顺序，一个字节的数据没有顺序的问题了。

所以：在将一个地址绑定到socket的时候，请先将"主机"字节序转换成为"网络"字节序，而"不要"假定主机字节序跟网络字节序一样使用的是Big-Endian。由于这个问
题曾引发过血案！公司项目代码中由于存在这个问题，导致了很多莫名其妙的问题，所以请谨记对主机字节序"不要"做任何"假定"，"务必"将其"转化"为"网络字节序"
再赋给socket。

"""

import socket 
import select 
import sys 
import signal 
import cPickle 
import struct 
import argparse 
import time

SERVER_HOST = 'localhost'
CHAT_SERVER_NAME = 'server'


#Some utilities 
def send(channel,*args):
	"""
	send()函数接收一个具名参数channel和一个定位参数*args，使用cPickle模块中的dumps()方法序列化数据，使用struct模块计算数据的大小。
	"""

	buffer = cPickle.dumps(args)#dump： 将python对象序列化保存到本地的文件。
	value = socket.htonl(len(buffer))##hostbyte to network byte (long int )
	size = struct.pack("L",value)
	"""
	   我们知道python只定义了6种数据类型，字符串，整数，浮点数，列表，元组，字典。但是C语言中有些字节型的变量，在python中该如何实现呢？这点颇为重要，特别是要在网络上进行数据传输的话。
    python提供了一个struct模块来提供转换。下面就介绍这个模块中的几个方法。
    struct.pack():
    struct.pack用于将Python的值根据格式符，转换为字符串（因为Python中没有字节(Byte)类型，可以把这里的字符串理解为字节流，或字节数组）。


	Format        C Type       			Python type    			Standard size  
	c 			 char          			string of length 1		1 
	Q 			unsigned long long 		integer					8
	......
	d			double 					float					8
	s 			char[]					string 					n*1
	i         	int 					integer 				4
	L 			unsigned long 			integer					4

	"""
	channel.send(size)
	channel.send(buffer)

def receive(channel):
	"""
	同样， receive()函数也接收一个具名参数channel。
	"""
	size = struct.calcsize("L")
	size = channel.recv(size)
	try:
		size = socket.ntohl(struct.unpack("L",size)[0])
	except struct.error,e:
		return ''

	buf = "" 
	while len(buf) < size:
		buf = channel.recv(size - len(buf))
	return cPickle.loads(buf)[0]# load：载入本地文件，恢复python对象

class ChatServer(object):
	"""An example chat server using select """
	def __init__(self,port,backlog=5):
		"""
		初始化聊天服务器的时候创建了一些属性：客户端数量，客户端映射和输出的套接字。
		和之前创建服务器套接字一样，初始化时候也设定了重用地址的选项，这么做可以使用同一个端口重启服务器
		聊天服务器类的构造方法还有one可选参数backlog，用于设定服务器监听的链接队列的最大数量
		这个聊天室有一个值得介绍的地方，他可以使用signal 模块捕获用户的中断操作。中断操作一般通过键盘输入。
		ChatServer类为中断信号（SIGINT）注册了一个信号处理方法sighandler。信号处理方法捕获从键盘输入的中断信号后，关闭所有输出套接字，其中一些套接字可能还有数据等待发送。
		"""
		self.clients = 0 
		self.clientmap = {}
		self.outputs = [] #list output socket 
		self.server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
		self.server.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
		self.server.bind((SERVER_HOST,port))
		print 'Server listening to port: %s ...' % port 
		self.server.listen(backlog)
		#Catch keyboard interrupts 
		signal.signal(signal.SIGINT,self.sighandler)#

	def sighandler(self,signum,frame):
		"""clean up client outputs"""
		#close the server 
		print 'Shutting down server'
		#close existing client sockets 
		for output in self.outputs:
			output.close()
		self.server.close()

	def get_client_name(self,client):
		"""return the name of the client """
		info = self.clientmap[client]
		host,name = info[0][0],info[1]
		return '@'.join((name,host))#the input argument of join if a tuple 

## the main execute method is below 
	def run(self):
		"""
		聊天室服务器的主要执行方法是run()，在while循环中执行操作。 run()方法注册了一个
		select接口，输入参数是聊天室服务器套接字stdin，输出参数由服务器的输出套接字列表指
		定。调用select.select()方法后得到三个列表：可读套接字、可写套接字和异常套接字。聊
		天室服务器只关心可读套接字，其中保存了准备被读取的数据。如果可读套接字是服务器本身，
		表示有一个新客户端连到服务器上了，服务器会读取客户端的名字，将其广播给其他客户端。如
		果输入参数中有内容，聊天室服务器会退出。类似地，这个聊天室服务器也能处理其他客户端套
		接字的输入，转播客户端直接传送的数据，还能共享客户端进入和离开聊天室的信息。
		"""
		inputs = [self.server,sys.stdin]
		print inputs
		self.outputs = []#这个outputs是用来存储客户端的连接上之后的客户端的socket的
		running = True
		while running:
			time.sleep(3)
			print 'go into running function of server '
			try:
				readable,writeable,exceptional = select.select(inputs,self.outputs,[])
			except select.error,e:
				break
			print 'the readable list is ' + str(readable)
			for sock in readable:
				if sock == self.server:
					"""
					当有新的链接进来的时候进入这里
					"""
					#handle the server socket 
					client,address = self.server.accept()
					"""
					self.server ，称为监听socket描述字,而accept函数返回的是"已连接"的socket描述字
					一个服务器通常通常"仅仅只"创建"一个"监听socket描述字，它在该服务器的生命周期内"一直"存在。
					内核为"每个"由服务器进程接受的客户连接创建了一个"已连接"socket描述字，当服务器"完成了"对某个客户的服务，相应的已连接socket描述字就被"关闭"。
					"""
					print "Chat server: got connection %d from %s"  % (client.fileno(),address)

					#read the login name 
					cname = receive(client).split('NAME: ')[1]

					#Compute client name and send back 
					self.clients += 1 
					send(client,'CLIENT: ' + str(address[0]))
					inputs.append(client)
					self.clientmap[client] = (address,cname)

					#Send joining information to other clients 
					msg = "\n(Connected:New client (%d) from %s)" % (self.clients,self.get_client_name(client))
					for output in self.outputs:
						send(output,msg)
					self.outputs.append(client)
					print 'output client is ' + str(self.outputs)

				elif sock == sys.stdin:#这里经过实际测试发现在服务器端输入一行文本的时候，会终止掉server
					#handle standard input 
					junk = sys.stdin.readline()
					print 'you input %s' % junk
					running = False
				else:
					#handle all other sockets 	
					print 'read data from client sockets'
					try:
						data = receive(sock)
						if data:
							#Send as new client's message ...
							msg = '\n#[' + self.get_client_name(sock) + ']>>' + data
							#Send data to all except ourself
							print 'all output cleints are %s' % self.outputs
							for output in self.outputs:
								if output != sock:
									"""
									因为这个outputs里面存储的是链接到服务器端的所有客户端
									而通过select.select获取到的readable中的sock池中的sock是发来信息的client_socket
									当有消息从其他client_socket发过来的时候，获取到client_socket的消息，然后转发给所有其他链接的客户端（除了发消息的客户端）
									"""
									send(output,msg)
						else:
							print 'Chat server: %d hung up ' % sock.fileno()
							self.clients -= 1 
							sock.close()
							inputs.remove(sock)
							self.outpus.remove(sock)

							#Sending client leaving infomation to others 
							msg = '\n(Now hung up: Client from %s)' % self.get_client_name(sock)
							for output in self.outputs:
								send(output,msg)
					except socket.error,e:
						#Remove
						inputs.remove(sock)
						self.outputs.remove(sock)

		self.server.close()



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
		print self.prompt ##[client444@localhost]
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
			self.prompt = '[' + '@'.join((self.name, addr)) + ']> '
		except socket.error,e:
			print "Failed to connect to chat server @ port %d" % self.port 
			sys.exit(1)

	def run(self):
		"""
		Chat client main loop
		这个run一直在循环执行的，这里为啥只有其他客户端发送文字信息的时候，才能看到测试点的here it is 执行了呢？？
		我猜测这里的select.select是一种异步等待的方式，也就是一直监听这socket，当监听到有数据流的时候那么执行下面的语句
		"""
		while self.connected:
			try:
				sys.stdout.write(self.prompt)
				print 'here it is '
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





if __name__ == '__main__':
	parser = argparse.ArgumentParser(description='Socket Server Example with Select ')
	parser.add_argument('--name',action="store",dest="name",required=True)
	parser.add_argument('--port',action="store",dest="port",type=int,required=True)
	given_args = parser.parse_args()
	port = given_args.port
	name = given_args.name
	if name == CHAT_SERVER_NAME:
		server = ChatServer(port)
		server.run()

	else:
		client = ChatClient(name=name,port=port)
		client.run()



"""
这个脚本要运行三次： 
一次用于启动聊天服务器，两次用于启动两个聊天客户端。
启动服务器时，在命令行中传入参数 --name=server --port=8800
启动clinet1时，把名字参数改成 --name=client1 
启动clinet2时，把名字参数改成 --name=client2
然后在client1中发送消息"hello from client1",这个消息会显示在client2的终端里。同样在client2
同样，在client2中发送消息"hello from client2",也会在client1的终端里显示
"""