# -*- coding=utf-8 -*-
from matplotlib  import pyplot 
from pandas import DataFrame,Series
import pandas as pd;import numpy as np 
import json
import sys
path = './time_zone.txt'
records = [json.loads(line) for line in open(path)]
print records[0]  
"""
{
u'a': u'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.78 Safari/535.11', 
u'c': u'US', 
u'nk': 1, 
u'tz': u'America/New_York', 
u'gr': u'MA', 
u'g': u'A6qOVH', 
u'h': u'wfLQtf', 
u'cy': u'Danvers', 
u'l': u'orofrog', 
u'al': u'en-US,en;q=0.8', 
u'hh': u'1.usa.gov', 
u'r': u'http://www.facebook.com/l/7AQEFzjSi/1.usa.gov/wfLQtf', 
u'u': u'http://www.ncbi.nlm.nih.gov/pubmed/22415991', 
u't': 1331923247, 
u'hc': 1331822918, 
u'll': [42.576698, -70.954903]
}
"""
frame = DataFrame(records)
print frame
tz_counts = frame['tz'].value_counts()
print tz_counts
"""
America/New_York                  1251
                                   521
America/Chicago                    400
America/Los_Angeles                382
America/Denver                     191
......
America/La_Paz                       1
Asia/Nicosia                         1
Europe/Uzhgorod                      1
America/Costa_Rica                   1
America/Montevideo                   1
Name: tz, dtype: int64
这里是统计tz列各个东西出现的次数的
"""
clean_tz = frame['tz'].fillna('Mising')#it wiil fill out the NAN row with Mising ,and return the Series 
print clean_tz
"""

3541    America/Los_Angeles
3542    America/Los_Angeles
3543                 Mising
3544        America/Chicago
3545        America/Chicago
3546    America/Los_Angeles
3547       America/New_York
3548        America/Chicago
3549       Europe/Stockholm
3550       America/New_York
3551                       
3552        America/Chicago
"""


"""
just a little test 
"""
print '-------------------'
print type(clean_tz)
print clean_tz == ''
print type(clean_tz == '')
print clean_tz[0] 

"""
<class 'pandas.core.series.Series'>
0       False
1       False
2       False
3       False
...
3558    False
3559    False
Name: tz, dtype: bool

<class 'pandas.core.series.Series'>
America/New_York


yinshuai:通过这些测试语句，可以清晰的看到，一个DataFrame是由多列Series构成的,可以通过DataFrame中每列的列标题(name)
来选择这一个Series，当然对于所选定的Series来说，其索引所使用的是从0开始编号的auto_increment index
using the index of Series can fetch out the element in Series
"""



print '----------------------------'
clean_tz[clean_tz == ''] = 'Unknown'#yinshuai:the type of clean_tz is Series
print clean_tz
"""
7                   Unknown
8                   Unknown
9                   Unknown
10      America/Los_Angeles
11         America/New_York
12         America/New_York
13                   Mising
14         America/New_York
15           Asia/Hong_Kong
16           Asia/Hong_Kong
17         America/New_York
18           America/Denver
"""

tz_counts = clean_tz.value_counts()
ten_tz_counts = tz_counts[:10]
print ten_tz_counts #
print type(ten_tz_counts) #<class 'pandas.core.series.Series'>
ten_tz_counts.to_csv('./haha.csv')
##write Ser
"""
America/New_York       1251
Unknown                 521  ######
America/Chicago         400
America/Los_Angeles     382
America/Denver          191
Mising                  120 #######
Europe/London            74
Asia/Tokyo               37
Pacific/Honolulu         36
Europe/Madrid            35
Name: tz, dtype: int64

"""
ten_tz_counts.plot(kind='barh',rot=0)



print '---------'
"""
{ "a": "Mozilla\/5.0 (Macintosh; Intel Mac OS X 10_6_8) AppleWebKit\/534.52.7 (KHTML, like Gecko) Version\/5.1.2 Safari\/534.52.7", 
从数据中截取了代理 agent这一列的示例,将这些"agent"字符串中的所有信息都解析出来是很郁闷的工作，但是可以使用python内置的字符串函数和正则表达式事情就好办了
我们可以将这种字符串的第一节（与浏览器大致对应）分离出来，并得到另外一份用户行为摘要
"""
results = Series([x.split()[0] for x in frame.a.dropna()])
print results
"""
0                  Mozilla/5.0
1       GoogleMaps/RochesterNY
2                  Mozilla/4.0
3                  Mozilla/5.0
4                  Mozilla/5.0
....
3435               Mozilla/4.0
3436               Mozilla/5.0
3437    GoogleMaps/RochesterNY
3438            GoogleProducer
3439               Mozilla/4.0
yinshuai:由于有些行数据是没有agent这个字段的，那么直接使用dropna 去掉这行
"""

###now you can do something on Series  
print results.value_counts()[:8]
"""
Mozilla/5.0                 2594
Mozilla/4.0                  601
GoogleMaps/RochesterNY       121
Opera/9.80                    34
TEST_INTERNET_AGENT           24
GoogleProducer                21
Mozilla/6.0                    5
BlackBerry8520/5.0.0.681       4
dtype: int64
"""





"""
{ "a": "Mozilla\/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.2.17) Gecko\/20110420 Firefox\/3.6.17", "c": "US", "nk": 1, "tz": "America\/New_York",
 "gr": "GA", "g": "2rOUYc", "h": "2rOUYc", "l": "bitly", "al": "en-us,en;q=0.5", "hh": "1.usa.gov", "r": "direct", "u": "http:\/\/toxtown.nlm.nih.gov\/index.php", 
 "t": 1331923262, "hc": 1255769846, "cy": "Marietta", "ll": [ 33.953201, -84.517700 ] }
 yinshuai: 现在来判断那些是windows用户做的请求，目前，假定请求当中含有WIndows的为WIndows用户的请球
"""

