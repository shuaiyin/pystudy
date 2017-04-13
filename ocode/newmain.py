# -*- coding: utf-8 -*-
import os 
import time 
import datetime 
import sys 

import numpy as np
# import matplotlib.pyplot as plt
from pylab import *


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

def draw_pic(figsizex,figsizey,draw_dict,color_count,ylimt_bot,ylim_top,title="this is the title",xlabel="this is xlabel",ylabel="this is y label"):
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
	plt.title(title)
	plt.xlabel(xlabel)
	plt.ylabel(ylabel)

	# plt.savefig("./a.png")
	plt.show()


ONION_DIR_PATH = '/home/yinshuai/oresp0310/'
NEED_INIT_MYSQL_DATA = False #judge if need reinit the data,default not use,but if you add new onon data.you should reinit the data in db 
DATA_DRAW = 2#control data draw with default value 0  
STAT_START_TIME = "2017-02-10 00:00:00"#start time to statistic
STAT_END_TIME  = "2017-04-06 00:00:00"#end time to statistic 




conn= MySQLdb.connect(
        host='localhost',
        port = 3306,
        user='root',
        passwd='111111',
        db ='onion_resp',
        )

cur = conn.cursor()




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
 	if DATA_DRAW == 1:
		for ip in ip_list:
			sql = "select count(*) from ONION where ip='%s' and ip_class='%s' and getstamp >=%s and getstamp <  %s" % (ip[0],'A',temp_timestamp,temp_timestamp+24*3600)
			cur.execute(sql)
			stat_data.setdefault(ip[0] + 'A',[])
			stat_data[ip[0] + 'A'].append(cur.fetchone()[0])
			sql = "select count(*) from ONION where ip='%s' and ip_class='%s' and getstamp >= %s and getstamp < %s" % (ip[0],'B',temp_timestamp,temp_timestamp+24*3600)
			cur.execute(sql)
			stat_data.setdefault(ip[0] + 'B',[])
			stat_data[ip[0] + 'B'].append(cur.fetchone()[0])
	elif DATA_DRAW == 2:  
		stat_data.setdefault('AverageOnionGetEachDay',[])
		sql = "select count(*) from ONION  where getstamp >=%s and getstamp <  %s" % (temp_timestamp,temp_timestamp+24*3600)
		cur.execute(sql) 
		onion_count = cur.fetchone()[0]
		sql = "select count(distinct(ip)) from ONION where  getstamp >=%s and getstamp <  %s " % (temp_timestamp,temp_timestamp+24*3600)
		cur.execute(sql)
		ip_count = cur.fetchone()[0]
		node_count = ip_count << 1
		stat_data['AverageOnionGetEachDay'].append(onion_count/node_count)


###FINALLY close the handler 
conn.close()

if DATA_DRAW == 1:#draw pic use all data 
	draw_data= {}
	draw_data['xval']  = stat_data['xval']
	draw_data['NodeA'] = stat_data['47.88.18.218A']
	draw_data['NodeB'] = stat_data['47.88.18.218B']
	draw_data['NodeC'] = stat_data['47.88.12.14A']
	draw_data['NodeD'] = stat_data['47.88.12.14B']
	draw_pic(100,200,draw_data,21,0,500,title="Onion address count get each inject node each day",xlabel="Datetime",ylabel="Onion address count")
elif DATA_DRAW == 2:
	draw_pic(100,200,stat_data,21,50,500,title="Onion address count get each inject node each day",xlabel="Datetime",ylabel="Onion address count")


