import MySQLdb
import time 
import os 
import sys
CONFIG_PATH = '/var/onion_config'

class Config():
	def __init__(self):
		self.config_file_path = CONFIG_PATH
		self.node1_path = ""
		self.node2_path = ""
		self.db_pass = ""
		f = open(self.config_file_path,'r')
		config_lines =  f.readlines()
		self.db_pass = config_lines[0].strip('\n').split(' ')[1]
		self.node1_path = config_lines[1].strip('\n').split(' ')[1]
		self.node2_path = config_lines[2].strip('\n').split(' ')[1]
		self.ip = config_lines[3].strip('\n').split(' ')[1]

	def get_db_pass(self):
		return self.db_pass

	def get_node1_path(self):
		return self.node1_path

	def get_node2_path(self):
		return self.node2_path
	def get_ip(self):
		return self.ip;

class Db():
	def __init__(self):
		self.conn= MySQLdb.connect(
        host='localhost',
        port = 3306,
        user='root',
        passwd=Config().get_db_pass(),
        db ='onion_resp',
        )

	def get_instance(self):
		return self.conn

def date_to_stamp(date_str):
    return int(time.mktime(time.strptime(date_str,'%Y-%m-%d %H:%M:%S')))

conn = Db().get_instance()
node1_path = Config().get_node1_path()
node2_path = Config().get_node2_path()
ip = Config().get_ip()

table_name = "onion_unique_node"
#get the last data 
sql = "SELECT * FROM %s ORDER BY getstamp desc limit 1" % (table_name) 
cur = conn.cursor()
cur.execute(sql)
data = cur.fetchone()
last_stamp = data[4]
last_onion = data[5]
# last_onion = data

def update_data(node_path,ip_class,ip):
	try:
		time_struct =  time.localtime(time.time())
		# print time_struct
		year = time_struct.tm_year
		month = time_struct.tm_mon
		day = time_struct.tm_mday
		date_path = time.strftime("%Y-%m/%m%d")
		file_path = node_path + '/' + date_path
		unique_set = set()
		for onion_line in open(file_path,'r').readlines():
			onion_line_data = onion_line.split('\t')
			get_datetime = onion_line_data[0]
			onion_addr = onion_line_data[2][:-1]
			ip_class = ip_class
			ip = ip
			getstamp = date_to_stamp(get_datetime)
			if (getstamp < last_stamp) or (getstamp == last_stamp and onion_addr == last_onion):
				continue
			unique_set.add((ip,ip_class,get_datetime,getstamp,onion_addr))
		if len(unique_set) > 0:
			sql = "INSERT INTO %s (ip,ip_class,getdatetime,getstamp,onion_addr) VALUES " % (table_name)
			for onion_line in unique_set:
				sql += str(onion_line) + ','
			sql = sql[:-1]
			cur.execute(sql)
			conn.commit()
	except Exception,e:
		print e 
				
				

update_data(node1_path,'A',ip)
update_data(node2_path,'B',ip)
conn.close()