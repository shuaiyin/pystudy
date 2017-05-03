

import sys
import argparse

import MySQLdb
import stem
from stem.control import Controller

def get_mysql_pass():
    f = open('/var/mysql-pass','r')
    password = f.readline(6)
    return password


conn= MySQLdb.connect(
        host='localhost',
        port = 3306,
        user='root',
        passwd=get_mysql_pass(),
        db ='onion_resp',
        )

cur = conn.cursor()
print cur