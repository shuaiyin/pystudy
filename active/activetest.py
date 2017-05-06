
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
        try:
            cur = conn.cursor()
            hs_descriptor = controller.get_hidden_service_descriptor(onion_addr,await_result = True)
            # print(hs_descriptor)
            # sql = 'update ONION SET status = 1 WHERE onion_addr = "%s" ' % (onion_addr[:-6])
            sql = 'SELECT check_info,check_times  FROM %s WHERE onion_addr = "%s" '  % (table_name, onion_addr[:16])
            cur.execute(sql)
            res = cur.fetchone()
            check_info = res[0]
            print check_info
            if not check_info:
                check_info = ""
                new_json = [{'check_time':int(time.time()),'status':1,'times':res[1]}]
            else:
                new_json = json.loads(check_info).append({'check_time':int(time.time()),'status':1,'times':res[1]})

            new_check_info = json.dumps(new_json)
            print new_check_info
            print '\n\n'
            sql = "UPDATE %s SET recent_check_time = %s, recent_status= 1, alive_times = alive_times + 1," + \
                "check_info = '%s' WHERE onion_addr = %s " % (table_name, int(time.time()), new_check_info,onion_addr)

            print(sql)
            cur.execute(sql)
            print(onion_addr + " is alive from process " + str(proc) + time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time())))

        except stem.DescriptorUnavailable:
            sql = 'SELECT check_info,check_times  FROM %s WHERE onion_addr = "%s" '  % (table_name, onion_addr)
            print sql
            cur.execute(sql)
            res = cur.fetchone()
            print res
            new_json = {'check_time':int(time.time()),'status':1,'times':3}
            new_check_info = check_info + json.dumps(new_json)
            sql = 'UPDATE %s set recent_check_time = %s and recent_status  =  1 and alive_times = alive_times + 1' + \
                  ' and check_info = "%s" ' % (table_name, int(time.time()), new_check_info)
            print sql
            print(onion_addr + " is died from process " + str(proc) + time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time())))
        # except Exception,e:
        #     print '------------------------------------'
        #     print("timeout is found " + onion_addr +  str(e) + time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time())))
        #     print ("-----------------------------")
        try:#This place is more important that using the try catch make the timeout come realize and useable,so why
            controller.close()
            conn.commit()
            cur.close()
            conn.close()
        except Exception,e:
            print "excepiton found" + str(e)


conn  = get_connection()
cur = conn.cursor()
# judgeActive('ityukvsoqjgzcimm.onion')
onion_addr  = "ityukvsoqjgzcimm.onion"
sql = 'SELECT check_info,check_times  FROM %s WHERE onion_addr = "%s" '  % (table_name, onion_addr[:16])
print sql
cur.execute(sql)
res = cur.fetchone()
check_info = res[0]
print check_info
if check_info == 'null':
    check_info = ""
    new_check_info = [{'check_time':int(time.time()),'status':1,'times':res[1]}]
else:
    print "new check" 
    print json.loads(check_info)
    
    check_info_list = json.loads(check_info)
    # append({'check_time':int(time.time()),'status':1,'times':res[1]})
    print "after append"
    # new_check_info =  check_info_list  + [{'check_time':int(time.time()),'status':1,'times':res[1]}]

new_check_info_str = json.dumps(new_check_info)
print "the val is " + new_check_info_str
print '\n\n'
sql = 'UPDATE %s SET recent_check_time = %s,recent_status=1, alive_times=alive_times+1,check_info="%s" WHERE onion_addr = "%s" ' % (table_name, int(time.time()), new_check_info, onion_addr[:16])

print(sql)
cur.execute(sql)
conn.commit()
sys.exit(0)

# https://www.blog.pythonlibrary.org/2016/08/02/python-201-a-multiprocessing-tutorial/


def main():
    process_cnt = 5
    #get distinct ip address 
    conn = get_connection()
    cur = conn.cursor()
    i = 0
    time_need_check = int(time.time()) - 86400
    sql = "SELECT count(onion_addr) FROM %s WHERE recent_check_time <= %s" % (table_name, time_need_check)
    cur.execute(sql)
    count = cur.fetchall()[0]
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



# if __name__ == '__main__':
#     sys.exit(main())


