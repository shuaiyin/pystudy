
import sys
import argparse

import MySQLdb
import stem
from stem.control import Controller
from connection import Connection
import tornado.ioloop
import tornado.web




def get_mysql_pass():
    f = open('/var/mysql-pass','r')
    print f.read()


class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("Hello, world")

def make_app():
    return tornado.web.Application([
        (r"/", MainHandler),
    ])

# if __name__ == "__main__":
#     app = make_app()
#     app.listen(8888)
#     tornado.ioloop.IOLoop.current().start()




conn= MySQLdb.connect(
        host='localhost',
        port = 3306,
        user='root',
        passwd='111111',
        db ='onion_resp',
        )

cur = conn.cursor()




# def main():

#     get_mysql_pass()
#     sys.exit(0)
#     alive_cnt = 0
#     died_cnt = 0


#     ##get distinct ip address 
#     cur.execute("select distinct(onion_addr) from ONION WHERE ip = '47.88.12.14' and ip_class = 'B'");
#     ip_list = cur.fetchall()
#     for ip in ip_list[6:]:
#         onion_addr = ip[0] + ".onion"
#         print onion_addr
#         with Controller.from_port(port=9051) as controller:
#             controller.authenticate("111111")

#             try:
#                 hs_descriptor = controller.get_hidden_service_descriptor(onion_addr)
#                 published_time = hs_descriptor.published##get publish time of the hidden service 
#                 # print(hs_descriptor)
#                 print onion_addr + " is alive"
#                 alive_cnt += 1
#                 print 'current-alive-count is ' + str(alive_cnt)

#             # except stem.DescriptorUnavailable:
#             #     print("Descriptor not found, the hidden service may be offline.")
#             #     died_cnt += 1
#             #     print 'currendef main():

#     get_mysql_pass()
#     sys.exit(0)
#     alive_cnt = 0
#     died_cnt = 0


#     ##get distinct ip address 
#     cur.execute("select distinct(onion_addr) from ONION WHERE ip = '47.88.12.14' and ip_class = 'B'");
#     ip_list = cur.fetchall()
#     for ip in ip_list[6:]:
#         onion_addr = ip[0] + ".onion"
#         print onion_addr
#         with Controller.from_port(port=9051) as controller:
#             controller.authenticate("111111")

#             try:
#                 hs_descriptor = controller.get_hidden_service_descriptor(onion_addr)
#                 published_time = hs_descriptor.published##get publish time of the hidden service 
#                 # print(hs_descriptor)
#                 print onion_addr + " is alive"
#                 alive_cnt += 1
#                 print 'current-alive-count is ' + str(alive_cnt)

#             # except stem.DescriptorUnavailable:
#             #     print("Descriptor not found, the hidden service may be offline.")
#             #     died_cnt += 1
#             #     print 'current-died-count is ' + str(died_cnt)
#             except Exception,e:
#                 print e 
#     return 1t-died-count is ' + str(died_cnt)
#             except Exception,e:
#                 print e 
#     return 1

# main()
# def main():


#     # sys.exit(0)
#     parser = argparse.ArgumentParser(description="%s fetches a Tor hidden "
#                                      "service descriptor." % sys.argv[0])

#     parser.add_argument("-p", "--port", type=int, default=9051,
#                         help="Tor controller port")

#     parser.add_argument('onion_address', type=str, help='Onion address')

#     args = parser.parse_args()

#     with Controller.from_port(port=args.port) as controller:
#         controller.authenticate("111111")

#         try:
#             hs_descriptor = controller.get_hidden_service_descriptor(args.onion_address)
#             print(hs_descriptor)

#         except stem.DescriptorUnavailable:
#             print("Descriptor not found, the hidden service may be offline.")
#             return 1


# if __name__ == '__main__':
#     sys.exit(main())


