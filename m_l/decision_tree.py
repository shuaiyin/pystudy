#coding=utf-8
"""
yinshuai: 决策树类似于我们之前喝酒玩的猜数字游戏，逐步缩小树值空间。。 

advantage:(1)计算复杂度不高，输出结果易于理解，对中间值的缺失状态不敏感，可以处理不相关特征数据
disadvatage:(1)可能会产生过度匹配问题 

适用数据类型： 数值型和标称型

在解决decision tree 这个问题时，我们需要解决的第一个问题就是：当前数据集上哪个特征在划分数据分类时起决定性作用
为了找到决定性的特征，划分出最好的结果，我们必须评估每个特征

1.在信息论和概率统计中，熵是表示随机变量不确定性的度量，熵越大，表示数据越杂乱无章，反之，则说明数据越有序

2.一条信息的信息量大小和它的不确定性有直接的关系。比如说，我们要搞清楚一件非常非常不确定的事，或是我们一无所知的事情，
就需要了解大量的信息。相反，如果我们对某件事已经有了较多的了解，我们不需要太多的信息就能把它搞清楚。所以，从这个角度，
我们可以认为，信息量的度量就等于不确定性的多少。
"""

from math import log
import operator 
import sys
def createDataSet():
	"""
	create test dateset 
	这个测试数据集的最后一列是具体的分类
	index	不浮出水面是否可以生存   是否有脚蹼  属于鱼类	 
	1		是(1)					是(1)	 是(yes)
	2		是(1)					是(1)	 是(yes)
	3		是(1)					否(0)	 否(0)
	4		否(0)					是(1)	 否(0)
	5		否(0)					是(1)	 否(0)
    

	"""
	dataSet = [[1,1,'yes'],[1,1,'yes'],[1,0,'no'],[0,1,'no'],[0,1,'no']]
	labels = ['no surfacing','flippers']#标签有两个（是否有脚蹼 and ..)
	return dataSet,labels

def majorityCnt(classList):
	"""
	返回出现次数最多的分类名称
	input argument:
		classList 是最后分类的列表 而不是特征值的列表

	yinshuai:
	我的理解：之所以要统计出现次数最多的分类名称
	那么我们如何来量化度量信息量呢？我们来看一个例子，马上要举行世界杯赛了。大家都很关心谁会是冠军。假如我错过了看世界杯，赛后我问一个知道比赛结果的观众“哪支球队
	是冠军”？ 他不愿意直接告诉我， 而要让我猜，并且我每猜一次，他要收一元钱才肯告诉我是否猜对了，那么我需要付给他多少钱才能知道谁是冠军呢? 我可以把球队编上号，从 
	1 到 32， 然后提问： “冠军的球队在 1-16 号中吗?” 假如他告诉我猜对了， 我会接着问： “冠军在 1-8 号中吗?” 假如他告诉我猜错了， 我自然知道冠军队在 9-16 中。
	 这样最多只需要五次， 我就能知道哪支球队是冠军。所以，谁是世界杯冠军这条消息的信息量只值五块钱。
	有些读者此时可能会发现我们实际上可能不需要猜五次就能猜出谁是冠军，因为象巴西、德国、意大利这样的球队得冠军的可能性比日本、美国、韩国等队大的多。因此，我们第一次
	猜测时不需要把 32 个球队等分成两个组，而可以把少数几个最可能的球队分成一组，把其它队分成另一组。然后我们猜冠军球队是否在那几只热门队中。我们重复这样的过程，根据
	夺冠概率对剩下的候选球队分组，直到找到冠军队。这样，我们也许三次或四次就猜出结果。

	还是拿世界杯做例子，在这些训练数据中，经过多年的积累，我们发现巴西队赢的次数最多，然后是西班牙队，那么我们猜测的起点就可以从巴西队或者西班牙队开始哦，然后数据再分叉


	"""
	classCount = {}
	for vote in classList:
		if vote not in classCount.keys():
			classCount[vote] = 0
		classCount[vote] += 1
		sortedClassCount = sorted(classCount.iteritems(),key=operator.itemgetter(1),reverse=True)#
	print sortedClassCount#这里返回的结果是一个列表（字典被拆分成一个一个的元组(固化为(key,value)），而不是原始的输入排序的字典了，
	return sortedClassCount[0][0]


