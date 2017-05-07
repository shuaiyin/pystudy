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
		self.node_list = config_lines[4]

	def get_db_pass(self):
		return self.db_pass

	def get_node1_path(self):
		return self.node1_path

	def get_node2_path(self):
		return self.node2_path
	def get_ip(self):
		return self.ip;

	def get_node_list(self):
		print self.ip


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


def main():
	Config().get_node_list()



main()