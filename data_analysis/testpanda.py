#-*- coding=utf-8 -*-
import numpy as np 
from pandas import *
import sys
arr1 = np.array([[1,2,3],[4,5,6]])
sdata = {'name':'yinshuai','age':55,'aaa':444,'ace':444}
print Series(sdata) #观察如何做的自动索引

"""
aaa          444
ace          444
age           55
name    yinshuai

"""

ssdata = {'state':['china','am','am','china','china'],
			'year':[2000,2015,2001,2002,2018],
			'pop':[1.5,1.2,1.6,1.7,1.9]}

frame = DataFrame(ssdata)#观察如何做的自动索引
print frame
"""
 pop  state  year
0  1.5  china  2000
1  1.2     am  2015
2  1.6     am  2001
3  1.7  china  2002
4  1.9  china  2018

"""
frame1 = DataFrame(ssdata,columns=['year','pop','state'])#按照设定的顺序添加索引
print frame1
"""
   year  pop  state
0  2000  1.5  china
1  2015  1.2     am
2  2001  1.6     am
3  2002  1.7  china
4  2018  1.9  china

"""
#照设定的顺序添加索引,索引的名字也是我们的,对于没有数据的列设置NAN
frame2 = DataFrame(ssdata,columns=['year','pop','state','dept'],index=['one','two','three','four','five']) 
print frame2
"""
       year  pop  state dept
one    2000  1.5  china  NaN
two    2015  1.2     am  NaN
three  2001  1.6     am  NaN
four   2002  1.7  china  NaN
five   2018  1.9  china  NaN
"""
frame2['dept'] = np.arange(5.)#这里通过这种方式补充上空缺值，但是要注意这个arange生成的Series要与rows一挃
# print np.arange(5.6)
print frame2
"""
       year  pop  state  dept
one    2000  1.5  china   0.0
two    2015  1.2     am   1.0
three  2001  1.6     am   2.0
four   2002  1.7  china   3.0
five   2018  1.9  china   4.0

"""

val = Series([-1.2,-1.5,-1.7],index=['two','four','five'])
frame2['debt'] = val #这是通过这种索引的方式控制缺口补充
print frame2
"""
       year  pop  state  dept  debt
one    2000  1.5  china   0.0   NaN
two    2015  1.2     am   1.0  -1.2
three  2001  1.6     am   2.0   NaN
four   2002  1.7  china   3.0  -1.5
five   2018  1.9  china   4.0  -1.7

"""

#为不存在的列赋值会创建一个新列，关键字del用于删除列
frame2['eastern'] = frame2.state = 'Ohio'
print frame2
"""
       year  pop state  dept  debt eastern
one    2000  1.5  Ohio   0.0   NaN    Ohio
two    2015  1.2  Ohio   1.0  -1.2    Ohio
three  2001  1.6  Ohio   2.0   NaN    Ohio
four   2002  1.7  Ohio   3.0  -1.5    Ohio
five   2018  1.9  Ohio   4.0  -1.7    Ohio
"""

del frame2['eastern']
print frame2
"""
       year  pop state  dept  debt
one    2000  1.5  Ohio   0.0   NaN
two    2015  1.2  Ohio   1.0  -1.2
three  2001  1.6  Ohio   2.0   NaN
four   2002  1.7  Ohio   3.0  -1.5
five   2018  1.9  Ohio   4.0  -1.7
"""

print frame2.columns
"""
Index([u'year', u'pop', u'state', u'dept', u'debt'], dtype='object')
"""



###########################看下面这种结构 ==嵌套字典
pop = {'Nevada':{2001:2.4,2002:2.9},'Ohio':{2000:1.5,2001:1.7,2002:3.6}}
frame3 = DataFrame(pop)
print frame3
"""
将嵌套字典传递给DataFrame，他就会被解释为：外层字典的键作为列；内层键则作为行索引
内层字典的键会被合并，排序形成最终的索引，如果显式的设定了索引，则不会这样
      Nevada  Ohio
2000     NaN   1.5
2001     2.4   1.7
2002     2.9   3.6

"""
print frame3.T
"""
作转置
        2000  2001  2002
Nevada   NaN   2.4   2.9
Ohio     1.5   1.7   3.6

"""

