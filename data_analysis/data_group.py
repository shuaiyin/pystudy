#coding=utf-8
from pandas import DataFrame,Series 
import pandas as pd 
import numpy as np 
import sys



df = DataFrame({'key1':['a','a','b','b','a'],
				'key2':['one','two','one','two','one'],
				'data1':np.random.randn(5)})

print df

#group by key1  and calculate the average value of column data1
groupd = df['data1'].groupby(df['key1'])
print groupd

means =  groupd.mean()

#using two keys to group and calculate the average value (using in Series)
means = df['data1'].groupby([df['key1'],df['key2']]).mean()
print means

#the key of group by can be every array the length of which is approprivate
states = np.array(['Ohio','California','California','Ohio','Ohio'])
years = np.array([2005,2005,2006,2005,2006])
means = df['data1'].groupby([states,years]).mean()
print means



#using column name as group key 
means = df.groupby('key1').mean() 
"""
there is no column key2 in the output,for that the data type of column key2 is string and not num !! so it will be filtered 
"""
print means
print df.groupby(['key1','key2']).size()


for name,group in df.groupby('key1'):
	print  'name is ',name
	print 'value is: \n',group


print '\n----------------\n'
for (k1,k2),group in df.groupby(['key1','key2']):
	print 'the key name is ',k1,k2
	print 'the value is:\n',group 



people = DataFrame(np.random.randn(5,5),columns=['a','b','c','d','e'],index=['Joe','Steve','Wes','Jim','Travis'])#索引值为人的名字
print people
"""
               a         b         c         d         e
Joe     1.304699  0.100459 -0.000408 -1.095217 -1.142781
Steve  -1.224551  0.478045 -1.328901 -0.365792 -1.339277
Wes     0.330814 -0.768008 -0.599442 -0.854585 -0.174300
Jim     0.701609 -1.466142 -0.207906 -0.870489  0.963129
Travis -2.215134 -0.821001  0.361285 -0.935930 -0.472026

"""
people.ix[2:3,['b','c']] = np.nan #add some NA value
print people
"""
               a         b         c         d         e
Joe     1.304699  0.100459 -0.000408 -1.095217 -1.142781
Steve  -1.224551  0.478045 -1.328901 -0.365792 -1.339277
Wes     0.330814       NaN       NaN -0.854585 -0.174300
Jim     0.701609 -1.466142 -0.207906 -0.870489  0.963129
Travis -2.215134 -0.821001  0.361285 -0.935930 -0.472026

"""
mapping = {'a':'red','b':'red','c':'blue','d':'blue','e':'red','f':'orange'}
#那么分组是可以按照index（索引行）或者column（列）来进行分组的，那么默认情况下是按照index来进行分组的，那么如果想指定column进行分组的话，需要设置axis参数为1
by_column = people.groupby(mapping,axis=1)

print by_column.sum()#做一次列的汇总求和
"""
            blue       red
Joe    -1.095625  0.262377
Steve  -1.694693 -2.085783
Wes    -0.854585  0.156513
Jim    -1.078395  0.198596
Travis -0.574644 -3.508161

"""
print by_column.count()#做一次列的汇总求总数
"""
        blue  red
Joe        2    3
Steve      2    3
Wes        1    2
Jim        2    3
Travis     2    3

"""



# 通过函数进行分组，相较于字典或Series，python函数在定义分组映射关系时可以更有创意且更为抽象，任何被当做分组建的函数都会在各个索引值上被调用一次，其返回值会被用作分组名称
print people.groupby(len).sum()#using fuction len as group function 
"""
          a         b         c         d         e
3 -0.817955  0.202583  1.424850  1.375932  0.589461
5 -0.865928  0.517076 -0.981535  0.816557  1.303144
6  1.700588  1.281608  0.025498 -0.415192  0.114043
"""
print people.groupby(len).count()
"""
   a  b  c  d  e
3  3  2  2  3  3
5  1  1  1  1  1
6  1  1  1  1  1

"""

