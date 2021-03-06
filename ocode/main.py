# -*- coding: utf-8 -*-
import os 
import time 
import datetime 
import sys 

import numpy as np
# import matplotlib.pyplot as plt
from pylab import *
from matplotlib.font_manager import FontProperties
font = FontProperties(fname = "/usr/share/fonts/truetype/arphic/ukai.ttc", size=14)

import MySQLdb

#four fields  pk,ip getdatetime,getstamp,onion_addr
'''
create database onion_resp;
create table onion(
	id int unsigned auto_increment primary key ,
	ip char(16) not null default '',
	ip_class char(1) not null default '',
	getdatetime char(19) not null default '',
	getstamp int(11),
	onion_addr char(16)
)engine=innodb;

'''

cnames = {
'aliceblue':            '#F0F8FF',
'antiquewhite':         '#FAEBD7',
'aqua':                 '#00FFFF',
'aquamarine':           '#7FFFD4',
'azure':                '#F0FFFF',
'beige':                '#F5F5DC',
'bisque':               '#FFE4C4',
'black':                '#000000',
'blanchedalmond':       '#FFEBCD',
'blue':                 '#0000FF',
'blueviolet':           '#8A2BE2',
'brown':                '#A52A2A',
'burlywood':            '#DEB887',
'cadetblue':            '#5F9EA0',
'chartreuse':           '#7FFF00',
'chocolate':            '#D2691E',
'coral':                '#FF7F50',
'cornflowerblue':       '#6495ED',
'cornsilk':             '#FFF8DC',
'crimson':              '#DC143C',
'cyan':                 '#00FFFF',
'darkblue':             '#00008B',
'darkcyan':             '#008B8B',
'darkgoldenrod':        '#B8860B',
'darkgray':             '#A9A9A9',
'darkgreen':            '#006400',
'darkkhaki':            '#BDB76B',
'darkmagenta':          '#8B008B',
'darkolivegreen':       '#556B2F',
'darkorange':           '#FF8C00',
'darkorchid':           '#9932CC',
'darkred':              '#8B0000',
'darksalmon':           '#E9967A',
'darkseagreen':         '#8FBC8F',
'darkslateblue':        '#483D8B',
'darkslategray':        '#2F4F4F',
'darkturquoise':        '#00CED1',
'darkviolet':           '#9400D3',
'deeppink':             '#FF1493',
'deepskyblue':          '#00BFFF',
'dimgray':              '#696969',
'dodgerblue':           '#1E90FF',
'firebrick':            '#B22222',
'floralwhite':          '#FFFAF0',
'forestgreen':          '#228B22',
'fuchsia':              '#FF00FF',
'gainsboro':            '#DCDCDC',
'ghostwhite':           '#F8F8FF',
'gold':                 '#FFD700',
'goldenrod':            '#DAA520',
'gray':                 '#808080',
'green':                '#008000',
'greenyellow':          '#ADFF2F',
'honeydew':             '#F0FFF0',
'hotpink':              '#FF69B4',
'indianred':            '#CD5C5C',
'indigo':               '#4B0082',
'ivory':                '#FFFFF0',
'khaki':                '#F0E68C',
'lavender':             '#E6E6FA',
'lavenderblush':        '#FFF0F5',
'lawngreen':            '#7CFC00',
'lemonchiffon':         '#FFFACD',
'lightblue':            '#ADD8E6',
'lightcoral':           '#F08080',
'lightcyan':            '#E0FFFF',
'lightgoldenrodyellow': '#FAFAD2',
'lightgreen':           '#90EE90',
'lightgray':            '#D3D3D3',
'lightpink':            '#FFB6C1',
'lightsalmon':          '#FFA07A',
'lightseagreen':        '#20B2AA',
'lightskyblue':         '#87CEFA',
'lightslategray':       '#778899',
'lightsteelblue':       '#B0C4DE',
'lightyellow':          '#FFFFE0',
'lime':                 '#00FF00',
'limegreen':            '#32CD32',
'linen':                '#FAF0E6',
'magenta':              '#FF00FF',
'maroon':               '#800000',
'mediumaquamarine':     '#66CDAA',
'mediumblue':           '#0000CD',
'mediumorchid':         '#BA55D3',
'mediumpurple':         '#9370DB',
'mediumseagreen':       '#3CB371',
'mediumslateblue':      '#7B68EE',
'mediumspringgreen':    '#00FA9A',
'mediumturquoise':      '#48D1CC',
'mediumvioletred':      '#C71585',
'midnightblue':         '#191970',
'mintcream':            '#F5FFFA',
'mistyrose':            '#FFE4E1',
'moccasin':             '#FFE4B5',
'navajowhite':          '#FFDEAD',
'navy':                 '#000080',
'oldlace':              '#FDF5E6',
'olive':                '#808000',
'olivedrab':            '#6B8E23',
'orange':               '#FFA500',
'orangered':            '#FF4500',
'orchid':               '#DA70D6',
'palegoldenrod':        '#EEE8AA',
'palegreen':            '#98FB98',
'paleturquoise':        '#AFEEEE',
'palevioletred':        '#DB7093',
'papayawhip':           '#FFEFD5',
'peachpuff':            '#FFDAB9',
'peru':                 '#CD853F',
'pink':                 '#FFC0CB',
'plum':                 '#DDA0DD',
'powderblue':           '#B0E0E6',
'purple':               '#800080',
'red':                  '#FF0000',
'rosybrown':            '#BC8F8F',
'royalblue':            '#4169E1',
'saddlebrown':          '#8B4513',
'salmon':               '#FA8072',
'sandybrown':           '#FAA460',
'seagreen':             '#2E8B57',
'seashell':             '#FFF5EE',
'sienna':               '#A0522D',
'silver':               '#C0C0C0',
'skyblue':              '#87CEEB',
'slateblue':            '#6A5ACD',
'slategray':            '#708090',
'snow':                 '#FFFAFA',
'springgreen':          '#00FF7F',
'steelblue':            '#4682B4',
'tan':                  '#D2B48C',
'teal':                 '#008080',
'thistle':              '#D8BFD8',
'tomato':               '#FF6347',
'turquoise':            '#40E0D0',
'violet':               '#EE82EE',
'wheat':                '#F5DEB3',
'white':                '#FFFFFF',
'whitesmoke':           '#F5F5F5',
'yellow':               '#FFFF00',
'yellowgreen':          '#9ACD32'}


