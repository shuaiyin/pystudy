#coding=utf-8

import MySQLdb
from time import sleep,ctime
# con_pool = []
# num = 60
# while num > 0:
# 	con = MySQLdb.connect("101.200.214.68","root","tZ3BtYCeQLdwyKqF","fitness")
# 	con_pool.append(con)
# 	num -=1 


# for info in con_pool:
# 	print info
# con = con_pool[0]
# print con
# for x in range(1000):

# 	con.cursor().execute("select * from fs_users limit 2")

class NotSingle(object):
	def __init__(self):
		conn = MySQLdb.connect("101.200.214.68","root","tZ3BtYCeQLdwyKqF","fitness")



class Single(object):
	def __init__(self):
		self.conn = MySQLdb.connect("101.200.214.68","root","tZ3BtYCeQLdwyKqF","fitness")


	instance = None


	@classmethod
	def get_instance(cls):
		if not cls.instance:cls.instance = Single()
		return cls.instance

	@classmethod
	def set_init(cls):
		cls.instance = None

Single.get_instance()
print ctime()
print 'first 5 second ...'
sleep(5)
Single.get_instance().conn.close()
Single.set_init()
print 'second 5 second ...'
sleep(5)
print 'thrid 5 second '
Single.get_instance()
sleep(5)
print ctime()
# for i in range(100000):
# 	print Single.get_instance().conn
# # print  Single.get_instance().conn