#将函数与跟数组，列表。字典，Series混合使用也不是问题，因为任何东西都会被转换为数组。
key_list = ['one','one','one','two','two']
print people
print people.groupby([len,key_list]).sum()
print people.groupby(len).sum()
"""
               a         b         c         d         e
Joe    -0.044850  1.446475 -0.354495 -0.892443 -0.415122
Steve  -0.941921 -1.141826 -0.947607 -0.854944  1.867269
Wes    -1.419970       NaN       NaN -0.339313 -2.458381
Jim    -0.397000  1.715947 -0.654819 -1.420298 -0.806450
Travis -1.463469  0.356982  0.131443  1.245837 -0.365482

------优先按照长度来分组，那么发现这个key_list的长度恰好和索引的长度相同，那么第二级分组就靠它了
              a         b         c         d         e
3 one -1.464820  1.446475 -0.354495 -1.231757 -2.873503
  two -0.397000  1.715947 -0.654819 -1.420298 -0.806450
5 one -0.941921 -1.141826 -0.947607 -0.854944  1.867269
6 two -1.463469  0.356982  0.131443  1.245837 -0.365482

-------
          a         b         c         d         e
3 -1.861820  3.162422 -1.009314 -2.652055 -3.679954
5 -0.941921 -1.141826 -0.947607 -0.854944  1.867269


"""

df = DataFrame({
	 'A':['foo','bar','foo','bar','foo','bar','foo','foo'],
	 'B':['one','one','two','three','two','two','one','three'],
	 'C': np.random.randn(8),
	 'D':np.random.randn(8)
	})
print df
result = df.groupby('A').min()
print result
"""

     A      B         C         D
0  foo    one  1.271095  0.524734
1  bar    one -1.606482  0.945581
2  foo    two -1.770528 -2.329267
3  bar  three -0.525324 -0.197216
4  foo    two -0.572990  1.313470
5  bar    two -0.319865 -0.241170
6  foo    one  0.126530  0.443100
7  foo  three -0.956525 -1.255222

----这里按照A列进行分组，那么这里求得分组之后分组中数据的最小值（当然对于str类型的数据是无法输出的）
       B         C         D
A                           
bar  one -1.606482 -0.241170
foo  one -1.770528 -2.329267

"""




##根据索引级别分组，层次化索引数据集最方便的地方就在于他能够根据索引级别进行聚合。要实现该目的通过level关键字传入级别编号或名称即可
ls = [['US','US','US','JP','JP'],[1,3,5,1,3]]
columns = pd.MultiIndex.from_arrays(ls,names=['city','tenor'])
hier_df = DataFrame(np.random.randn(4,5),columns=columns)
print hier_df
print hier_df.groupby(level='city',axis=1).count()#
print hier_df.groupby(level='tenor',axis=1).count()#
"""
##根据索引级别分组，层次化索引数据集最方便的地方就在于他能够根据索引级别进行聚合。要实现该目的通过level关键字传入级别编号或名称即可

city         US                            JP          
tenor         1         3         5         1         3
0      0.781725  1.171544 -0.743763  0.887777 -0.487526
1     -0.162591 -0.510159 -0.898424  0.341528  2.143882
2     -0.204438 -0.709068 -3.320502  1.403123  1.065139
3      0.965160  0.898632 -0.390778  0.036086  1.621391

--------
city  JP  US
0      2   3
1      2   3
2      2   3
3      2   3

--------
tenor  1  3  5
0      2  2  1
1      2  2  1
2      2  2  1
3      2  2  1

"""

df = DataFrame({'data1':np.random.randn(5),
				'data2':np.random.randn(5),
				'key1':['a','a','b','b','a'],
				'key2':['one','two','one','two','one']})

print df
grouped = df.groupby('key1')
print grouped['data1'].quantile(0.9)

"""
key1
a    0.543716
b    0.870144
Name: data1, dtype: float64

"""



####如果要使用你自己的聚合函数，只需传入aggregate或agg方法即可
df = DataFrame({'data1':np.random.randn(5),
				'data2':np.random.randn(5),
				'key1':['a','a','b','b','a'],
				'key2':['one','two','one','two','one']})

print df
grouped = df.groupby('key1')
def peak_to_peak(arr):
	print '\nthe arr is\n',arr,'\n'
	return arr.max() - arr.min()

print grouped.agg(peak_to_peak)
"""
      data1     data2 key1 key2
0 -1.195139  0.874116    a  one
1 -0.824895  1.735717    a  two
2 -1.097719  0.243204    b  one
3  0.906202 -0.072424    b  two
4 -0.357310  1.201323    a  one
-----------
如果要使用你自己的聚合函数，只需要将其传入aggregate或agg方法即可
         data1     data2
key1                    
a     0.837828  0.861601
b     2.003922  0.315628

"""



# def test(x):
# 	return pd.Series([x,x+1],index=['x','x+1'])
# grouped = df.groupby('A')
# print grouped['C'].apply(test)

# # print grouped['C'].apply(lambda x : x.describe())




sys.exit(0)

