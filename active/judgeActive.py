

import sys
import argparse

import MySQLdb
import stem
from stem.control import Controller
from timeout import timeout
import os 
import time 
def get_mysql_pass():
    f = open('/var/mysql-pass','r')
    password = f.readline(6)
    return password


conn= MySQLdb.connect(
        host='localhost',
        port = 3306,
        user='root',
        passwd=get_mysql_pass(),
        db ='onion_resp',
        )


@timeout(20)
def judgeActive(onion_addr):
    # conn = get_connection()
    proc = os.getpid()
    print('{0} doubled to {1} by process id: {2}'.format(
        onion_addr, '*', proc))
    with Controller.from_port(port=9053) as controller:
        controller.authenticate("111111")
        try:
            # cur = conn.cursor()######
            hs_descriptor = controller.get_hidden_service_descriptor(onion_addr,await_result = True)
            # print(hs_descriptor)
            sql = 'update ONION SET status = 1 WHERE onion_addr = "%s" ' % (onion_addr[:-6])
            # print(sql)
            # cur.execute(sql)#######
            print(onion_addr + " is alive from process " + str(proc) + time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time())))

        except stem.DescriptorUnavailable:
            # print("Descriptor not found, the hidden service may be offline.")
            sql = 'update ONION SET status = -1 WHERE onion_addr = "%s" ' % (onion_addr[:-6])
            # print(sql)
            # cur.execute(sql)#########
            print(onion_addr + " is died from process " + str(proc) + time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time())))
        except Exception,e:
            print '------------------------------------'
            print("timeout is found" + onion_addr + str(e) + time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time())))
            print ("-----------------------------")
        try:#This place is more important that using the try catch make the timeout come realize and useable,so why
            controller.close()
            # conn.commit()#######
            # cur.close()#########
            # conn.close()########
        except Exception,e:
            print "excepiton found" + str(e)

@timeout(6)
def fun(onion_addr):
	try:
		with Controller.from_port(port=9053) as controller:
			controller.authenticate("111111")
			try:
				print 'come here'
				hs_descriptor = controller.get_hidden_service_descriptor(onion_addr)
				print hs_descriptor
			except Exception,e:
				print 'exception found'
	except Exception,e:
		print "except found "
fun('emzcsjhcho3c7flk.onion')
# judgeActive('emzcsjhcho3c7flk.onion')