print DataFrame(pop,index=[2001,2002,2003])
"""
内层字典的键会被合并，排序形成最终的索引，如果显式的设定了索引，则不会这样
      Nevada  Ohio
2001     2.4   1.7
2002     2.9   3.6
2003     NaN   NaN
"""

######## pandas  的索引对象 负责管理轴标签和其他元数据，比如轴名称等

obj = Series(range(3),index=['a','b','c'])
print obj
"""
a    0
b    1
c    2
dtype: int64

"""
index = obj.index
print index
print type(index)
"""
Index([u'a', u'b', u'c'], dtype='object')
<class 'pandas.indexes.base.Index'>
index对象是不可以修改的,不可修改是非常重要的，这样才能使Index对象在多个数据结构之间安全共享
"""
index = pandas.Index(np.arange(3))
print index
"""
Int64Index([0, 1, 2], dtype='int64')
"""
obj2 = Series([1.5,-2.5,0],index=index)
print obj2
print obj2.index is index
"""
0    1.5
1   -2.5
2    0.0
dtype: float64
True
"""


################重新索引
obj = Series([4.5,7.2,-5.3,3.6],index=['d','b','a','c'])
print obj
"""
d    4.5
b    7.2
a   -5.3
c    3.6
dtype: float64

"""


obj2 = obj.reindex(['a','b','c','d','e'])
print obj2
"""
a   -5.3
b    7.2
c    3.6
d    4.5
e    NaN  #注意观察这一行，Series的reindex将会根据新索引进行重排,if the value of index if not exist ,then import NaN
dtype: float64

"""

obj3 = obj.reindex(['a','b','c','d','e'],fill_value=0)
print obj3
"""
dtype: float64
a   -5.3
b    7.2
c    3.6
d    4.5
e    0.0
dtype: float64

fill_value is a good way for data clean 
"""


########一个json dict转换为DataFrame
user_info = {'username':'yinshuai','age':24,'sex':'boy'}
ser = Series(user_info)
print ser
frame = DataFrame(user_info,index=[0,1,2])
print frame
"""
age               24
sex              boy
username    yinshuai
dtype: object



   age  sex  username
0   24  boy  yinshuai
1   24  boy  yinshuai
2   24  boy  yinshuai
备注：怎么感觉这个字典充其量也就是个轴，对于轴来说使用Series最好了,如果不加index(轴index)竟然还会throw exception 

"""

########### 字典数组看看怎么转换的
user_list = [{'username':'yinshuai','age':24,'sex':'boy'},{'username':'yinna','age':18,'sex':'gril'}]
frame = DataFrame(user_list)
print frame
"""
   age   sex  username
0   24   boy  yinshuai
1   18  gril     yinna
其实放现这个和上面的同样，但是这种数据表示方式更加友好
"""

frame = DataFrame(user_list,index=['one','two'])
print frame
"""
     age   sex  username
one   24   boy  yinshuai
two   18  gril     yinna
"""

###再看看如何再增加一个列数据呢》
frame['area'] = ['beijing','langfang']
print frame
"""

     age   sex  username      area
one   24   boy  yinshuai   beijing
two   18  gril     yinna  langfang
"""

print frame.age
"""
one    24
two    18
Name: age, dtype: int64
获取一列数据 only fetch the special columns 
"""

print frame.username 
"""
one    yinshuai
two       yinna
Name: username, dtype: object
"""

####做一次其他的测试
frame['univer'] = Series(['bupt'],index=['one'])
print frame
"""
利用Series为特定索引插入数据
     age   sex  username      area univer
one   24   boy  yinshuai   beijing   bupt
two   18  gril     yinna  langfang    NaN

"""

