#coding=utf-8
from pandas import DataFrame,Series 
import pandas as pd
df1 = DataFrame({'key':['b','b','a','c','a','a','b'],'data1':range(7)})
df2 = DataFrame({'key':['a','b','d'],'data2':range(3)})

print df1
"""
   data1 key
0      0   b
1      1   b
2      2   a
3      3   c
4      4   a
5      5   a
6      6   b
"""

print df2
"""
   data2 key
0      0   a
1      1   b
2      2   d

"""

print pd.merge(df1,df2)
"""
   data1 key  data2
0      0   b      1
1      1   b      1
2      6   b      1
3      2   a      0
4      4   a      0
5      5   a      0

注意：这里并没有指明用那个列进行链接，如果没有指定,merge就会将重叠列的列名当作键，不过最好显式的指定一下,as follows 
"""

pd.merge(df1,df2,on='key')
"""
   data1 key  data2
0      0   b      1
1      1   b      1
2      6   b      1
3      2   a      0
4      4   a      0
5      5   a      0
"""




"""
如果两个对象的列名不同，也可以分别进行指明
"""
df3 = DataFrame({'lkey':['b','b','a','c','a','a','b'],
				'data1':range(7)})
df4 = DataFrame({'rkey':['a','b','d'],
				'data2':range(3)})
print pd.merge(df3,df4,left_on='lkey',right_on='rkey')
"""
   data1 lkey  data2 rkey
0      0    b      1    b
1      1    b      1    b
2      6    b      1    b
3      2    a      0    a
4      4    a      0    a
5      5    a      0    a
merge有种交和的感觉,the c d in connection is disappear!the default operation of merage is innter! and there are other operation,such as "left","right","outer"
"""

df1 = DataFrame({'key':['b','b','a','c','a','a','b'],'data1':range(7)})
df2 = DataFrame({'key':['a','b','d'],'data2':range(3)})
print pd.merge(df1,df2,how='outer')
"""
   data1 key  data2
0    0.0   b    1.0
1    1.0   b    1.0
2    6.0   b    1.0
3    2.0   a    0.0
4    4.0   a    0.0
5    5.0   a    0.0
6    3.0   c    NaN
7    NaN   d    2.0
"""



"""
多对多的合并操作非常简单，无需额外的工作，如下所示
"""
df1 = DataFrame({'key':['b','b','a','c','a','b'],'data1':range(6)})
df2 = DataFrame({'key':['a','b','a','b','d'],'data2':range(5)})
print df1
"""
   data1 key
0      0   b
1      1   b
2      2   a
3      3   c
4      4   a
5      5   b
"""

print df2
"""
   data2 key
0      0   a
1      1   b
2      2   a
3      3   b
4      4   d
"""

print pd.merge(df1,df2,on='key',how='left')
"""
    data1 key  data2
0       0   b    1.0
1       0   b    3.0
2       1   b    1.0
3       1   b    3.0
4       2   a    0.0
5       2   a    2.0
6       3   c    NaN
7       4   a    0.0
8       4   a    2.0
9       5   b    1.0
10      5   b    3.0
多对多链接产生的是行迪卡尔积，由于左边的DataFrame有3个"b"行，右边有2个，所以最终结果中就有
6个‘b‘行，链接结果只影响出现在结果中的键
"""


print pd.merge(df1,df2,how='inner')
"""
   data1 key  data2
0      0   b      1
1      0   b      3
2      1   b      1
3      1   b      3
4      5   b      1
5      5   b      3
6      2   a      0
7      2   a      2
8      4   a      0
9      4   a      2
"""



"""
根据多个键合并，传入一个由列名组成的列表即可
"""
left = DataFrame({'key1':['foo','foo','bar'],
				  'key2':['one','two','one'],
				  'lval':[1,2,3]})

right = DataFrame({'key1':['foo','foo','bar','bar'],
				   'key2':['one','one','one','two'],
				   'key3':[4,5,6,7]})
print left
print right
print pd.merge(left,right,on=['key1','key2'],how='outer')
"""
  key1 key2  lval
0  foo  one     1
1  foo  two     2
2  bar  one     3

  key1 key2  key3
0  foo  one     4
1  foo  one     5
2  bar  one     6
3  bar  two     7

key1 key2  lval  key3
0  foo  one   1.0   4.0
1  foo  one   1.0   5.0
2  foo  two   2.0   NaN
3  bar  one   3.0   6.0
4  bar  two   NaN   7.0
"""
# p202