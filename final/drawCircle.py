#!/usr/bin/env python
#-*- coding: UTF-8 -*
#coding:utf-8 

import json
import sys
path = './heheda.txt'



f=file("./result.txt","a+")

# li=["hello world\n","hello china\n"]
# f.writelines(li)
# f.close()

# def write_line_to_file(file_path,line_content):
# 	f = file(file_path,line_content)
# 	f.writelines(line_content)
# 	f.close


save_key_value = {}

num = 0
for line in open(path,'r'):
	ss = line.strip()
	if num <= 6000:
		line_content = line.split()#the content of the line  return list 
		weight = line_content[0]
		keyword = line_content[1]
		url_click = line_content[2]
		if url_click in save_key_value:
			save_key_value[url_click].append(keyword + "---" + weight)
		else:
			save_key_value.setdefault(url_click,[])
			save_key_value[url_click].append(keyword + "---" + weight)
		num += 1 
	else:
		break


num = 0
new_num = 0
# print save_key_value
for key in save_key_value:
	num += 1
	# print num 
	value = save_key_value[key]
	if len(value) >=2:
		new_num += 1
		url_line = "\nthe url is " + key + "\n" 
		f.writelines(url_line)
		f.writelines(value)
		for v in value:
			print v
		print '----'
print num
print 'new_num is ' + str(new_num)
sys.exit(0)
for key,value in enumerate(save_key_value):
	print key
	print len(value)