def date_to_stamp(date_str):
    return int(time.mktime(time.strptime(date_str,'%Y-%m-%d %H:%M:%S')))


def stamp_to_Ymd(stamp):
	return datetime.datetime.fromtimestamp(stamp)#return datetime object


def choose_some_color(cnames,count):
	color_list = [] 
	for color in cnames:
		if len(color_list) <= count:
			color_list.append(color)
	return color_list

def draw_pic(figsizex,figsizey,draw_dict,color_count,ylimt_bot,ylim_top,title="this is the title",xlabel="this is xlabel",ylabel="this is y label"
	,fontproperties=font,fontsize=20):
	print draw_dict
	plt.figure(figsize=(figsizex,figsizey))
	x = draw_dict['xval']
	color_list = choose_some_color(cnames,color_count)
	color_num = 0
	print "the length of xval is " + str(len(draw_dict['xval']))
	for key in draw_dict:
		print "the length of y is " + str(len(draw_dict[key]))
		if key == 'xval': continue
		linewidth = 4 if key in ('totalStatistic','totalDistinctStatistic') else 2
		y = draw_dict[key]
		print y
		plt.gcf().autofmt_xdate()#make x datetime show beautiful
		try:
			plt.plot(x,y,color=color_list[color_num],label=key,linewidth=linewidth)
		except Exception,e:
			print e

		color_num += 1 
	plt.ylim(ylimt_bot,ylim_top)#set the limit of y xlia 
	plt.legend(loc="top left",shadow=True)#set the tuli 
	# plt.rcParams['font.sans-serif'] = ['SimHei'] #指定默认字体
	plt.title(title)
	plt.xlabel(xlabel,fontproperties=font,fontsize=fontsize)
	plt.ylabel(ylabel,fontproperties=font,fontsize=fontsize)

	# plt.savefig("./a.png")
	plt.show()




ONION_DIR_PATH = '/home/yinshuai/onion0428/'
NEED_INIT_MYSQL_DATA = False#judge if need reinit the data,default not use,but if you add new onon data.you should reinit the data in db 
DATA_DRAW = 7#control data draw with default value 0  
STAT_START_TIME = "2017-02-01 00:00:00"#start time to statistic
STAT_END_TIME  = "2017-04-27 00:00:00"#end time to statistic 




conn= MySQLdb.connect(
        host='localhost',
        port = 3306,
        user='root',
        passwd='111111',
        db ='onion_resp',
        )

