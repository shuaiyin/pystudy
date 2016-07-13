#-*- coding=utf-8 -*- 
import pandas as pd
import sys
from pandas import DataFrame,Series
import numpy as np 
import copy
import csv
csv_path = './ch06/ex1.csv'
content = pd.read_table(csv_path,sep=',')
print content
print type(content)
"""
   a   b   c   d message
0  1   2   3   4   hello
1  5   6   7   8   world
2  9  10  11  12     foo

<class 'pandas.core.frame.DataFrame'>

"""

csv_path2 = './ch06/ex2.csv'
print  pd.read_table(csv_path2,sep=',')
"""
   1   2   3   4  hello
0  5   6   7   8  world
1  9  10  11  12    foo
"""

print pd.read_csv(csv_path2,header=None)

"""
   0   1   2   3      4
0  1   2   3   4  hello
1  5   6   7   8  world
2  9  10  11  12    foo
"""

print pd.read_csv(csv_path2,names=['a','b','c','d','message'])
"""
   a   b   c   d message
0  1   2   3   4   hello
1  5   6   7   8   world
2  9  10  11  12     foo
"""

names = ['a','b','c','d','message']
print pd.read_csv(csv_path2,names=names,index_col='message')
"""
         a   b   c   d
message               
hello    1   2   3   4
world    5   6   7   8
foo      9  10  11  12
"""

path_minindex = './ch06/csv_mindex.csv'
parsed = pd.read_csv(path_minindex,index_col=['key1','key2'])
print parsed
"""
key1 key2                
one  a          1       2
     b          3       4
     c          5       6
     d          7       8
two  a          9      10
     b         11      12
     c         13      14
     d         15      16
"""


print '---------'
ex3_path = './ch06/ex3.txt'
info = list(open(ex3_path))
print info
""""
['            A         B         C\n',
 'aaa -0.264438 -1.026059 -0.619500\n',
 'bbb  0.927272  0.302904 -0.032399\n',
 'ccc -0.264273 -0.386314 -0.217601\n',
 'ddd -0.871858 -0.348382  1.100491\n']
 说明：这个文件由数量不定的空白符分隔，虽然可以手工进行调整，但是还是处理下比较好！！ USING regex \s+
"""

result = pd.read_table(ex3_path,sep='\s+')
print result
"""
            A         B         C
aaa -0.264438 -1.026059 -0.619500
bbb  0.927272  0.302904 -0.032399
ccc -0.264273 -0.386314 -0.217601
ddd -0.871858 -0.348382  1.100491
"""


ex4_path = './ch06/ex4.csv'
print pd.read_table(ex4_path,skiprows=[0,2,3])
"""
  a,b,c,d,message
0   1,2,3,4,hello
1   5,6,7,8,world
2  9,10,11,12,foo
"""

ex5_path = './ch06/ex5.csv'
result = pd.read_csv(ex5_path)
print result 
print type(result)

"""
  something  a   b     c   d message
0       one  1   2   3.0   4     NaN
1       two  5   6   NaN   8   world
2     three  9  10  11.0  12     foo
<class 'pandas.core.frame.DataFrame'>

"""
print pd.isnull(result)
"""
  something      a      b      c      d message
0     False  False  False  False  False    True
1     False  False  False   True  False   False
2     False  False  False  False  False   False
"""


##### read files by block  
ex6_path = './ch06/ex6.csv'
result = pd.read_csv(ex6_path)
print result 
print len(result)
"""
           one       two     three      four key
0     0.467976 -0.038649 -0.295344 -1.824726   L
1    -0.358893  1.404453  0.704965 -0.200638   B
2    -0.501840  0.659254 -0.421691 -0.057688   G
3     0.204886  1.074134  1.388361 -0.982404   R
4     0.354628 -0.133116  0.283763 -0.837063   Q
5     1.817480  0.742273  0.419395 -2.251035   Q
6    -0.776764  0.935518 -0.332872 -1.875641   U
7    -0.913135  1.530624 -0.572657  0.477252   K

10000 the length of the DataFrame is 10000  !!
........
read all data from the file  
"""
##just read some rows  
print pd.read_csv(ex6_path,nrows=6)
"""
        one       two     three      four key
0  0.467976 -0.038649 -0.295344 -1.824726   L
1 -0.358893  1.404453  0.704965 -0.200638   B
2 -0.501840  0.659254 -0.421691 -0.057688   G
3  0.204886  1.074134  1.388361 -0.982404   R
4  0.354628 -0.133116  0.283763 -0.837063   Q
5  1.817480  0.742273  0.419395 -2.251035   Q
"""
##just read some chunk  设置每个读取的chunk有1000行数据
chunker = pd.read_csv(ex6_path,chunksize=1000)
# chunker_bak = copy.deepcopy(chunker)

print '----------'
print chunker #<pandas.io.parsers.TextFileReader object at 0x35d6ed0>  it return a handler 
###test area 
for piece in chunker:
	print len(piece)
	print type(piece)
	print piece
