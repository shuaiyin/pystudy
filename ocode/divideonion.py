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



rowsEachFile = 25
fileCnt = 20

for i in range(0,fileCnt):
	filename = str(1000 + i*rowsEachFile+1)+"-"+str(1000 +(i+1)*rowsEachFile) + '.txt'
	f = open('/home/yinshuai/onionFolder1214-1001-1500/' + filename,'a')
	sql = "select distinct(onion_addr) as onion_addr,id from ONION where ip = '47.88.12.14' and ip_class = 'B' order by id desc limit " + str(1000 + i*rowsEachFile) + ',' + str(rowsEachFile)
	print sql
	cur.execute(sql) 
	onion_data = cur.fetchall()
	for onion in onion_data:
		onion_add  = onion[0] + '.onion'
		f.write(onion_add + '\n')

