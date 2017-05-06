# -*- coding: utf-8 -*-
import os 
import time 
import datetime 
import sys 
try: 
  import xml.etree.cElementTree as ET 
except ImportError: 
  import xml.etree.ElementTree as ET 

port_list = [80,22,443,11009,4050,6667,8080,25,5222,21,55080]
counter = {}
for port in port_list:
	counter[str(port)] = 0


#different folder 
file_list = ['portResult1214','portResult1214-501-1000','portResult1214-1001-1500','portResult1214-1501-2000','portResult1214-2001-2500',
			 'portResult1214-2501-3000','portResult1214-3001-3500','portResult1214-3501-4000','portResult1214-4001-4757']

for file in file_list:
	for i in range(20):
		# print '----------------------------'
		try: 
		  tree = ET.parse("/home/yinshuai/%s/result%s.xml" % (file,i+1))     #打开xml文档 
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
					try:
						service_name =  portinfo.find('service').get('name') #
					except Exception,e:
						print e 

				# print hostname + " " + service_name + " " + portid

				# print portinfo.find('service').get('name')
			# print '*****************'
			# service_name = host.find('ports').find('port').find('service').get('name')
			# print hostname + " " + str(protocol) + " " + service_name
	print '\n\n'
	for port in port_list:
		print str(port) + ":" + str(counter[str(port)])