
import sys
import argparse

import MySQLdb
import stem
from stem.control import Controller
import os
import time 
from multiprocessing import Process
from timeout import timeout
import json
def get_connection():
    conn= MySQLdb.connect(
        host='localhost',
        port = 3306,
        user='root',
        passwd='111111',
        db ='onion_resp',
        )
    return conn


table_name = "onion_uniques"
# data = [{"name":"yinshuai"},{"age":44}]
# data_string = json.dumps(data)
# print type(data_string) ##str 
# decoded = json.loads(data_string)
# print type(decoded)##list 

# create table onion_uniques (
#     id int unsigned auto_increment primary key,
#     onion_addr char(16) not null default '',
#     recent_check_time int unsigned  not null default 0,
#     recent_status tinyint unsigned not null default 0 comment '0 is default, 1 is alieve ,2 is died, 3 is timeout',
#     check_times smallint unsigned not null default 0,
#     alive_times tinyint unsigned not null default 0,
#     died_times tinyint unsigned not null default 0,
#     timeout_times tinyint unsigned not null default 0,
#     check_info blob,
#     INDEX rctime (recent_check_time),
#     INDEX on_ar (onion_addr)
# )engine innodb charset utf8;


# sys.exit(0)

@timeout(120)
def judgeActive(onion_addr):
    conn = get_connection()
    proc = os.getpid()
    print('{0} check to {1} by process id: {2}'.format(
        onion_addr, '*', proc))
    with Controller.from_port(port=9052) as controller:
        controller.authenticate("111111")
        print controller
        try:
            hs_descriptor = controller.get_hidden_service_descriptor(onion_addr,await_result = True)
            # print hs_descriptor
            cur = conn.cursor()
            # judgeActive('ityukvsoqjgzcimm.onion')
            sql = 'SELECT check_info,check_times  FROM %s WHERE onion_addr = "%s" '  % (table_name, onion_addr[:16])
            # print sql
            cur.execute(sql)    
            res = cur.fetchone()
            check_info = res[0]
            # sys.exit(0)
            if check_info == None:
                check_info = ""
                new_check_info = [{'check_time':int(time.time()),'status':1,'times':res[1] + 1}]
            else:
                check_info_list = eval(check_info)
                new_check_info =  check_info_list  + [{'check_time':int(time.time()),'status':1,'times':res[1] + 1}]

            new_check_info_str = json.dumps(new_check_info)
            sql = 'UPDATE %s SET recent_check_time = %s,recent_status=1, alive_times=alive_times+1,check_info="%s" ,check_times = check_times + 1 WHERE onion_addr = "%s" ' % (table_name, int(time.time()), new_check_info, onion_addr[:16])
            print(sql)
            cur.execute(sql)
            print(onion_addr + " is alive from process " + str(proc) + time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time())))

        except stem.DescriptorUnavailable:
            cur = conn.cursor()
            sql = 'SELECT check_info,check_times  FROM %s WHERE onion_addr = "%s" '  % (table_name, onion_addr[:16])
            # print sql
            cur.execute(sql)
            res = cur.fetchone()
            check_info = res[0]
            if check_info == None:
                check_info = ""
                new_check_info = [{'check_time':int(time.time()),'status':2,'times':res[1] + 1}]
            else:
                check_info_list = eval(check_info)
                new_check_info =  check_info_list  + [{'check_time':int(time.time()),'status':2,'times':res[1] + 1}]

            new_check_info_str = json.dumps(new_check_info)
            sql = 'UPDATE %s SET recent_check_time = %s,recent_status=2, died_times=died_times+1,check_info="%s",check_times = check_times + 1 WHERE onion_addr = "%s" ' % (table_name, int(time.time()), new_check_info, onion_addr[:16])
            print sql
            cur.execute(sql)
            print(onion_addr + " is died from process " + str(proc) + time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time())))
        
        except Exception,e:#timeout error
            cur = conn.cursor()
            sql = 'SELECT check_info,check_times  FROM %s WHERE onion_addr = "%s" '  % (table_name, onion_addr[:16])
            cur.execute(sql)
            res = cur.fetchone()
            check_info = res[0]
            print "check info is "
            print check_info
            if check_info == None:
                check_info = ""
                new_check_info = [{'check_time':int(time.time()),'status':3,'times':res[1] + 1}]
            else:
                check_info_list = eval(check_info)
                new_check_info =  check_info_list  + [{'check_time':int(time.time()),'status':3,'times':res[1] + 1}]

            new_check_info_str = json.dumps(new_check_info)
            sql = 'UPDATE %s SET recent_check_time = %s,recent_status=3, timeout_times=timeout_times+1,check_info="%s",check_times = check_times + 1 WHERE onion_addr = "%s" ' % (table_name, int(time.time()), new_check_info, onion_addr[:16])
            print sql
            print '------------------------------------'
            print("timeout is found " + onion_addr +  str(e) + time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time())))
            print ("-----------------------------")
        try:#This place is more important that using the try catch make the timeout come realize and useable,so why
            controller.close()
            conn.commit()
            cur.close()
            conn.close()
        except Exception,e:
            print "excepiton found" + str(e)



# https://www.blog.pythonlibrary.org/2016/08/02/python-201-a-multiprocessing-tutorial/

# onion_addr = "2263srk5vjpiap74.onion"
# conn = get_connection()
# cur = conn.cursor()
# sql = 'SELECT check_info,check_times  FROM %s WHERE onion_addr = "%s" '  % (table_name, onion_addr[:16])
# print sql
# cur.execute(sql)
# res = cur.fetchone()
# check_info = res[0]
# if check_info == None:
#     check_info = ""
#     new_check_info = [{'check_time':int(time.time()),'status':2,'times':res[1] + 1}]
# else:
#     check_info_list = eval(check_info)
#     new_check_info =  check_info_list  + [{'check_time':int(time.time()),'status':2,'times':res[1] + 1}]

# new_check_info_str = json.dumps(new_check_info)
# sql = 'UPDATE %s SET recent_check_time = %s,recent_status=2, died_times=died_times+1,check_info="%s",check_times = check_times + 1 WHERE onion_addr = "%s" ' % (table_name, int(time.time()), new_check_info, onion_addr[:16])
# print sql
# cur.execute(sql)
# print(onion_addr + " is died from process " + str(proc) + time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time())))


def main():
    process_cnt = 5
    #get distinct ip address 
    conn = get_connection()
    cur = conn.cursor()
    i = 0
    time_need_check = int(time.time()) - 86400
    sql = "SELECT count(onion_addr) FROM %s WHERE recent_check_time <= %s" % (table_name, time_need_check)
    print sql
    cur.execute(sql)
    count = cur.fetchone()
    print count
    while i <= count:
        sql = "SELECT onion_addr FROM %s WHERE recent_check_time <= %s limit %s,%s" % (table_name, time_need_check, i, process_cnt)
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


if __name__ == '__main__':
    sys.exit(main())


