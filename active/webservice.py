import tornado.ioloop
import tornado.web
import tornado.options
import tornado.autoreload
import tornado
import MySQLdb
settings = {'debug' : True}
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

# define("debug",default=True,help="Debug Mode",type=bool)
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

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("Hello, world")

class LatestHandler(tornado.web.RequestHandler):
	def get(self):
		onion_addr = self.get_argument('onion_addr') #get lastest onion_addr
		latest_stamp = self.get_argument('latest_stamp') #get lastest stamp
		# sql = "SELECT"
		conn = Db().get_instance()
		cur = conn.cursor()
		sql = "SELECT * FROM %s WHERE getstamp >= %s  "  % ("onion_unique_node",latest_stamp)
		print sql
		cur.execute(sql)
		res = cur.fetchall()
		data_return = []
		for onion_tuple in res:
			ret_line = {}
			ret_line['ip'] = onion_tuple[1]
			ret_line['ip_class'] = onion_tuple[2]
			ret_line['getdatetime'] = onion_tuple[3]
			ret_line['getstamp'] = onion_tuple[4]
			ret_line['onion_addr'] = onion_tuple[5]
			if ret_line['onion_addr'] == onion_addr:
				continue
			data_return.append(ret_line)
		return_dict = {'result':'success','data':data_return}
		self.write(return_dict)
		

def make_app():
    return tornado.web.Application([
        (r"/", MainHandler),
        (r"/getlatest",LatestHandler)
    ],**settings)

if __name__ == "__main__":
    app = make_app()
    app.listen(8888)
    tornado.ioloop.IOLoop.current().start()