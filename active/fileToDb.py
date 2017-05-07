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

creat_table = """
	CREATE TABLE If Not Exists onion_unique_node(
	id int unsigned auto_increment primary key ,
	ip char(16) not null default '',
	ip_class char(1) not null default '',
	getdatetime char(19) not null default '',
	getstamp int(11),
	onion_addr char(16),
	KEY `sindex` (`ip`,`ip_class`,`onion_addr`)
)engine=innodb"""
cur = conn.cursor()
cur.execute(creat_table)##1.create table 
table_name = "onion_unique_node"
#get the last data 
sql = "SELECT * FROM %s ORDER BY id desc limit 1" % (table_name) 
cur.execute(sql)
data = cur.fetchone()
# last_datetime = data[3]
#2017-01    0120

time_struct =  time.localtime(time.time())
# print time_struct
year = time_struct.tm_year
month = time_struct.tm_mon
day = time_struct.tm_mday

def init_data(node_path,ip_class,ip):
	year_day_list = sorted(os.listdir(node_path))
	for year_day in year_day_list:
		year_day_path = node1_path + '/' + year_day
		mon_day_list = sorted(os.listdir(year_day_path))
		for mon_day in mon_day_list:
			unique_set = set()
			onion_file_path = year_day_path + '/' + mon_day
			for onion_line in open(onion_file_path,'r').readlines():
				onion_line_data = onion_line.split('\t')
				get_datetime = onion_line_data[0]
				onion_addr = onion_line_data[2][:-1]
				ip_class = ip_class
				ip = ip
				getstamp = date_to_stamp(get_datetime)
				unique_set.add((ip,ip_class,get_datetime,getstamp,onion_addr))
			sql = "INSERT INTO %s (ip,ip_class,getdatetime,getstamp,onion_addr) VALUES " % (table_name)
			for line_data in unique_set:
				sql += str(line_data) + ','
			sql = sql[:-1]
			# sys.exit(0)
			cur.execute(sql)
			conn.commit()


				

init_data(node1_path,'A',ip)
init_data(node2_path,'B',ip)
conn.close()