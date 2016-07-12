#coding=utf-8

##下面这种是新式类
class Man(object):
	def __init__(self):
		self.legs = 25 

	def get_legs(self):
		return self.legs


class Yinshuai(Man):
	def __init__(self):
		super(Yinshuai,self).__init__()
		self.eyes = 2 

	def get_eyes(self):
		return self.eyes


print Yinshuai().get_eyes()
print Yinshuai().get_legs()


print  '--------new start --------'
def checkIndex(key):
	"""
	is the key can be receviced ?? 
	in order to recevice the key,the key must be a nonegative interger,if the key is not interger, it will raise TypeError
	if the key is a negative interger, it will raise IndexError,for that the length of the  sequence if unlimit 

	"""
	if not isinstance(key,(int,long)):raise TypeError
	if key < 0: raise IndexError

####看下如何创建一个无穷序列
class ArithmeticSequence(object):
	def __init__(self,start=0,step=1):
		"""
		init ArithmeticSequence
		start  first value in sequence 
		step 两个相邻值之间的差别
		changed 用户修改的值的字典  
		"""
		self.start  = start
		self.step = step 
		self.changed = {} 

	def __getitem__(self,key):
		"""
		Get an item from arithmetic sequence 
		"""
		checkIndex(key)
		try:
			return self.changed[key] #if has been modified ?? 
		except KeyError: # or 
			return self.start + key*self.step ##calc the value 

	def __setitem__(self,key,value):
		"""
		modify an item in arithmetic sequence
		"""
		checkIndex(key)
		self.changed[key] = value #save the value been modified 

seq = ArithmeticSequence(1,2)
print seq[4]  ###直接在对象中进行索引
"""
9
"""

try:
	index = input('Enter your index number ')
	print seq[index] ##直接在对象中进行索引而且是直接取值，会调用到对象中的__getitem__魔术方法,其中的index作为参数传入
except IndexError:
	print 'wrong index'
except TypeError:
	print 'wrong type '
"""
1 		3 
-77  	wrong index 
'tt'    wront type 
"""

seq[4] = 6666 ##通过索引进行值的设置  传入index 和 value参数
print seq[4] ##6666
print seq.changed#{4: 6666}

###


########about property 
class Rectangle(object):
	def __init__(self):
		self.width = 100
		self.height = 0 

	def setSize(self,size):
		self.width,self.height = size 

	def getSize(self):
		return self.width,self.height

	size = property(getSize,setSize)

	@property
	def getWidth(self):
		return self.width


r = Rectangle()
r.width = 300
r.height = 600
print r.size 
print r.getWidth

"""
(300,600)
300
"""


####### 生成器
def flatten(nested):
	for sublist in nested:
		for element in sublist:
			yield element #任何包含yield语句的函数称为迭代器

nested = [[1,2,3],[4,5,6],[7,8,9]]
flat = flatten(nested)
print flat  ##<generator object flatten at 0x7f768a97a0f0>
for num in flat:
	print num ##通过在生成器上迭代来使用所有的值


#######递归生成器
def flattenR(nested):
	try:
		for sublist in nested:
			for element in flatten(sublist):
				yield element
	except TypeError:
		yield nested


		#########stop at page 155 






	