cur = conn.cursor()

if NEED_INIT_MYSQL_DATA:
	cur.execute("DROP TABLE IF EXISTS ONION")
	creat_table = """
		CREATE TABLE If Not Exists ONION(
		id int unsigned auto_increment primary key ,
		ip char(16) not null default '',
		ip_class char(1) not null default '',
		getdatetime char(19) not null default '',
		getstamp int(11),
		onion_addr char(16),
		KEY `sindex` (`ip`,`ip_class`,`onion_addr`)
	)engine=innodb"""
	cur.execute(creat_table)
	for ip_dir in os.listdir(ONION_DIR_PATH):
		ip_dir_full = ONION_DIR_PATH + ip_dir
		if os.path.isdir(ip_dir_full):
			ip = ip_dir#ipfield 
			ip_class_path = os.listdir(ip_dir_full)
			for ip_class_sub in ip_class_path:
				if os.path.isdir(ip_dir_full + '/' + ip_class_sub):
					date_dir_list = os.listdir(ip_dir_full + '/' + ip_class_sub)
					for date_dir in date_dir_list:#date_dir such as 2015-02 
						onion_file_dir = os.listdir(ip_dir_full + '/' + ip_class_sub + '/' + date_dir)
						onion_file_dir =  sorted(onion_file_dir)
						for onion_file in onion_file_dir:
							onion_set = set() #only contain one day onion addr
							onion_resp_today = []
							ip_class = ''
							ip_class = 'A' if ip_class_sub == 'onion_dir' else 'B'#ip_class filed 
							onion_file_path = ip_dir_full + '/' + ip_class_sub + '/' + date_dir + '/' + onion_file
							for onion_line in open(onion_file_path,'r').readlines():
								onion_line_data = onion_line.split('\t')
								getdatetime = onion_line_data[0]
								try:
									getstamp = date_to_stamp(getdatetime)
								except:
									print onion_file_path + onion_line 
									break
								onion_addr = onion_line_data[2][:-1]
								if onion_addr not in  onion_set:
									onion_line_insert = [ip,ip_class,getdatetime,getstamp,onion_addr]
									onion_resp_today.append(onion_line_insert)
									onion_set.add(onion_addr)
							today_onion_len = len(onion_set)
							if today_onion_len < 6: continue
							cur.executemany("insert into ONION (ip,ip_class,getdatetime,getstamp,onion_addr) \
								              values(%s,%s,%s,%s,%s)",onion_resp_today)
	                		conn.commit()#if do not add you cant commmit 


	#filter some extra data 
	cur.execute('select * from ONION')
	data_resp = cur.fetchall()
	for row in data_resp:
		ip = row[1]
		ip_class = row[2]
		timestamp = row[4]
		onion_addr = row[5]  
		expire_timestamp = int(timestamp) + 24*3600
		sql = "delete from ONION where ip='%s' and ip_class='%s' and  onion_addr = '%s' and getstamp > %s and getstamp < %s"\
					% (ip,ip_class,onion_addr,timestamp,expire_timestamp)
		count = cur.execute(sql)
		conn.commit()###must have this sentense,or it will not execute 



