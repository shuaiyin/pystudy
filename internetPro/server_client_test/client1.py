#coding=utf-8
import socket 
import sys 
import argparse
host = 'localhost'

def echo_client(port):
	""" A simple echo client """
	#Create a TCP/IP socket 
	sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
	#connect the socket to the server 
	server_address = (host,port)
	print "Connecting to  %s port %s" % server_address 
	sock.connect(server_address)

	#Send data 
	try:
		#send data 
		message = "Test message, this will be echoed "
		print "Sending %s" % message 
		sock.sendall(message)
		#Look for the response 
		amount_received = 0
		amount_expected = len(message)
		while amount_received < amount_expected:
			data = sock.recv(16)##the length of the receive buffer is 16 
			amount_received += len(data)
			print "Received: %s" % data 
	except socket.error,e:
		print "Socket error: %s" %  str(e) 

	except Exception,e:
		print "Other exception: %s" % str(e)

	finally:
		print "Closing connection to the server "
		sock.close()


if __name__ == '__main__':
	parser = argparse.ArgumentParser(description='Socket Clinet Example')
	parser.add_argument('--port',action="store",dest="port",type=int,required=True)
	given_args = parser.parse_args()
	port = given_args.port
	echo_client(port)

"""
[root@localhost internetPro]# python client1.py --port=9901
Connecting to  localhost port 9901
Sending Test message, this will be echoed 
Received: Test message, th
Received: is will be echoe
Received: d 
Closing connection to the server 

yinshuai: the size of receive buffer is 16 bytes ,so it can only receive 16 bytes data once time 
"""






