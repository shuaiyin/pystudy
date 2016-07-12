#-*- coding=utf-8 -*-
import numpy as np 
from numpy import random
import sys
"""
ndarray , ndarray 是一个通用的同构数据多维容器，,that to say,the ele in the container must have same type!!
each ndarray has a shape attribute(a tuple to show the dim of the ndarray) and a dtype(an object used  to showw the type of the element)
"""



"""
创建数据的最简单的办法就是使用array函数，他接受all序列类型的对象
"""


data1 = [6,7.5,8,0,1]
arr1 = np.array(data1)
print arr1
print arr1.dtype
print arr1.shape
"""
[ 6.   7.5  8.   0.   1. ] yeal,it's a vector 
float64
(5,)
"""

data2 =[ [1,2,3,4],[5,6,7,8] ]
arr2 = np.array(data2)
print arr2
print arr2.dtype
print arr2.shape
print arr2.ndim
"""
[[1 2 3 4]
 [5 6 7 8]]
int64
(2, 4)
2
"""


print np.zeros(10)
print np.zeros((3,6))
"""
[ 0.  0.  0.  0.  0.  0.  0.  0.  0.  0.]
[[ 0.  0.  0.  0.  0.  0.]
 [ 0.  0.  0.  0.  0.  0.]
 [ 0.  0.  0.  0.  0.  0.]]

"""

arr3 = np.arange(15)
print arr3,arr3.shape,arr3.dtype
"""
arrange if a fast way to create an array, it's just like the use of range in the list .. 
arrange(array range )
[ 0  1  2  3  4  5  6  7  8  9 10 11 12 13 14] (15,) int64

"""


arr = np.array([1,2,3],dtype=np.float64)
print arr
print arr.dtype
"""
change a list into an array and set the data save type  
[ 1.  2.  3.]
float64

"""


arr = np.array([1,2,3],dtype=np.int32)
print arr
print arr.dtype 
"""
[1 2 3]
int32

"""

### another way to change the dtype of an array 
arr_int = np.array([1,2,3,4])
print arr.dtype 
float_arr = arr_int.astype(np.float64)
print float_arr.dtype
"""
int32
float64
"""

float_arr = np.array([1.2,2.6,2.3,2.8])
print float_arr
print float_arr.dtype
arr_int = float_arr.astype(np.int32)
print arr_int
print arr_int.dtype
"""
[ 1.2  2.6  2.3  2.8]
float64
[1 2 2 2]
int32
"""


#### array is very important ,we can use it to do vertor calc intead of iterator to calc 
arr = np.array([[1.,2.,3.],[4.,5.,6.]])
print arr
"""
[[ 1.  2.  3.]
 [ 4.  5.  6.]]
"""


print arr * arr
"""
[[  1.   4.   9.]
 [ 16.  25.  36.]]

"""

print arr-arr
"""
[[ 0.  0.  0.]
 [ 0.  0.  0.]]
"""

print 1/arr
"""
[[ 1.          0.5         0.33333333]
 [ 0.25        0.2         0.16666667]]
"""

print arr*0.5
"""
[[ 0.5  1.   1.5]
 [ 2.   2.5  3. ]]
"""

###fast way to create array using arange 
arr = np.arange(10)
print arr
print arr.dtype
print arr.shape
"""
[0 1 2 3 4 5 6 7 8 9]
int64
(10,)
"""

arr_slice = arr[5:8]
print arr_slice
print arr
arr[5:8] = 12 
print arr
"""
[5 6 7]
[0 1 2 3 4 5 6 7 8 9]
[ 0  1  2  3  4 12 12 12  8  9]  ###broadcast 
"""

arr_slice[:] = 64
print arr 
"""
[ 0  1  2  3  4 64 64 64  8  9]
"""


######## high dim array   the dim is 2 
arr2d = np.array([[1,2,3],[4,5,6],[7,8,9]])
print arr2d.shape #(3,3)
print arr2d[1]
print arr2d[2]
"""
(3,3)
[4 5 6]
[7 8 9]
"""


arr2d[0][1] = 438 
print arr2d
"""
[[  1 438   3]
 [  4   5   6]
 [  7   8   9]]
"""


#hign dim array  the dim is 3 such as  2*2*3 
arr3d = np.array([[[1,2,3],[4,5,6]],[[7,8,9],[10,11,12]]])
print arr3d
print arr3d.shape
"""
[[[ 1  2  3]
  [ 4  5  6]]

 [[ 7  8  9]
  [10 11 12]]]
(2, 2, 3)
"""

print arr3d[0]
"""
[[1 2 3]
 [4 5 6]]
"""
print arr3d[1]
"""
[[ 7  8  9]
 [10 11 12]]
"""

print arr3d[0][0]
print arr3d[0][1]
"""
[1 2 3]
[4 5 6]
"""
arr3d[0][0] = (33,44,55)
print arr3d
print '-----------'
"""
[[[33 44 55]
  [ 4  5  6]]

 [[ 7  8  9]
  [10 11 12]]]
"""


#######SLICE IN high dim narray 
## 2 dim  
arr2d = np.array([[1,2,3],[4,5,6],[7,8,9]])
print arr2d[:,:1]
print arr2d[:,:2]
"""
[[1]
 [4]
 [7]]

[[1 2]
 [4 5]
 [7 8]]
分析：按照轴度依次切片,在上面这里对第0轴不做slice 对第1轴做的slice 
"""
print '--------------'
print arr2d[1:,:]
print arr2d[2:,:]
"""
[[4 5 6]
 [7 8 9]]


[[7 8 9]]  
分析：这里对第0轴做切片，但是对于第1轴不做，其实轴和维度我认为是一养的
"""