###get distinct ip address 
cur.execute("select distinct(ip) from ONION")
ip_list = cur.fetchall()
#start from 0201 
start_datetime = STAT_START_TIME
start_timestamp = date_to_stamp(start_datetime)
end_datetime = STAT_END_TIME
end_timestamp = date_to_stamp(end_datetime)
temp_timestamp = start_timestamp
stat_data = {}#such as {'125.25.2.6.A':[1250,1560,2015,2500],'125.25.2.6.B':[1000,1500,2000,2500]}
while temp_timestamp < end_timestamp:
	temp_timestamp = temp_timestamp + 24 * 3600#temp same as end static_time 
	stat_data.setdefault('xval',[])
	stat_data['xval'].append(stamp_to_Ymd(temp_timestamp))
	#sum num
	sql = "select count(*) from ONION where getstamp <%s" % (temp_timestamp)
	stat_data.setdefault('totalStatistic',[])
	cur.execute(sql)
	sum_num = cur.fetchone()[0]
	stat_data['totalStatistic'].append(sum_num)
	#distinct sum num 
	sql = "select count(distinct onion_addr) from ONION where getstamp<%s" % (temp_timestamp)
	stat_data.setdefault('totalDistinctStatistic',[])
	cur.execute(sql)
	stat_data['totalDistinctStatistic'].append(cur.fetchone()[0])

	for ip in ip_list:
		sql = "select count(*) from ONION where ip='%s' and ip_class='%s' and getstamp<%s" % (ip[0],'A',temp_timestamp)
		cur.execute(sql)
		stat_data.setdefault(ip[0] + 'A',[])
		stat_data[ip[0] + 'A'].append(cur.fetchone()[0])
		sql = "select count(*) from ONION where ip='%s' and ip_class='%s' and getstamp<%s" % (ip[0],'B',temp_timestamp)
		cur.execute(sql)
		stat_data.setdefault(ip[0] + 'B',[])
		stat_data[ip[0] + 'B'].append(cur.fetchone()[0])

		##this position we add a new param,which is used as calculate the distinct count of each node 
		sql = "select count(distinct(onion_addr)) from ONION where ip='%s' and ip_class='%s' and getstamp<%s" % (ip[0],'A',temp_timestamp)
		cur.execute(sql)
		stat_data.setdefault('distinct:' + ip[0] + 'A',[])##
		stat_data['distinct:' + ip[0] + 'A'].append(cur.fetchone()[0])
		sql = "select count(distinct(onion_addr)) from ONION where ip='%s' and ip_class='%s' and getstamp<%s" % (ip[0],'B',temp_timestamp)
		cur.execute(sql)
		stat_data.setdefault('distinct:' + ip[0] + 'B',[])##
		stat_data['distinct:' + ip[0] + 'B'].append(cur.fetchone()[0])
		


###FINALLY close the handler 
conn.close()

"""
data_sample 
key  value[]
47.88.22.116B [0L, 0L, 0L, 0L, 0L, 0L, 0L, 0L, 0L, 0L, 74L, 154L, 237L, 330L, 409L, 504L, 570L, 659L, 769L, 868L, 974L, 1059L, 1146L, 1235L, 1333L]
"""
"""
for key in stat_data:
	print key,stat_data[key]
"""
# print 'ddd'
if DATA_DRAW == 1:#draw pic use all data 
	draw_pic(100,200,stat_data,21,2000,10000)
elif DATA_DRAW == 2:#draw pic use all data except for totalStatistic and totalDistinctStatistic 
	del stat_data['totalDistinctStatistic']
	del stat_data['totalStatistic']
	draw_pic(100,200,stat_data,21,100,8000)

elif DATA_DRAW == 3:#draw pic use just totalStatistic and totalDistinctStatistic    important 
	stat_data_new = {}
	stat_data_new['totalStatistic'] = stat_data['totalStatistic']
	stat_data_new['totalDistinctStatistic'] = stat_data['totalDistinctStatistic']
	stat_data_new['xval'] = stat_data['xval']
	draw_pic(100,200,stat_data_new,21,5000,238000,title=u"洋葱地址总数统计图",ylabel="Onion address count",xlabel="Datetime")#ylim from 5000 to 50000 

elif DATA_DRAW == 4:#draw all data simple from some ip .  important 
	draw_data = {}
	draw_data['xval'] = stat_data['xval']
	draw_data['NodeA'] = stat_data['47.88.18.218A']
	draw_data['NodeB'] = stat_data['47.88.18.218B']
	draw_data['NodeC'] = stat_data['47.88.12.14A']
	draw_data['NodeD'] = stat_data['47.88.12.14B']
	draw_pic(100,200,draw_data,21,100,12000,title="Total onion address of seperate inject node",xlabel="Datetime",ylabel="Onion address count")

elif DATA_DRAW == 5:#draw difference of total (distinct) for each day 
	stat_data_new = {}
	stat_data_new['Difference'] = []
	statLen = len(stat_data['totalStatistic'])
	for index in xrange(statLen):
		stat_data_new['Difference'].append(stat_data['totalStatistic'][index] - stat_data['totalDistinctStatistic'][index])
	stat_data_new['xval'] = stat_data['xval']
	draw_pic(100,200,stat_data_new,21,0,90000,title="The Difference between origin onion address and distinct onion address", \
			 xlabel="Datetime",ylabel="Onion address count")

elif DATA_DRAW == 6:
	stat_data_new = {}
	stat_data_new['47.88.12.14A'] = stat_data['47.88.12.14A']
	stat_data_new['distinct:47.88.12.14A'] = stat_data['distinct:47.88.12.14A']
	stat_data_new['xval'] = stat_data['xval']
	draw_pic(100,200,stat_data_new,21,1000,5000,title="(Distinct) Total onion address plot",ylabel="Onion address count",xlabel="Datetime")#ylim from 5000 to 50000 

