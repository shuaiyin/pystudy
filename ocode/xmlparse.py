# -*- coding: utf-8 -*-
import os 
import time 
import datetime 
import sys 
try: 
  import xml.etree.cElementTree as ET 
except ImportError: 
  import xml.etree.ElementTree as ET 

port_list = [80,22,443,11009,4050,6667,8080,25,5222]
counter = {}
for port in port_list:
	counter[str(port)] = 0
for i in range(20):
	print '----------------------------'
	try: 
	  tree = ET.parse("/home/yinshuai/portResult1214-1001-1500/result%s.xml" % (i+1))     #打开xml文档 
	  #root = ET.fromstring(country_string) #从字符串传递xml 
	  root = tree.getroot()         #获得root节点  
	except Exception, e: 
	  print "Error:cannot parse file:country.xml."
	  sys.exit(1) 
	# for child in root: 
	#   print child.tag, "---", child.attrib 
	for host in root.findall('host'):
		hostname = host.find('hostnames').find('hostname').get('name')
		protocol = host.find('ports').find('port').get('protocol')
		# print protocol
		for portinfo in host.find('ports').findall('port'):
			protocol = portinfo.get('protocol')
			portid = portinfo.get('portid')
			counter[portid] += 1
			if portid == '11009':
				service_name = 'torchat'
			else:
				service_name =  portinfo.find('service').get('name') #

			print hostname + " " + service_name + " " + portid

			# print portinfo.find('service').get('name')
		print '*****************'
		# service_name = host.find('ports').find('port').find('service').get('name')
		# print hostname + " " + str(protocol) + " " + service_name
print '\n\n'
for port in port_list:
	print str(port) + ":" + str(counter[str(port)])