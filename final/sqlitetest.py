import sqlite3 

cx = sqlite3.connect("yin")
cu = cx.cursor()
# cu.execute('create table catalog(id integer primary key, \
# 			pid integer,name varchar(10) UNIQUE)')

cu.execute("insert into catalog values(0,0,'name1')")
cu.execute("insert into catalog values(1,0,'hello')")
cx.commit()

#find 
cu.execute("select * from catalog")
print cu.fetchall()


