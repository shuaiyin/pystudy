#coding=utf-8

"""
apriori算法的一般过程
(1)收集数据：使用任意方法  
(2)准备数据：任何数据类型都可以。 
(3)分析数据：任意方法
(4)训练算法：使用apriori算法来找到频繁项集
(5)测试算法： 不需要测试过程  
(6) 使用算法：用于发现频繁项集以及物品之间的关联规则




频繁项集的量化定义：满足最小支持度要求。
 对于关联规则的量化指标成为可信度（置信度）

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
	input param:
		Lk:1项集输入，这算是一个起点吧
		k:获取到k项集,这里的k是从2开始的！！就是从2项集开始的,就是说从获取2项集开始才能开始使用这个函数哦,这里为啥要使用k-2?
		  因为这里的k代表的是项集数，那么只有项集数大于等于2才可以开始使用这个合并

	这个称作F(k-1)xF(k-1)方法

	函数apriorGen的输入参数为频繁项集列表Lk与项集元素个数k，输出为Ck
	举例来说，该函数以{0},{1},{2}作为输入，会生成{0,1},{0,2}以及{1,2}

	"""
	retList = []
	lenLk = len(Lk)
	#
	for i in range(lenLk):#通过两个for循环来实现比较LK中的每一个元素与其他元素
		for j in range(i+1,lenLk):
			#取列表中的两个集合进行比较，如果两个集合的前面k-2个元素都相等，那么就将这个两个集合合成一个大小为k的集合（通过集合的并操作完成，对应python中的|)
			L1 = list(Lk[i])[:k-2]
			L2 = list(Lk[j])[:k-2]
			"""
			这里进行排序其实目的就是使字典更有序，使得排序更好
			频繁项集{面包，尿布}和{面包，牛奶}合并，形成了候选3-项集{面包，尿布，牛奶},算法不会合并项集{啤酒，尿布},{尿布，牛奶}，因为他们第一个项不同
			使用这种方式可以减少很多重复项集！！！
			"""
			L1.sort();L2.sort()#List.sort函数会改变list自身,
			if L1 == L2:#如果前k-2项相同的话，那么就可以合并为应k-1项集
				retList.append(Lk[i]|Lk[j])
	return retList






def aprior(dataSet,minSupport=0.5):
	"""

	main function:
	step1: 获取C1,C1是大小为1的所有候选项集的集合
	step2: 列表数据集映射到set上
	step3: 获取L1（去掉C1中那些不满足最小支持度的项集）
	step4:...
	"""
	C1 = createC1(dataSet)#获取到最小项集(all min)
	D = map(set,dataSet)#映射成集合 [set([1, 3, 4]), set([2, 3, 5]), set([1, 2, 3, 5]), set([2, 5])]
	L1,supportData = scanD(D,C1,minSupport)#去掉那些不满足最小支持度的项集,从底层开始去的话，可以减少下一级的无畏运算
	L = [L1]#这里的L存储的是多个列表，每个列表存储着n 项集
	k =2 
	while(len(L[k-2]) > 0):
		# print L[k-2]
		Ck = apriorGen(L[k-2],k)
		Lk,supK = scanD(D,Ck,minSupport)#the input of D is the remap of the origin dataset 
		supportData.update(supK)
		L.append(Lk)
		k += 1
	return L,supportData







def calcConf(freqSet,H,supportData,br1,minConf=0.7):
	"""
	如果项集只有两个元素，那么使用这个函数计算可信度（置信度）
	计算规则的可信度以及找到满足最小可信度要求的规则
	函数返回一个满足最小可信度要求的规则列表
	"""
	prunedH = []
	for conseq in H:
		conf = supportData[freqSet]/supportData[freqSet-conseq]
		if conf >= minConf:
			print freqSet-conseq,'--->',conseq,'conf:',conf
			br1.append((freqSet-conseq,conseq,conf))#集合的减法其实就是求差集
			prunedH.append(conseq)
	return prunedH



def rulesFromConseq(freqSet,H,supportData,br1,minConf=0.7):
	"""
	从最初的项集生成更多的关联规则
	input argument:
		freqSet:  频繁项集，
		H: 可以出现在规则右部的元素列表H

	"""
	m = len(H[0])
	if len(freqSet)> m + 1 :
		Hmp1 = apriorGen(H,m+1)
		Hmp1 = calcConf(freqSet,Hmp1,supportData,br1,minConf)
		if len(Hmp1) > 1:
			rulesFromConseq(freqSet,Hmp1,supportData,br1,minConf)



def generateRules(L,supportData,minConf=0.7):
	"""
	input argument:
		L: 频繁项集列表  
		supportData: 包含哪些频繁项集支持数据的字典  
		minConf: 最小可信度阀值
	output:
		生成一个包含可信度的规则列表,后面可以基于可信度对他们进行排序
	"""
	bigRuleList = []
	for i in range(1,len(L)):#iterator from index 1 因为无法从单元素项集中构建关联规则，所以要从包含两个或者更多元素的项集开始构造
		for freqSet in L[i]:#所迭代的每个元素都是一个度的频繁项集
			H1 = [frozenset([item]) for item in freqSet]#将每一个频繁集中的元素进行解包，因为频繁集中的元素之间可能存在着关联规则。
			if i > 1:
				rulesFromConseq(freqSet,H1,supportData,bigRuleList,minConf)
			else:#因为这里的i从1开始的，那么L[1]表示的是频繁二项集
				calcConf(freqSet,H1,supportData,bigRuleList,minConf)
	return bigRuleList

dataSet = loadDataSet()
aprior(dataSet)
L,supportData =  aprior(dataSet)
rules  = generateRules(L,supportData,minConf=0.7)
sys.exit(0)









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