print arr2d[1,1:]
"""
[5 6]
第0轴定死，然后对于第二轴做切片
"""


##########bool index 
print '--------------------'
names = np.array(['Bob','Joe','Will','Bob','Will','Joe','Joe'])
print names
"""
['Bob' 'Joe' 'Will' 'Bob' 'Will' 'Joe' 'Joe']
"""
print names == 'Bob'
"""
[ True False False  True False False False]
yinshuai:这里我们想选择出对应于名字"Bob"的所有行，跟算数运算一样，数组的比较运算(如==)也是vector化的.
因此，对names和字符串"Bob"的比较会产生一个bool 类型的数组
"""
data = random.randn(7,4)
print data
"""
上面这个bool类型的数组可以用于数组索引: 
"""
print data[names == 'Bob']

"""
[[ -1.34229624e-01  -3.65056520e-01  -7.79152632e-01   2.33340512e-01]
 [  7.64305194e-02   6.94274840e-01   2.02828574e+00  -1.28913277e+00]
 [ -2.24775689e-01  -5.47903595e-02   2.34428308e-01   8.30913841e-01]
 [ -1.28792279e+00  -2.68620558e-01  -7.07189035e-01  -1.06134403e+00]
 [  3.07340587e+00  -7.67207395e-01   1.13446617e+00  -1.35521062e-03]
 [  5.86101949e-01  -1.32567614e+00  -1.03247392e+00  -1.50122449e-01]
 [ -4.12355291e-01   3.69874971e-01  -6.61987705e-02  -1.57886620e+00]]
 yinshuai:the ndarray above is 正态分布

[[-0.13422962 -0.36505652 -0.77915263  0.23334051]
 [-1.28792279 -0.26862056 -0.70718903 -1.06134403]]

yinshuai: 使用这个boolean类型的数组作为索引之后就可以选择出为True的维度,you should pay attention to the follow:::
the length of bool array must as same as 被索引的轴长度

"""

print '50.---------------'
##ok say follow test !!
print names != 'Bob' 
"""
[False  True  True False  True  True  True]
yinshuai:yeal!you can    =====================================================================================================p105
"""




data[data < 0] = 0
print data
"""
[[ 0.          0.14298878  0.          0.        ]
 [ 0.69048901  0.56703142  0.          0.        ]
 [ 0.          0.73459869  0.          0.        ]
 [ 0.          0.          0.          1.49436849]
 [ 0.          1.68278072  1.39582148  0.        ]
 [ 0.          0.          0.          1.49037216]
 [ 0.67747602  0.          0.          0.        ]]
"""


####花式索引花式索引花式索引花式索引花式索引
arr = np.empty((8,4))
print arr
"""
[[  1.21002228e-312   1.21002228e-312   1.16270208e-316   1.16270089e-316]
 [  1.16270089e-316   1.16270089e-316   1.16270089e-316   1.16270089e-316]
 [  1.16270208e-316   1.16270089e-316   1.16270089e-316   1.16270089e-316]
 [  1.16270089e-316   1.16270089e-316   1.16270089e-316   1.16270089e-316]
 [  1.16270089e-316   1.16270089e-316   1.16270089e-316   1.16270089e-316]
 [  1.16270089e-316   1.16270089e-316   1.16270089e-316   1.16270208e-316]
 [  1.16270089e-316   1.16270089e-316   1.16270089e-316   1.16270089e-316]
 [  6.01334619e-154   9.62021462e+140   4.48505083e-308   1.63041663e-322]]

"""

for i in range(8):
	arr[i] = i
print arr
"""
[[ 0.  0.  0.  0.]
 [ 1.  1.  1.  1.]
 [ 2.  2.  2.  2.]
 [ 3.  3.  3.  3.]
 [ 4.  4.  4.  4.]
 [ 5.  5.  5.  5.]
 [ 6.  6.  6.  6.]
 [ 7.  7.  7.  7.]]

"""
print arr[1]
"""
[ 1.  1.  1.  1.]

"""
print arr[[4,3,0,6]] #using ndarray to fetch sub set from the set 
"""
[[ 4.  4.  4.  4.]
 [ 3.  3.  3.  3.]
 [ 0.  0.  0.  0.]
 [ 6.  6.  6.  6.]]

"""

print arr[[-3,-5,-7]]
"""
使用负数索引 将从末尾开始选取行
[[ 5.  5.  5.  5.]
 [ 3.  3.  3.  3.]
 [ 1.  1.  1.  1.]]
"""


##some knowlege about reshape  
arr = np.arange(32).reshape((8,4))
print arr
print arr[[2,5,6],[1,2,3]]
"""
[[ 0  1  2  3]
 [ 4  5  6  7]
 [ 8  9 10 11]
 [12 13 14 15]
 [16 17 18 19]
 [20 21 22 23]
 [24 25 26 27]
 [28 29 30 31]]

[ 9 22 27]
分析：最终选择出来的数据是(2,1) (5,2) (6,3) 所索引到的数据

"""

##数组的转置和轴对换，他返回的是源数据的view 不会进行任何复制操作
arr = np.arange(15).reshape((3,5))
print arr
"""
[[ 0  1  2  3  4]
 [ 5  6  7  8  9]
 [10 11 12 13 14]]
"""

























