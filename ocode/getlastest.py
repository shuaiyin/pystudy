
# -*- coding: utf-8 -*-
import os 
import time 
import datetime 
import sys 

import numpy as np
import matplotlib.pyplot as plt
from pylab import *


from matplotlib.font_manager import FontProperties
font = FontProperties(fname = "/usr/share/fonts/truetype/arphic/ukai.ttc", size=14)
import MySQLdb

conn= MySQLdb.connect(
        host='localhost',
        port = 3306,
        user='root',
        passwd='111111',
        db ='onion_resp',
        )

cur = conn.cursor()
cur.execute('select ip,ip_class from ONION group by ip,ip_class')
data = cur.fetchall()




# for line in data:
# 	ip = line[0]
# 	ip_class = line[1]
# 	cur.execute('select ip,ip_class,getdatetime from ONION where ip = "%s" and ip_class = "%s" order by getdatetime asc limit 1' % (ip,ip_class))
# 	da = cur.fetchall()[0]
# 	print da[0] + da[1] + " " + da[2]


node_list = []
count_list = []
for line in data:
	ip = line[0]
	ip_class = line[1]
	# cur.execute('select count(*) from ONION where ip = "%s" and ip_class = "%s" ' % (ip,ip_class))
	# count =  cur.fetchall()[0][0]
	# print count
	cur.execute('select count(distinct onion_addr) from ONION where ip = "%s" and ip_class = "%s" ' % (ip,ip_class))
	distinct_cnt = cur.fetchall()[0][0]
	node_list.append(ip + ip_class)
	count_list.append(distinct_cnt)



# service_port = ('80:http','8080','https:443','ssh:22','smtp:25','xmpp:5222','tor-chat:11009','irc:6667')
y_pos = np.arange(len(count_list))
count = np.array(count_list)
plt.barh(y_pos,count,0.5,align='center',alpha=0.4)
plt.xlabel(u"总数",fontproperties=font)#
plt.title(u"各个节点获取到的独特洋葱地址总数统计图",fontproperties=font)
plt.yticks(y_pos,node_list)
plt.show()
