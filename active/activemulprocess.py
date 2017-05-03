
import sys
import argparse

import MySQLdb
import stem
from stem.control import Controller
import os
 
from multiprocessing import Process

conn= MySQLdb.connect(
        host='localhost',
        port = 3306,
        user='root',
        passwd='111111',
        db ='onion_resp',
        )

cur = conn.cursor()

global alive_cnt
global died_cnt
alive_cnt = 0
died_cnt = 0

def judgeActive(onion_addr):
    global alive_cnt
    global died_cnt
    proc = os.getpid()
    print('{0} doubled to {1} by process id: {2}'.format(
        onion_addr, '*', proc))
    with Controller.from_port(port=9051) as controller:
        controller.authenticate("111111")
        try:
            hs_descriptor = controller.get_hidden_service_descriptor(onion_addr)
            # print(hs_descriptor)
            print onion_addr + " is alive"
            alive_cnt += 1
            print 'current-alive-count is ' + str(alive_cnt)

        except stem.DescriptorUnavailable:
            print("Descriptor not found, the hidden service may be offline.")
            died_cnt += 1
            print 'current-died-count is ' + str(died_cnt)
        except Exception,e:
            print e 

 



def main():
    ##get distinct ip address 
    # cur.execute("select distinct(onion_addr) from ONION WHERE ip = '47.88.12.14' and ip_class = 'A'");
    # ip_list = cur.fetchall()
    ip_list = ['22222222xsj7g55v','22222uacnky7x5jr','222wagcpzf3aip2f','22a5mu4fojklcd4q','222222222c7r2gdj']
    # numbers = [5, 10, 15, 20, 25]
    procs = []
 
    for ip in ip_list:
        proc = Process(target=judgeActive, args=(ip,))
        procs.append(proc)
        proc.start()
 
    for proc in procs:
        proc.join()

    procs2 = []
    ip_list2 = ['22gfaas667uywsfi','22n54hmykxi5bgnu','22wbl5hfruytp2zj','23o32ocvsec6ruge','244zgjtnfrvn5gac']
    for ip in ip_list2:
        proc2 = Process(target=judgeActive, args=(ip,))
        procs2.append(proc)
        proc2.start()
 
    for proc2 in procs2:
        proc2.join()

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


if __name__ == '__main__':
    sys.exit(main())


