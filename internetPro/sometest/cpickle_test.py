#coding=utf-8
import cPickle 
"""
在程序运行的过程中，所有的变量都是在内存中，比如，定义一个dict：
d = dict(name='Bob', age=20, score=88)
可以随时修改变量，比如把name改成'Bill'，但是一旦程序结束，变量所占用的内存就被操作系统全部回收。如果没有把修改后的'Bill'存储到磁盘上，
下次重新运行程序，变量又被初始化为'Bob'。我们把变量从内存中变成可存储或传输的过程称之为序列化，在Python中叫pickling，在其他语言中也
被称之为serialization，marshalling，flattening等等，都是一个意思。
序列化之后，就可以把序列化后的内容写入"磁盘"，或者通过"网络"传输到别的机器上。

"""
# data = range(10)
file_path = "../test_file/data.pkl"
data = {'name':'yinshuai','age':58}
cPickle.dump(data,open(file_path,"wb"))

"""
dump函数需要指定两个参数，第一个是需要序列化的python对象名称,第二个是本地的文件，需要注意的是，
在这里需要使用open函数打开一个文件，并指定“写”操作。

(dp1
S'age'
p2
I58
sS'name'
p3
S'yinshuai'
p4
s.


"""

data_string = cPickle.load(open(file_path,"rb"))
print data_string
"""
{'age': 58, 'name': 'yinshuai'}

同dump一样，这里需要使用open函数打开本地的一个文件，并指定“读”操作
"""


#####dumps：将python对象序列化保存到一个字符串变量中。
data_string = cPickle.dumps(data)
print data_string

data = cPickle.loads(data_string)
print data
"""
(dp1
S'age'
p2
I58
sS'name'
p3
S'yinshuai'
p4
s.

{'age': 58, 'name': 'yinshuai'}

其实写入文件和这个的效果是一样的
""