
# -*- coding: utf-8 -*-
import os 
import time 
import datetime 
import sys 

import numpy as np
# import matplotlib.pyplot as plt
from pylab import *


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
for line in data:
	ip = line[0]
	ip_class = line[1]
	cur.execute('select ip,ip_class,getdatetime from ONION where ip = "%s" and ip_class = "%s" order by getdatetime asc limit 1' % (ip,ip_class))
	da = cur.fetchall()[0]
	print da[0] + da[1] + " " + da[2]