def createTree(dataSet,labels):
	"""
	创建树的函数代码
	input argument:
		dataSet
		labels:labels中包含了数据集中所有特征的标签，
	"""
	classList = [example[-1] for example in dataSet] #获取所有分类构成的list
	print 'the class list is ' + str(classList)
	if classList.count(classList[0]) == len(classList):#递归函数的第一个停止条件是所有的类标签完全相同，则直接返回该类标签
		return classList[0]
	#遍历完所有的特征时返回出现次数最多的,这里之所以要用递归，这是因为决策树的从入口判断点开始到下面层的每个判断点都应该是最优的判断点，也就是我们不能说入口判断点是巴西，
	#然后第二个判断点就是中国了，当然第二个判断点依旧应该是胜算最大的判断点
	if len(dataSet[0]) == 1:#
		return majorityCnt(classList)

	bestFeat = chooseBestFeatureToSplit(dataSet)#从数据集中获取到用于分区（优胜区）的最优特征  now to vetify this 
	bestFeatLabel = labels[bestFeat]
	myTree = {bestFeatLabel:{}}
	del(labels[bestFeat])
	featValues = [example[bestFeat] for example in dataSet]
	uniqueVals = set(featValues)
	for value in uniqueVals:#最后，遍历当前选择特征包含的所有属性值，在每个数据集划分上递归调用函数createTree
		subLabels = labels[:]
		myTree[bestFeatLabel][value] = createTree(splitDataSet(dataSet,bestFeat,value),subLabels)
	return myTree





def calcShannonEnt(dataSet):
	"""
	计算给定数据集的香农熵
	"""
	numEntries = len(dataSet)#yinshuai：这里计算的时候的结果是数据的行数
	labelCounts = {}#创建一个数据字典，他的键值是最后一列的数值
	for fetVec in dataSet:
		currentLabel = fetVec[-1]#取出最后一列的分类
		if currentLabel not in labelCounts.keys():
			labelCounts[currentLabel] = 0
		labelCounts[currentLabel] += 1#每个键值都记录了当前类别出现的次数

	print labelCounts##
	shannonEnt = 0.0 #init the shanon ent 
	for key in labelCounts:#使用所有的类标签的发生频率计算类别出现的概率，我们将用这个概率计算香农熵
		prob = float(labelCounts[key])/numEntries
		print prob
		shannonEnt -= prob * log(prob,2)
	return shannonEnt

# splitDataSet(myDat,0,1)
def splitDataSet(dataSet,axis,value):
	"""
	按照给定的特征划分数据集,当然使用不同的特征值划分数据集达到的效果是不一定的
	input param: 
		dataSet: s待划分的数据集
		axis: 划分数据集的特征 0 1 2 ...etc
		value: 特征的返回值
	"""
	retDataSet = []#由于需要在数据集上进行多次修改，所以创建一个新的列表对象
	for featVec in dataSet:
		# print featVecs
		if featVec[axis] == value:#将符合特征的数据抽取出来,当我们按照某个特征划分数据集时，就需要将所有符合要求的元素抽取出来
			reducedFeatVec = featVec[:axis]
			# print 'the feactVec[:axis] data is %s' % featVec[:axis]
			reducedFeatVec.extend(featVec[axis+1:])
			# print reducedFeatVec
			retDataSet.append(reducedFeatVec)
			# print retDataSet
	return retDataSet

dataSet,labels = createDataSet()
print splitDataSet(dataSet,0,1)
print splitDataSet(dataSet,0,0)


sys.exit(0)

def chooseBestFeatureToSplit(dataSet):
	"""
	该函数选取特征，划分数据集，计算得出最好的划分数据集的特征
	在函数中调用的数据需要满足一定的要求：第一个要求是，数据必须是一种由列表元素组成的列表
	第二个要求是，数据的最后一列或者每个实例的最后一个元素是当前实例的类别标签
	熵计算将会告诉我们如何划分数据是最好的数据组织方式
	"""
	numFeatures = len(dataSet[0]) -1 #计算出特征值的数目，减去1 是因为最后一列是分类 
	baseEntropy = calcShannonEnt(dataSet)#计算整个数据集的原始shannon entropy 我们保持最初的无序度量值，用于与划分之后的数据集计算的熵值进行比较
	bestInfoGain = 0.0 #init the 最高的信息增益
	bestFeature = -1 
	for i in range(numFeatures):#这里的i其实也是这些特征值列的索引
		featList = [example[i] for example in dataSet]#总是感觉这样特别不好，为了取出特征值这一列的数据也是蛮拼的
		print featList
		uniqueVals = set(featList)#取出特征值这一列数据中的特征项
		# print uniqueVals
		newEntropy = 0.0#
		for value in uniqueVals:
			##这里splitDataSet函数的第二个参数为特征值的列位,我们将对每个特征划分数据集的结果计算一次信息熵，然后判断按照哪个特征划分数据集是最好的划分方式
			subDataSet = splitDataSet(dataSet,i,value)
			prob = len(subDataSet)/float(len(dataSet))
			newEntropy += prob * calcShannonEnt(subDataSet)
		infoGain = baseEntropy - newEntropy
		if infoGain > bestInfoGain:
			bestInfoGain = infoGain
			bestFeature = i 
	return bestFeature