new_frame = frame.univer.dropna()#数据清洗，将那些在指定列的值为NAN的轴去掉
print new_frame
"""
one    bupt
Name: univer, dtype: object
only fetch out the columns of univer

"""
print type(new_frame)
"""
<class 'pandas.core.series.Series'>
the series is iterable 
"""
print len(new_frame)
"""
1  the obj of the series if iterable and you can oper it just like list 
"""

print type(frame['age']) 
print type(frame.age)
print isinstance(frame.age,Series)
print  isinstance(frame,DataFrame)
"""
<class 'pandas.core.series.Series'>
<class 'pandas.core.series.Series'>
True
True
"""

print frame.username.value_counts()
"""
yinna       1
yinshuai    1
统计数目
"""

######下面以上面的数据为例继续测试
testdata = {'state':['china','am','am','china','china'],
			'year':[2000,2015,2001,2002,2018],
			'pop':[1.5,1.2,1.6,1.7,1.9]}

frame = DataFrame(testdata)
print frame
"""
   pop  state  year
0  1.5  china  2000
1  1.2     am  2015
2  1.6     am  2001
3  1.7  china  2002
4  1.9  china  2018
"""

#我们这里给这组数据添加一列Series
new_columns = Series(['','oil','woods'],index=[0,3,4])
frame['source'] = new_columns
print frame
"""
   pop  state  year source
0  1.5  china  2000       
1  1.2     am  2015    NaN
2  1.6     am  2001    NaN
3  1.7  china  2002    oil
"""

series_source =  frame.source.dropna()#
print series_source
print len(series_source)
"""
0         
3      oil
4    woods
Name: source, dtype: object

3  (this is the length)
"""

series_source = frame.source.fillna('Mising')
print series_source
"""
0          
1    Mising
2    Mising
3       oil
4     woods
Name: source, dtype: object

shuai:we can figure out that when use the fillna method of the Series,it will fill out the NaN value ,
but when using droupna,it will drop out the NAN rows.neither will change the ori DataFrame
"""
print type(series_source) 
"""<class 'pandas.core.series.Series'>"""

for ele in series_source: print ele
"""

Mising
Mising
oil
woods
"""

# series_source = series_source[series_source == ''] == 'Unknown'

####### reindex 
se_obj = Series(np.arange(1,5),index=['a','b','c','d'])
print se_obj
"""
a    1
b    2
c    3
d    4
e    5
f    6
dtype: int64
"""

print se_obj.reindex(['a','b','c','d','e'])
"""
a    1.0
b    2.0
c    3.0
d    4.0
e    NaN
dtype: float64
"""


print se_obj.reindex(['a','b','c','d','e'],fill_value=0)
"""
a    1
b    2
c    3
d    4
e    0
dtype: int64
"""


se_obj3 = Series(['blue','red','orange'],index=[0,2,4])
print se_obj3
"""
0      blue
2       red
4    orange
dtype: object
"""

print se_obj3.reindex(range(6),method='ffill')
"""
0      blue
1      blue
2       red
3       red
4    orange
5    orange
dtype: object
###########重新索引的时候进行前向插值处理，通过method option 
"""


frame = DataFrame(np.arange(9).reshape(3,3),index=['a','c','d'],columns=['Ohio','Texas','California'])
print frame
"""
   Ohio  Texas  California
a     0      1           2
c     3      4           5
d     6      7           8
"""

###reindex
state = ['Texas','Utal','California']
print frame.reindex(columns=state)
"""
对于这种DataFrame 和 Series是不同的，进行reindex的时候要指明 index or column
   Texas  Utal  California
a      1   NaN           2
c      4   NaN           5
d      7   NaN           8

"""
print frame.reindex(index=['a','b','c','d'])
"""
   Ohio  Texas  California
a   0.0    1.0         2.0
b   NaN    NaN         NaN
c   3.0    4.0         5.0
d   6.0    7.0         8.0

"""
#### this is a easy way  use ix tag index function  it can clear the reindex function 
frame.ix[['a','b','c','d'],state]
"""
   Ohio  Texas  California
a   0.0    1.0         2.0
b   NaN    NaN         NaN
c   3.0    4.0         5.0
d   6.0    7.0         8.0
"""

