#coding=utf-8
import socket 
hostname = socket.gethostname()
print hostname 
"""
localhost.localdomain
yinshuai: return the current host name 
"""
print socket.gethostbyname(hostname)
"""
127.0.0.1
yinshuai: return the ip address 
"""


##获取远端设备的ip地址 函数
def get_remote_machine_info():
	remote_host = 'www.python.org'
	try:
		print "IP address is %s" % socket.gethostbyname(remote_host)
	except socket.error,err_msg:
		print " %s: %s" % (remote_host,err_msg)

get_remote_machine_info() #IP address is 151.101.16.223

##将ip地址转换为不同的格式
from binascii import hexlify 
def convert_ip4_address():
	for ip_address in ['127.0.0.1','192.168.0.1']:
		packed_ip_addr = socket.inet_aton(ip_address)
		unpacked_ip_address = socket.inet_ntoa(packed_ip_addr)
		print " IP Address: %s => Packed : %s,Unpacked:%s" % (ip_address,hexlify(packed_ip_addr),unpacked_ip_address)

convert_ip4_address()
"""
 IP Address: 127.0.0.1 => Packed : 7f000001,Unpacked:127.0.0.1
 IP Address: 192.168.0.1 => Packed : c0a80001,Unpacked:192.168.0.1
 yinshuai:
 调用socket的inet_aton 函数之后可以将一个string形式的ip地址为打包二进制的表示
 调用socket.inet_ntoa 可以将一个二进制的包还原为ip地址
 为了便于显示，所以使用hexlify 来将二进制用16进制显示
 """


 ###通过指定的端口和协议找到服务名
 ##if you want to find net service, you'd better know the PORT TCP OR UDP RUNING IN 

def find_service_name():
 	protocolname = 'tcp'
 	for port in [80,25,3306]:
 		print "Port %s=> service name: %s" % (port,socket.getservbyport(port,protocolname))

find_service_name()
"""
Port 80=> service name: http
Port 25=> service name: smtp
Port 3306=> service name: mysql

"""

###主机字节序和网络字节序之间的相互转换
def convert_integer():
	data = 1234 
	#32-bit
	print "Original %s => Long host byte order : %s,NetWork byte order : %s" % (data,socket.ntohl(data),socket.htonl(data)) 
	#16-bit 
	print "Original %s=> Short host byte order : %s, NetWork byte order : %s" % (data,socket.ntohs(data),socket.htons(data))

convert_integer()
"""
Original 1234 => Loing host byte order : 3523477504,NetWork byte order : 3523477504
Original 1234=> Short host byte order : 53764, NetWork byte order : 53764

yinshuai: 这里以整数为例，演示了如何把他转换成网络字节序列和主机字节序列。socket 序列中的类函数ntoh1()
把网络字节序列转换成了long int 主机字节序列 函数名中的n表示网络，h表示主机 l表示long int  s  表示 short int 
ntohl and ntohs and htonl htons is class method 

"""



#####set and fetch default socket expire  
def test_socket_timeout():
	s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
	print "Default socket timeout : %s " % s.gettimeout() 
	s.settimeout(100)
	print "Current socket timeout: %s" % s.gettimeout()

test_socket_timeout()
"""
Default socket timeout : None 
Current socket timeout: 100.0
yinshuai: if the param of settimeout if None,it means stop the socket time expire detect 
"""


####treat socket exception gracely 
import sys 
import argparse 
def main():
	#setup argument parsing 
	parser = argparse.ArgumentParser(description='Socket Error Example')
	parser.add_argument('--host',action="store",dest="host",required=False)
	parser.add_argument('--port',action="store",dest="port",required=False)
	parser.add_argument('--file',action="store",dest="file",required=False)
	given_args = parser.parse_args()
	host = given_args.host
	port = int(given_args.port)
	filename = given_args.file
	#first try-except block -- create socket 
	try:
		s  = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
		print s  # <socket._socketobject object at 0x7fd8c491df30>
	except socket.error,e:
		print "Error when creating socket : %s" % e 
		sys.exit(1)
	#Second try-except block -- connect to give host/post
	try:
		s.connect((host,port))
	except socket.gaierror,e:
		print "Address-related error connecting to server : %s" % e 
		sys.exit(1)
	except socket.error,e:
		print "Connection error: %s" % e 
		sys.exit(1)

	#Third try-except block ---sending data 
	try:
		print 'GET %s HTTP/1.1\r\n\r\n' % filename
		s.sendall("GET %s HTTP/1.1\r\n\r\n" % filename)
	except socket.error,e:
		print "Error sending data : %s" % e 
		sys.exit(1)

	while 1:
		#Fourth tr-except --- waiting to receivedata from remote host 
		try:
			buf = s.recv(2048)
			print 'buffer is %s' % buf
		except socket.error,e:
			print "Error receiving data: %s " % e 
			sys.exit(1)

		if not len(buf):
			break
		#write the received data 
	sys.stdout.write(buf)

### python ch1.py --host=www.python.org --port=80 --file=1_7_scoket_errors.py
###python ch1.py --host=101.200.214.68 --port=80 --file=qyh.html
main()
"""
<socket._socketobject object at 0x7f0c5c016ec0>
GET /file.html HTTP/1.1


buffer is HTTP/1.1 400 Bad Request
Server: nginx/1.10.0
Date: Mon, 04 Jul 2016 02:37:33 GMT
Content-Type: text/html
Content-Length: 173
Connection: close

<html>
<head><title>400 Bad Request</title></head>
<body bgcolor="white">
<center><h1>400 Bad Request</h1></center>
<hr><center>nginx/1.10.0</center>
</body>
</html>

buffer is 
yinshuai: try to modity the length of receive buffer,and you will learn more about how to set buffer size 

"""


#### modify the length of socket send and receive buffer  
## in more case,the default length of socket buffer may not enough 
print '----------------------'
SEND_BUF_SIZE = 4096 
RECV_BUF_SIZE = 4096 

def modify_buff_size(): 
	sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
	#get the size of the socket's send buffer 
	bufsize = sock.getsockopt(socket.SOL_SOCKET,socket.SO_SNDBUF)
	print  "Buffer size [Before]: %d" %  bufsize

	sock.setsockopt(socket.SOL_SOCKET,socket.TCP_NODELAY,1)
	sock.setsockopt(
			socket.SOL_SOCKET,
			socket.SO_SNDBUF,
			SEND_BUF_SIZE)
	sock.setsockopt(
			socket.SOL_SOCKET,
			socket.SO_RCVBUF,
			RECV_BUF_SIZE)
	bufsize = sock.getsockopt(socket.SOL_SOCKET,socket.SO_SNDBUF)
	print  "Buffer size [After]: %d" %  bufsize

modify_buff_size()
"""
Buffer size [Before]: 16384
Buffer size [After]: 8192
yinshuai: the input param of setsockopt is level,optname,the value set 

"""




