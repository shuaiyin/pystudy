#coding=utf-8
import operator 

new_list = sorted([5,2,3,1,4])
print new_list #[1, 2, 3, 4, 5] 当然也可以使用list.sort()  但是会改变原始list

##
user_info = [{'username':'yinshuai','age':25,'sex':'man'},{'username':'yinkai','age':18,'sex':'man'},{'username':'yinna','age':19,'sex':'woman'}]



##key参数的值为一个函数，此函数只有一个参数且返回一个值用来进行比较。这个技术是快速的因为key指定的函数将准确地对每个元素调用。
##这里的user是自动被迭代出来的list中的元素 当然list当中也可以是tuple
print sorted(user_info,key=lambda user: user['age'])# sort by age
"""
[{'username': 'yinkai', 'age': 18, 'sex': 'man'}, {'username': 'yinna', 'age': 19, 'sex': 'woman'}, {'username': 'yinshuai', 'age': 25, 'sex': 'man'}]
"""

print sorted(user_info,key=lambda user: user['sex'])#sort by sex
"""
[{'username': 'yinshuai', 'age': 25, 'sex': 'man'}, {'username': 'yinkai', 'age': 18, 'sex': 'man'}, {'username': 'yinna', 'age': 19, 'sex': 'woman'}]

"""



print '------------'
##上面这种使用key的方式很常用，于是python提供了更加方便的函数
user_info = [{'username':'yinshuai','age':25,'sex':'man'},{'username':'yinkai','age':18,'sex':'man'},{'username':'yinna','age':19,'sex':'woman'}]
print sorted(user_info,key=operator.itemgetter('age'))
print sorted(user_info,key=operator.itemgetter('age'),reverse=True)
"""
[{'username': 'yinkai', 'age': 18, 'sex': 'man'}, {'username': 'yinna', 'age': 19, 'sex': 'woman'}, {'username': 'yinshuai', 'age': 25, 'sex': 'man'}] #default asc 
[{'username': 'yinshuai', 'age': 25, 'sex': 'man'}, {'username': 'yinna', 'age': 19, 'sex': 'woman'}, {'username': 'yinkai', 'age': 18, 'sex': 'man'}]# desc 

"""

print '------------------'
#当然这同样适用于元组构成的list etc
score_info = [('yinshuai','B',52),('yinna','A',100),('yinkai','C',44)]
print sorted(score_info,key=operator.itemgetter(2),reverse=True) #[('yinna', 'A', 100), ('yinshuai', 'B', 52), ('yinkai', 'C', 44)]


print '--------------'
# python 字典排序
my_dict = {'a':3,'b':1,'c':2}
print my_dict.iteritems()#以迭代器对象返回字典键值对
print sorted(my_dict.iteritems(),key=lambda asd : asd[0],reverse=True) #[('c', 2), ('b', 1), ('a', 3)]
print sorted(my_dict.iteritems(),key=lambda asd : asd[1],reverse=True) #[('a', 3), ('c', 2), ('b', 1)]
#: 在函数sorted(dic.iteritems(), key = lambda asd:asd[1])中，第一个参数传给第二个参数“键-键值”，第二个参数取出其中的键([0])或键值(1])
#当然还可以使用更加便捷的方法
print sorted(my_dict.iteritems(),key=operator.itemgetter(0),reverse=True) ##[('c', 2), ('b', 1), ('a', 3)]


