#coding=utf-8
from numpy import * 

"""
tile函数位于python模块 numpy.lib.shape_base中，他的功能是重复某个数组。
比如tile(A,n)，功能是将数组A重复n次，构成一个新的数组，我们还是使用具体的例子来说明问题：
"""
a = [0,1,2]
b = tile(a,2) #[0 1 2 0 1 2]
print b
print type(b)
"""
[0 1 2 0 1 2]
<type 'numpy.ndarray'>
"""

b = tile(a,(1,2))
print b
print type(b)
print tile(a,(1,3))
print tile(a,(2,1))
print tile(a,(2,2))

"""
[[0 1 2 0 1 2]]

<type 'numpy.ndarray'>


[[0 1 2 0 1 2 0 1 2]]


[[0 1 2]
 [0 1 2]]



[[0 1 2 0 1 2]
 [0 1 2 0 1 2]]

"""

###argsort 


"""
something about ndarray
"""

arr = array([[1,2,3],[4,5,6]])
print arr[1,2] #6
print arr[1] #[4 5 6]
arr[1] = [7,8,9] #or also can use arr[1,:] = [7,8,9]
print arr[1]#[7 8 9]
print type(arr[1])#<type 'numpy.ndarray'>
"""
the ndarray is so easy to use and flexiy 


"""