"""
那么问题来了，frame[frame.a.notnull()]  和 frame.a.dropna() 的区别是啥？ 
frame.a.dropna() only return 'a' column and it only retains the rows which the value in specify column is not NaN and not ' ' 
frame[frame.a.notnull()] will return all columns and it only retains the rows which  the value in specify column is not NaN 

"""
cframe = frame[frame.a.notnull()]
operating_system = np.where(cframe['a'].str.contains('Windows'),'Windows','Not Windows')
print operating_system[:5]
"""
['Windows' 'Not Windows' 'Windows' 'Not Windows' 'Windows']

yinshuai: just show you ... it only rechange the 'a' column
yinshuai:when using the str property method,it will return something like <pandas.core.strings.StringMethods object at 0x1def210 
yinshuai:when using the 'contains' method on strings.StringMethods object,it will return True or false,and maybe the "where method" of numpy is just 
iterate the Series and set different specify value,finaly, it return the modified Series,.
"""

by_tz_os =  cframe.groupby(['tz',operating_system])
"""
<pandas.core.groupby.DataFrameGroupBy object at 0x3ff7190>
这里是分组哦

"""
tz_os_value_count = by_tz_os.size()
print tz_os_value_count
"""
                                Not Windows    245
                                Windows        276
Africa/Cairo                    Windows          3
Africa/Casablanca               Windows          1
Africa/Ceuta                    Windows          2
Africa/Johannesburg             Windows          1
Africa/Lusaka                   Windows          1
America/Anchorage               Not Windows      4
                                Windows          1
America/Caracas                 Windows          1
America/Chicago                 Not Windows    115
                                Windows        285
yinshuai:分组的时候是以tz为基准的!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!P39

"""


print '2.---'
after_unstack =  tz_os_value_count.unstack()
"""
                                Not Windows  Windows
tz                                                  
                                      245.0    276.0
Africa/Cairo                            NaN      3.0
Africa/Casablanca                       NaN      1.0
Africa/Ceuta                            NaN      2.0
Africa/Johannesburg                     NaN      1.0
Africa/Lusaka                           NaN      1.0
America/Anchorage                       4.0      1.0
America/Argentina/Buenos_Aires          1.0      NaN
America/Argentina/Cordoba               NaN      1.0
America/Argentina/Mendoza               NaN      1.0
America/Bogota                          1.0      2.0
America/Caracas                         NaN      1.0
.......
"""


print '3------'
after_fillna = after_unstack.fillna(0)# using 0 to fill the NAN value 
print after_fillna
"""
                                Not Windows  Windows
tz                                                  
                                      245.0    276.0
Africa/Cairo                            0.0      3.0
Africa/Casablanca                       0.0      1.0
Africa/Ceuta                            0.0      2.0
Africa/Johannesburg                     0.0      1.0
Africa/Lusaka                           0.0      1.0
America/Anchorage                       4.0      1.0
America/Argentina/Buenos_Aires          1.0      0.0
America/Argentina/Cordoba               0.0      1.0
America/Argentina/Mendoza               0.0      1.0
America/Bogota                          1.0      2.0
America/Caracas                         0.0      1.0
.....
"""



###########接下来我们选取最常出现的时区，那么我们根据agg_counts中的行数构造了一个渐接索引数组
agg_counts = after_fillna
print agg_counts[:10]
print type(agg_counts)
"""
                                Not Windows  Windows
tz                                                  
                                      245.0    276.0
Africa/Cairo                            0.0      3.0
Africa/Casablanca                       0.0      1.0
Africa/Ceuta                            0.0      2.0
Africa/Johannesburg                     0.0      1.0
Africa/Lusaka                           0.0      1.0
America/Anchorage                       4.0      1.0
America/Argentina/Buenos_Aires          1.0      0.0
America/Argentina/Cordoba               0.0      1.0
America/Argentina/Mendoza               0.0      1.0

<class 'pandas.core.frame.DataFrame'>

"""


print agg_counts.sum(1)[:5]
print type(agg_counts.sum(1)[:5])
"""
tz
                       521.0
Africa/Cairo             3.0
Africa/Casablanca        1.0
Africa/Ceuta             2.0
Africa/Johannesburg      1.0
dtype: float64
<class 'pandas.core.series.Series'>

yinshuai:做sum操作之后是这个效果
"""

##那么我们根据agg_counts中的行数构造了一个渐接索引数组
indexer = agg_counts.sum(1).argsort()
print indexer[:10]
"""
tz
                                  24
Africa/Cairo                      20
Africa/Casablanca                 21
Africa/Ceuta                      92
Africa/Johannesburg               87
Africa/Lusaka                     53
America/Anchorage                 54
America/Argentina/Buenos_Aires    57
America/Argentina/Cordoba         26
America/Argentina/Mendoza         55
dtype: int64
"""


count_subset = agg_counts.take(indexer)[-10:]
print count_subset
print type(count_subset)
"""
                     Not Windows  Windows
tz                                       
America/Sao_Paulo           13.0     20.0
Europe/Madrid               16.0     19.0
Pacific/Honolulu             0.0     36.0
Asia/Tokyo                   2.0     35.0
Europe/London               43.0     31.0
America/Denver             132.0     59.0
America/Los_Angeles        130.0    252.0
America/Chicago            115.0    285.0
                           245.0    276.0
America/New_York           339.0    912.0
<class 'pandas.core.frame.DataFrame'>
"""

##write back 
count_subset.to_csv('./333.csv')
print '----'
print Series.from_csv('./333.csv',parse_dates=True)
# print pd.read_csv(csv_path2,header=None)
