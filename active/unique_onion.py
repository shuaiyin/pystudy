
import sys
import argparse

import MySQLdb
import stem
from stem.control import Controller
import os
import time 
from multiprocessing import Process
from timeout import timeout
import json
def get_connection():
    conn= MySQLdb.connect(
        host='localhost',
        port = 3306,
        user='root',
        passwd='111111',
        db ='onion_resp',
        )
    return conn


conn = get_connection()
sql = "select distinct(onion_addr) from ONION";
cur = conn.cursor()
cur.execute(sql);
ip_list = cur.fetchall()
for ip in ip_list:
    onion_addr = ip[0]
    print onion_addr
    sql = 'insert into onion_uniques (onion_addr) values ("%s")' % (onion_addr)
    # print sql
    cur.execute(sql)
    conn.commit()
    # cur.commit()
