# -*-coding:utf-8-*-
from collections import defaultdict 
from collections import Counter
import json

def get_counts2(sequence):
	"""这是一种方式"""
	counts = defaultdict(int) #所有的值均会被初始化为0 
	for x in sequence:
		counts[x] += 1 
	return counts

path = './time_zone.txt'
records = [json.loads(line) for line in open(path)]
time_zones = [info['tz'] for info in records if 'tz' in info]
counts = Counter(time_zones)#这是一种更加简单的方式，
print counts.most_common(10)

