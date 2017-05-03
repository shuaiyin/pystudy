

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

	def get_db_pass(self):
		return self.db_pass

	def get_node1_path(self):
		return self.node1_path

	def get_node2_path(self):
		return self.get_node2_path



# conf = Config()
# conf.readConfigFile()
# print conf.get_db_pass()