# dataSet,labels = createDataSet()
# print chooseBestFeatureToSplit(dataSet)
# sys.exit(0)

def classify(inputTree,featLabels,testVec):
	"""
	使用决策树的分类函数
	"""
	firstStr = inputTree.keys()[0]
	secondDict = inputTree[firstStr]#扩展
	featIndex = featLabels.index(firstStr)
	for key in secondDict.keys():
		if testVec[featIndex] == key:
			if type(secondDict[key]).__name__ == 'dict':
				classLabel = classify(secondDict[key],featLabels,testVec)
			else:
				classLabel = secondDict[key]
	return classLabel

def storeTree(inputTree,filename):
	"""
	决策树的存储
	构造决策树是件很耗时的任务，即使处理很小的数据集，也要花费几ｓ的时间，因此，为了节省时间，最好能够在每次执行分类时调用已经构造好的决策树
	使用pickle模块存储决策树
	"""
	import pickle
	fw = open(filename,'w')
	pickle.dump(inputTree,fw)
	fw.close()

def grabTree(filename):
	import pickle
	fr = open(filename)
	return pickle.load(fr)





if __name__ == '__main__':
	myDat,labels = createDataSet()

	print myDat[0]
	# def splitDataSet(dataSet,axis,value):
	# """
	# 按照给定的特征划分数据集
	# input param: 
	# 	dataSet: s待划分的数据集
	# 	axis: 划分数据集的特征 
	# 	value: 特征的返回值
	# """
	# retDataSet = []#由于需要在数据集上进行多次修改，所以创建一个新的列表对象
	# for featVec in dataSet:
	# 	if featVec[axis] == value:
	# 		reducedFeatVec = featVec[:axis]
	# 		reducedFeatVec.extend(featVec[axis+1:])
	# 		retDataSet.append(reducedFeatVec)
	# return retDataSet


	# print splitDataSet(myDat,0,1)
     
	# print labels
	country_list = ['baxi','meiguo','baxi','xibanya','baxi','xibanya']
	# print majorityCnt(country_list)

# sorted(classCount.iteritems(),key=operator.itemgetter(1),reverse=True)
	sys.exit(0) 	






	print calcShannonEnt(myDat)
	"""
	{'yes': 2, 'no': 3}
	0.4
	0.6
	0.970950594455
	ys：其实对于刚才的测试数据集来说，数据集的长度为5 其中分类'yes'出现了2次(概率0.4)，分类'no'出现了3次（概率3/5=0.6)
	"""

	#熵越高，则混合的数据也越多，我们可以在数据集合中添加更多的分类，观察熵的变化,这里我们增加第三个名为maybe的分类
	myDat[0][-1] = 'maybe'
	print calcShannonEnt(myDat)
	"""
	{'maybe': 1, 'yes': 1, 'no': 3}
	0.2
	0.2
	0.6
	1.37095059445

	"""
	myDat,labels = createDataSet() #re init the dataset 
	chooseBestFeatureToSplit(myDat)
	myDat,labels = createDataSet() #re init the dataset 
	print myDat #[[1, 1, 'yes'], [1, 1, 'yes'], [1, 0, 'no'], [0, 1, 'no'], [0, 1, 'no']]
	print labels  #['no surfacing', 'flippers']
	myTree = createTree(myDat,labels)
	print myTree
	"""
	{'no surfacing': {0: 'no', 1: {'flippers': {0: 'no', 1: 'yes'}}}}

	"""

	####p 147  has problem