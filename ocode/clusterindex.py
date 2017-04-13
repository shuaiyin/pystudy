import sys 
# -*- coding: utf-8 -*-
import os 
import time 
import datetime 
import sys 


import MySQLdb


charstr = 'abc'



conn= MySQLdb.connect(
        host='localhost',
        port = 3306,
        user='root',
        passwd='111111',
        db ='onion_resp',
        )

cur = conn.cursor()
cur.execute("DROP TABLE IF EXISTS CLUSTER")
creat_table = """
	CREATE TABLE CLUSTER(
	id varchar(64) primary key,
	value int not null default 0,
	KEY `vindex` (`value`)
)engine=innodb"""
cur.execute(creat_table)

for _ in xrange(100000):
	break

