
import sys
import argparse

import MySQLdb
import stem
from stem.control import Controller
import os
import time 
from multiprocessing import Process
from timeout import timeout
# conn= MySQLdb.connect(
#         host='localhost',
#         port = 3306,
#         user='root',
#         passwd='111111',
#         db ='onion_resp',
#         )

def get_connection():
    conn= MySQLdb.connect(
        host='localhost',
        port = 3306,
        user='root',
        passwd='111111',
        db ='onion_resp',
        )
    return conn

@timeout(120)
def judgeActive(onion_addr):
    conn = get_connection()
    proc = os.getpid()
    print('{0} doubled to {1} by process id: {2}'.format(
        onion_addr, '*', proc))
    with Controller.from_port(port=9052) as controller:
        controller.authenticate("111111")
        try:
            cur = conn.cursor()
            hs_descriptor = controller.get_hidden_service_descriptor(onion_addr,await_result = True)
            # print(hs_descriptor)
            sql = 'update ONION SET status = 1 WHERE onion_addr = "%s" ' % (onion_addr[:-6])
            # print(sql)
            cur.execute(sql)
            print(onion_addr + " is alive from process " + str(proc) + time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time())))

        except stem.DescriptorUnavailable:
            # print("Descriptor not found, the hidden service may be offline.")
            sql = 'update ONION SET status = -1 WHERE onion_addr = "%s" ' % (onion_addr[:-6])
            # print(sql)
            cur.execute(sql)
            print(onion_addr + " is died from process " + str(proc) + time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time())))
        except Exception,e:
            print '------------------------------------'
            print("timeout is found" + onion_addr +  str(e) + time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time())))
            print ("-----------------------------")
        try:#This place is more important that using the try catch make the timeout come realize and useable,so why
            controller.close()
            conn.commit()
            cur.close()
            conn.close()
        except Exception,e:
            print "excepiton found" + str(e)

 

# https://www.blog.pythonlibrary.org/2016/08/02/python-201-a-multiprocessing-tutorial/

def main():
    process_cnt = 20
    #get distinct ip address 
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("select count(distinct(onion_addr)) from ONION  WHERE ip = '47.88.6.38' AND status =0")
    count = cur.fetchall()[0]
    cur.close()
    i = 0
    while i <= count:
        cur = conn.cursor()
        sql = "select distinct(onion_addr) from ONION WHERE (ip = '47.88.6.38')   AND status = 0 limit %s,%s" % (i,process_cnt)
        cur.execute(sql);
        i += process_cnt
        procs = []
        ip_list = cur.fetchall()
        for ip in ip_list:
            onion_addr = ip[0] + '.onion'
            proc = Process(target=judgeActive, args=(onion_addr,))
            procs.append(proc)
            proc.start()
        for proc in procs:
            proc.join()
        print("sleeping now is " + time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time())))
        time.sleep(1)
        cur.close()
    print("finished")
    sys.exit(0)
    # ip_list = ['22222222xsj7g55v','22222uacnky7x5jr','222wagcpzf3aip2f','22a5mu4fojklcd4q','222222222c7r2gdj']
    # # numbers = [5, 10, 15, 20, 25]
    # procs = []
 
    # for ip in ip_list:
    #     proc = Process(target=judgeActive, args=(ip,))
    #     procs.append(proc)
    #     proc.start()
 
    # for proc in procs:
    #     proc.join()
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