"""
1000
<class 'pandas.core.frame.DataFrame'>
          one       two     three      four key
0    0.467976 -0.038649 -0.295344 -1.824726   7
1   -0.358893  1.404453  0.704965 -0.200638   W
2   -0.501840  0.659254 -0.421691 -0.057688   C
3    0.204886  1.074134  1.388361 -0.982404   S
4    0.354628 -0.133116  0.283763 -0.837063   H
..        ...       ...       ...       ...  ..
993  1.821117  0.416445  0.173874  0.505118   W
994  0.068804  1.322759  0.802346  0.223618   S
995  2.311896 -0.417070 -1.409599 -0.515821   W
996 -0.479893 -0.650419  0.745152 -0.646038   N
997  0.523331  0.787112  0.486066  1.093156   Q
998 -0.362559  0.598894 -1.843201  0.887292   R
999 -0.096376 -1.012999 -0.657431 -0.573315   M
[1000 rows x 5 columns]

.....

1000
<class 'pandas.core.frame.DataFrame'>
          one       two     three      four key
0    0.467976 -0.038649 -0.295344 -1.824726   7
1   -0.358893  1.404453  0.704965 -0.200638   W
2   -0.501840  0.659254 -0.421691 -0.057688   C
3    0.204886  1.074134  1.388361 -0.982404   S
4    0.354628 -0.133116  0.283763 -0.837063   H
..        ...       ...       ...       ...  ..
993  1.821117  0.416445  0.173874  0.505118   W
994  0.068804  1.322759  0.802346  0.223618   S
995  2.311896 -0.417070 -1.409599 -0.515821   W
996 -0.479893 -0.650419  0.745152 -0.646038   N
997  0.523331  0.787112  0.486066  1.093156   Q
998 -0.362559  0.598894 -1.843201  0.887292   R
999 -0.096376 -1.012999 -0.657431 -0.573315   M
[1000 rows x 5 columns]

##其实通过设置chunksize可以控制每次只是加载设定的行数(save memory)
after setting chunksize in read_csv,it will read one piece(setting 1000 rows) from chunk handler  each  time ,and construct a DataFrame
"""

###还是看看这个chunk里面有什么
print '--------'
# print chunker_bak
for piece in chunker:
	print 'dd'
print '====='
"""
and in this place it will print nothing,for that the chunker is a file handler,and after iteration, it will at the end of the file, and it is can not use 
so recreate TextFileReaderHandler
"""



chunker = pd.read_csv(ex6_path,chunksize=1000)
for piece in chunker:
	print type(piece)
	print type(piece['key'])
	print piece['key'].value_counts()
"""
<class 'pandas.core.frame.DataFrame'>
<class 'pandas.core.series.Series'>
J    42
M    40
E    39
.......
5    13
3    13
1    12


<class 'pandas.core.frame.DataFrame'>
<class 'pandas.core.series.Series'>
E    54
Q    42
L    40
H    39
.....
U    33
N    33
Z    31

..........

对每个piece(1000rows)的key的Series做value_count

"""

######################测试一下Series 的add function 
print '----------just test '
test_se = Series([])
a_se = Series(np.arange(5),index=['one','two','three','four','five'])
b_se = Series(np.arange(5),index=['one','three','four','five','six'])
print a_se
print b_se

test_se = test_se.add(a_se,fill_value=0) #after add it won't change the ori value, it will create a new value in new memory 
##using fill_value= 0 or it will not not add the data in a_se,and the value will be NaN
test_se = test_se.add(b_se,fill_value=0)
print test_se
print test_se.sort_values(ascending=False)

"""
one      0
two      1
three    2
four     3
five     4
dtype: int64

one      0
three    1
four     2
five     3
six      4
dtype: int64


## the add method of the Series will conbine the data using the index 
five     7.0
four     5.0
one      0.0
six      4.0
three    3.0
two      1.0
dtype: float64

#after sort by value 
five     7.0
four     5.0
six      4.0
three    3.0
two      1.0
one      0.0
dtype: float64

"""



chunker = pd.read_csv(ex6_path,chunksize=1000)
tot = Series([])
for piece in chunker:
	tot = tot.add(piece['key'].value_counts(),fill_value=0)
print tot # Series([], dtype: object)
print len(tot)
"""
0    151.0
1    146.0
2    152.0
3    162.0
.......
W    305.0
X    364.0
Y    314.0
Z    288.0
dtype: float64
"""

tot = tot.sort_values(ascending=False)
print tot
"""
sort by values  !!!
E    368.0
X    364.0
L    346.0
O    343.0
Q    340.0
M    338.0
......
3    162.0
5    157.0
2    152.0
0    151.0
9    150.0
1    146.0
dtype: float64

"""

