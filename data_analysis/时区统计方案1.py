# -*-coding:utf-8 -*-

"""
分析的时候使用的数据是time_zone.txt
"""
import json 
import sys

#纯python方式
def get_counts(sequence): 
	"""
	很简单的一种方式，输入为列表，用dict处理数目
	"""
	counts = {}
	for x in sequence:
		if x in counts:
			counts[x] += 1
		else:
			counts[x] = 1 
	return counts

def top_counts(count_dict,n=10):
	"""
	function 获取前10个最多的timezone
	input param: 
			count_dict 

	"""
	value_key_pairs = [(count,tz) for tz,count in count_dict.items()]#将同质字典转换为元组数组便于排序，当然也可以转换为字典数组，但是不这样做
	value_key_pairs.sort()#数组进行排序
	return value_key_pairs[-n:]# 从倒数地n个开始取得数据


if __name__ == '__main__':
	path = './time_zone.txt'
	records = [json.loads(line) for line in open(path)]#一行数据是通过\n来区分的，通过json.loads可以将string to dict ，同样可以使用eval
	time_zones = [info['tz'] for info in records if 'tz' in info]#有的数据是没有tz字段的
	time_zone_static = get_counts(time_zones)#统计出现次数
	print top_counts(time_zone_static)

	