print frame.ix[['a','b','c','d'],['Texas','Utal','California']]
"""
double dim reindex yinshuai

   Texas  Utal  California
a    1.0   NaN         2.0
b    NaN   NaN         NaN
c    4.0   NaN         5.0
d    7.0   NaN         8.0
"""


############ Series丢弃指定轴上的项
obj = Series(np.arange(5.),index=['a','b','c','d','e'])
print obj
new_obj = obj.drop('c')
print new_obj
"""
a    0.0
b    1.0
c    2.0
d    3.0
e    4.0
dtype: float64
a    0.0
b    1.0
d    3.0
e    4.0
dtype: float64
"""

########### for DataFrame 可以删除任意轴上的索引值
data = DataFrame(np.arange(16).reshape((4,4)),
        index=['beijing','shanghai','guangzhou','shenzhen'],
        columns=['one','two','three','four'])

print data
"""
           one  two  three  four
beijing      0    1      2     3
shanghai     4    5      6     7
guangzhou    8    9     10    11
shenzhen    12   13     14    15
"""
print data.drop(['beijing','shanghai'])
"""
           one  two  three  four
guangzhou    8    9     10    11
shenzhen    12   13     14    15
"""

print data.drop(['one'],axis=1)
"""
           two  three  four
beijing      1      2     3
shanghai     5      6     7
guangzhou    9     10    11
shenzhen    13     14    15
yinshuai: i think the axis is to set the index or columns
"""

print data.drop(['one','two'],axis=1)
"""
           three  four
beijing        2     3
shanghai       6     7
guangzhou     10    11
shenzhen      14    15

"""

print data.one
print data['one']
"""
beijing       0
shanghai      4
guangzhou     8
shenzhen     12
Name: one, dtype: int64

beijing       0
shanghai      4
guangzhou     8
shenzhen     12
Name: one, dtype: int64
"""

print data[['one','two']]
"""
           one  two
beijing      0    1
shanghai     4    5
guangzhou    8    9
shenzhen    12   13
"""

###special case## use slice or bool narray to fetch rows !!!!!!!
print data[:2]
"""
          one  two  three  four
beijing     0    1      2     3
shanghai    4    5      6     7
"""


print data[data['three'] > 5]
"""
           one  two  three  four
shanghai     4    5      6     7
guangzhou    8    9     10    11
shenzhen    12   13     14    15
"""
print data < 5
"""
             one    two  three   four
beijing     True   True   True   True
shanghai    True  False  False  False
guangzhou  False  False  False  False
shenzhen   False  False  False  False
"""
result = data['three'] > 5
print result 
print type(result)
"""
beijing      False
shanghai      True
guangzhou     True
shenzhen      True
Name: three, dtype: bool
<class 'pandas.core.series.Series'>

"""

data[data < 5 ] = 0
print data
"""
           one  two  three  four
beijing      0    0      0     0
shanghai     0    5      6     7
guangzhou    8    9     10    11
shenzhen    12   13     14    15
"""

####### using ix(tag index) to simplify the reindex
print data.ix['shenzhen',['two','one']]
"""
two    13
one    12
Name: shenzhen, dtype: int64
"""

print data.ix[['beijing','shenzhen'],[3,0,1]]
"""
          four  one  two
beijing      0    0    0
shenzhen    15   12   13
"""

print '-----'
print data
print data.ix[2]
"""
           one  two  three  four
beijing      0    0      0     0
shanghai     0    5      6     7
guangzhou    8    9     10    11
shenzhen    12   13     14    15



one       8
two       9
three    10
four     11
"""


print '---'
print data.ix[:'shanghai','two']
"""
beijing     0
shanghai    5
Name: two, dtype: int64
"""

print '---'
print data.ix[data.three > 5,:3]
"""
           one  two  three
shanghai     0    5      6
guangzhou    8    9     10
shenzhen    12   13     14
"""

























