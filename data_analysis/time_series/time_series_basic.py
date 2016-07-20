#coding=utf-8
"""
pandas最基本的时间序列类型就是以时间戳(通常以Python字符串或datetime对象表示）为索引的Series
"""

from datetime import datetime 
import numpy as np
from pandas import DataFrame,Series 
import pandas as pd 

'***************ex1 start ********************'
dates = [datetime(2011,1,2),datetime(2011,1,5),datetime(2011,1,7),
		 datetime(2011,1,8),datetime(2011,1,10),datetime(2011,1,12)]
print dates
ts = Series(np.random.randn(6),index=dates)
print ts
print type(ts)
print ts.index
print ts.index.dtype
"""
[datetime.datetime(2011, 1, 2, 0, 0), datetime.datetime(2011, 1, 5, 0, 0), datetime.datetime(2011, 1, 7, 0, 0), 
datetime.datetime(2011, 1, 8, 0, 0), datetime.datetime(2011, 1, 10, 0, 0), datetime.datetime(2011, 1, 12, 0, 0)]

2011-01-02   -0.503800
2011-01-05    1.536077
2011-01-07    0.740233
2011-01-08    0.955738
2011-01-10   -0.495558
2011-01-12    0.797788
dtype: float64

<class 'pandas.core.series.Series'>

DatetimeIndex(['2011-01-02', '2011-01-05', '2011-01-07', '2011-01-08',
               '2011-01-10', '2011-01-12'],
              dtype='datetime64[ns]', freq=None)

datetime64[ns]

yinshuai:这些datetime对象实际上是被放在一个DatetimeIndex中的，现在，变量ts就成为一个TimeSeries了
		 pandas用Numpy的datetime64 数据类型以纳米形式存储时间戳


"""
print ts.index[0] #<Timestamp: 2011-01-02 00:00:00>
print type(ts.index[0]) #<class 'pandas.tslib.Timestamp'>
stamp = ts.index[2]
print stamp #2011-01-07 00:00:00
print ts[stamp] #0.740233
#还可以有一种更为方便的用法： 传入一个可以被解释为日期的字符串
print ts['1/10/2011'] #-0.495558
print ts['20110110'] #-0.495558

"""
yinshuai:只要有需要，TimeStamp 可以随时自动转换为datetime对象。 
"""

'***************ex1 end ********************'


'***************ex2 start ********************'
long_ts  = Series(np.random.randn(1000),index=pd.date_range('1/1/2000',periods=1000))
print long_ts
"""
2000-01-01    1.354106
2000-01-02   -0.182798
2000-01-03    0.337722
2000-01-04    0.682909
2000-01-05    0.276081
....
2002-09-20   -1.873343
2002-09-21    0.223002
2002-09-22    0.234768
2002-09-23   -0.342976
2002-09-24    1.661379
2002-09-25   -0.163396
2002-09-26    0.219868
Freq: D, dtype: float64

"""

'***************ex1 end ********************'
