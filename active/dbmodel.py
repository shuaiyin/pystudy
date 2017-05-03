import MySQLdb
from config import Config 


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



if __name__ == "__main__":
	db = Db()
	print db.get_instance()