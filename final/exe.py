# -*- coding=utf-8 -*-
from matplotlib  import pyplot 
from pandas import DataFrame,Series
import pandas as pd;import numpy as np 
import json
import sys
path = './SogouQ1.txt'
# path = './test.txt'
a = pd.read_table(path,header=None,names=['click_time','user_id','query_name','page_rank','url_click'],nrows=500)
print a 

# records = [line for line in open(path)]
# print len(records)
# frame = DataFrame(records)

# # records = [line.decode('gbk').ecode('utf-8') for line in open(path)]
# except_num = 0
# output = open(new_path,'w+')
# for line in open(path):
# 	t
# 		new_line = line.decode('gbk').encode('utf-8')
# 		output.write(new_line)
# 		sys.exit(1)
# 	except: 
# 		except_num = except_num + 1

# print 'except num is %s' % (except_num) 

# records = [json.loads(line) for line in open(path)]