####将数据写出到文本格式
data = pd.read_csv(ex5_path)
print data
"""
  something  a   b     c   d message
0       one  1   2   3.0   4     NaN
1       two  5   6   NaN   8   world
2     three  9  10  11.0  12     foo
"""
data.to_csv('ch06/out.csv')
"""
下面是文件的内容
,something,a,b,c,d,message
0,one,1,2,3.0,4,
1,two,5,6,,8,world
2,three,9,10,11.0,12,foo
"""

data.to_csv('ch06/out.csv',sep='|')
"""
##you can set different seperate way !!!!this is the content of file out.csv
|something|a|b|c|d|message
0|one|1|2|3.0|4|
1|two|5|6||8|world
2|three|9|10|11.0|12|foo
"""


print data.to_csv(sys.stdout,na_rep='NULL')
"""
yinshuai: the standard output mod is different to the file save mode !! if you set na_rep(NAN replace),the NAN will show as what you want !!
and the default is replace NAN with null str('') 

,something,a,b,c,d,message
0,one,1,2,3.0,4,NULL
1,two,5,6,NULL,8,world
2,three,9,10,11.0,12,foo
None
"""
print data.to_csv(sys.stdout,index=False,header=False)
"""
yinshuai: if set nothing in method to_csv of DataFrame,it will print out all data,include index and header, so if you do not want it ,do index=False AND header=False

one,1,2,3.0,4,
two,5,6,,8,world
three,9,10,11.0,12,foo
None
"""


##当然如果你只是向要写出一部分列，并以你指定的顺序排序
print type(data)
print data.to_csv(sys.stdout,index=False,cols=['a','b','c'])

"""
<class 'pandas.core.frame.DataFrame'>
这里其实说好了是如果设置了cols 的话，那么将只显示a b c 列 但是实际上却没有出来这个效果
something,a,b,c,d,message
one,1,2,3.0,4,
two,5,6,,8,world
three,9,10,11.0,12,foo
None
"""


##上面都是DataFrame的to_csv方法，Series也有一个
dates = pd.date_range('1/1/2000',periods=7)
print dates
print type(dates)
"""
DatetimeIndex(['2000-01-01', '2000-01-02', '2000-01-03', '2000-01-04',
               '2000-01-05', '2000-01-06', '2000-01-07'],
              dtype='datetime64[ns]', freq='D')
<class 'pandas.tseries.index.DatetimeIndex'>
"""
ts = Series(np.arange(7),index=dates)
print ts 
"""
2000-01-01    0
2000-01-02    1
2000-01-03    2
2000-01-04    3
2000-01-05    4
2000-01-06    5
2000-01-07    6
Freq: D, dtype: int64
"""

ts.to_csv('ch06/out.csv')
"""
this is the content of file out.csv
2000-01-01,0
2000-01-02,1
2000-01-03,2
2000-01-04,3
2000-01-05,4
2000-01-06,5
2000-01-07,6
"""
#既然写入的时候是Series那么我们读出的时候人家可就不认为是Series了
print pd.read_csv('ch06/out.csv')
"""
yinshuai: appearly, this is not the result we want to say,if we want the result ,we should get rid of header row ,and use the first columns as index,
but there is a more easy way !!!

   2000-01-01  0
0  2000-01-02  1
1  2000-01-03  2
2  2000-01-04  3
3  2000-01-05  4
4  2000-01-06  5
5  2000-01-07  6

"""

print Series.from_csv('ch06/out.csv',parse_dates=True)
"""
yinshuai:when using the from_csv method of Series,and set the parse_dates option, then it will show the data like follows,this method if friendly to the time Series

2000-01-01    0
2000-01-02    1
2000-01-03    2
2000-01-04    3
2000-01-05    4
2000-01-06    5
2000-01-07    6
dtype: int64

"""


###手工处理分割符格式
"""
yinshuai: the follow is the content of ex7.csv
"a","b","c"
"1","2","3"
"1","2","3","4"
"""
print pd.read_table('ch06/ex7.csv')
"""
       a,"b","c"
0      1,"2","3"
1  1,"2","3","4"
yinshuai: when i use pd.read_csv,it turn out exception, for that the data format in ex7.csv if not rugular !!
when using pd.read_table it all show the content we do not want !!!
"""

"""

"""
f =  open('ch06/ex7.csv')
print f 
"""
<open file 'ch06/ex7.csv', mode 'r' at 0x3615930>
"""

reader = csv.reader(f)
print reader
for line in reader:
  print line 
"""
yinshuai: do iterates over the reader handler,it will create a data tuple(but the result seems not ) for each line (get rid of the "")
<_csv.reader object at 0x2444600>
['a', 'b', 'c']
['1', '2', '3']
['1', '2', '3', '4']

"""


"""
Now, in order to make the format of the data satisfy command! you should do some operation 
"""
line = list(csv.reader(open('ch06/ex7.csv')))
print line
"""
[['a', 'b', 'c'], ['1', '2', '3'], ['1', '2', '3', '4']]

"""
header,values  = lines[0],lines[1:]
data_dict = {h:v fopr h,v }

#p182