#coding=utf-8
from pandas import Series,DataFrame
### the funciton of zip 
#the zip funciton receive any more (even zero) list param, and it will return a list of tuple   
x = [1,2,3]
y = [4,5,6]
z = [7,8,9]
xyz = zip(x,y,z)
print xyz
"""
[(1, 4, 7), (2, 5, 8), (3, 6, 9)]
"""

x = [1,2,3]
y = [4,5,6,7]
xy = zip(x,y)
print xy 
"""
[(1, 4), (2, 5), (3, 6)]
"""

x = zip()
print x
"""
[]
"""


records = [{'username':'yinshuai','age':25},{'username':'yinkai','age':24},{'username':'wangna','age':44}]
frame = DataFrame(records)
username_col = frame.username
print username_col.str.contains('shua')
