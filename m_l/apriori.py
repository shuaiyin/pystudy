#coding=utf-8

"""
apriori算法的一般过程
(1)收集数据：使用任意方法  
(2)准备数据：任何数据类型都可以。 
(3)分析数据：任意方法
(4)训练算法：使用apriori算法来找到频繁项集
(5)测试算法： 不需要测试过程  
(6) 使用算法：用于发现频繁项集以及物品之间的关联规则

"""
import sys
from numpy import *

def loadDataSet():
	return [[1,3,4],[2,3,5],[1,2,3,5],[2,5]]

def createC1(dataSet):
	"""
	用于构建集合C1，C1是大小为1的所有候选项集的集合
	算法首先构建集合C1，然后扫描数据集来判断这些"只有""一个"元素的项集是否满足最小支持度的要求
	对大列表C1进行排序，然后将其"映射"到frozenset(),最后返回frozenset的列表
	"""
	C1= []
	for transaction in dataSet:
		for item in transaction:
			if not [item] in C1:
				C1.append([item])#
	C1.sort()#	[[1], [2], [3], [4], [5]]
	#由于之后必须将这些集合作为字典键值使用，所以采用frozenset而不是set，因为set是可变的，可变的量不可以作为hash键
	return map(frozenset,C1)#[frozenset([1]), frozenset([2]), frozenset([3]), frozenset([4]), frozenset([5])]



def scanD(D,Ck,minSupport):
	"""
	function:从C1生成L1
	input agument:
		D:数据集Ck 
		Ck:包含候选集合的列表:the data type in the list is frozenset
		minSupport:以及感兴趣项集的最小支持度
	return:返回一个满足最小支持度的项集列表和包含支持度值的字典以备后用
	"""
	ssCnt = {}
	for tid in D:
		for can in Ck:#the data type of the can is frozenset
			if can.issubset(tid):#判断集合是否是某个集合的自己，这里不分frozenset or set 
				if not ssCnt.has_key(can):ssCnt[can] = 1
				else:ssCnt[can] += 1 #for that the set can not used as the key of the hash dict ,so this place using frozenset  to instead set 
	numItems = float(len(D))
	retList = [] 
	supportData = {}
	for key in ssCnt:
		support = ssCnt[key]/numItems
		if support >= minSupport:
			retList.insert(0,key)#在列表收不插入任意新的集合
		supportData[key] = support
	return retList,supportData


def apriorGen(Lk,k):
	"""
	"""
	retList = []
	lenLk = len(Lk)




dataSet = loadDataSet()
print dataSet#[[1, 3, 4], [2, 3, 5], [1, 2, 3, 5], [2, 5]]
C1 = createC1(dataSet)#创建第一个候选项集集合C1
print 'the first set is ',C1#the first set is  [frozenset([1]), frozenset([2]), frozenset([3]), frozenset([4]), frozenset([5])]
D = map(set,dataSet)#映射数据集中的元素到set上,有了集合形式的数据，就可以去掉那些不满足最小支持度的项集，在这里我们使用0.5作为最小支持度水平
print D#[set([1, 3, 4]), set([2, 3, 5]), set([1, 2, 3, 5]), set([2, 5])]

retList,supportData = scanD(dataSet,C1,0.5)
print retList,supportData
"""
[frozenset([1]), frozenset([3]), frozenset([2]), frozenset([5])]  保留下来的频繁项集
{frozenset([4]): 0.25, frozenset([5]): 0.75, frozenset([2]): 0.75, frozenset([3]): 0.75, frozenset([1]): 0.5}

"""