elif DATA_DRAW == 7: #the average sum ??
	stat_data_new = {}
	##less one day 
	stat_data_new['totalIncreEachDay'] = []
	stat_data_new['unqiueIncreEachDay'] = []
	stat_data_new['diffIncreEachDay'] = []

	for index in xrange(1,len(stat_data['totalStatistic'])-4):
		stat_data_new['totalIncreEachDay'].append(stat_data['totalStatistic'][index] - stat_data['totalStatistic'][index - 1])
		stat_data_new['unqiueIncreEachDay'].append(stat_data['totalDistinctStatistic'][index] - stat_data['totalDistinctStatistic'][index-1])
		# stat_data_new['diffIncreEachDay'].append(stat_data_new['totalIncreEachDay'][index] - stat_data_new['unqiueIncreEachDay'])
	
	for index in xrange(0,len(stat_data_new['totalIncreEachDay'])):
		stat_data_new['diffIncreEachDay'].append(stat_data_new['totalIncreEachDay'][index] - stat_data_new['unqiueIncreEachDay'][index])

	stat_data_new['xval'] = stat_data['xval'][1:-4]
	draw_pic(100,200,stat_data_new,21,0,6000,title="Daily onion address increment graph", \
			 xlabel="Datetime",ylabel="Onion address count")	

# elif DATA_DRAW == 7:
# 	stat_data_new = {}
# 	# stat_data_new['subval'] = []
# 	stat_data['totalDistinctStatistic'] = [6096L, 7553L, 9169L, 10656L, 12352L, 13878L, 15252L, 16499L, 17985L, 19394L, 21054L, 22918L, 24627L, 26549L, 28441L, 30420L, 32265L, 34016L, 35772L, 37523L, 39307L, 41118L, 42778L, 44620L, 46495L, 48187L, 49958L, 51947L, 53543L, 55081L, 56524L, 57968L, 59658L, 61395L, 62915L, 64424L, 65891L, 67361L, 68745L, 70415L, 71805L, 73097L, 74492L, 75744L, 76927L, 84225L, 88015L, 89198L, 90432L, 92171L, 93242L, 94427L, 95639L, 100198L, 101408L, 102503L, 103642L, 104779L, 106020L, 107376L, 108627L, 109872L, 111289L, 112653L, 113941L, 115170L, 116282L, 117707L, 118847L, 120731L, 122124L, 123590L, 124767L, 126281L, 127664L, 128992L, 130435L, 131773L, 132855L, 133856L, 134847L, 135957L, 137042L, 137884L, 138639L, 139307L]

# 	stat_data['totalStatistic'] = [6304L, 7877L, 9634L, 11281L, 13198L, 14913L, 16487L, 17937L, 19700L, 21405L, 23437L, 25711L,
# 	 27886L, 30374L, 32905L, 35494L, 38019L, 40456L, 42961L, 45530L, 48169L, 50858L, 53439L, 56318L, 59220L, 61889L, 64689L, 67623L, 70239L, 72755L, 75139L, 77530L, 80407L, 83385L, 86095L, 88721L, 91463L, 94259L, 96869L, 99857L, 102524L, 104998L, 107763L, 110252L, 112650L, 121174L, 126161L, 128454L, 130730L, 133612L, 135814L, 138272L, 140603L, 146455L, 149036L, 151317L, 153737L, 156104L, 158621L, 161225L, 163758L, 166442L, 169266L, 172041L, 174697L, 177294L, 179637L, 182439L, 184880L, 188146L, 191173L, 194319L, 196938L, 199847L, 202661L, 205371L, 208246L, 210840L, 213282L, 215578L, 217922L, 220509L, 223070L, 225140L, 226930L, 228646L]

		
	# statLen = len(stat_data['totalStatistic'])
	# for index in xrange(statLen):
	# 	stat_data_new['Difference'].append(stat_data['totalStatistic'][index] - stat_data['totalDistinctStatistic'][index])
	# stat_data_new['xval'] = stat_data['xval']
	# draw_pic(100,200,stat_data_new,21,0,90000,title="The Difference between origin onion address and distinct onion address", \
	# 		 xlabel="Datetime",ylabel="Onion address count")


