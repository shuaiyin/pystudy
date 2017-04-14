# -*- coding: utf-8 -*-
import os 
import time 
import datetime 
import sys 


import MySQLdb

conn= MySQLdb.connect(
        host='localhost',
        port = 3306,
        user='root',
        passwd='111111',
        db ='onion_resp',
        )

cur = conn.cursor()



rowsEachFile = 1000
fileCnt = 10
for i in range(0,fileCnt):
	filename = str(i*1000+1)+"-"+str((i+1)*rowsEachFile) + '.txt'
	f = open('/home/yinshuai/onionFolder/' + filename,'a')
	sql = "select distinct(onion_addr) as onion_addr,id from ONION order by id asc limit " + str(i*1000) + ',1000'
	print sql
	cur.execute(sql) 
	onion_data = cur.fetchall()
	for onion in onion_data:
		onion_add  = onion[0] + '.onion'
		f.write(onion_add + '\n')

