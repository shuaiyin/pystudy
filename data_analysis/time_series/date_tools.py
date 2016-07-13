#coding=utf-8
from datetime import datetime
now = datetime.now()
print now 
print now.year,now.month,now.day

"""
2016-07-11 23:57:17.493485
2016 7 11
datetime以毫秒形式存储日期和时间

"""


delta = datetime(2011,1,7) - datetime(2008,6,24,8,15)
print delta
print delta.days
print delta.seconds
"""
datetime.timedelta(926, 56700)  from console
926
56700 (15*3600 +  45 * 60)

926 days, 15:45:00  
# datetime.timedelta 表示两个datetime对象之间的时间差
"""





from datetime import timedelta 
'*****************ex2 start *****************'

start = datetime(2011,1,7)
print start + timedelta(12)
"""
datetime.datetime(2011,1,19,0,0)
"""

'***************ex2 end ********************'










'*****************ex3 start *****************'
"""
字符串和datetime之间的相互转换
利用str或strftime方法(传入一个格式化字符串),datetime对象和pandas的Timestamp对象可以被格式化为字符串

"""
stamp = datetime(2011,1,3)

print stamp #2011-01-03 00:00:00
print type(stamp)#<type 'datetime.datetime'>
print str(stamp) #'2011-01-03 00:00:00'
print stamp.strftime('%Y-%m-%d')#'2011-01-03'


##datetime.strptime也可以用这些格式化编码将字符串转为日期,只有转换为日期之后才可以使用datetime类的各种方法了
value = '2011-01-03'
out_date = datetime.strptime(value,'%Y-%m-%d') #2011-01-03 00:00:00
print type(out_date) #<type 'datetime.datetime'>

datestrs = ['7/6/2011','8/6/2011']
out_date_list = [datetime.strptime(x,'%m/%d/%Y') for x in datestrs]
print out_date_list#[datetime.datetime(2011, 7, 6, 0, 0), datetime.datetime(2011, 8, 6, 0, 0)]
"""
datetime.strptime是通过已知格式进行日期解析的最佳方式。
但是每次都要编写格式定义是很麻烦的事情，尤其对于一些常见的日期格式，那么可以使用下面的包
dateutil can almost parse every date format which man can understand 
"""
from dateutil.parser import parse 
date_result = parse('2011-01-03') ##str to datetime  
print date_result #2011-01-03 00:00:00
print parse('05/06/2016') #2016-05-06 00:00:00
print parse('Jan 31,1997 10:45 PM') #1997-01-31 22:45:00

##在国际通用的格式中，日通常出现在月前面，
print parse('6/12/2011') #2011-06-12 00:00:00
print parse('6/12/2011',dayfirst=True) #2011-12-06 00:00:00




'***************ex3 end ********************'


import pandas as pd 
'***************ex4 start ********************'
datestrs = ['7/6/2011','8/6/2011']
print pd.to_datetime(datestrs) #DatetimeIndex(['2011-07-06', '2011-08-06'], dtype='datetime64[ns]', freq=None)

#to_datetime可以处理缺失值(None,空字符串等)
idx = pd.to_datetime(datestrs + [None])
print idx #DatetimeIndex(['2011-07-06', '2011-08-06', 'NaT'], dtype='datetime64[ns]', freq=None)

print idx[2] #NaT    yinshuai:NaT(Not a Time)是pandas时间戳数据中的NA值
print pd.isnull(idx) #[False False  True]


'***************ex4 end ********************'



















'***************ex5 start ********************'
'***************ex5 end ********************'



'***************ex6 start ********************'
'***************ex6 end ********************'