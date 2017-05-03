from config import Config
from dbmodel import Db

conn = Db().get_instance()
node1_path = Config().get_node1_path()
node2_path = Config().get_node2_path()

